from flask import jsonify, Blueprint, request
from app.services.raffle_services import RaffleService
from app.models.response_message import ResponseBuilder
from app.mapping import ResponseSchema, RaffleSchema

raffle = Blueprint('raffle', __name__)
raffle_schema = RaffleSchema()
response_schema = ResponseSchema()

@raffle.route('/create', methods=['POST'])
def create_raffle():
    try:
        service = RaffleService()
        raffle_data = request.json
        raffle = raffle_schema.load(raffle_data)
        created_raffle = service.create(raffle)
        response = {"raffle": raffle_schema.dump(created_raffle)}
        return jsonify(response), 201
    except Exception as e:
        error_message = f"Error al agregar un Sorteo: {str(e)}"
        return jsonify({"error": error_message}), 500


@raffle.route('/all', methods=['GET'])
def find_all():
    service = RaffleService()
    response_builder = ResponseBuilder()
    raffles = service.find_all()
    raffles_json = [raffle_schema.dump(raffle) for raffle in raffles]
    response_builder.add_message("Sorteos encontrados").add_status_code(100).add_data({'Sorteos': raffles_json})
    return response_schema.dump(response_builder.build())

@raffle.route('/<int:id>', methods=['GET'])
def find(id):
    service = RaffleService()
    raffle = service.find_by_id(id)

    if raffle:
        response_builder = ResponseBuilder()
        response_builder.add_message("Sorteo encontrado").add_status_code(100).add_data(raffle_schema.dump(raffle))
        return jsonify(response_schema.dump(response_builder.build()))
    else:
        return jsonify({"error": "Sorteo no encontrado"}), 404
    

@raffle.route('/delete/<int:raffle_id>', methods=['DELETE'])
def delete_raffle(raffle_id):
    try:
        service = RaffleService()
        deleted = service.delete(raffle_id)

        if deleted:
            return jsonify({"message": "Sorteo eliminado con éxito", "status_code": 200}), 200

        return jsonify({"error": "Sorteo no encontrado", "status_code": 404}), 404
    except Exception as e:
        return jsonify({"error": str(e), "status_code": 500}), 500
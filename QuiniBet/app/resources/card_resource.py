from flask import jsonify, Blueprint, request
from app.services.card_services import CardService
from app.models.response_message import ResponseBuilder
from app.mapping import CardSchema, ResponseSchema

#Blueprint de Card
card = Blueprint('card', __name__)
card_schema = CardSchema()
response_schema = ResponseSchema()


@card.route('/create', methods=['POST'])
def create_card():
    data = request.get_json()
    numbers = data.get('numbers')
    user_id = data.get('user_id')

    if not numbers or len(numbers) != 6:
        return jsonify({'error': 'Los números deben ser exactamente 6.'}), 400

    card_service = CardService()  # Crea una instancia de CardService
    new_card = card_service.create_card(numbers, user_id)

    return jsonify({'message': 'Tarjeta creada con éxito', 'card': new_card}), 201


@card.route('/<int:id>', methods=['GET'])
def find(id):
    service = CardService()
    card = service.find_by_id(id)

    if card:
        response_builder = ResponseBuilder()
        response_builder.add_message("Card encontrada").add_status_code(100).add_data(card_schema.dump(card))
        return response_schema.dump(response_builder.build())
    else:
        return jsonify({"error": "Card no encontrado"}), 404

@card.route('/numbers/<string:numbers>', methods=['GET'])
def find_by_numbers(numbers):
    service = CardService()
    card = service.find_by_numbers(numbers)

    if card:
        response_builder = ResponseBuilder()
        response_builder.add_message("Cartón encontrado").add_status_code(100).add_data(card_schema.dump(card))
        return response_schema.dump(response_builder.build())
    else:
        return jsonify({"error": "Cartón no encontrado"}), 40

@card.route('/<int:card_id>/', methods=['DELETE'])
def delete_card(card_id):
    try:
        service = CardService()
        deleted = service.delete(card_id)

        if deleted:
            return jsonify({"message": "Cartón eliminado con éxito", "status_code": 200}), 200

        return jsonify({"error": "Cartón no encontrado", "status_code": 404}), 404
    except Exception as e:
        return jsonify({"error": str(e), "status_code": 500}), 500
from flask import jsonify, Blueprint, request
from app.services.user_services import UserService
from app.models.response_message import ResponseBuilder
from app.mapping import ResponseSchema, UserSchema


user = Blueprint('user', __name__)
user_schema = UserSchema()
response_schema = ResponseSchema()

"""
id: int ingresado por el usuario
return: json con los datos del usuario

"""

@user.route('/add', methods=['POST'])
def post_user():
    try:
        service = UserService()
        user = user_schema.load(request.json)
        created_user = service.create(user)
        response = {"user": user_schema.dump(created_user)}
        return jsonify(response), 201
    except Exception as e:
        error_message = f"Error al agregar usuario: {str(e)}"
        return jsonify({"error": error_message}), 400


@user.route('/<int:id>', methods=['GET'])
def find(id):
    service = UserService()
    raffle = service.find_by_id(id)

    if raffle:
        response_builder = ResponseBuilder()
        response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(user_schema.dump(raffle))
        return jsonify(response_schema.dump(response_builder.build()))
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


@user.route('/all', methods=['GET'])
def find_all():
    service = UserService()
    response_builder = ResponseBuilder()
    users = service.find_all()
    users_json = [user_schema.dump(user) for user in users]
    response_builder.add_message("Usuarios encontrados").add_status_code(100).add_data({'users': users_json})
    return response_schema.dump(response_builder.build())
  

@user.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Datos de usuario no proporcionados"}), 400

        service = UserService()
        updated_user = service.update(user_id, data)

        if updated_user:
            response_builder = ResponseBuilder()
            response_builder.add_message("Usuario actualizado con éxito").add_status_code(200).add_data(user_schema.dump(updated_user))
            return response_schema.dump(response_builder.build())

        return jsonify({"error": "El usuario no se pudo actualizar"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@user.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        service = UserService()
        deleted = service.delete(user_id)

        if deleted:
            return jsonify({"message": "Usuario eliminado con éxito", "status_code": 200}), 200

        return jsonify({"error": "Usuario no encontrado", "status_code": 404}), 404
    except Exception as e:
        return jsonify({"error": str(e), "status_code": 500}), 500
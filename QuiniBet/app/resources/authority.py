from functools import wraps
from flask import jsonify
from flask_jwt_extended import current_user, jwt
from app.services import UserService

def roles_required(roles: list[str]):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            print(f"Info {current_user.roles}")
            is_allowed = any(role.name in current_user.roles for role in roles)
            
            if not is_allowed:
                return jsonify(error='Access denied'), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    service = UserService()
    print(f"Claims Loader {identity}")
    usuario = service.find_by_identity(identity)
    list_roles = [role.name for role in usuario.roles]
    # Do something with list_roles if needed

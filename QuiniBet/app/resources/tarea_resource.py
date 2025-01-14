
"""tarea_schema = TareaSchema()

tarea.route('/', methods = ['GET'])
@jwt_required()


@roles_required(['ROLES_TAREAS_READ'])
def all():
    resp = tarea_schema.dump(service.get_all(), many = True)
    return resp, 200


 @tarea.route('<int:id>', methods = ['GET'])
@jwt_required()
@roles_required(['ROLES_TAREAS_READ'])
def one(id):
    resp = tarea_schema.dump[(service.get_by_id(id))]
    return resp , 200

@tarea.route('/', methods= ['POST'])
@jwt_required()
@roles_required(['ROLES_TAREAS_CREATE'])
def add():
 """
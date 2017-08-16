from app import db,orm
'Clase User ==> modelo de base de datos de la tabla user (pony orm)'
class User(db.Entity):
    _type = "user"
    _fields = ['name', 'email', 'position', 'age', 'image']
    name = orm.Required(str)
    email = orm.Required(str)
    position = orm.Required(str)
    age = orm.Required(int)
    image = orm.Optional(str)


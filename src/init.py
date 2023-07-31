from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# initialising packages so we can reference in other files
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()

# SQLAlchemy is an SQL toolkit and the Object Relational Mapper (ORM) that will be used on this project
# Marshmallow is an ORM/Framework library that converts complex data types like objects to and from native Python datatypes
# Bcrypt is a password hashing function that will be used on the user passwords
# JWT (JSON Web Token) allows us to securely authenticate and authorise users as a JSON object
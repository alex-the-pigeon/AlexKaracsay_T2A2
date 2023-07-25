from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, user_schema, users_schema
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def auth_register():
    try: # this is to avoid having an SQLalchemy integrity error (either 23502 - not_null_violation or 23505 - unique_violation) as we've set email to "unique" and "not null" in user.py
        body_data = request.get_json() #requesting the JSON data - username, email, password

        user = User()
        user.username = body_data.get('username') 
        user.email = body_data.get('email')
        if body_data.get('password'):
            user.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8') #this hashes the user password and decodes to utf-8
        #add the user to session
        db.session.add(user)
        #add user to database
        db.session.commit()
        #client response
        return user_schema.dump(user), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return { 'error': 'Email address is already in use'}, 409
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {'error': f'The {err.orig.diag.column_name} is required'}, 409 # This line will show the name of a field eg. password or email if the user does not input
        


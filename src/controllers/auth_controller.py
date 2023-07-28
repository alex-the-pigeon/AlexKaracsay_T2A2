from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, user_schema, users_schema
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from datetime import timedelta

auth_bp = Blueprint('auth', __name__, url_prefix='/auth') # this sets the prefix for all the requests in this file

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
        
@auth_bp.route('/login', methods=['POST'])
def auth_login():
    body_data = request.get_json()
    # how to find the user by their email using a statement
    stmt = db.select(User).filter_by(email=body_data.get('email'))
    user = db.session.scalar(stmt)
    # if user credentials are correct
    if user and bcrypt.check_password_hash(user.password, body_data.get('password')): # this checks if the password matches the username at login
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1)) #this creates the session token and how long it is valid for, in this case 1 day
        return { 'email': user.email, 'token': token, 'is_admin': user.is_admin }
    else:
        return { 'error': 'Invalid email or password'}, 401 # this is the error message to be thrown if the user credentials are incorrectly entered
    

from flask import Blueprint
from init import db, bcrypt 
from models.user import User 

db_commands = Blueprint('db', '__name__')

# this organises our routes so we don't have to type out full route every time
# auth_routes = Blueprint('auth', __name__, url_prefix="/auth/")

# @auth_routes.route("/register")

# database commands to create, delete and update user table
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables Dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
       # creating an admin for example
        User(
            username="admin",
            email="admin@admin.com",
            password=bcrypt.generate_password_hash('admin123').decode('utf-8'),
            is_admin=True
        )
    ]
    db.session.add_all(users)
    db.session.commit()
    print("Tables Seeded")

    # hello
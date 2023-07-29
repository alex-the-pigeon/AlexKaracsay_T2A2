from flask import Blueprint
from init import db, bcrypt 
from models.user import User 
from models.rider import Rider

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

    riders = [
        Rider(
            last_name='Doe',
            first_name='Jane',
            sex='Female',
            age='33',
            user=users[0],
        ),
        Rider(
            last_name='Doe',
            first_name='John',
            sex='Male',
            age='35',
            user=users[1],  
        
        )
    ]

    db.session.add_all(riders)

    # add races here

    # add safety contacts here

    db.session.commit()
    print("Tables Seeded")


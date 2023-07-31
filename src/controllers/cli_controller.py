from flask import Blueprint
from init import db, bcrypt 
from models.user import User 
from models.rider import Rider

db_commands = Blueprint('db', '__name__')

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
       # creating an admin for example of showing user creation
        User(
            username="admin",
            email="admin@admin.com",
            password=bcrypt.generate_password_hash('admin123').decode('utf-8'),
            is_admin=True
        )
    ]
    db.session.add_all(users)
    # creating some example riders, each associated with a single user account
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

    # creating some example races linked to a single user
     
    races = [
        Race(
            race_name='Turbulence',
            race_type='Downhill',
            user=users[1],
        ),
        Race(
            race_name='Lactic Acid',
            race_type='Enduro',
            user=users[1],

        )
    ]

    db.session.add_all(races)
# example safety contacts for two different riders
    safety = [
        Safety(
            last_name='Williams',
            first_name='Steve',
            relationship='Partner',
            user=users[0],
        ),
        Safety(
            last_name='Capone',
            first_name='Tony',
            relationship='Brother',
            user=users[1],
        
        )
    ]

    db.session.add_all(safety)

    db.session.commit()
    print("Tables Seeded")


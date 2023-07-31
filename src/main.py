from flask import Flask
import os
from init import db, ma, bcrypt, jwt 
from controllers.cli_controller import db_commands
from controllers.auth_controller import auth_bp
from controllers.rider_controller import riders_bp
from controllers.race_controller import races_bp
from controllers.safety_controller import safety_bp


def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False
    #                                    linking to .env file (which will be included in final source code, NOT uploaded to GitHub as it contains sensitive information)                                   
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
# importing cli command blueprint
    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)

    return app
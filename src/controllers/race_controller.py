from flask import Blueprint, request
from init import db
from models.race import Race, race_schema, races_schema

races_bp = Blueprint('races', __name__, url_prefix='/races')

@races_bp.route('/')
def get_all_races():
    stmt = db.select(Race).order_by(Race.race_type.asc()) # sort races by type in ascending order
    races = db.session.scalar(stmt)
    return races_schema.dump(races)

from flask import Blueprint, request
from init import db
from models.rider import Rider, riders_schema, rider_schema

riders_bp = Blueprint('riders', __name__, url_prefix='/riders')

@riders_bp.route('/')
def get_all_riders():
    stmt = db.select(Rider).order_by(Rider.last_name.asc()) # sort riders by surname ascending order
    riders = db.session.scalar(stmt)
    return riders_schema.dump(riders)

from flask import Blueprint, request
from init import db
from models.safety import Safety, safety_schema

safety_bp = Blueprint('safety', __name__, url_prefix='/safety')

@safety_bp.route('/')
def get_all_safety():
    stmt = db.select(Safety).order_by(Safety.last_name.asc()) # sort safety contacts by surname. I wanted to have this sort by association to rider_id
    safety = db.session.scalar(stmt)
    return safety_schema.dump(safety)
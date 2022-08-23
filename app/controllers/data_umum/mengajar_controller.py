from flask import Blueprint, request, jsonify
from app.models.mengajar_model import MengajarModel

mengajar = Blueprint('mengajar', __name__, url_prefix='/mengajar')

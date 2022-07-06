from flask import Blueprint
from app.extensions import db
from app.models.user_model import UserModel, UserDetailModel

user = Blueprint('user', __name__, url_prefix='/user')


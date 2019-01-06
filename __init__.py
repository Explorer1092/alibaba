from flask import Blueprint

cpu = Blueprint('cpu', __name__)
from . import views



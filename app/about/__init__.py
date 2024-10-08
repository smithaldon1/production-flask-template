from flask import Blueprint

about_bp = Blueprint('about', __name__, template_folder='templates')

from . import views
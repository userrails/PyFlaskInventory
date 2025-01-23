from flask import Blueprint

stocks_bp = Blueprint('stocks', __name__)

from . import routes

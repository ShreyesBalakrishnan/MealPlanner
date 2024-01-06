from flask import Blueprint

main = Blueprint("main", __name__)

# noinspection PyPep8Naming
from . import routes

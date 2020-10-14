from flask import Blueprint

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/hello")
def hello_pybo():
    return "Hello pybo"


@bp.route("/")
def index():
    return "pybo index"

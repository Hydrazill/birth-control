
from flask import (
                    Flask,
                    Blueprint,
                    redirect,
                    session,
                    url_for,
                )

from app.routes.auth import (
                                login,
                                register,
                            )
from app.routes.main import (
                                acceuil,
                                create_admin,
                            )

app = Flask(__name__, static_url_path='/static', static_folder='static')

bp_main = Blueprint('main', __name__)
bp_auth = Blueprint('auth', __name__)

@bp_auth.route('/')
def home():
    return redirect(url_for('auth.auth_login'))
@bp_auth.route('/login', methods=["GET", "POST"])
def auth_login():
    return login()
@bp_auth.route('/register', methods=["GET", "POST"])
def auth_register():
    return register()

@bp_main.route('/acceuil', methods=["GET", "POST"])
def main_acceuil():
    return acceuil()
@bp_main.route('/logout')
def main_logout():
    session.pop("user")
    return redirect(url_for("auth.auth_login"))
    # route annexe de main
@bp_main.route('/create_admin')
def new_admin():
    if create_admin():
        return "<h1>Succes</h1>"
    else:
        return "<h1>Failure</h1>"
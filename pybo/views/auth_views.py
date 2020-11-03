from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/signup/", methods=("GET", "POST"))
def signup():
    form = UserCreateForm()
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(
                username=form.username.data,
                password=generate_password_hash(form.password1.data),
                email=form.email.data,
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("main.index"))
        else:
            flash("이미 존재하는 사용자 입니다.")
    return render_template("auth/signup.html", form=form)


@bp.route("/login/", methods=("GET", "POST"))
def login():
    form = UserLoginForm()
    if request.method == "POST" and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            # 세션은 플라스크 메모리에 저장되기 때문에 플라스크 서버가 구동중인 동안에는 영구적으로 사용할 수 있는 값
            # ※ 세션은 영구적이지만 타임아웃이 설정되어 있어서 타임아웃 시간동안 접속이 없으면 세션정보가 삭제된다.
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("main.index"))
        flash(error)
    return render_template("auth/login.html", form=form)


# 라우트 함수 실행전에 항상 먼저 실행
#  g변수는 플라스크가 제공하는 컨텍스트 변수로 request변수와 마찬가지로 요청과 응답이라는 한 사이클에서만 유효
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for("main.index"))

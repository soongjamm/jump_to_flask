from flask import Blueprint, url_for, g, flash
from pybo import db
from ..views.auth_views import login_required
from ..models import Question, Answer
from werkzeug.utils import redirect


bp = Blueprint("vote", __name__, url_prefix="/vote")


@bp.route("/question/<int:question_id>/")
@login_required
def question(question_id):
    _question = Question.query.get_or_404(question_id)
    if g.user == _question.user:
        flash("본인이 작성한 글은 추천할 수 없습니다.")
    else:
        _question.voter.append(g.user)
        db.session.commit()
    return redirect(url_for("question.detail", question_id=question_id))


@bp.route("/answer/<int:answer_id>/")
@login_required
def answer(answer_id):
    _answer = Answer.query.get_or_404(answer_id)
    if g.user == _answer.user:
        flash("본인이 작성한 글은 추천할 수 없습니다.")
    else:
        _answer.voter.append(g.user)
        db.session.commit()
    return redirect(url_for("question.detail", question_id=_answer.question.id))

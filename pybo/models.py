from pybo import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        # server_default="1",
    )
    # User 스키마의 id를 참조함
    user = db.relationship(
        "User", backref=db.backref("question_set")
    )  # question을 이용해 user를 참조하기 위함


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(
        db.Integer, db.ForeignKey("question.id", ondelete="CASCADE")
    )
    question = db.relationship(
        "Question", backref=db.backref("answer_set")
    )  # backref 속성은 answer.question.subject 와는 반대로 질문에서 답변모델을 참조하기 위해서 사용되는 속성이다. 중요한 기능
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False
        # server_default="1",
    )
    user = db.relationship("User", backref=db.backref("answer_set"))

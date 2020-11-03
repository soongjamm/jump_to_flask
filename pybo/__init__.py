from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    # config.py에 작성한 항목들을 app.config 환경변수로 읽어들이기 위해
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # blueprint
    from .views import main_views, question_views, answer_views, auth_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime

    app.jinja_env.filters[
        "datetime"
    ] = format_datetime  # app.jinja_env.filters['datetime'] 처럼 datetime 이라는 이름의 필터로 등록해 주었다. 이제 템플릿에서 |datetime 으로 사용

    return app
# [점프 투 플라스크](https://wikidocs.net/book/4542)
===============
### 가상환경
- virtualenv venv
- source venv/bin/activate
- deactivate  
  
### flask
- pip install flask
- export FLASK_APP=__init__
- export FLASK_ENV=development
- flask run  
  
### DB
- SQLAlchemy, Flask-Migrate
- 'flask db init' 
- 만약 db 커맨드가 존재하지 않는다고 뜨면 venv를 나가서 flask 삭제 (global로 설치된 flask), venv 재진입 후 시도 (https://github.com/miguelgrinberg/microblog/issues/69)
- flask db init 명령은 최초 한번만 수행하면 된다. 앞으로 모델을 추가하고 변경할때는 flask db migrate와 flask db upgrade 명령 두개만 반복적으로 사용하면 된다.
    * flask db migrate - 모델을 신규로 생성하거나 변경할때 사용
    * flask db upgrade - 변경된 내용을 적용할때 사용
    * SQLAlchemy docs : https://docs.sqlalchemy.org/en/13/orm/query.html


import os

# BASE_DIR은 프로젝트의 루트 디렉터리 의미
# SQLALCHEMY_TRACK_MODIFICATIONS는 SQLAlchemy의 이벤트들을 처리하기 위한 옵션인데 추가적인 메모리를 사용하기도 하고 파이보 서비스에는 필요없는 기능이므로 False로 비활성화시키도록 하자.
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, "pybo.db"))
SQLALCHEMY_TRACK_MODIFICATIONS = False
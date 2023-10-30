DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 엔진
        "NAME": "django_db",  # 데이터베이스 이름
        "USER": "root",  # 사용자
        "PASSWORD": "1234",  # 비밀번호
        "HOST": "localhost",  # 호스트
        "PORT": "3306",  # 포트번호
    }
}

# SECRET_KEY
# settings.py에서 가져온다
# 원래 있던 녀석은 주석처리 됨
SECRET_KEY = "django-insecure-ct)$8xo55yy*#60nrm78!n*g9^nmqlg5(*&nil0_-o*ak(+77#"
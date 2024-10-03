# Python 3.12 이미지 사용
FROM python:3.12

# 작업 디렉터리 설정
WORKDIR /app

# requirements.txt 복사 및 설치
COPY ./requirements.txt requirements.txt

# pip 업그레이드 및 패키지 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 프로젝트 파일 복사
COPY . .

# Gunicorn 설치
RUN pip install gunicorn

# Django 마이그레이션 실행 후 Gunicorn으로 서버 시작
CMD ["sh", "-c", "python manage.py loaddata /app/data.json && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 project.wsgi:application"]
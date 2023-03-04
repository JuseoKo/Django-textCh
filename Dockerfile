#파이썬 버전
#FROM python:3.10.5
FROM --platform=linux/amd64 python:3.10.5-slim-buster as build
# 작업디렉토리 설정
WORKDIR /app

# 종속성 라이브러리 설치
RUN pip3 install django
RUN pip3 install django-ckeditor
RUN pip3 install django-js-asset
RUN pip3 install mysqlclient
RUN pip3 install gunicorn

# 명령어를 실행하는 디렉토리 내부에 있는 모든 파일을 /app에 복사
COPY . .

# Expose the port 8000
EXPOSE 8000
# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

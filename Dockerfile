# Dockerfile
FROM python:3.10

WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python backend/manage.py collectstatic --noinput
CMD gunicorn backend.wsgi --bind 0.0.0.0:$PORT
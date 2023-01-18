FROM python:3.10-slim

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache -r requirements.txt

COPY . . 

CMD gunicorn recipe.wsgi:application --bind 0.0.0.0:80

EXPOSE 80
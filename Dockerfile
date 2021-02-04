FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "app.wsgi"]
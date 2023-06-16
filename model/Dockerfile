FROM python:3.9

WORKDIR /app
# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

COPY . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
FROM python:3.11.4

WORKDIR /app

ENV RUNNING_IN_DOCKER Yes

RUN python -m pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

COPY . /app

ENV FLASK_ENV="docker"

CMD [ "python", "app.py"]

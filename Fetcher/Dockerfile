FROM python:3.11.4

WORKDIR /app

ENV RUNNING_IN_DOCKER Yes

RUN python -m pip install --upgrade pip
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python", "fetch_data.py" ]

FROM python:3.10.2-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt update \
    && apt install -y libpq-dev gcc

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

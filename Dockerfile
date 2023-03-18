# app/Dockerfile

FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 zbar-tools -y


COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

LABEL version="1.0.0"
LABEL description="Richard's Automated Text Messaging Machine"

ENV DIRECTORY=/app
WORKDIR /app

COPY . /app
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \   
    pwd && ls -lta && \
    /py/bin/pip install -r ./requirements.txt

ENV PATH="/py/bin:$PATH"


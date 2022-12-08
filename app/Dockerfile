FROM python:3.11.1-alpine3.17
LABEL maintainer="main app"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY . /app
WORKDIR /app

RUN python -m venv /py && \
  /py/bin/pip install --upgrade pip && \
  # apk add --update --no-cache postgresql-client jpeg-dev && \
  # apk add --update --no-cache --virtual .tmp-build-deps \
  # build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
  /py/bin/pip install -r /tmp/requirements.txt && \
  rm -rf /tmp && \
  # apk del .tmp-build-deps && \
  adduser \
  --disabled-password \
  --no-create-home \
  app-user

ENV PATH="/py/bin:$PATH"

USER app-user

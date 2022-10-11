FROM alpine:3.14

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

WORKDIR /latex-linter

COPY src ./src
COPY settings/settings.json ./settings/settings.json
COPY output ./output
COPY input ./input
COPY tests ./tests
COPY main.py .
COPY test.py .
COPY README.MD .
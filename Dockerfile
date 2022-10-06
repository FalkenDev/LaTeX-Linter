FROM ubuntu:22.04

RUN apt update && apt install -y python3

WORKDIR /latex-linter

COPY src .
COPY settings/settings.json ./settings
COPY output .
COPY input .
COPY tests .
COPY main.py .
COPY test.py .
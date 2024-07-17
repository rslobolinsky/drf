FROM python:3

WORKDIR /drf

COPY ./pyproject.toml /drf
COPY . .
RUN pip install poetry
RUN poetry install


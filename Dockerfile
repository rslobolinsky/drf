FROM python:3

WORKDIR /drf

COPY ./pyproject.toml /drf
RUN pip install poetry
RUN poetry install


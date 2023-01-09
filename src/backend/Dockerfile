FROM python:3.9-slim

WORKDIR /backend

ADD pyproject.toml .
RUN pip install poetry
RUN poetry install

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV PYTHONPATH=.

COPY ./app ./app

CMD ["poetry", "run", "python", "/backend/app/main.py"]

FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml ./
COPY cli.py ./
COPY tests/ ./tests/

RUN pip install --no-cache-dir pytest .

ENTRYPOINT ["python", "cli.py"]

CMD [ "executable" ]

FROM python:3.10.5

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD [ "alembic", "upgrade", "head" ]
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload" ]

FROM python:3.9.5

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt && rm requirements.txt

COPY src/main /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

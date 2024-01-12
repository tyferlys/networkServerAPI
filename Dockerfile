FROM python:3.10

RUN mkdir /fastapi_app
WORKDIR /fastapi_app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD uvicorn main:app --workers 4 --host 0.0.0.0 --port 80
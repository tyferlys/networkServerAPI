FROM python:3.10

RUN mkdir /fastapi_app
WORKDIR /fastapi_app

COPY requirements.txt .

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install libgl1-mesa-glx
RUN pip install opencv-python-headless
RUN pip install -r requirements.txt

COPY . .

WORKDIR /src

CMD uvicorn main:app --workers 4 --host 0.0.0.0 --port 443 --ssl-keyfile private.key --ssl-certfile certificate.crt
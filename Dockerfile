FROM python:3.9.13-slim-buster
LABEL Name="Aws-Tagger (Datakind)"
LABEL Version=0.0.1

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN apt-get update && \ 
apt-get install git -y && \
pip install --upgrade pip && \
pip install -r requirements.txt \
&& rm -rf /var/cache/apk/*

COPY . /app
RUN pip install .

# CMD gunicorn -k eventlet -w 1 app:app -b 0.0.0.0:$PORT
CMD gunicorn -k eventlet -w 1 app:app -b 0.0.0.0

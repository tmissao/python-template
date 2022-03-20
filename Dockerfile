FROM python:3.9-alpine as build

RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY app .
WORKDIR /
COPY wsgy.py wsgy.py
COPY gunicorn.conf.py gunicorn.conf.py

CMD ["gunicorn", "-c", "gunicorn.conf.py", "wsgy:app"]

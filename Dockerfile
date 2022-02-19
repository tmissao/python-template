# FROM python:3.8-alpine

# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD [ "python", "-m" , "demo"]

FROM python:3.8-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY app /app

WORKDIR /app

CMD ["python", "-m" , "app"]

FROM python:3.9-slim as build

RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY app .

FROM gcr.io/distroless/python3
COPY --from=build /app /app
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
WORKDIR /
ENV PYTHONPATH=/usr/local/lib/python3.9/site-packages
EXPOSE 5000
CMD ["-m", "app"]

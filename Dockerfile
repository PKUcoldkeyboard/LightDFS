FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV NAMESERVER_PORT=9000
ENV DATASERVER_PORT=10070
ENV CLIENT_PORT=9070

CMD ["python", "nameserver/server.py"]
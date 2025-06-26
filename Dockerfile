# Use an official Python runtime as a parent image
FROM python:3.12-slim
 
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 
# Set work directory
WORKDIR /usr/src/app
 
COPY . /usr/src/app/
# Install dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --upgrade pip
RUN pip install  -r requirements.txt
 
# Make ports 80 and 443 available to the world outside this container
EXPOSE 80 443
 
ENV TZ="Asia/Manila"
ENV DJANGO_ALLOWED_HOSTS=139.144.127.183,172.104.37.198,nginx-host,0.0.0.0,localhost,127.0.0.1,happyplay-api.ept.ph
ENV SOCKET_SERVICE_URL=http://hp-websockets/
ENV KAFKA_SERVICE_URL=http://happy-play-message-broker/
 
# Run the application
CMD ["gunicorn", "-b", "0.0.0.0:8000", "HPGameApi.wsgi:application"]
 
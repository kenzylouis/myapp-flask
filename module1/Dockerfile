FROM python:2.7-slim
MAINTAINER Nick Janetakis <nick.janetakis@gmail.com>

ENV INSTALL_PATH /myapp
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "myapp.app:create_app()"
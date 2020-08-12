FROM python:3-alpine
RUN apk update && apk add gcc musl-dev
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN django-admin startproject sansa .
COPY . /app
COPY ./start.sh /start.sh
RUN chmod ug+x /start.sh
CMD ["/start.sh"]

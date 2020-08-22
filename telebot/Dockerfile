FROM python:3.7-alpine

#Directorio de trabajo
WORKDIR /bot

# instalar git
RUN apk update && apk add git  

# Obtener el repositorio de pyTelegramBotAPI

#COPY ./pyTelegramBotAPI /bot/pyTelegramBotAPI 
#COPY ./Pipfile /bot/

# Instalar pyTelegramBotAPI

ADD ./bot /bot/app
RUN pip install --upgrade pip && \
	pip install -r /bot/app/requirements.txt
ENV APIKEY INSERTAR-API-KEY

ENV PYTHONUNBUFFERED 1
CMD ["python","./app/bot.py"]

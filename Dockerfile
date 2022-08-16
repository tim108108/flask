FROM python:3.9-slim

WORKDIR /app 
COPY ./requirements.txt /app 

RUN apt-get update 
RUN apt-get install nano
RUN apt-get -y install vim
RUN pip install -r requirements.txt

#CMD python main.py

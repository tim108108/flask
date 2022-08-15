FROM python:3.9-slim

WORKDIR /app 
COPY ./requirements.txt /app 

RUN apt-get update 
RUN apt-get install nano
RUN pip install -r requirements.txt

#CMD python main.py

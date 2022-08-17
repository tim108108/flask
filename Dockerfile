#FROM python:3.9-slim
#FROM pytorch/pytorch:latest
FROM ultralytics/yolov5:latest

WORKDIR /app/flask 
COPY ./requirements.txt /app/flask 

RUN apt-get update 
#RUN apt-get -y install git
#RUN apt-get -y install vim nano
RUN pip install -r requirements.txt
#RUN git clone https://github.com/ultralytics/yolov5.git

#CMD python main.py

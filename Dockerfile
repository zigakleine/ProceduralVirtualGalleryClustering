FROM python:3.7.5-buster
RUN echo \
   && apt-get update \
   && apt-get --yes install apt-file \
   && apt-file update
RUN echo \
   && apt-get --yes install build-essential
ARG USER=nobody
RUN usermod -aG sudo $USER
RUN pip3 install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
USER $USER

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]

#FROM ubuntu:latest
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
#WORKDIR /app
#COPY . /app
#RUN pip install -r requirements.txt
#EXPOSE 5000
#ENTRYPOINT ["python"]
#CMD ["app.py"]
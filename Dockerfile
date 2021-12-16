FROM python:3.9

RUN apt-get update && apt-get upgrade -y && apt-get install git libgl1-mesa-glx -y && pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r /requirements.txt

RUN mkdir -p /project
COPY . /project
WORKDIR /project

ENTRYPOINT [ "/bin/bash" ]
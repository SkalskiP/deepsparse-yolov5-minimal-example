FROM python:3.8

RUN apt-get update && apt-get upgrade -y && apt-get install git libgl1-mesa-glx -y && pip install --upgrade pip && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN pip install -r --no-cache-dir /requirements.txt

RUN mkdir -p /project
COPY . /project
WORKDIR /project

RUN git clone https://github.com/neuralmagic/deepsparse.git

ENTRYPOINT [ "/bin/bash" ]

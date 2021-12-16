## Build docker image

```console
docker build -t deepsparse-yolov5-minimal-example -f Dockerfile .
```

## Run docker image

```console
docker run -it deepsparse-yolov5-minimal-example:latest
```

## Run example

```console
python -m src.example
```

## Install venv locally

```console
virtualenv venv
source venv/bin/activate
pip install -r docker/requirements.txt
```
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

## Run yolo5s benchmark

```console
python benchmark.py \
    zoo:cv/detection/yolov5-s/pytorch/ultralytics/coco/pruned_quant-aggressive_94 \
    --batch-size 1 \
    --quantized-inputs \
    --num-iterations 500 \
    --num-warmup-iterations 100
```

## Run yolov5l benchmark

```console
python benchmark.py \
    zoo:cv/detection/yolov5-l/pytorch/ultralytics/coco/pruned_quant-aggressive_95 \
    --batch-size 1 \
    --quantized-inputs \
    --num-iterations 500 \
    --num-warmup-iterations 100
```

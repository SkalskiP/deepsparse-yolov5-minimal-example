from deepsparse import compile_model

from src.deepsparse_utils import modify_yolo_onnx_input_shape, postprocess_nms

import numpy as np
import cv2

from typing import Tuple

MODEL_PATH = 'data/model.onnx'
IMAGE_PATH = 'data/image-1.jpeg'
BATCH_SIZE = 1
INPUT_RESOLUTION = (800, 800)


def preprocess_image(image: np.ndarray, image_size: Tuple[int, int] = (640, 640)) -> np.ndarray:
    image_resized = cv2.resize(image, image_size)
    image_transposed = image_resized[:, :, ::-1].transpose(2, 0, 1)
    image_wrapped = image_transposed[np.newaxis, ...]
    return np.ascontiguousarray(image_wrapped)


model_path, _ = modify_yolo_onnx_input_shape(MODEL_PATH, INPUT_RESOLUTION)
engine = compile_model(model_path, batch_size=BATCH_SIZE)
print(f"Engine info: {engine}")

image = cv2.imread(IMAGE_PATH)
batch = preprocess_image(image=image, image_size=INPUT_RESOLUTION)
outputs = engine.run([batch])[0]
results = postprocess_nms(outputs)[0]
print(results)
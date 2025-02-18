import cv2
from processing.image.utils import read_grayscale


def threshold_method(input_image_path, threshold_type):
    image_data = read_grayscale(input_image_path)
    return cv2.threshold(image_data, 127, 255, threshold_type)

import cv2
from processing.image.utils import read_grayscale


def interpolation_method(input_image_path, size, interpolation_type):
    image_data = read_grayscale(input_image_path)
    return cv2.resize(image_data, size, interpolation_type)

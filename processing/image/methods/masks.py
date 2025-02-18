from processing.image.utils import read_grayscale
import cv2


def mask_invert_method(image_file_path):
    image_data = read_grayscale(image_file_path)
    return cv2.bitwise_not(image_data)

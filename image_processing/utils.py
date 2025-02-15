import cv2


def read_grayscale(image_path):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

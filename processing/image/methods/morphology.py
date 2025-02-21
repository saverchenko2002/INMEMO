from processing.image.utils import read_grayscale

import numpy as np
import cv2


def dilation_method(image_path, kernel_size, iterations):
    image = read_grayscale(image_path)
    kernel = np.ones(kernel_size, np.uint8)
    return cv2.dilate(image, kernel, iterations)


def erosion_method(image_path, kernel_size, iterations):
    image = read_grayscale(image_path)
    kernel = np.ones(kernel_size, np.uint8)
    return cv2.erode(image, kernel, iterations)


def morphology_method(image_path, kernel_size, morphology_type):
    image = read_grayscale(image_path)
    kernel_size = np.ones(kernel_size, np.uint8)
    return cv2.morphologyEx(image, morphology_type, kernel_size)

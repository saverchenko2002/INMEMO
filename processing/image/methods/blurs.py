import cv2

from processing.image.utils import read_grayscale


def gaussian_blur_method(image_path, kernel_size, sigma_x, sigma_y):
    image_data = read_grayscale(image_path)
    image_data = cv2.GaussianBlur(image_data, kernel_size, sigma_x, sigma_y)
    return image_data

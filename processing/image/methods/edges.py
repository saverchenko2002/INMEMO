import cv2

from processing.image.utils import read_grayscale


def canny_method(image_path, threshold1, threshold2, aperture_size, l2gradient):
    image_data = read_grayscale(image_path)
    return cv2.Canny(image_data, threshold1, threshold2, apertureSize=aperture_size, L2gradient=l2gradient)

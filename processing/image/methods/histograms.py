from processing.image.utils import read_grayscale
import cv2


def ghe_method(image_path):
    image_data = read_grayscale(image_path)
    return cv2.equalizeHist(image_data)


def clahe_method(image_path, clip_limit, tile_grid_size: (int, int)):
    image_data = read_grayscale(image_path)
    clahe = cv2.createCLAHE(clip_limit, tile_grid_size)
    return clahe.apply(image_data)

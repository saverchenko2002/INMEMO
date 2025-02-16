import cv2
import matplotlib.pyplot as plt


def read_grayscale(image_path):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


def save_image(image_path, image_data):
    plt.imsave(image_path, image_data)
    return image_path

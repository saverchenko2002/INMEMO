import cv2
import matplotlib.pyplot as plt
import os


def read_grayscale(image_path):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


def save_image(image_path, image_data, unique_filename=False):
    filename = image_path
    if unique_filename:
        filename = get_unique_filename(os.path.dirname(image_path), image_path)
    plt.imsave(filename, image_data)
    return filename


def get_unique_filename(directory, filename):
    name, ext = os.path.splitext(filename)
    new_filename = filename
    counter = 1

    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{name}_{counter}{ext}"
        counter += 1

    return os.path.normpath(new_filename)

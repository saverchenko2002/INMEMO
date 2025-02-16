import numpy as np
from sklearn.cluster import KMeans
from image_processing.utils import read_grayscale
import matplotlib.pyplot as plt
import os


def kmeans_method(image_path, clustering_directory, k_number):

    clustering_image_paths = set()

    image = read_grayscale(image_path)

    pixels = image.reshape((-1, 1))

    kmeans = KMeans(n_clusters=k_number, init='k-means++', max_iter=300, n_init=10)

    kmeans.fit(pixels)

    labels = kmeans.labels_

    segmented_image = labels.reshape(image.shape)

    segmented_image = np.uint8(255*segmented_image/(k_number-1))

    unique_colors = np.unique(segmented_image)

    for color in unique_colors:
        mask = (segmented_image == color).astype(np.uint8) * 255
        file_name = os.path.join(clustering_directory, f'cluster_{color}.png')
        plt.imsave(file_name, mask)
        clustering_image_paths.add(file_name)

    segmented_file_name = os.path.join(clustering_directory, 'segmented.png')

    plt.imsave(segmented_file_name, segmented_image)

    clustering_image_paths.add(segmented_file_name)

    return clustering_image_paths

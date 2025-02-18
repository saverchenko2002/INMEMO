import numpy as np
from sklearn.cluster import KMeans
from processing.image.utils import read_grayscale
import os
from processing.image.utils import save_image


#не должно тут сейвов быть думаю)))
def kmeans_method(image_file_path, clustering_directory_path, k_number):

    clustering_image_paths = []

    image = read_grayscale(image_file_path)

    pixels = image.reshape((-1, 1))

    kmeans = KMeans(n_clusters=k_number, init='k-means++', max_iter=300, n_init=10)
    kmeans.fit(pixels)
    labels = kmeans.labels_

    segmented_image = labels.reshape(image.shape)
    segmented_image = np.uint8(255*segmented_image/(k_number-1))

    unique_colors = np.unique(segmented_image)

    segmented_file_name = os.path.join(clustering_directory_path, 'segmented.png')

    segmented_file_name = save_image(segmented_file_name, segmented_image, unique_filename=True)

    clustering_image_paths.append(segmented_file_name)

    for color in unique_colors:
        mask = (segmented_image == color).astype(np.uint8) * 255
        file_name = os.path.join(clustering_directory_path, f'cluster_{color}.png')
        file_name = save_image(file_name, mask, unique_filename=True)
        clustering_image_paths.append(file_name)



    return clustering_image_paths

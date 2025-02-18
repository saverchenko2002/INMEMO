from processing.image.methods.masks import mask_invert_method


def perform_invert_mask(image_file_path):
    image_data = mask_invert_method(image_file_path)
    return image_file_path, image_data

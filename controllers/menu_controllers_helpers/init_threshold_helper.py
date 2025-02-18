from processing.image.methods.threshold import threshold_method
import os
from processing.image.constants import ThresholdConstants

def perform_threshold(image_path, threshold_type):
    threshold_type_cv2 = ThresholdConstants[threshold_type].value
    _, image_data = threshold_method(image_path, threshold_type_cv2)
    file_name = f'{os.path.splitext(os.path.basename(image_path))[0]}_{threshold_type}.png'
    file_path = os.path.join(os.path.dirname(image_path), file_name)
    return file_path, image_data

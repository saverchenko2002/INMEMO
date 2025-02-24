import cv2

def canny_method(image_data, threshold1, threshold2, aperture_size, l2gradient):
    return cv2.Canny(image_data, threshold1, threshold2, apertureSize=aperture_size, L2gradient=l2gradient)


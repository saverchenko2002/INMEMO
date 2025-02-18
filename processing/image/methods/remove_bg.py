from rembg import remove
import cv2

def rembg_method(input_image_path):
    input_image = cv2.imread(input_image_path)
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGBA)
    return remove(input_image, alpha_matting=True)


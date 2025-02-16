import cv2

from enum import Enum


#https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
class MorphologicalConstants(Enum):
    MORPH_DILATION = None
    MORPH_EROSION = None
    MORPH_OPEN = cv2.MORPH_OPEN
    MORPH_CLOSE = cv2.MORPH_CLOSE
    MORPH_GRADIENT = cv2.MORPH_GRADIENT
    MORPH_TOPHAT = cv2.MORPH_TOPHAT
    MORPH_BLACKHAT = cv2.MORPH_BLACKHAT

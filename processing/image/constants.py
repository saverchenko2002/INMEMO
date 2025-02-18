import cv2

from enum import Enum


#https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
class MorphologicalConstants(Enum):
    MORPH_DILATION = "MORPH_DILATION"
    MORPH_EROSION = "MORPH_EROSION"
    MORPH_OPEN = cv2.MORPH_OPEN
    MORPH_CLOSE = cv2.MORPH_CLOSE
    MORPH_GRADIENT = cv2.MORPH_GRADIENT
    MORPH_TOPHAT = cv2.MORPH_TOPHAT
    MORPH_BLACKHAT = cv2.MORPH_BLACKHAT


class ThresholdConstants(Enum):
    THRESH_BINARY = cv2.THRESH_BINARY


class InterpolationConstants(Enum):
    INTER_NEAREST = cv2.INTER_NEAREST
    INTER_LINEAR = cv2.INTER_LINEAR
    INTER_CUBIC = cv2.INTER_CUBIC
    INTER_LANCZOS = cv2.INTER_LANCZOS4

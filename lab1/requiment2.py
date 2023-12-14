import cv2
import matplotlib.pyplot as plt
import numpy as np
from setting import *
# 2. Image transformation
# - Convert the loaded color image to grayscale.
# - Scale image with double weight and height size.
# - Applying points operations on the resized image.
# - Display the grayscale image and transformed images after each operation.
def convert_to_grayscale(image_path: str) -> None:
    image = cv2.imread(f"{SOURCE_IMAGES}/{image_path}")
    output_path = f'{DES_IMAGES}/req2-gray-{image_path.split(".")[0]}.png'
    grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, grayscale_img)

def x2_image(image_path: str) -> str:
    """
    In this funtion, I well return image name as a variable for contrast_adjustment function bellow
    """
    image = cv2.imread(f"{SOURCE_IMAGES}/{image_path}")
    output_path = f'{DES_IMAGES}/req2-x2-{image_path.split(".")[0]}.png'
    height, width = image.shape[:2]
    scaled_img = cv2.resize(image, (2 * width, 2 * height))
    cv2.imwrite(output_path, scaled_img)
    return output_path.split("/")[1]

def contrast_adjustment(image_path: str) -> None:
    """
    In this funtion, we will x2 contrast adjustment base on x2 scale image
    """
    x2image = x2_image(image_path)
    image = cv2.imread(f"{DES_IMAGES}/{x2image}")
    contraste_number = 2
    contrasted = cv2.convertScaleAbs(image, alpha=contraste_number)
    output_path = f'{DES_IMAGES}/req2-x2contrast-{image_path.split(".")[0]}.png'
    cv2.imwrite(output_path, contrasted)


if __name__ == "__main__":
    convert_to_grayscale(DEFAULT_IMAGES)
    print(x2_image(DEFAULT_IMAGES))

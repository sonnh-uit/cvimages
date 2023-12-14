import cv2
import matplotlib.pyplot as plt
import numpy as np
from setting import *

# 1. Image Loading and Displaying
# - Load an color image of your choice.
# - Display the loaded image.

def load(image_path: str) -> np:
    image = cv2.imread(f"{SOURCE_IMAGES}/{image_path}")
    output_path = f'{DES_IMAGES}/req1-{image_path.split(".")[0]}.png'
    cv2.imwrite(output_path, image)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.show()
    plt.close()
    return image

if __name__ == "__main__":
    load(DEFAULT_IMAGES)


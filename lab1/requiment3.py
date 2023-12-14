import cv2
import matplotlib.pyplot as plt
import numpy as np
from setting import *

# 3. Image enhancement
# - Enhance the image contrast by using global histogram equalization
# - Enhance the image contrast by using adaptive histogram equalization
#  - Enhance the image by average; Gaussian and median filters (blur; GaussianBlur; medianBlur). Experiment with 4 different kernel sizes and observe the effects on the filtered images.
# - Display all the result images with its histogram.

def save_histogram(image_path: str):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 2)
    plt.hist(image.ravel(), 256, [0, 256])

    output_path = f'{DES_IMAGES}/req3-his-{image_path.split("/")[1].split(".")[0]}.png'
    plt.title(f'req3-his-{image_path.split("/")[1].split(".")[0]}')
    plt.savefig(output_path)
    plt.close()

def global_equalization(image_path: str) -> None:
    save_histogram(f"{SOURCE_IMAGES}/{image_path}")
    
    image = cv2.imread(f"{SOURCE_IMAGES}/{image_path}", cv2.IMREAD_GRAYSCALE)
    global_hist_equalized = cv2.equalizeHist(image)
    output_path = f'{DES_IMAGES}/req3-global-{image_path.split(".")[0]}.png'
    cv2.imwrite(output_path, global_hist_equalized)
   
    save_histogram(output_path)


def adaptive_equalization(image_path: str) -> None:
    image = cv2.imread(f"{SOURCE_IMAGES}/{image_path}", cv2.IMREAD_GRAYSCALE)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    adaptive_equalized = clahe.apply(image)
    
    output_path = f'{DES_IMAGES}/req3-adap-{image_path.split(".")[0]}.png'
    cv2.imwrite(output_path, adaptive_equalized)
    save_histogram(output_path)
  
def kernel_equalization(image_path: str) -> None:
    image = cv2.imread(f"{SOURCE_IMAGES}/{image_path}", cv2.IMREAD_GRAYSCALE)

    kernel_sizes = [1, 3, 5, 9]
    for kernel_size in kernel_sizes:
        # Average Filtering
        average_filtered = cv2.blur(image, (kernel_size, kernel_size))
        output_path = f'{DES_IMAGES}/req3-ker-{kernel_size}-Average-{image_path.split(".")[0]}.png'
        cv2.imwrite(output_path, average_filtered)
        save_histogram(output_path)

        # Gaussian Filtering
        gaussian_filtered = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
        output_path = f'{DES_IMAGES}/req3-ker-{kernel_size}-Gaussian-{image_path.split(".")[0]}.png'
        cv2.imwrite(output_path, gaussian_filtered)
        save_histogram(output_path)
    
        # Median Filtering
        median_filtered = cv2.medianBlur(image, kernel_size)
        output_path = f'{DES_IMAGES}/req3-ker-{kernel_size}-Median-{image_path.split(".")[0]}.png'
        cv2.imwrite(output_path, median_filtered)
        save_histogram(output_path)
      
   

if __name__ == "__main__":
    global_equalization(DEFAULT_IMAGES)


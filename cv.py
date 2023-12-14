import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load an image
def print_histogram(image_path: str):
    image = cv2.imread(f"images/{image_path}", cv2.IMREAD_GRAYSCALE)

    # Calculate histogram
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])

    # Normalize the histogram
    hist_normalized = hist / sum(hist)

    # Create a bar plot
    plt.bar(range(256), hist_normalized, color='black', alpha=1)
    plt.title('Image Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Normalized Frequency')

    # Save the histogram plot as an image
    histogram_image_path = f"results/histogram-{image_path}.png"
    plt.savefig(histogram_image_path)
    plt.close()

def invert_image(image_path: str):
    
    original_image = cv2.imread(f"images/{image_path}")

# Invert the image
    inverted_image = cv2.bitwise_not(original_image)

    # Save the inverted image
    inverted_image_path = f'results/inverted_image-{image_path}.png'
    cv2.imwrite(inverted_image_path, inverted_image)
    plt.imshow(cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.savefig(inverted_image_path, bbox_inches='tight', pad_inches=0)
    plt.close()

def enhance_and_save(image_path):
    # Load the image
    original_image = cv2.imread(f"images/{image_path}")
    save_path = f"results/enhance-{image_path}.png"
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Apply contrast stretching for image enhancement
    min_val = np.min(gray_image)
    max_val = np.max(gray_image)
    enhanced_image = ((gray_image - min_val) / (max_val - min_val) * 255).astype(np.uint8)

    # Save the enhanced image using matplotlib
    plt.imshow(enhanced_image, cmap='gray')
    plt.axis('off')
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    plt.close()

print_histogram("2.jpg")
print_histogram("enhance-2.jpg.png")
# enhance_and_save("2.jpg")
from PIL import Image
import numpy as np

def detect_lsb_steganography(image_path):
    image = Image.open(image_path)
    image_data = np.array(image)

    lsb_data = image_data & 1
    lsb_image = Image.fromarray((lsb_data * 255).astype(np.uint8))

    lsb_image.show()

# Test image
detect_lsb_steganography("hacker.jpg")
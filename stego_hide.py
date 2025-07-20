from PIL import Image
import stepic

# Load the original image
img = Image.open("hacker.jpg")

# Secret hacker message 🔐
secret = "If you’re reading this, you’ve already been compromised 🕵‍♀"

# Encode the message into the image
encoded_img = stepic.encode(img, secret.encode())

# Save the new image with hidden message
encoded_img.save("hacker_hidden.png")

print("[+] Secret message embedded successfully into 'hacker_hidden.png'")
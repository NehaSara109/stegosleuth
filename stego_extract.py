from PIL import Image
import stepic

# Load the image with the hidden message
img = Image.open("hacker_hidden.png")

# Extract the hidden message
secret = stepic.decode(img)

print("[+] Hidden message extracted:")
print(secret)
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image

def embed_message():
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
    if not img_path:
        return

    img = Image.open(img_path)
    message = "If you’re reading this, you’ve already been compromised 🕵‍♀#"

    binary_message = ''.join([format(ord(char), "08b") for char in message])
    pixels = list(img.getdata())

    new_pixels = []
    message_index = 0
    message_length = len(binary_message)

    for pixel in pixels:
        r, g, b = pixel[:3]
        if message_index < message_length:
            r = (r & ~1) | int(binary_message[message_index])
            message_index += 1
        if message_index < message_length:
            g = (g & ~1) | int(binary_message[message_index])
            message_index += 1
        if message_index < message_length:
            b = (b & ~1) | int(binary_message[message_index])
            message_index += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Success", f"Message hidden in: {save_path}")

def extract_message():
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".png", ".bmp")])
    if not image_path:
        return

    img = Image.open(image_path)
    binary_data = ""
    hidden_message = ""

    img_data = img.getdata()

    for pixel in img_data:
        for channel in pixel[:3]:  # Only RGB channels
            binary_data += str(channel & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    for byte in all_bytes:
        char = chr(int(byte, 2))
        if char == "#":
            break
        hidden_message += char

    messagebox.showinfo("Hidden Message", f"The hidden message is:\n\n{hidden_message}")

# GUI setup
root = Tk()
root.title("StegoSleuth - Steganography Tool")
root.geometry("400x200")

Label(root, text="StegoSleuth", font=("Helvetica", 16, "bold")).pack(pady=10)
Button(root, text="Hide Message", command=embed_message).pack(pady=10)
Button(root, text="Extract Message", command=extract_message).pack(pady=10)

root.mainloop()
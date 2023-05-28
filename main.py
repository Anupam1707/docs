from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO
import fetchify
import time
import threading
import json
import random

# Create a Tkinter window
window = Tk()
window.title("Image Display")
window.attributes('-fullscreen', True)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()

main = Frame(window)
main.pack()

image_content = fetchify.fetch("Intro.png", "docs", image=True)
image = Image.open(BytesIO(image_content))
image = image.resize((w, h))
photo = ImageTk.PhotoImage(image)
label = Label(main, image=photo)
label.image = photo  # Save a reference to the image
label.pack()

 
def display(picture):
    global label
    label.pack_forget()
    # Get image from Internet
    image_content = fetchify.fetch(picture, "docs", image=True)

    # Create a PIL Image object from the image content
    image = Image.open(BytesIO(image_content))
    width, height = image.size

    # Resize the image if necessary
    if width <= w and height >= h:
        image = image.resize((width, height))
    else:
        aspect_ratio = min(w / width, h / height)
        new_size = (int(width * aspect_ratio), int(height * aspect_ratio))
        image = image.resize(new_size, Image.LANCZOS)

    # Convert the PIL Image to Tkinter PhotoImage
    photo = ImageTk.PhotoImage(image)

    # Create a Tkinter label with the image
    label = Label(main, image=photo)
    label.image = photo  # Save a reference to the image
    label.pack()

def display_images(images):
    time.sleep(5)
    while True:
        image = random.choice(images)
        display(image)
        time.sleep(7)

data = requests.get("https://api.github.com/repos/Anupam1707/docs/contents").json()
pics = [file['name'] for file in data if file['type'] == 'file']
pics.remove("README.md")
pics.remove("main.py")
pics.remove("Intro.png")

# Create a thread for displaying images
display_thread = threading.Thread(target=display_images, args=(pics,))
display_thread.start()

# Start the Tkinter event loop
window.mainloop()

from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO
import fetchify

# Create a Tkinter window
window = Tk()
window.title("Image Display")
window.attributes('-fullscreen', True)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()

main = Frame(window)
main.pack()

def display(picture):
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

        # Convert the PIL Image to Tkinter PhotoImage
    photo = ImageTk.PhotoImage(image)

    # Create a Tkinter label with the image
    label = Label(main, image=photo)
    label.image = photo  # Save a reference to the image
    label.pack()

display("App.png")

# Start the Tkinter event loop
window.mainloop()

import tkinter as tk
from captcha.image import ImageCaptcha
import random
from PIL import Image, ImageTk  # To handle image display in tkinter

# Create a window
root = tk.Tk()
root.title("CAPTCHA Verification")

# Function to generate a new CAPTCHA
def generate_captcha():
    global num  # Make num global to access it in the verify function
    num = random.randint(100000, 999999)  # Generate random number
    cap = ImageCaptcha(width=200, height=100)
    captcha_image = cap.create_captcha_image(str(num), color='white', background='black')
    captcha_image.save("captcha.png")
    load_captcha()  # Update the CAPTCHA image

# Function to load and display the CAPTCHA
def load_captcha():
    img = Image.open("captcha.png")
    img = ImageTk.PhotoImage(img)
    captcha_label.config(image=img)
    captcha_label.image = img  # Keep reference to avoid garbage collection

# Function to verify the CAPTCHA
def verify_captcha():
    entered_text = text_field.get()
    if entered_text == str(num):
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Incorrect! Please try again.", fg="red")
    
    # Clear the text field
    text_field.delete(0, 'end')
    
    # Generate a new CAPTCHA for the next attempt
    generate_captcha()

# Create and display CAPTCHA image in the window
captcha_label = tk.Label(root)
captcha_label.pack()

# Initial CAPTCHA generation
generate_captcha()

# Create a label for instructions
label = tk.Label(root, text="Enter the CAPTCHA:")
label.pack()

# Create a text field (Entry widget) to input CAPTCHA
text_field = tk.Entry(root, width=40)
text_field.pack()

# Create a button to verify the CAPTCHA
button = tk.Button(root, text="Submit", command=verify_captcha)
button.pack()

# Create a label to show the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()

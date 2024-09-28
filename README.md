CAPTCHA Verification using Python and Tkinter

Description :

This project is a simple CAPTCHA verification system built using Python's `Tkinter` for the GUI, `captcha` library to generate CAPTCHA images, and `PIL` (Python Imaging Library) to handle and display images in the Tkinter window.

The program generates a new CAPTCHA image each time the user opens the application or submits a response. The user is prompted to enter the correct CAPTCHA number displayed in the image. After entering the CAPTCHA, the program checks if the entered text matches the generated CAPTCHA, and provides feedback accordingly.

Features :

- Dynamically generates random numeric CAPTCHA images using the `captcha` library.
- Verifies user input and displays feedback (either "Correct!" or "Incorrect!").
- Automatically generates a new CAPTCHA image after every verification attempt.
- Simple and intuitive user interface using `Tkinter`.

Requirements :

- Python 3.x
- `captcha` library (for generating CAPTCHA images)
- `Pillow` library (for handling and displaying images in Tkinter)

Installation :

1. Clone or download the repository to your local machine.
2. Install the required Python packages by running:

bash(cmd) :
pip install captcha pillow


Usage :

1. Run the `captcha_verification.py` script:

bash(cmd) :
python captcha_verification.py

2. A window will appear displaying a CAPTCHA image and a text field.
3. Enter the correct CAPTCHA number shown in the image.
4. Click "Submit" to verify your input.
5. The program will display whether the input was correct or incorrect, and will generate a new CAPTCHA image for the next attempt.

Code Breakdown :

- CAPTCHA Generation : 
   - The function `generate_captcha()` creates a random 6-digit number and generates a corresponding CAPTCHA image using the `ImageCaptcha` class from the `captcha` library.
   
- CAPTCHA Display : 
   - The `load_captcha()` function loads the CAPTCHA image from disk and displays it in the Tkinter window using `PIL.Image` and `ImageTk.PhotoImage`.

- Verification : 
   - When the user clicks "Submit", the function `verify_captcha()` compares the entered text with the generated CAPTCHA number. Based on the result, it displays feedback ("Correct!" or "Incorrect!") and generates a new CAPTCHA image.

Dependencies :

- `tkinter`: Standard Python library for GUI applications.
- `captcha`: A Python library for generating CAPTCHA images.
- `Pillow`: Python Imaging Library (PIL), used for image handling in Tkinter.

License :

This project is licensed under the MIT License.

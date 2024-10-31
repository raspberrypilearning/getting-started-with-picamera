## Take still pictures with Python code

Now use the Camera Module and Python to take some still pictures.

`picamzero` has a very convenient function (`take_photo`) for capturing images. 

--- task ---
- Type in and run the code

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 
---
from picamzero import Camera
import os

home_dir = os.environ['HOME'] #set the location of your home directory
cam = Camera()

cam.start_preview()
cam.take_photo(f"{home_dir}/Desktop/new_image.jpg") #save the image to your desktop
cam.stop_preview()
--- /code ---
--- /task ---

A preview window will open. 
Your file will appear on your Desktop 
The preview will close.

You can also use `capture_sequence` to capture multiple images.

This code captures three images and uses a 2 second delay between each image. 

--- task ---
- Amend line 6 in your code:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 6
---
from picamzero import Camera
import os

home_dir = os.environ['HOME']
cam = Camera()

cam.start_preview()
cam.capture_sequence(f"{home_dir}/Desktop/sequence.jpg", num_images=3, interval=2)
cam.stop_preview()
--- /code ---
--- /task ---

--- task ---
- Run the code again
--- /task ---

The camera should take one picture every two seconds. Once the third picture is taken, the preview closes.

--- task ---
- Look at your desktop to find the three new pictures.
--- /task ---

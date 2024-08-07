## How to change the image settings and add image effects

The Python `picamera2` library provides a number of effects and configurations to change how your images look.

**Note:** some settings only affect the preview and not the captured image, some affect only the captured image, and many others affect both.

--- collapse ---

---
title: Set the image resolution
---

You can change the resolution of the image that the Camera Module takes.

Each Camera Module has different resolution capabilities.

The V1 Module has a maximum resolution of `2592×1944` so we will try that!

- Use the following code to set the resolution to maximum and take a picture.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights:
---
from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()

picam2.preview_configuration.size = (2592, 1944)
picam2.start(show_preview=True)

sleep(2)

picam2.capture_file("max.jpg")
picam2.close()

--- /code ---

The minimum resolution is `64×64`.

- Try taking a picture with the minimum resolution.

--- /collapse ---

--- collapse ---

---
title: Set different preview and capture resolutions
---

- Use the following code to set the preview resolution at a lower resolution to the capture image.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 6-8
---
from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()

picam2.preview_configuration.sensor.output_size = (2592, 1944)
picam2.preview_configuration.main.size = (800,600)
picam2.configure("preview")
picam2.start(show_preview=True)

sleep(2)

picam2.capture_file("max.jpg")
picam2.close()

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Add text to your image
---

The text on line 13 is added to the photo at the origin location set on line 9.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 13, 36
---

from picamera2 import Picamera2, MappedArray
import cv2, time

resolution = (2592, 1944)

def apply_text(request):
    # Text options
    colour = (255, 255, 255)
    origin = (0, 60)
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 2
    thickness = 2
    text = "Looking good!"
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, text, origin, font, scale, colour, thickness)

# Create camera object
picam2 = Picamera2()

# Create two separate configs - one for preview and one for capture.
# Make sure the preview is the same resolution as the capture, to make
# sure the overlay stays the same size 
capture_config = picam2.create_still_configuration({"size": resolution})
preview_config = picam2.create_preview_configuration({"size": resolution})

# Set the current config as the preview config
picam2.configure(preview_config)

# Add the timestamp
picam2.pre_callback = apply_text
# Start the camera
picam2.start(show_preview=True)
time.sleep(2)

# Switch to the capture config and then take a picture 
image = picam2.switch_mode_and_capture_file(capture_config, "textOnPhoto.jpg")

# Close the camera
picam2.close()

--- /code ---

Try changing the text and origin location.

You can also experiment with: 

- photo resolution (line 4)
- text options (lines 8-12)

### I want to add a timestamp

Look at the highlighted lines to see the changes.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 13, 37
---

from picamera2 import Picamera2, MappedArray
import cv2, time

resolution = (2592, 1944)

def apply_text(request):
    # Text options
    colour = (255, 255, 255)
    origin = (0, 60)
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 2
    thickness = 2
    text = time.strftime("%Y-%m-%d %X")
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, text, origin, font, scale, colour, thickness)

# Create camera object
picam2 = Picamera2()

# Create two separate configs - one for preview and one for capture.
# Make sure the preview is the same resolution as the capture, to make
# sure the overlay stays the same size 
capture_config = picam2.create_still_configuration({"size": resolution})
preview_config = picam2.create_preview_configuration({"size": resolution})

# Set the current config as the preview config
picam2.configure(preview_config)

# Add the timestamp
picam2.pre_callback = apply_text

# Start the camera
picam2.start(show_preview=True)
time.sleep(2)

# Switch to the capture config and then take a picture 
image = picam2.switch_mode_and_capture_file(capture_config, "timestampedPhoto.jpg")

# Close the camera
picam2.close()

--- /code ---

--- /collapse ---

### Add cool image effects

--- collapse ---

---
title: Make the image greyscale
---

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 12, 13, 18, 19
---

from picamera2 import Picamera2
from time import sleep
import cv2

picam2 = Picamera2()

picam2.preview_configuration.size = (2592, 1944)
picam2.start(show_preview=True)

sleep(2)

picam2.capture_file("toProcess.jpg")
picam2.close()

img = cv2.imread("toProcess.jpg")

# Convert to greyscale
greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("greyscaleImage.jpg", greyscale)

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Create a negative effect
---

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 19
---

from picamera2 import Picamera2
from time import sleep
import cv2

picam2 = Picamera2()

picam2.preview_configuration.size = (2592, 1944)
picam2.start(show_preview=True)

sleep(2)

picam2.capture_file("toProcess.jpg")
picam2.close()

img = cv2.imread("toProcess.jpg")

# Convert to negative
greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("negativeImage.jpg", 255 - greyscale)

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Create a sketch effect
---

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 19-23
---

from picamera2 import Picamera2
from time import sleep
import cv2

picam2 = Picamera2()

picam2.preview_configuration.size = (2592, 1944)
picam2.start(show_preview=True)

sleep(2)

picam2.capture_file("toProcess.jpg")
picam2.close()

img = cv2.imread("toProcess.jpg")

# Convert to sketch
greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted = 255 - greyscale
blur_inverted = cv2.GaussianBlur(inverted, (125, 125), 0)
inverted_blur = 255 - blur_inverted
sketch = cv2.divide(greyscale, inverted_blur, scale=256)
cv2.imwrite("sketchImage.jpg", sketch)

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Set the image exposure, gain and contrast levels
---

This code demonstrates how to set the camera controls (line 13).

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 13
---

from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()

# Show unaltered image
picam2.start(show_preview=True)
sleep(2)
picam2.stop_preview()
picam2.stop()

# Alter the image levels
controls = {"ExposureTime": 10000, "AnalogueGain": 1.0, "Contrast": 2}
preview_config = picam2.create_preview_configuration(controls=controls)
picam2.configure(preview_config)

# Show altered image
picam2.start(show_preview=True)
sleep(2)
picam2.close()

--- /code ---

Experiment with different exposure times, gain levels and contrast values.

--- /collapse ---
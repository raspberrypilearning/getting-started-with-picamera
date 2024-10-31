## How to change the image settings and add image effects

The Python `picamzero` library provides a number of effects and configurations to change how your images look.

**Note:** some settings only affect the preview and not the captured image, some affect only the captured image, and many others affect both.

--- collapse ---

---
title: Set the image resolution
---

You can change the resolution of the image that the Camera Module takes.

Each Camera Module has different resolution capabilities.

The V1 Module has a maximum still resolution of `2592×1944` so we will try that!
(For other camera versions, check the specs on [this page](https://www.raspberrypi.com/documentation/accessories/camera.html#hardware-specification).

- Use the following code to set the resolution to maximum and take a picture.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights:
---
from picamzero import Camera
from time import sleep
import os

home_dir = os.environ['HOME']
cam = Camera()
cam.still_size = (2592, 1944)
cam.start_preview()

sleep(2)

cam.take_photo(f"{home_dir}/Desktop/max.jpg")
cam.stop_preview()

--- /code ---

The minimum resolution is `15x15`.

--- /collapse ---

--- collapse ---

---
title: Set different preview and image resolutions
---

- Use the following code to set the preview resolution at a lower resolution to the capture image.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 6-7
---
from picamzero import Camera
from time import sleep
import os

home_dir = os.environ['HOME']
cam = Camera()
cam.preview_size = (1920, 1080)
cam.still_size = (2592, 1944)

cam.start_preview()

sleep(2)

cam.take_photo(f"{home_dir}/Desktop/max.jpg")
cam.stop_preview()

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Add text to your image
---

The text on line 5, "Hello, world!" is added to the photo taken on line 6.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 5
---
from picamzero import Camera
import os

home_dir = os.environ['HOME']
cam = Camera()
cam.annotate("Hello, world!")

cam.start_preview()
cam.take_photo(f"{home_dir}/Desktop/textOnPhoto.jpg")
cam.stop_preview()
--- /code ---

The `annotate` method allows you to change where the text is positioned using the `position` argument. You can also [change the text colour, font, and background colour](https://raspberrypifoundation.github.io/picamera-zero/photo_methods/annotate). 

### Add a timestamp

Look at the highlighted lines to see the changes.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 2, 8
---
from picamzero import Camera
from datetime import datetime
import os

home_dir = os.environ['HOME']
cam = Camera()

cam.start_preview()
cam.annotate(str(datetime.now()))
cam.take_photo(f"{home_dir}/Desktop/textOnPhoto.jpg")
cam.stop_preview()
--- /code ---

--- /collapse ---

### Add image effects

--- collapse ---

---
title: Take a black and white photograph
---

You can take pictures in black and white using the greyscale setting.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 5
---
from picamzero import Camera
from time import sleep

cam = Camera()
cam.greyscale = True
cam.start_preview()

sleep(2)

cam.take_photo(f"{home_dir}/Desktop/bnw.jpg")
cam.stop_preview()

--- /code ---

--- /collapse ---


--- collapse ---

---
title: Set the image exposure, gain and contrast levels
---

This code demonstrates how to set the camera controls for exposure, gain and contrast.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 7-9
---
from picamzero import Camera
from time import sleep

cam = Camera()

# Alter the image levels
cam.gain = 1.0
cam.contrast = 2
cam.exposure = 1000000

# Wait a second for changes to take effect
sleep(1)

# Show altered image
cam.start_preview()
sleep(2)
cam.stop_preview()


--- /code ---

Experiment with different exposure times, gain levels and contrast values.

--- /collapse ---

--- collapse ---

---
title: Set the brightness
---

This code demonstrates how to set the brightness control.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 7
---
from picamzero import Camera
from time import sleep

cam = Camera()

# Alter the image levels
cam.brightness = 0.2

# Wait a second for changes to take effect
sleep(1)

# Show altered image
cam.start_preview()
sleep(2)
cam.stop_preview()


--- /code ---

--- /collapse ---

--- collapse ---

---
title: Set the white balance
---

You can set the white balance mode. Available modes are `auto`, `tungsten`, `fluorescent`, `indoor`, `daylight`, `cloudy`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 7
---
from picamzero import Camera
from time import sleep

cam = Camera()

# Alter the image levels
cam.white_balance = 'cloudy'

# Wait a second for changes to take effect
sleep(1)

# Show altered image
cam.start_preview()
sleep(2)
cam.stop_preview()


--- /code ---

--- /collapse ---


--- collapse ---

---
title: Create a negative effect
---
The negative effect is applied using the cv2 library to an image after it is captured, so it cannot be shown on the preview.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
from picamzero import Camera
from time import sleep
import cv2
import os

home_dir = os.environ['HOME']
cam = Camera()
rgb_array = cam.capture_array()

bgr_array = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2BGR)
negative_bgr_array = 255 - bgr_array
cv2.imwrite(f"{home_dir}/Desktop/negativeImage.jpg", negative_bgr_array)
--- /code ---

--- /collapse ---

--- collapse ---

---
title: Create a sketch effect
---
The sketch effect is applied to an image after it is captured, so it cannot be shown on the preview.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
from picamzero import Camera
from time import sleep
import cv2
import os

home_dir = os.environ['HOME']
cam = Camera()

sleep(2)

rgb_array = cam.capture_array()
img = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2BGR)

# Convert to sketch
greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted = 255 - greyscale
blur_inverted = cv2.GaussianBlur(inverted, (125, 125), 0)
inverted_blur = 255 - blur_inverted
sketch = cv2.divide(greyscale, inverted_blur, scale=256)
cv2.imwrite(f"{home_dir}/Desktop/sketchImage.jpg", sketch)
--- /code ---

--- /collapse ---
## How to change the image settings and add image effects

The Python `picamera2` library provides a number of effects and configurations to change how your images look.

**Note:** some settings only affect the preview and not the captured image, some affect only the captured image, and many others affect both.

### Set the image resolution

You can change the resolution of the image that the Camera Module takes.

Each Camera Module has different resolution capabilities.

The V1 Module has a maximum resolution of `2592×1944` so we will try that!

- Use the following code to set the resolution to maximum and take a picture.

    ```python
    from picamera2 import Picamera2
    from time import sleep
    
    picam2 = Picamera2()
    
    picam2.preview_configuration.size = (2592, 1944)
    picam2.start(show_preview=True)

    sleep(2)

    picam2.capture_file("max.jpg")
    picam2.stop_preview()
    ```

The minimum resolution is `64×64`.

- Try taking a picture with the minimum resolution.

### Set different preview and capture resolutions

- Use the following code to set the preview resolution at a lower resolution to the capture image.

    ```python
    from picamera2 import Picamera2
    from time import sleep

    picam2 = Picamera2()

    picam2.preview_configuration.sensor.output_size = (2592, 1944)
    picam2.preview_configuration.main.size = (800,600)
    picam2.configure("preview")
    picam2.start(show_preview=True)

    sleep(2)

    picam2.capture_file("max.jpg")
    picam2.stop_preview()
    ```

### Add text to your image

The text on line 13 is added to the photo at the origin location set on line 9.

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

--- collapse ---

---
title: I want to add a timestamp
---

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

### Change the brightness of the preview

You can change how bright the preview appears. The default brightness is `50`, and you can set it to any value between `0` and `100`.

* Run the following code to try this out:

    ```python
    picam2.start_preview()
    picam2.brightness = 70
    sleep(5)
    picam2.capture('/home/pi/Desktop/bright.jpg')
    picam2.stop_preview()
    ```

- The following loop adjusts the brightness and also adds text to display the current brightness level:

    ```python
    picam2.start_preview()
    for i in range(100):
        picam2.annotate_text = "Brightness: %s" % i
        picam2.brightness = i
        sleep(0.1)
    picam2.stop_preview()
    ```

### Change the contrast of the preview

Similarly to the preview brightness, you can change the contrast of the preview.

- Run the following code to try this out:

    ```python
    picam2.start_preview()
    for i in range(100):
        picam2.annotate_text = "Contrast: %s" % i
        picam2.contrast = i
        sleep(0.1)
    picam2.stop_preview()
    ```

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
line_highlights: 11, 12, 17, 18
---

from picamera2 import Picamera2
from time import sleep
import cv2

picam2 = Picamera2()

picam2.preview_configuration.size = (2592, 1944)
picam2.start(show_preview=True)

sleep(2)

picam2.capture_file("toProcess.jpg")
img = cv2.imread("toProcess.jpg")

picam2.stop_preview()

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
line_highlights: 18
---

from picamera2 import Picamera2
from time import sleep
import cv2

picam2 = Picamera2()

picam2.preview_configuration.size = (2592, 1944)
picam2.start(show_preview=True)

sleep(2)

picam2.capture_file("toProcess.jpg")
img = cv2.imread("toProcess.jpg")

picam2.stop_preview()

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
line_highlights: 18-22
---

from picamera2 import Picamera2
from time import sleep
import cv2

picam2 = Picamera2()

picam2.preview_configuration.size = (2592, 1944)
picam2.start(show_preview=True)

sleep(2)

picam2.capture_file("toProcess.jpg")
img = cv2.imread("toProcess.jpg")

picam2.stop_preview()

# Convert to sketch
greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted = 255 - greyscale
blur_inverted = cv2.GaussianBlur(inverted, (125, 125), 0)
inverted_blur = 255 - blur_inverted
sketch = cv2.divide(greyscale, inverted_blur, scale=256)
cv2.imwrite("sketchImage.jpg", sketch)

--- /code ---

--- /collapse ---

### Set the image exposure mode

You can use `picam2.exposure_mode` to set the exposure to a particular mode. 

The exposure mode options are:
* `off`
* `auto`
* `night`
* `nightpreview`
* `backlight`
* `spotlight`
* `sports`
* `snow`
* `beach`
* `verylong`
* `fixedfps`
* `antishake`
* `fireworks`

The default mode is `auto`.
    
* Pick an exposure mode and try it out:

    ```python
    picam2.start_preview()
    picam2.exposure_mode = 'beach'
    sleep(5)
    picam2.capture('/home/pi/Desktop/beach.jpg')
    picam2.stop_preview()
    ```

* You can loop over all the exposure modes with `picam2.EXPOSURE_MODES`, like you did for the image effects.

### Change the image white balance

You can use `picam2.awb_mode` to set the auto white balance to a preset mode. 

The available auto white balance modes are:
* `off`
* `auto`
* `sunlight`
* `cloudy`
* `shade`
* `tungsten`
* `fluorescent`
* `incandescent`
* `flash`
* `horizon`

The default is `auto`. 
    
* Pick an auto white balance mode and try it out:

    ```python
    picam2.start_preview()
    picam2.awb_mode = 'sunlight'
    sleep(5)
    picam2.capture('/home/pi/Desktop/sunlight.jpg')
    picam2.stop_preview()
    ```

* You can loop over all the auto white balance modes with `picam2.AWB_MODES`, like you did for the image effects.
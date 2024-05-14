## How to control the Camera Module with Python code

The Python `picamera2` library allows you to control your Camera Module and create amazing projects.

- Open a Python 3 editor, such as **Thonny Python IDE**:

    ![Open Thonny](images/thonny-app-menu.png)

- Open a new file and save it to your Desktop as `camera.py`. 

    **Note:** it's important that you **never save the file as `picamera2.py`**.

- Enter the following code:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---

from picamera2 import Picamera2, Preview
from time import sleep

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()
sleep(2)
picam2.stop_preview()

--- /code ---

- Save and run your program. The camera preview should be shown for five seconds and then close again. 
    
    **Note:** the camera preview only works when a monitor is connected to your Raspberry Pi or if you are using remote access (with VNC or Raspberry Pi Connect).

- If you need to rotate your preview, you can use vertical flip: `vflip=True` or horizontal flip: `hflip=True`. You need to import the `Transform` module from the `libcamera` library and add a `transform` parameter to your code:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 3, 6
---

from picamera2 import Picamera2, Preview
from time import sleep
from libcamera import Transform

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL, transform=Transform(hflip=True))
picam2.start()
sleep(2)
picam2.stop_preview()

--- /code ---

**Tip:** You can use combine `vflip` and `hflip` to achieve a 180 degree rotation.

```python
   Transform(hflip=True, vflip=True))
``` 
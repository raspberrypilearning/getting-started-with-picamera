## Take still pictures with Python code

Now use the Camera Module and Python to take some still pictures.

Picamera2 has a very convenient function (`start_and_capture_file`) for capturing images. 

```python
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_capture_file("Desktop/newimage.jpg")
picam2.stop_preview()
```

- Run the code

A preview window will open. 
Your file will appear on your Desktop 
The preview will close.

You can also use `start_and_capture_files` to capture multiple images.

This code captures three images and uses a 0.5 second delay between each image. 

- Amend line 4 in your code:

```python
picam2.start_and_capture_files("Desktop/sequence{:d}.jpg", num_files=3, delay=0.5)
```

- Run the code again

The camera should take one picture every five seconds. Once the third picture is taken, the preview closes. 

- Look at your Desktop to find the three new pictures.
## Recording video with Python code

Now record a video!

--- task ---
- Change line 8 in your code

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 8
---
from picamzero import Camera
import os

home_dir = os.environ['HOME']
cam = Camera()

cam.start_preview()
cam.record_video(f"{home_dir}/Desktop/new_video.mp4", duration=5)
cam.stop_preview()
--- /code ---
--- /task ---

--- task ---
- Run the code
--- /task ---

You should see a preview while the camera records 5 seconds of video and then closes the preview.

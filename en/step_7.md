## Recording video with Python code

Now record a video!

--- task ---
- Change line four in your code

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 5
---
from picamzero import Camera

cam = Camera()
cam.start_preview()
cam.record_video("~/Desktop/new_video.mp4", duration=5)
cam.stop_preview()
--- /code ---
--- /task ---

--- task ---
- Run the code
--- /task ---

You should see a preview while the camera records 5 seconds of video and then closes the preview.

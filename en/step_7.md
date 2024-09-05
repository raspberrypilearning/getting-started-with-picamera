## Recording video with Python code

Now record a video!

- Amend line four in your code

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
cam.record_video("Desktop/new_video.mp4", duration=5)
cam.stop_preview()
--- /code ---

- Run the code

Your Raspberry Pi should open a preview, record 5 seconds of video, and then close the preview.

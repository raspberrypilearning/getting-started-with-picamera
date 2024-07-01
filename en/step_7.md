## Recording video with Python code

Now record a video!

- Amend line four in your code

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 4
---
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_record_video("Desktop/new_video.mp4", duration=5, show_preview=True)
picam2.close()

--- /code ---

- Run the code

Your Raspberry Pi should open a preview, record 5 seconds of video, and then close the preview.
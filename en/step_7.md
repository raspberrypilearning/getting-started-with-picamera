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
picam2.start_and_record_video("Desktop/new_video.mp4", duration=5)
picam2.stop_preview()

--- /code ---

--- collapse ---

---
title: I'm not using a Raspberry Pi 5
---

You need to specify the encoder and output to use.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights:
---
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from time import sleep

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
picam2.start(show_preview=True)

encoder = H264Encoder(10000000)
output = FfmpegOutput('new_video.mp4')

picam2.start_recording(encoder, output)
sleep(5)
picam2.stop_recording()
picam2.stop_preview()

--- /code ---

**Tip:** The `10000000` is the bitrate.

--- /collapse ---

- Run the code

Your Raspberry Pi should open a preview, record 5 seconds of video, and then close the preview.
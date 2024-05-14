## Recording video with Python code

Now record a video!

- Amend your code

     ```python
    from picamera2 import Picamera2

    picam2 = Picamera2()
    picam2.start_and_record_video("Desktop/new_video.mp4", duration=5)
    picam2.stop_preview()
    ```

- Run the code

Your Raspberry Pi should open a preview, record 5 seconds of video, and then close the preview.
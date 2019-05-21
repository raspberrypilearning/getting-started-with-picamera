## Recording video

Now you've used the camera to take still pictures, you can move on to recording video.

- Amend your code to replace `capture()` with `start_recording()` and `stop_recording()`:

    ```python
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    ```

- Run the code; it will record 5 seconds of video and then close the preview.


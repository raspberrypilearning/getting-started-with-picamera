## Recording video

Now you've used the camera to take still pictures, you can move on to recording video.

- Amend your code to replace `capture()` with `start_recording()` and `stop_recording()`:

    ```python
    camera.start_preview()
    camera.start_recording('/home/pi/video.h264')
    sleep(10)
    camera.stop_recording()
    camera.stop_preview()
    ```

- Run the code; it will record 10 seconds of video and then close the preview.

- To play the video, you'll need to open a terminal window by clicking the black monitor icon in the taskbar:

    ![Open terminal](images/open-terminal.png)

- Type the following command and press **Enter** to play the video:

    ```bash
    omxplayer video.h264
    ```

    ![omxplayer](images/omxplayer.png)

- The video should play. It may actually play at a faster speed than what has been recorded, due to `omxplayer`'s fast frame rate.


## Controlling the camera with Python

Using the Python and `picamera` library allows you to control your camera module and use it create some amazing projects.

- Open a Python 3 editor, such as **Thonny Python IDE**:

    ![Open Thonny](images/thonny-app-menu.png)

- Open a new file and save it as `camera.py`. 

    **Note -** it's important that you **do not** save it as `picamera.py`

- Enter the following code:

    ```python
    from picamera import PiCamera
    from time import sleep

    camera = PiCamera()

    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    ```

- Save and run your prgram. The camera preview should be shown for 5 seconds, and then close. 

    ![Image preview](images/preview.jpg)
    
    **Note -** The camera preview only works when a monitor is connected to the Pi, so remote access (such as SSH and VNC) will not allow you to see the camera preview.

- If your preview was upside-down, you can rotate it with the following code:

    ```python
    camera = PiCamera()
    camera.rotation = 180
    ```

    You can rotate the image by `90`, `180`, or `270` degrees, or you can set it to `0` to reset.

- You can alter the transparency of the camera preview by setting an `alpha` level:

    ```python
    camera.start_preview(alpha=200)
    ```

    `alpha` can be any value between `0` and `255`.

    **Tip -** setting the alpha is a good idea because you will be able to see if any errors occur in your program while the preview is on.
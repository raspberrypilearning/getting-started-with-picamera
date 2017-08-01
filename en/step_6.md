## Still pictures

The most common use for the Camera Module is taking still pictures.

- Amend your code to reduce the `sleep` and add a `camera.capture()` line:

    ```python
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    ```

    It's important to sleep for at least 2 seconds before capturing, to give the sensor time to set its light levels.

- Run the code and you'll see the camera preview open for 5 seconds before capturing a still picture. You'll see the preview adjust to a different resolution momentarily as the picture is taken.

- You'll see your photo on the Desktop. Double-click the file icon to open it:

    ![Image on Desktop](images/desktop.png)

- Now try adding a loop to take five pictures in a row:

    ```python
    camera.start_preview()
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    camera.stop_preview()
    ```

    The variable `i` contains the current iteration number, from `0` to `4`, so the images will be saved as `image0.jpg`, `image1.jpg`, and so on.

- Run the code again and hold the camera in position. It will take one picture every five seconds.

- Once the fifth picture is taken, the preview will close. Now look at the images on your Desktop and you'll see five new pictures.


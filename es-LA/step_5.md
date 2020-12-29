## Cómo controlar el Módulo de Cámara con código Python

La biblioteca Python `picamera` te permite controlar tu Módulo de Cámara y crear proyectos increíbles.

- Abre un editor Python 3, como **Thonny Python IDE**:

    ![Open Thonny](images/thonny-app-menu.png)

- Abre un nuevo archivo y guárdalo como `camera.py`.

    **Nota:** es importante que **nunca guardes el archivo como `picamera.py`**.

- Escribe el siguiente código:

    ```python
    from picamera import PiCamera
    from time import sleep

    camera = PiCamera()

    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    ```

- Guarda y ejecuta tu programa. La vista previa de la cámara debería mostrarse durante cinco segundos y luego cerrarse nuevamente.

    ![Image preview](images/preview.jpg)

    **Note:** the camera preview only works when a monitor is connected to your Raspberry Pi. If you are using remote access (such as SSH or VNC), you won't' see the camera preview.

- If your preview is upside-down, you can rotate it by 180 degrees with the following code:

    ```python
    camera = PiCamera()
    camera.rotation = 180
    ```

    You can rotate the image by `90`, `180`, or `270` degrees. To reset the image, set `rotation` to `0` degrees.

It's best to make the preview slightly see-through so you can see whether errors occur in your program while the preview is on.

- Make the camera preview see-through by setting an `alpha` level:

    ```python
    camera.start_preview(alpha=200)
    ```

    The `alpha` value can be any number between `0` and `255`.
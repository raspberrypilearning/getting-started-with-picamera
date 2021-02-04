## Graba videos con código Python

¡Ahora graba un video!

- Modifica tu código para eliminar `capture()` y en su lugar agrega `start_recording()` y `stop_recording()`

    Tu código debería verse así:

    ```python
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    ```

- Ejecuta el código.

Tu Raspberry Pi debería abrir una vista previa, grabar 5 segundos de video y luego cerrar la vista previa.


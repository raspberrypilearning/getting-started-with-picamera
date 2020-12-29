## Take still pictures with Python code

Ahora usa el Módulo de Cámara y Python para capturar imágenes fijas.

- Modifica tu código para agregar una línea `camera.capture()`:

    ```python
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    ```

    **Nota:** es importante configurar `sleep` durante al menos dos segundos antes de capturar una imagen, ya que esto le da tiempo al sensor de la cámara para detectar los niveles de luz.

- Ejecuta el código.

Deberías ver la vista previa de la cámara abierta durante cinco segundos y luego debería capturarse una imagen fija. Mientras se está tomando la foto, puedes ver la vista previa ajustarse brevemente a una resolución diferente.

Tu nueva imagen se guardará en el Escritorio.

- Ahora agrega un ciclo para tomar cinco fotos seguidas:

    ```python
    camera.start_preview()
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    camera.stop_preview()
    ```

    La variable `i` cuenta cuántas veces se ejecutó el ciclo, de `0` a `4`. Por lo tanto, las fotos se guardan como `image0.jpg`, `image1.jpg` y así sucesivamente.

- Ejecuta el código otra vez y mantén el Módulo de Cámara en su posición.

La cámara debería tomar una foto cada cinco segundos. Una vez que se toma la quinta foto, se cierra la vista previa.

- Mira el Escritorio para encontrar las cinco fotos nuevas.
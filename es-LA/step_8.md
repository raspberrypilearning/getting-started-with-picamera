## Cómo cambiar las configuraciones de la imagen y agregarle efectos

El software Python `picamera` proporciona un número de efectos y configuraciones para cambiar la apariencia de tus imágenes.

**Nota:** algunas configuraciones solo afectan la vista previa y no la imagen capturada, algunos afectan solo la imagen capturada y muchos otros afectan a ambas.

### Define la resolución de la imagen

Puedes cambiar la `resolución` de la imagen que el Módulo de Cámara produce.

Por defecto, la resolución de la imagen está configurada segun la resolución de tu monitor. La resolución máxima es 2592×1944 para imágenes fijas, y 1920×1080 para grabaciones de video.

- Utiliza el siguiente código para establecer la `resolución` al máximo y tomar una foto.

    **Nota:** también tienes que establecer la velocidad de los fotogramas por segundo a `15` para permitir esta resolución máxima.

    ```python
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/max.jpg')
    camera.stop_preview()
    ```

La resolución mínima es 64x64.

- Intenta tomar una foto con la resolución mínima.

### Agrega texto a tu imagen

Puedes agregar texto a tu imagen usando el comando `annotate_text`.

- Ejecuta este código para probarlo:

    ```python
    camera.start_preview()
    camera.annotate_text = "Hello world!"
    sleep(5)
    camera.capture('/home/pi/Desktop/text.jpg')
    camera.stop_preview()
    ```

### Cambia el aspecto del texto agregado

- Establece el tamaño del texto con el siguiente código:

    ```python
    camera.annotate_text_size = 50
    ```

    Puedes establecer el tamaño del texto en cualquier valor entre `6` y `160`. El tamaño predeterminado es `32`.

También es posible cambiar el color del texto.

- En primer lugar, agrega `Color` a tu línea `import` en la parte superior del programa:

    ```python
    from picamera import PiCamera, Color
    ```

- Luego, debajo de la línea `import`, modifica el resto de tu código para que se vea así:

    ```python
    camera.start_preview()
    camera.annotate_background = Color('blue')
    camera.annotate_foreground = Color('yellow')
    camera.annotate_text = " Hello world "
    sleep(5)
    camera.stop_preview()
    ```

### Cambia el brillo de la vista previa

Puedes cambiar el brillo de la vista previa. El brillo predeterminado es `50` y puedes establecerlo en cualquier valor entre `0` y `100`.

* Ejecuta el siguiente código para probarlo:

    ```python
    camera.start_preview()
    camera.brightness = 70
    sleep(5)
    camera.capture('/home/pi/Desktop/bright.jpg')
    camera.stop_preview()
    ```

- El siguiente ciclo ajusta el brillo y también agrega texto para mostrar el nivel de brillo actual:

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Brightness: %s" % i
        camera.brightness = i
        sleep(0.1)
    camera.stop_preview()
    ```

### Cambia el contraste de la vista previa

De manera similar al brillo de la vista previa, puedes cambiar el contraste de la vista previa.

- Ejecuta el siguiente código para probarlo:

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Contrast: %s" % i
        camera.contrast = i
        sleep(0.1)
    camera.stop_preview()
    ```

### Agrega efectos de imagen geniales

Puedes usar `camera.image_effect` para utilizar un efecto de imagen particular.

Las opciones de efecto de imagen son las siguientes:

* `ninguno`
* `negative`
* `solarize`
* `sketch`
* `denoise`
* `emboss`
* `oilpaint`
* `hatch`
* `gpen`
* `pastel`
* `watercolor`
* `film`
* `blur`
* `saturation`
* `colorswap`
* `washedout`
* `posterise`
* `colorpoint`
* `colorbalance`
* `cartoon`
* `deinterlace1`
* `deinterlace2`

The default effect is `none`.

* Pick an image effect and try it out:

    ```python
    camera.start_preview()
    camera.image_effect = 'colorswap'
    sleep(5)
    camera.capture('/home/pi/Desktop/colorswap.jpg')
    camera.stop_preview()
    ```

* Run this code to loop over **all** the image effects with `camera.IMAGE_EFFECTS`:

    ```python
    camera.start_preview()
    for effect in camera.IMAGE_EFFECTS:
        camera.image_effect = effect
        camera.annotate_text = "Effect: %s" % effect
        sleep(5)
    camera.stop_preview()
    ```

    ![Effects](images/effects.jpg)

### Set the image exposure mode

You can use `camera.exposure_mode` to set the exposure to a particular mode.

The exposure mode options are:
* `off`
* `auto`
* `night`
* `nightpreview`
* `backlight`
* `spotlight`
* `sports`
* `snow`
* `beach`
* `verylong`
* `fixedfps`
* `antishake`
* `fireworks`

The default mode is `auto`.

* Pick an exposure mode and try it out:

    ```python
    camera.start_preview()
    camera.exposure_mode = 'beach'
    sleep(5)
    camera.capture('/home/pi/Desktop/beach.jpg')
    camera.stop_preview()
    ```

* You can loop over all the exposure modes with `camera.EXPOSURE_MODES`, like you did for the image effects.

### Change the image white balance

You can use `camera.awb_mode` to set the auto white balance to a preset mode.

The available auto white balance modes are:
* `off`
* `auto`
* `sunlight`
* `cloudy`
* `shade`
* `tungsten`
* `fluorescent`
* `incandescent`
* `flash`
* `horizon`

The default is `auto`.

* Pick an auto white balance mode and try it out:

    ```python
    camera.start_preview()
    camera.awb_mode = 'sunlight'
    sleep(5)
    camera.capture('/home/pi/Desktop/sunlight.jpg')
    camera.stop_preview()
    ```

* You can loop over all the auto white balance modes with `camera.AWB_MODES`, like you did for the image effects.
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
* `negativo`
* `sobreexposición`
* `bosquejo`
* `eliminar el ruido de color`
* `relieve`
* `pintura al óleo`
* `eclosión`
* `dibujo a lápiz`
* `pastel`
* `acuarela`
* `película`
* `desenfoque`
* `saturación`
* `cambio de color`
* `desteñido`
* `estilo póster`
* `punto de color`
* `balance de color`
* `caricatura`
* `desentrelazado1`
* `desentrelazado2`

El efecto predeterminado es `ninguno`.

* Elige un efecto de imagen y pruébalo:

    ```python
    camera.start_preview()
    camera.image_effect = 'colorswap'
    sleep(5)
    camera.capture('/home/pi/Desktop/colorswap.jpg')
    camera.stop_preview()
    ```

* Ejecuta este código para probar **todos** los efectos de imágenes con `camera.IMAGE_EFFECTS`:

    ```python
    camera.start_preview()
    for effect in camera.IMAGE_EFFECTS:
        camera.image_effect = effect
        camera.annotate_text = "Effect: %s" % effect
        sleep(5)
    camera.stop_preview()
    ```

    ![Efectos](images/effects.jpg)

### Establece el modo de exposición de la imagen

Puedes usar `camera.exposure_mode` para establecer la exposición en un modo particular.

Las opciones del modo de exposición son las siguientes:
* `apagado`
* `auto`
* `noche`
* `vista previa nocturna`
* `luz de fondo`
* `foco`
* `deportes`
* `nieve`
* `playa`
* `prolongada`
* `fps fijos`
* `estabilización de imagen`
* `fuegos artificiales`

El modo predeterminado es `auto`.

* Elige un modo de exposición y pruébalo:

    ```python
    camera.start_preview()
    camera.exposure_mode = 'beach'
    sleep(5)
    camera.capture('/home/pi/Desktop/beach.jpg')
    camera.stop_preview()
    ```

* Puedes repetir todos los modos de exposición con `camera.EXPOSURE_MODES`, así como lo hiciste con efectos de imagen.

### Cambiar el balance de blancos de la imagen

Puedes utilizar `camera.awb_mode` para establecer el balance de blancos automático en un modo predeterminado.

Los modos de balance de blancos disponibles son los siguientes:
* `apagado`
* `auto`
* `iluminación`
* `nublado`
* `sombra`
* `tungsteno`
* `fluorescente`
* `incandescente`
* `destello de luz`
* `horizonte`

El modo predeterminado es `auto`.

* Escoge un modo de balance de blancos automático y pruébalo:

    ```python
    camera.start_preview()
    camera.awb_mode = 'sunlight'
    sleep(5)
    camera.capture('/home/pi/Desktop/sunlight.jpg')
    camera.stop_preview()
    ```

* Puedes repetir el modo de balance de blancos automático `camera.AWB_MODES`, así como hiciste con efectos de imagen.
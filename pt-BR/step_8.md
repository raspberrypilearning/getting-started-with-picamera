## Como alterar as configurações da imagem e adicionar efeitos de imagem

O software Python `picamera` disponibiliza uma série de efeitos e configurações para alterar o visual de suas imagens.

**Nota:** algumas configurações afetam apenas a pré-visualização e não a imagem capturada, algumas afetam apenas a imagem capturada e muitas outras afetam ambos.

### Defina a resolução da imagem

Você pode alterar a `resolução` da imagem que o Módulo de Câmera produz.

Por padrão, a resolução da imagem é definida para a resolução do seu monitor. A resolução máxima é de 2592×1944 para fotos, e de 1920×1080 para gravação de vídeo.

- Use o código a seguir para definir a `resolution` ao máximo e tire uma foto.

    **Nota:** você também precisa definir a taxa de quadros para `15` para habilitar esta resolução máxima.

    ```python
    camera.resolução = (2592, 1944)
    camera.framerate = 15
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/max.jpg')
    camera.stop_preview()
    ```

A resolução mínima é de 64×64.

- Tente tirar uma foto com a resolução mínima.

### Adicione texto à sua imagem

Você pode adicionar texto à sua imagem usando o comando `annotate_text`.

- Execute este código para testar isso:

    ```python
    camera.start_preview()
    camera.annotate_text = "Hello world!"
    sleep(5)
    camera.capture('/home/pi/Desktop/text.jpg')
    camera.stop_preview()
    ```

### Altere a aparência do texto adicionado

- Defina o tamanho do texto com o seguinte código:

    ```python
    camera.annotate_text_size = 50
    ```

    Você pode definir o tamanho do texto para qualquer valor entre `6` e `160`. O tamanho padrão é `32`.

Também é possível alterar a cor do texto.

- Antes de tudo, adicione `Color` à sua linha `import` na parte superior do programa:

    ```python
    from picamera import PiCamera, Color
    ```

- Então abaixo da linha de `import`, altere o resto do seu código para que fique assim:

    ```python
    camera.start_preview()
    camera.annotate_background = Color('blue')
    camera.annotate_foreground = Color('yellow')
    camera.annotate_text = " Hello world "
    sleep(5)
    camera.stop_preview()
    ```

### Altere o brilho da pré-visualização

Você pode mudar o brilho da pré-visualização. O brilho padrão é `50`, e você pode defini-lo para qualquer valor entre `0` e `100`.

* Execute o seguinte código para experimentar isso:

    ```python
    camera.start_preview()
    camera.brightness = 70
    sleep(5)
    camera.capture('/home/pi/Desktop/bright.jpg')
    camera.stop_preview()
    ```

- O ciclo a seguir ajusta o brilho e também adiciona texto para exibir o nível atual de brilho:

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Brightness: %s" % i
        camera.brightness = i
        sleep(0.1)
    camera.stop_preview()
    ```

### Alterar o contraste da pré-visualização

Da mesma forma que o brilho da pré-visualização, você pode mudar o contraste da pré-visualização.

- Execute o seguinte código para experimentar isso:

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Contrast: %s" % i
        camera.contrast = i
        sleep(0.1)
    camera.stop_preview()
    ```

### Adicione efeitos de imagem legais

Você pode usar `camera.image_effect` para aplicar um efeito de imagem específico.

As opções de efeito de imagem são:

* `none`
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

O efeito padrão é `none`.

* Escolha um efeito de imagem e experimente:

    ```python
    camera.start_preview()
    camera.image_effect = 'colorswap'
    sleep(5)
    camera.capture('/home/pi/Desktop/colorswap.jpg')
    camera.stop_preview()
    ```

* Execute este código para experimentar **todos** os efeitos de imagem com `camera.IMAGE_EFFECTS`:

    ```python
    camera.start_preview()
    for effect in camera.IMAGE_EFFECTS:
        camera.image_effect = effect
        camera.annotate_text = "Effect: %s" % effect
        sleep(5)
    camera.stop_preview()
    ```

    ![Efeitos](images/effects.jpg)

### Definir o modo de exposição de imagem

Você pode usar `camera.exposure_mode` para definir a exposição para um modo específico.

As opções do modo de exposição são:
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

O modo padrão é `auto`.

* Escolha um modo de exposição e experimente:

    ```python
    camera.start_preview()
    camera.exposure_mode = 'beach'
    sleep(5)
    camera.capture('/home/pi/Desktop/beach.jpg')
    camera.stop_preview()
    ```

* Você pode repetir todos os modos de exposição com `camera.EXPOSURE_MODES`, assim como foi feito com os efeitos de imagem.

### Alterar o balanço de branco da imagem

Você pode usar `camera.awb_mode` para definir o balanço de branco automático para um modo predefinido.

Os modos de balanço de branco automático disponíveis são:
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

O padrão é `auto`.

* Escolha um modo de balanço de branco automático e experimente:

    ```python
    camera.start_preview()
    camera.awb_mode = 'sunlight'
    sleep(5)
    camera.capture('/home/pi/Desktop/sunlight.jpg')
    camera.stop_preview()
    ```

* Você pode repetir todos os modos de balanço de branco automático com `camera.AWB_MODES`, assim como foi feito com os efeitos de imagem.
## Tirar fotos com o código Python

Agora use o Módulo de Câmera e o Python para tirar algumas fotos.

- Altere seu código para adicionar uma linha de `camera.capture()`:

    ```python
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    ```

    **Nota:** é importante definir `sleep` por pelo menos dois segundos antes de capturar uma imagem, porque isso dá ao sensor da câmera o tempo necessário para detectar os níveis de luz.

- Execute o código.

Você deve ver a pré-visualização da câmera aberta por cinco segundos e, em seguida, uma imagem estática deve ser capturada. Conforme a foto é tirada, você pode ver a pré-visualização brevemente se ajustando a uma resolução diferente.

Sua nova imagem será salva na Área de Trabalho.

- Agora adicione um ciclo para tirar cinco fotos consecutivas:

    ```python
    camera.start_preview()
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    camera.stop_preview()
    ```

    A variável `i` conta quantas vezes o ciclo foi executado, de `0` até `4`. Assim, as imagens são salvas como `image0.jpg`, `image1.jpg`, e assim por diante.

- Execute o código novamente e segure o Módulo de Câmera na posição.

A câmera irá tirar uma foto a cada cinco segundos. Assim que a quinta foto é tirada, a pré-visualização se encerra.

- Acesse a sua Área de Trabalho para encontrar as cinco fotos novas.
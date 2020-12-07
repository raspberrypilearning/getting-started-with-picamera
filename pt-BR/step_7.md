## Gravar vídeo com código Python

Agora grave um vídeo!

- Ajuste seu código para remover `capture()` e, em vez disso, adicione `start_recording()` e `stop_recording()`

    Seu código deve ficar assim:

    ```python
    camera.start_preview()
    camera.start_graving('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_graving()
    camera.stop_preview()
    ```

- Execute o código.

Seu Raspberry Pi deve abrir uma pré-visualização, gravar 5 segundos de vídeo e, em seguida, fechar a prévia.


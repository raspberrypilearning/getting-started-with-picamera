## Como controlar o Módulo de Câmera através da linha de comando

Agora que seu Módulo de Câmera está conectado e o software está ativado, experimente as ferramentas de linha de comando `raspistill` e `raspivid`.

- Abra uma janela de terminal clicando no ícone do monitor preto na barra de tarefas:

![Terminal aberto](images/open-terminal-annotated.png)

- Digite o seguinte comando para tirar uma foto e salvá-la na área de trabalho:

```bash
raspistill -o Desktop/image.jpg
```

![comando raspistill inserido no terminal](images/raspistill-image.png)

- Pressione <kbd>Enter</kbd> para executar o comando.

Quando o comando é executado, você pode ver a pré-visualização da câmera abrir por cinco segundos antes de uma foto ser tirada.

- Procure o ícone do arquivo de imagem na área de trabalho e clique duas vezes no ícone do arquivo para abrir a imagem.

    ![Imagem na Área de Trabalho](images/desktop-annotated.png)

Ao adicionar diferentes opções, você pode definir o tamanho e a aparência da imagem que o comando `raspistill` gera.

- Por exemplo, adicione `-h` e `-w` para alterar a altura e largura da imagem:

```bash
raspistill -o Desktop/image-small.jpg -w 640 -h 480
```

- Agora grave um vídeo com o Módulo de Câmera usando o seguinte comando `raspivid`:

```bash
raspivid -o Desktop/video.h264
```

- Para reproduzir o arquivo de vídeo, clique duas vezes no ícone do arquivo `video.h264` na área de trabalho para abri-lo no VLC Media Player.

Para mais informações e outras opções que você pode usar com esses comandos, leia a [documentação para raspistill](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md) e a [documentação para raspivid](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md).

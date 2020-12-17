## コマンドラインでカメラモジュールをコントロールする方法

カメラモジュールが接続され、ソフトウェアが有効になりました。コマンドラインツールである `raspistill` と `raspivid` を試してみてください。

- タスクバーの黒いモニターアイコンをクリックして、ターミナルウィンドウを開きます。

![ターミナルを開く](images/open-terminal-annotated.png)

- 静止画を撮影し、デスクトップに保存するには、次のコマンドを入力します。

```bash
raspistill -o Desktop / image.jpg
```

![raspistillコマンドがターミナルに入力される](images/raspistill-image.png)

- <kbd>Enter</kbd> を押してコマンドを実行します。

コマンドが実行されると、静止画が撮影される5秒前からカメラのプレビューが開きます。

- デスクトップの画像ファイルアイコンを探し、ファイルアイコンをダブルクリックして画像を開きます。

    ![デスクトップ上の画像](images/desktop-annotated.png)

さまざまなオプションを追加することで、`raspistill` コマンドが受け取る画像サイズと見え方を設定することができます。

- たとえば、画像の高さと幅を変更するには、 `-h` と `-w` を追加します。

```bash
raspistill -o Desktop/image-small.jpg -w 640 -h 480
```

- 続いて、次の `raspivid` コマンドを使用して、カメラモジュールでビデオを録画します。

```bash
raspivid -o Desktop/video.h264
```

- ビデオファイルを再生するには、デスクトップの `video.h264` ファイルアイコンをダブルクリックして、VLC MediaPlayerで開きます。

より詳しい情報やこれらのコマンドで使用できるその他のオプションについては、[raspistill のドキュメント](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md) および [raspividのドキュメント](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md) を読んでください。

## Pythonコードでビデオを録画する

ビデオを録画しましょう！

- コードを修正して、 `capture()` を取り除き、代わりに `start_recording()` (録画開始)と `stop_recording()` (録画停止)を追加します。

    コードは次のようになります。

    ```python
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    ```

- コードを実行します。

Raspberry Piはプレビューを開き、5秒間のビデオを録画してから、プレビューを閉じます。


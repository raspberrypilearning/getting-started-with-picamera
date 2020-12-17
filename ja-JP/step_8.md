## 画像設定を変更して、画像効果を追加する方法

Pythonの `picamera` ソフトウェアは、画像の見た目を変更するための多くの効果と設定を提供します。

**注意:** 一部の設定は、プレビューにのみ反映され、撮影された画像には反映されません。また、一部の設定は撮影された画像にのみ反映されます。多くの設定は両方に反映されます。

### 画像の解像度を設定する

カメラモジュールが撮影する画像の `resolution`(解像度)を変更できます。

デフォルト（初期設定）では、画像の解像度はモニターの解像度に設定されています。 最大解像度は、静止画の場合は2592×1944、ビデオ録画の場合は1920×1080です。

- 次のコードを使用して、 `resolution` を最大に設定し、写真を撮ります。

    **注意:** この最大解像度を有効にするには、フレームレートを `15` に設定する必要があります。

    ```python
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/max.jpg')
    camera.stop_preview()
    ```

最小解像度は64×64です。

- 最小解像度で写真を撮ってみてください。

### 画像にテキストを追加する

コマンド `annotate_text` (注釈を付ける)を使用して画像にテキストを追加することができます。

- このコードを実行してみましょう。

    ```python
    camera.start_preview()
    camera.annotate_text = "Hello world!"
    sleep(5)
    camera.capture('/home/pi/Desktop/text.jpg')
    camera.stop_preview()
    ```

### 追加したテキストの見かけを変更する

- 次のコードでテキストサイズを設定します。

    ```python
    camera.annotate_text_size = 50
    ```

    `6` から `160` までの任意の文字サイズに設定できます。 デフォルトのサイズは `32` です。

テキストの色を変更することもできます。

- まず、`Color` を、プログラムの上部にある `import` 行に追加します。

    ```python
    from picamera import PiCamera, Color
    ```

- 次に、 `import` 行の下で、残りのコードを次のように修正します。

    ```python
    camera.start_preview()
    camera.annotate_background = Color('blue')
    camera.annotate_foreground = Color('yellow')
    camera.annotate_text = " Hello world "
    sleep(5)
    camera.stop_preview()
    ```

### プレビューの明るさを変更する

プレビューの明るさを変更できます。 デフォルトの明るさは `50`で、 `0` から `100` の間の任意の値に設定できます。

* これを試すには、次のコードを実行します。

    ```python
    camera.start_preview()
    camera.brightness = 70
    sleep(5)
    camera.capture('/home/pi/Desktop/bright.jpg')
    camera.stop_preview()
    ```

- 次のループは、明るさを調整し、現在の明るさのレベルを表示するテキストを追加します。

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Brightness: %s" % i
        camera.brightness = i
        sleep(0.1)
    camera.stop_preview()
    ```

### プレビューのコントラストを変更する

プレビューの明るさと同様に、プレビューのコントラストを変更できます。

- これを試すには、次のコードを実行します。

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Contrast: %s" % i
        camera.contrast = i
        sleep(0.1)
    camera.stop_preview()
    ```

### かっこいい画像効果を追加する

`camera.image_effect` を使用して、特定の画像効果を適用できます。

画像効果のオプションは次のとおりです。

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

デフォルトの効果は `none` です。

* 画像効果を選んで試してみてください。

    ```python
    camera.start_preview()
    camera.image_effect = 'colorswap'
    sleep(5)
    camera.capture('/home/pi/Desktop/colorswap.jpg')
    camera.stop_preview()
    ```

* **すべて** の画像効果を`camera.IMAGE_EFFECTS`を使ってループさせるためにこのコードを実行してください。

    ```python
    camera.start_preview()
    for effect in camera.IMAGE_EFFECTS:
        camera.image_effect = effect
        camera.annotate_text = "Effect: %s" % effect
        sleep(5)
    camera.stop_preview()
    ```

    ![効果](images/effects.jpg)

### 画像露出モード（光の量、明るさ）を設定する

`camera.exposure_mode` を使用して、露出を特定のモードに設定できます。

露出モードのオプションは次のとおりです。
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

デフォルトのモードは `auto` です。

* 露出モードを選択して試してみてください。

    ```python
    camera.start_preview()
    camera.exposure_mode = 'beach'
    sleep(5)
    camera.capture('/home/pi/Desktop/beach.jpg')
    camera.stop_preview()
    ```

* 画像効果で行ったように、`camera.EXPOSURE_MODES`を使ってすべての露出モードをループさせることができます。

### 画像のホワイトバランスを変更する

`camera.awb_mode` を使用して、オート(自動)ホワイトバランスをプリセットモードに設定できます。

利用できるオートホワイトバランスモードは次のとおりです。
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

デフォルトは `auto` です。

* オートホワイトバランスモードを選択して試してみてください。

    ```python
    camera.start_preview()
    camera.awb_mode = 'sunlight'
    sleep(5)
    camera.capture('/home/pi/Desktop/sunlight.jpg')
    camera.stop_preview()
    ```

* 画像効果で行ったように、`camera.AWB_MODES`を使ってすべてのオートホワイトバランスモードをループさせることができます。
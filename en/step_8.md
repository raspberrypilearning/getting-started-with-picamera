## How to change the image settings and add image effects

The Python `picamera` software provides a number of effects and configurations to change how your images look.

**Note:** some settings only affect the preview and not the captured image, some affect only the captured image, and many others affect both.

### Set the image resolution

You can change the `resolution` of the image that the Camera Module takes.

By default, the image resolution is set to the resolution of your monitor. The maximum resolution is 2592×1944 for still photos, and 1920×1080 for video recording.

- Use the following code to set the `resolution` to maximum and take a picture.

    **Note:** you also need to set the frame rate to `15` to enable this maximum resolution.

    ```python
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/max.jpg')
    camera.stop_preview()
    ```

The minimum resolution is 64×64.

- Try taking a picture with the minimum resolution.

### Add text to your image

You can add text to your image using the command `annotate_text`.

- Run this code to try it:

    ```python
    camera.start_preview()
    camera.annotate_text = "Hello world!"
    sleep(5)
    camera.capture('/home/pi/Desktop/text.jpg')
    camera.stop_preview()
    ```

### Change the look of the added text

- Set the text size with the following code:

    ```python
    camera.annotate_text_size = 50
    ```

    You can set the text size to anything between `6` to `160`. The default size is `32`.

It's also possible to change the text colour.

- First of all, add `Color` to your `import` line at the top of the program:

    ```python
    from picamera import PiCamera, Color
    ```

- Then below the `import` line, amend the rest of your code so it looks like this:

    ```python
    camera.start_preview()
    camera.annotate_background = Color('blue')
    camera.annotate_foreground = Color('yellow')
    camera.annotate_text = " Hello world "
    sleep(5)
    camera.stop_preview()
    ```

### Change the brightness of the preview

You can change how bright the preview appears. The default brightness is `50`, and you can set it to any value between `0` and `100`.

* Run the following code to try this out:

    ```python
    camera.start_preview()
    camera.brightness = 70
    sleep(5)
    camera.capture('/home/pi/Desktop/bright.jpg')
    camera.stop_preview()
    ```

- The following loop adjusts the brightness and also adds text to display the current brightness level:

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Brightness: %s" % i
        camera.brightness = i
        sleep(0.1)
    camera.stop_preview()
    ```

### Change the contrast of the preview

Similarly to the preview brightness, you can change the contrast of the preview.

- Run the following code to try this out:

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Contrast: %s" % i
        camera.contrast = i
        sleep(0.1)
    camera.stop_preview()
    ```

### Add cool image effects

You can use `camera.image_effect` to apply a particular image effect. 

The image effect options are:

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
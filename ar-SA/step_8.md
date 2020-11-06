## كيفية تغيير إعدادات الصورة وإضافة تأثيرات الى الصورة

يوفر برنامج Python `picamera` عددًا من التأثيرات والإعدادات لتغيير شكل صورك.

**ملاحظة:** بعض الإعدادات تؤثر فقط على المعاينة وليس على الصورة الملتقطة ، بعضها يؤثر فقط على الصورة الملتقطة ، والعديد من الإعدادات الأخرى تؤثر على كليهما.

### أضبط دقة الصورة

يمكنك تغيير دقة `` الصورة التي تلتقطها وحدة الكاميرا.

بشكل افتراضي ، يتم ضبط دقة الصورة بناءً على دقة شاشتك. الحد الأقصى للدقة هو 2592×1944 للصور الثابتة، و 1920×1080 لتسجيل الفيديو.

- استخدم الكود التالي لتعيين الدقة `` إلى الحد الأقصى والتقاط صورة.

    **ملاحظة:** تحتاج أيضًا إلى ضبط معدل الإطارات على `15` لتمكين الحد الأقصى من الدقة.

    ```python
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/max.jpg')
    camera.stop_preview()
    ```

الحد الأدنى للدقة هو 64 × 64.

- حاول التقاط صورة بأقل دقة ممكنة.

### أضف نصًا إلى صورتك

يمكنك إضافة نص إلى صورتك باستخدام الأمر `annotate_text`.

- قم بتشغيل هذه التعليمة البرمجية لتجربتها:

    ```python
    camera.start_preview()
    camera.annotate_text = "Hello world!"
    sleep(5)
    camera.capture('/home/pi/Desktop/text.jpg')
    camera.stop_preview()
    ```

### غَيِر مظهر النص المضاف

- اضبط حجم النص من خلال التعليمة البرمجية التالية:

    ```python
    camera.annotate_text_size = 50
    ```

    يمكنك ضبط حجم النص إلى أي حجم بين `6` و `160`. الحجم الافتراضي هو `32`.

من الممكن أيضًا تغيير لون النص.

- أولا وقبل كل شيء، أضف `Color` إلى سطر ال `import` في الجزء العلوي من البرنامج:

    ```python
    from picamera import PiCamera, Color
    ```

- ثم أسفل سطر `import` ، قم بتعديل بقية التعليمة البرمجية الخاصة بك بحيث تبدو كالتالي:

    ```python
    camera.start_preview()
    camera.annotate_background = Color('blue')
    camera.annotate_foreground = Color('yellow')
    camera.annotate_text = " Hello world "
    sleep(5)
    camera.stop_preview()
    ```

### غَيِر سطوع المعاينة

يمكنك تغيير مدى السطوع الذي تظهر به المعاينة. السطوع الافتراضي هو `50`، ويمكنك ضبطه على أي قيمة بين `0` و `100`.

* قم بتشغيل التعليمة البرمجية التالية لتجربة ذلك:

    ```python
    camera.start_preview()
    camera.brightness = 70
    sleep(5)
    camera.capture('/home/pi/Desktop/bright.jpg')
    camera.stop_preview()
    ```

- الحلقة التكرارية التالية تضبط السطوع وتضيف أيضًا نصًا لعرض مستوى السطوع الحالي:

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Brightness: %s" % i
        camera.brightness = i
        sleep(0.1)
    camera.stop_preview()
    ```

### غَيِر تباين المعاينة

على غرار سطوع المعاينة، يمكنك تغيير تباين المعاينة.

- قم بتشغيل الكود التالي لتجربة ذلك:

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Contrast: %s" % i
        camera.contrast = i
        sleep(0.1)
    camera.stop_preview()
    ```

### أضف تأثيرات صور رائعة

يمكنك استخدام `camera.image_effect` لتطبيق تأثير صورة معين.

خيارات تأثير الصورة هي:

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

التأثير الافتراضي هو `none`.

* اختر تأثير الصورة وجربه:

    ```python
    camera.start_preview()
    camera.image_effect = 'colorswap'
    sleep(5)
    camera.capture('/home/pi/Desktop/colorswap.jpg')
    camera.stop_preview()
    ```

* قم بتشغيل هذه التعليمة البرمجية كحلقة تكرارية على **جميع** تأثيرات الصورة بأستخدام `camera.IMAGE_EFFECTS`:

    ```python
    camera.start_preview()
    for effect in camera.IMAGE_EFFECTS:
        camera.image_effect = effect
        camera.annotate_text = "Effect: %s" % effect
        sleep(5)
    camera.stop_preview()
    ```

    ![تأثيرات](images/effects.jpg)

### اضبط وضع تعرض الصورة

يمكنك استخدام `camera.exposure_mode` لضبط التعرض إلى وضع معين.

خيارات وضع التعرض هي:
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

الوضع الافتراضي هو `auto`.

* اختر وضع التعرض و جربه:

    ```python
    camera.start_preview()
    camera.exposure_mode = 'beach'
    sleep(5)
    camera.capture('/home/pi/Desktop/beach.jpg')
    camera.stop_preview()
    ```

* يمكنك عمل حلقة تكرارية على جميع أوضاع التعرض باستخدام `camera.EXPOSURE_MODES`, كما فعلت لتأثيرات الصورة.

### قم بتغيير توازن بياض الصورة

يمكنك استخدام `camera.awb_mode` لضبط توازن اللون الأبيض التلقائي على الوضع المحدد مسبقًا.

أوضاع توازن البياض التلقائي المتاحة هي:
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

الافتراضي هو `auto`.

* اختر وضع توازن اللون الأبيض التلقائي وجربه:

    ```python
    camera.start_preview()
    camera.awb_mode = 'sunlight'
    sleep(5)
    camera.capture('/home/pi/Desktop/sunlight.jpg')
    camera.stop_preview()
    ```

* يمكنك عمل حلقة تكرارية على جميع أوضاع توازن اللون الأبيض التلقائي باستخدام `camera.AWB_MODES` كما فعلت مع تأثيرات الصورة.
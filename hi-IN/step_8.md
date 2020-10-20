## छवि सेटिंग्स कैसे बदलें और छवि प्रभाव जोड़ें

Python `picamera` सॉफ़्टवेयर आपकी छवियों को देखने के तरीके को बदलने के लिए कई प्रभाव और कॉन्फ़िगरेशन प्रदान करता है।

**नोट:** कुछ सेटिंग्स केवल पूर्वावलोकन को प्रभावित करती हैं न कि कैप्चर की गई छवि को, कुछ केवल कैप्चर की गई छवि को प्रभावित करती हैं, और कई अन्य दोनों को प्रभावित करती हैं।

### छवि रिज़ॉल्यूशन सेट करें

आप कैमरा मॉड्यूल द्वारा ली गई छवि के `resolution` को बदल सकते हैं।

डिफ़ॉल्ट रूप से, छवि रिज़ॉल्यूशन आपके मॉनिटर के रिज़ॉल्यूशन पर सेट होता है। स्थिर तस्वीर के लिए अधिकतम रिज़ॉल्यूशन 2592 × 1944, और वीडियो रिकॉर्डिंग के लिए 1920 × 1080 है।

- `resolution` को अधिकतम सेट करने और चित्र लेने के लिए निम्न कोड का उपयोग करें।

    **नोट:** आपको इस अधिकतम रिज़ॉल्यूशन को सक्षम करने के लिए फ्रेम दर को `15` पर सेट करने की भी आवश्यकता है।

    ```python
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/max.jpg')
    camera.stop_preview()
    ```

न्यूनतम रिज़ॉल्यूशन 64 × 64 है।

- न्यूनतम रिज़ॉल्यूशन के साथ एक तस्वीर लेने की कोशिश करें।

### अपनी छवि में टेक्स्ट जोड़ें

आप `annotate_text` कमांड का उपयोग करके अपनी छवि में टेक्स्ट जोड़ सकते हैं।

- इसे आज़माने के लिए यह कोड चलाएँ:

    ```python
    camera.start_preview()
    camera.annotate_text = "Hello world!"
    sleep(5)
    camera.capture('/home/pi/Desktop/text.jpg')
    camera.stop_preview()
    ```

### जोड़े गए टेक्स्ट का रूप बदलें

- निम्नलिखित कोड के साथ टेक्स्ट का आकार निर्धारित करें:

    ```python
    camera.annotate_text_size = 50
    ```

    आप टेक्स्ट साइज़ को `6` से `160` के बीच में कुछ भी सेट कर सकते हैं। डिफ़ॉल्ट आकार `32` है।

टेक्स्ट का रंग बदलना भी संभव है।

- सबसे पहले, प्रोग्राम के शीर्ष पर अपने `import` लाइन में `Color` जोड़ें:

    ```python
    from picamera import PiCamera, Color
    ```

- फिर `import` पंक्ति के नीचे, अपने शेष कोड में संशोधन करें ताकि यह इस तरह दिखाई दे:

    ```python
    camera.start_preview()
    camera.annotate_background = Color('blue')
    camera.annotate_foreground = Color('yellow')
    camera.annotate_text = " Hello world "
    sleep(5)
    camera.stop_preview()
    ```

### पूर्वावलोकन की चमक बदलें

आप बदल सकते हैं कि पूर्वावलोकन कितना उज्ज्वल दिखाई देता है। डिफ़ॉल्ट चमक `50` है, और आप इसे `0` और `100` के बीच किसी भी मूल्य पर सेट कर सकते हैं।

* इसे आज़माने के लिए निम्न कोड चलाएँ:

    ```python
    camera.start_preview()
    camera.brightness = 70
    sleep(5)
    camera.capture('/home/pi/Desktop/bright.jpg')
    camera.stop_preview()
    ```

- निम्न लूप चमक को समायोजित करता है और वर्तमान चमक स्तर को प्रदर्शित करने के लिए टेक्स्ट भी जोड़ता है:

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Brightness: %s" % i
        camera.brightness = i
        sleep(0.1)
    camera.stop_preview()
    ```

### पूर्वावलोकन का कॉन्ट्रास्ट बदलें

पूर्वावलोकन चमक की तरह, आप पूर्वावलोकन के कॉन्ट्रास्ट को बदल सकते हैं।

- इसे आज़माने के लिए निम्न कोड चलाएँ:

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Contrast: %s" % i
        camera.contrast = i
        sleep(0.1)
    camera.stop_preview()
    ```

### शानदार छवि प्रभाव जोड़ें

आप एक विशेष छवि प्रभाव को लागू करने के लिए `camera.image_effect` का उपयोग कर सकते हैं।

छवि प्रभाव के निम्नलिखित विकल्प हैं:

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

डिफ़ॉल्ट प्रभाव `none` है।

* एक छवि प्रभाव चुनें और इसे आज़माएँ:

    ```python
    camera.start_preview()
    camera.image_effect = 'colorswap'
    sleep(5)
    camera.capture('/home/pi/Desktop/colorswap.jpg')
    camera.stop_preview()
    ```

* `camera.IMAGE_EFFECTS` के साथ **सभी** छवि प्रभावों पर लूप करने के लिए इस कोड को चलाएं:

    ```python
    camera.start_preview()
    for effect in camera.IMAGE_EFFECTS:
        camera.image_effect = effect
        camera.annotate_text = "Effect: %s" % effect
        sleep(5)
    camera.stop_preview()
    ```

    ![प्रभाव](images/effects.jpg)

### छवि एक्सपोज़र मोड सेट करें

आप किसी विशेष मोड में एक्सपोज़र सेट करने के लिए `camera.exposure_mode` का उपयोग कर सकते हैं।

एक्सपोज़र मोड के विकल्प निम्नलिखित हैं:
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

डिफ़ॉल्ट मोड `auto` है।

* एक एक्सपोज़र मोड चुनें और इसे आज़माएँ:

    ```python
    camera.start_preview()
    camera.exposure_mode = 'beach'
    sleep(5)
    camera.capture('/home/pi/Desktop/beach.jpg')
    camera.stop_preview()
    ```

* आप सभी एक्सपोज़र मोड को `camera.EXPOSURE_MODES` के साथ लूप कर सकते हैं, जैसे आपने छवि प्रभावों के लिए किया था।

### छवि के व्हाइट बैलेंस को बदलें

प्रीसेट मोड में ऑटो व्हाइट बैलेंस को सेट करने के लिए आप `camera.awb_mode` का उपयोग कर सकते हैं।

उपलब्ध ऑटो व्हाइट बैलेंस मोड हैं:
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

डिफ़ॉल्ट `auto` है।

* एक ऑटो व्हाइट बैलेंस मोड चुनें और इसे आज़माएँ:

    ```python
    camera.start_preview()
    camera.awb_mode = 'sunlight'
    sleep(5)
    camera.capture('/home/pi/Desktop/sunlight.jpg')
    camera.stop_preview()
    ```

* आप सभी ऑटो व्हाइट बैलेंस मोड को `camera.EXPOSURE_MODES` के साथ लूप कर सकते हैं, जैसे आपने छवि प्रभावों के लिए किया था।
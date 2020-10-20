## Python कोड के साथ वीडियो रिकॉर्डिंग

अब एक वीडियो रिकॉर्ड करें!

- अपने कोड में संशोधन करके `capture()` को हटाएं और इसके बजाय ` start_recording ()` और `stop_recording (`) जोड़ें

    आपका कोड अब इस तरह दिखना चाहिए:

    ```python
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    ```

- अपना कोड चलाएँ।

आपके Raspberry Pi को एक पूर्वावलोकन खोलना चाहिए, 5 सेकंड का वीडियो रिकॉर्ड करना चाहिए, और फिर पूर्वावलोकन बंद करना चाहिए।


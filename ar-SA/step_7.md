## تسجيل فيديو باستخدام التعليمات البرمجية بلغة Python

الآن سجل فيديو!

- قم بتعديل التعليمة البرمجية الخاصة بك لإزالة `capture()` وبدلا من ذلك أضف `start_recording ()` و `stop_recording ()`

    يجب الآن أن تبدو التعليمة البرمجية الخاصة بك مثل هذه:

    ```python
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    ```

- قم بتشغيل التعليمة البرمجية.

يجب أن يفتح Raspberry Pi معاينة ، ويسجل 5 ثوانٍ من الفيديو ، ثم يغلق المعاينة.


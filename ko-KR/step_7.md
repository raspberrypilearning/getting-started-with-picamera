## Python 코드로 영상 녹화하기

이제 영상을 녹화합니다!

- `capture()` 코드를 제거하고 대신에 `start_recording()`과 `stop_recording()`을 추가하기 위해 코드를 수정합니다.

    다음과 같은 코드가 될 것입니다:

    ```python
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    ```

- 코드를 실행하세요.

Raspberry Pi가 미리보기를 열고 5초 동안 영상을 녹화하고, 미리보기를 닫아야 합니다.


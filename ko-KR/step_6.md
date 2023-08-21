## Python 코드로 스틸 사진 찍기

이제 스틸 사진을 찍기 위해 카메라 모듈과 Python을 사용합니다.

- `camera.capture()` 줄을 추가하도록 코드를 수정합니다:

    ```python
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    ```

    **주의:** 이미지를 찍기 적어도 2초 전에 `sleep`하는 것은 중요합니다. 왜냐하면 이는 카메라 센서가 조도를 감지할 시간을 주기 때문입니다.

- 코드를 실행하세요.

카메라 미리보기가 5 초 동안 열린 다음 스틸 사진이 찍혀야합니다. 사진이 찍히는 동안 미리보기가 다른 해상도로 잠시 조정되는 것을 볼 수 있습니다.

새 이미지는 컴퓨터에 저장되어야 합니다.

- 이제 연속으로 5 장의 사진을 찍는 루프를 추가합니다.

    ```python
    camera.start_preview()
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    camera.stop_preview()
    ```

    변수 `i`는 `0`에서 `4`까지 루프가 몇 번 실행되었는지 셉니다. 따라서 이미지는 `image0.jpg`, `image1.jpg`등으로 저장됩니다.

- 코드를 다시 실행하고 카메라 모듈을 제자리에 고정합니다.

카메라는 5 초마다 한 장의 사진을 찍어야합니다. 일단 다섯 번째 사진이 촬영되면 미리보기가 닫힙니다.

- 5개의 새로운 사진을 컴퓨터에서 찾습니다.
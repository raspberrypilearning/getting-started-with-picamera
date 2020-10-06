## Video opnemen met Python-code

Neem nu een video op!

- Wijzig je code om `capture()` te verwijderen en voeg in plaats daarvan `start_recording()` en `stop_recording()` toe

    Je code zou er als volgt uit moeten zien:

    ```python
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    ```

- Voer de code uit.

De Raspberry Pi zou een voorbeeld moeten openen, 5 seconden video moeten opnemen en vervolgens het voorbeeld moeten sluiten.


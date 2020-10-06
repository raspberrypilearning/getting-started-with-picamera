## Enregistrer des vidéos avec du code Python

Maintenant enregistre une vidéo !

- Modifie ton code pour supprimer `capture()` et ajoute à la place `start_recording()` et `stop_recording()`

    Ton code devrait ressembler à ceci :

    ```python
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    ```

- Exécute le code.

Ton Raspberry Pi devrait ouvrir un aperçu, enregistrer 5 secondes de vidéo, puis fermer l'aperçu.


## Capturer des images fixes avec du code Python

Utilise maintenant le module caméra et Python pour capturer des images fixes.

- Modifie ton code pour ajouter une ligne `camera.capture()` :

    ```python
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    ```

    **Remarque :** c'est important d'utiliser un `sleep` pendant au moins deux secondes avant de capturer une image, car cela donne au capteur de l'appareil photo le temps de détecter les niveaux de lumière.

- Exécute le code.

Tu devrais voir l'aperçu de la caméra pendant cinq secondes, et ensuite une image fixe devrait être capturée. Pendant la prise de vue, tu peux voir l'aperçu s'ajuster brièvement à une résolution différente.

Ta nouvelle image devrait être enregistrée sur le bureau.

- Maintenant, ajoute une boucle pour prendre cinq images d'affilée :

    ```python
    camera.start_preview()
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    camera.stop_preview()
    ```

    La variable `i` compte le nombre de fois que la boucle a été exécutée, de `0` à `4`. Par conséquent, les images sont enregistrées sous `image0.jpg`, `image1.jpg`, et ainsi de suite.

- Exécute à nouveau le code et maintiens le module caméra en position.

La caméra doit prendre une image toutes les cinq secondes. Une fois la cinquième image prise, l'aperçu se ferme.

- Regarde ton bureau pour trouver les cinq nouvelles images.
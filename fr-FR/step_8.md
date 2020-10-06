## Comment modifier les paramètres d'image et ajouter des effets d'image

Le logiciel Python `picamera` fournit un certain nombre d'effets et de configurations pour changer l'apparence de tes images.

**Remarque :** certains paramètres n'affectent que l'aperçu et non l'image capturée, certains n'affectent que l'image capturée, et beaucoup d'autres affectent les deux.

### Définir la résolution de l'image

Tu peux modifier la `résolution` de l'image prise par le module caméra.

Par défaut, la résolution de l'image est définie sur la résolution de ton moniteur. La résolution maximale est de 2592 × 1944 pour les images fixes et de 1920 × 1080 pour l'enregistrement vidéo.

- Utilise le code suivant pour définir la `résolution` au maximum et capture une image.

    **Remarque :** tu dois également définir le taux d'images à `15` pour activer cette résolution maximale.

    ```python
    camera.resolution = (2592, 1944)
    camera.framerate = 15
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/max.jpg')
    camera.stop_preview()
    ```

La résolution minimale est de 64 × 64.

- Essaie de capturer une image avec la résolution minimale.

### Ajouter du texte à ton image

Tu peux ajouter du texte à ton image à l'aide de la commande `annotate_text`.

- Exécute ce code pour l'essayer :

    ```python
    camera.start_preview()
    camera.annotate_text = "Bonjour le monde !"
    sleep(5)
    camera.capture('/home/pi/Desktop/text.jpg')
    camera.stop_preview()
    ```

### Modifier l'apparence du texte ajouté

- Définis la taille du texte avec le code suivant :

    ```python
    camera.annotate_text_size = 50
    ```

    Tu peux définir la taille du texte sur n'importe quelle valeur comprise entre `6` et `160`. La taille par défaut est `32`.

Il est également possible de modifier la couleur du texte.

- Tout d'abord, ajoute `Color` à ta ligne `import` en haut du programme :

    ```python
    from picamera import PiCamera, Color
    ```

- Ensuite, sous la ligne `import` , modifie le reste de ton code pour qu'il ressemble à ceci :

    ```python
    camera.start_preview()
    camera.annotate_background = Color('blue')
    camera.annotate_foreground = Color('yellow')
    camera.annotate_text = " Bonjour le monde "
    sleep(5)
    camera.stop_preview()
    ```

### Modifier la luminosité de l'aperçu

Tu peux modifier la luminosité de l'aperçu. La luminosité par défaut est `50` et tu peux la régler sur n'importe quelle valeur comprise entre `0` et `100`.

* Exécute le code suivant pour essayer ceci :

    ```python
    camera.start_preview()
    camera.brightness = 70
    sleep(5)
    camera.capture('/home/pi/Desktop/bright.jpg')
    camera.stop_preview()
    ```

- La boucle suivante ajuste la luminosité et ajoute également du texte pour afficher le niveau de luminosité actuelle :

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Brightness: %s" % i
        camera.brightness = i
        sleep(0.1)
    camera.stop_preview()
    ```

### Modifier le contraste de l'aperçu

De la même manière que la luminosité de l'aperçu, tu peux modifier le contraste de l'aperçu.

- Exécute le code suivant pour essayer ceci :

    ```python
    camera.start_preview()
    for i in range(100):
        camera.annotate_text = "Contrast: %s" % i
        camera.contrast = i
        sleep(0.1)
    camera.stop_preview()
    ```

### Ajouter des effets d'image sympas

Tu peux utiliser `camera.image_effect` pour appliquer un effet d'image particulier.

Les options d'effet d'image sont :

* `none (aucun)`
* `negative (négatif)`
* `solarize (solariser)`
* `sketch (dessin)`
* `denoise (antibruit)`
* `emboss (relief)`
* `oilpaint (peinture à l'huile)`
* `hatch (hachurer)`
* `gpen`
* `pastel`
* `watercolor (aquarelle)`
* `film`
* `blur (flou)`
* `saturation`
* `colorswap (permutation de couleur)`
* `washedout (délavé)`
* `posterise (postériser)`
* `colorpoint (point de couleur)`
* `colorbalance (balance des couleurs)`
* `cartoon (dessin animé)`
* `deinterlace1 (désentrelacement1)`
* `deinterlace2 (désentrelacement2)`

L'effet par défaut est `none`.

* Choisis un effet d'image et essaie-le :

    ```python
    camera.start_preview()
    camera.image_effect = 'colorswap'
    sleep(5)
    camera.capture('/home/pi/Desktop/colorswap.jpg')
    camera.stop_preview()
    ```

* Exécute ce code pour boucler sur **tous** les effets d'image avec `camera.IMAGE_EFFECTS` :

    ```python
    camera.start_preview()
    for effect in camera.IMAGE_EFFECTS:
        camera.image_effect = effect
        camera.annotate_text = "Effect: %s" % effect
        sleep(5)
    camera.stop_preview()
    ```

    ![Effets](images/effects.jpg)

### Définir le mode d'exposition de l'image

Tu peux utiliser `camera.exposure_mode` pour définir l'exposition sur un mode particulier.

Les options de mode d'exposition sont :
* `off (désactivé)`
* `auto (automatique)`
* `night (nuit)`
* `nightpreview (vision nocturne)`
* `backlight (éclairage de derrière)`
* `spotlight (projecteur)`
* `sports`
* `snow (neige)`
* `beach (plage)`
* `verylong (très long)`
* `fixedfps (image fixe par seconde )`
* `antishake (anti-tremblement)`
* `fireworks (feux d'artifice)`

Le mode par défaut est `auto`.

* Choisis un mode d'exposition et essaie-le :

    ```python
    camera.start_preview()
    camera.exposure_mode = 'beach'
    sleep(5)
    camera.capture('/home/pi/Desktop/beach.jpg')
    camera.stop_preview()
    ```

* Tu peux boucler tous les modes d'exposition avec `camera.EXPOSURE_MODES`, comme tu l'as fait pour les effets d'image.

### Modifier la balance des blancs de l'image

Tu peux utiliser `camera.awb_mode` pour régler la balance des blancs automatique sur un mode prédéfini.

Les modes de balance des blancs disponibles sont :
* `off (éteint)`
* `auto (automatique)`
* `sunlight (lumière du soleil)`
* `cloudy (nuageux)`
* `shade (ombre)`
* `tungsten (tungstène)`
* `fluorescent`
* `incandescent`
* `flash`
* `horizon`

La valeur par défaut est `auto`.

* Choisis un mode de balance des blancs automatique et essaie-le :

    ```python
    camera.start_preview()
    camera.awb_mode = 'sunlight'
    sleep(5)
    camera.capture('/home/pi/Desktop/sunlight.jpg')
    camera.stop_preview()
    ```

* Tu peux boucler tous les modes de balance des blancs automatique avec `camera.AWB_MODES`, comme tu l'as fait pour les effets d'image.
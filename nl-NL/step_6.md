## Maak foto's met Python-code

Gebruik nu de cameramodule en Python om wat foto's te maken.

- Wijzig je code om een `camera.capture()` regel toe te voegen:

    ```python
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    ```

    **Opmerking:** het is belangrijk om `te slapen` gedurende ten minste twee seconden voordat een afbeelding wordt gemaakt, omdat dit de sensor van de camera tijd geeft om het lichtniveau te detecteren.

- Voer de code uit.

Je zou het voorbeeld van de camera vijf seconden open moeten zien staan en dan zou er een foto moeten worden gemaakt. Terwijl de foto wordt gemaakt, kun je zien dat het voorbeeld kort wordt aangepast aan een andere resolutie.

Je nieuwe afbeelding moet op het bureaublad worden opgeslagen.

- Voeg nu een lus toe om vijf foto's achter elkaar te maken:

    ```python
    camera.start_preview()
    for i in range(5):
        sleep(5)
        camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    camera.stop_preview()
    ```

    De variabele `i` telt hoe vaak de lus is uitgevoerd, van `0` tot `4`. Daarom worden de afbeeldingen opgeslagen als `image0.jpg`, `image1.jpg`, enzovoort.

- Voer de code opnieuw uit en houd de cameramodule op zijn plaats.

De camera zou elke vijf seconden een foto moeten maken. Zodra de vijfde foto is gemaakt, wordt het voorbeeld gesloten.

- Kijk op je bureaublad om de vijf nieuwe afbeeldingen te vinden.
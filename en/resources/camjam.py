from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(21)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

while True:
    button.wait_for_press()
    lights.off()
    buzzer.on()
    button.wait_for_release()
    lights.on()
    buzzer.off()

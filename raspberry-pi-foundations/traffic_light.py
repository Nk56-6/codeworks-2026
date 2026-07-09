#traffic light system using Raspberry Pi and some LEDs

from gpiozero import LED
from time import sleep

ledRed = LED(17)
ledYellow = LED(22)
ledGreen = LED(2)

while True:
    ledRed.on()
    ledYellow.off()
    ledGreen.off()
    sleep(3)
    ledRed.off()
    ledYellow.on()
    ledGreen.off()
    sleep(3)
    ledRed.off()
    ledYellow.off()
    ledGreen.on()
    sleep(3)
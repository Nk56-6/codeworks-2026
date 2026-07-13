#traffic light system using Raspberry Pi and some LEDs

from gpiozero import LED
from time import sleep

ledRed = LED(17)
ledYellow = LED(22)
ledGreen = LED(2)
ledWhite = LED(21)
ledOrange = LED(8)
ledBlue = LED(12)

while True:
    ledRed.on()
    ledYellow.off()
    ledGreen.off()
    ledWhite.on()
    ledOrange.off()
    ledBlue.off()
    sleep(5)
    ledRed.off()
    ledYellow.on()
    ledGreen.off()
    ledWhite.off()
    ledOrange.on()
    ledBlue.off()
    sleep(2)
    ledRed.off()
    ledYellow.off()
    ledGreen.on()
    ledWhite.off()
    ledOrange.off()
    ledBlue.on()
    sleep(5)

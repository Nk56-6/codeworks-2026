#Simple blink led sketch using GPIO pins on Raspberry Pi

from gpiozero import LED
from time import sleep

ledRed = LED(17)

while True:
    ledRed.on()
    sleep(1)
    ledRed.off()
    sleep(1)
import RPi.GPIO as GPIO
from time import sleep

import spidev

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT) #RED LED
pwm=GPIO.PWM(27,50)

spi=spidev.SpiDev()
spi.open(0,0)

while True:
    spi.max_speed_hz=1350000

    r=spi.xfer2(1,8+0<<4,0)
    pot_value=((r[1]&3)<<8)+r[2]
    print(pot_value)

    pwm.start(pot_value*100/1023)

    sleep(1)


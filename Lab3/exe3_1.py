import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT) #RED LED
GPIO.setup(22, GPIO.OUT) #YELLOW LED
GPIO.setup(26, GPIO.OUT) #GREEN LED
GPIO.setup(19, GPIO.IN)  #push button
GPIO.setup(17, GPIO.OUT) #buzzer

while True:
    GPIO.output(27,0)
    GPIO.output(22,0)
    GPIO.output(26,1)
    count=0
    max=150
    while(count<max):
        if(GPIO.input(19)):
            max=100
        sleep(0.1)
        count+=1
    
    GPIO.output(27,0)
    GPIO.output(22,1)
    GPIO.output(26,0)
    sleep(2)

    GPIO.output(27,1)
    GPIO.output(22,0)
    GPIO.output(26,0)
    for i in range(10):
        GPIO.output(17,1)
        sleep(0.5)
        GPIO.output(17,0)
        sleep(0.5)


#import the modules needed
import RPi.GPIO as GPIO
from time import sleep
import spidev
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#set up
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
spi=spidev.SpiDev()
spi.open(0,0)

#count up continuously
count=0

#lists to store readings (0-1023) & entry numbers (0, 1, 2...) 
readings=[]
entries=[]

##one graph, and put this at row 1, col 1
fig=plt.figure()
pot_graph=fig.add_subplot(1,1,1) 

def animate(i):
    #make variables global
    global count

    #read potentiometer value
    spi.max_speed_hz=1350000
    r=spi.xfer2([1,8+0<<4,0])
    pot_value=((r[1]&3)<<8)+r[2]

    #for each list: keep 10 items, add new item at back, increment count
    if count>9:
        readings.pop(0)
        entries.pop(0)
    readings.append(pot_value)    
    entries.append(count)
    count=count+1 

    #update plot
    pot_graph.clear()
    pot_graph.plot(entries,readings)
    pot_graph.set_xlabel('1-sec samples',fontsize=10)
    pot_graph.set_ylabel('potentiometer values',fontsize=10)
    pot_graph.set_title('Matplotlib live graph')

ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()

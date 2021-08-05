import matplotlib.pyplot as plt
import csv
import numpy as np

n=[]
temp=[]
humi=[]
ave_temp=[]
ave_humi=[]

with open('sensordata.txt','r') as csvfile:
    data=csv.reader(csvfile,delimiter=',')
    for row in data:
        n.append(int(row[0]))
        temp.append(int(row[1]))
        humi.append(int(row[2]))

mean_temp=int(np.mean(temp))
mean_humi=int(np.mean(humi))
ave_temp=[mean_temp]*10
ave_humi=[mean_humi]*10

plt.plot(n,temp,label='temperature')
plt.plot(n,humi,label='humidity')
plt.plot(n,ave_temp,label='mean temperature')
plt.plot(n,ave_humi,label='mean humidity')
plt.xlabel('last 10 samples, 2 sec intervals')
plt.ylabel('temperature in deg C & humidity in %')
plt.legend()
plt.show()
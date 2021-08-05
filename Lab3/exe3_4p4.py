from picamera import PiCamera
from time import sleep

my_camera=PiCamera()
my_camera.resolution(1920,1080)
my_camera.vflip=True
my_camera.hflip=True

print('taking 5 photos...')

for i in range(5):
    print(i)
    sleep(2)
    my_camera.capture('image{0:03d}.jpg'.format(i))

print('done')
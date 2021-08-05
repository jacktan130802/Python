from picamera import PiCamera
from time import sleep

my_camera=PiCamera()
my_camera.resolution(1920,1080)
my_camera.vflip=True
my_camera.hflip=True

print("taking a 5-sec video clip...")

my_camera.start_preview()
my_camera.start_recording('video.h264')
sleep(5)
my_camera.stop_recording()
my_camera.stop_preview()

print("done")
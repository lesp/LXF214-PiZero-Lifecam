#!/usr/bin/env python3

import picamera
from gpiozero import Button, LED
import time
import datetime
from signal import pause

button = Button(17)
led = LED(27)

def video():
    print("RECORDING")
    led.on()
    with picamera.PiCamera() as camera:
        a = str(datetime.datetime.now())
        a = a[0:19]
        camera.resolution = (1280, 720)
        camera.start_preview()
        camera.start_recording(a +(".h264"))
        camera.wait_recording(30)
        camera.stop_recording()
        camera.stop_preview()
        led.off()

button.when_pressed = video
pause()
    

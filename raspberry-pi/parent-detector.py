import threading
# from .RPi import GPIO
import RPi.GPIO as GPIO
import time
import os

from threading import Thread

LedPin = 17
PirPin = 18

def playSirenOnThread():
    thread = Thread(target=playSiren, args=[])
    thread.start()

def playSiren():
    os.system('aplay /home/pi/rpi/siren.wav')

def captureImageOnThread():
    thread = Thread(target=captureImage, args=[])
    thread.start()

def captureImage():
    os.system('fswebcam -d /dev/video0 -r 640x480 -s 3 --jpeg 50 --save /home/pi/rpi/images/%Y-%m-%d_%H%M.jpg')

def setup():
    print ('Setting up GPIO')
    GPIO.setmode(GPIO.BCM)

    print ('Setting up PirPin as ', PirPin)
    GPIO.setup(PirPin, GPIO.IN)

    print ('Setting up edPin as ', LedPin)
    GPIO.setup(LedPin, GPIO.OUT)

def destroy():
    GPIO.cleanup()

def main():
    nobodyThere = False

    while True:
        j = GPIO.input(PirPin)
        if j == 0:
            if nobodyThere:
                continue

            print ('Nobody there ', j)
            nobodyThere = True
            GPIO.output(LedPin, GPIO.HIGH) # Turn off LED

        elif j == 1:
            nobodyThere = False

            print('Parent detected..!! ', j)
            GPIO.output(LedPin, GPIO.LOW) # Turn on LED

            playSirenOnThread()
            captureImageOnThread()

            time.sleep(10)
        
        time.sleep(0.5)

if __name__ == "__main__":
    setup()

    try:
        main()
    except KeyboardInterrupt:
        destroy()
        print ('Exiting...')

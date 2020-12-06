import RPi.GPIO as GPIO
import time

ledpin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledpin, GPIO.OUT)

    while True:
        print("LED is ON now...")
        GPIO.output(ledpin, GPIO.LOW)

        time.sleep(1)

        print("... OFF now...")
        GPIO.output(ledpin, GPIO.HIGH)

        time.sleep(1)

def destroy():
    GPIO.output(ledpin, GPIO.HIGH)
    GPIO.cleanup()

    print("Exiting...")

if __name__ == "__main__":
    setup()

    try:
        main()
    except KeyboardInterrupt:
        destroy()

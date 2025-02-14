import threading, subprocess
import RPi.GPIO as GPIO
while True:
    if __name__=='__main__':
        try:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(5, GPIO.IN)
            GPIO.wait_for_edge(5,GPIO.RISING)
            pin = GPIO.wait_for_edge(5, GPIO.FALLING, timeout = 3000)
            if pin is None:
                subprocess.call('sudo shutdown -h now', shell=True)
            else:
                subprocess.call('sudo reboot', shell=True)
        finally:
            GPIO.cleanup()
        
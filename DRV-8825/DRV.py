# Based upon online educational programs from various sources
# Optimised for current use in the robot by
# Balazs Barany

from time import sleep
import RPi.GPIO as GPIO

DIR = 20    # Direction pin
STEP = 21   # Step pin
CW = 1      # Clockwise rotation
CCW = 0     # Counterclockwise rotation
SPR = 400   # Steps per revolution (360/0,9)

GPIO.setmode(GPIO.BMC)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(Step, GPIO.OUT)
GPIO.output(DIR, CW)

MODE = (14, 15, 18) #Microstep GPIO pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1,0,1)}

GPIO.output(MODE, Resolution['Half'])

step cont = SPR
delay =.0025    # 1 sec divided by steps SPR?

for x in range (step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(Step, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR, CCW)

for x in range(step_count)
    GPIO.output(STEP,GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

GPIO.cleanup()

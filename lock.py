import RPi.GPIO as GPIO
import time
import os
import signal
import sys
import subprocess
import multiprocessing
import types

# wiring setup
PLS = 5
DIR = 6
ENA = 13

# MicroSwitch
switch_return = 12
switch_limit = 16



# Variable initialized
currentPosition = 0
nowPlaying = 0
wasPlaying = 0
runSecond = 50  #limitation of the moving Motor
turn_limit = runSecond*450

# stepMotor
delay = 0.001 # *2 = delay of steps

######## Setup ##########

# GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PLS, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(switch_return, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch_limit, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# GPIO Init
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(ENA, GPIO.HIGH)
time.sleep(0.001)
GPIO.output(ENA, GPIO.LOW)
GPIO.output(ENA, GPIO.LOW)
print("initialized")

# Function Setup
def turnOff(num):
    print("Released Motor")
    if(num == 0):
        GPIO.output(ENA, GPIO.HIGH)
    elif(num == 1):
        GPIO.output(ENA, GPIO.LOW)
######## Main ##########


turnOff(1)
currentPosition = 0
while True:
    time.sleep(5)


GPIO.cleanup()

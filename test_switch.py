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
runSecond = 60  #limitation of the moving Motor
turn_limit = runSecond*830 #450

# stepMotor
delay = 0.01 # *2 = delay of steps

######## Setup ##########

# GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PLS, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(switch_return, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch_limit, GPIO.IN, pull_up_down=GPIO.PUD_UP)

######## Main ##########

while True:
    btnR = GPIO.input(switch_return)
    btnL = GPIO.input(switch_limit)
    print('home:\t'+str(btnR)+"\tbtnL"+str(btnL))
    
    GPIO.output(PLS, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(PLS, GPIO.LOW)
    time.sleep(delay)

GPIO.cleanup()

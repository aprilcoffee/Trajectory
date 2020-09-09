import RPi.GPIO as GPIO
import time
import os
import signal
import sys
import subprocess
import multiprocessing
import types

# wiring setup
PLS = 17
DIR = 27
ENA = 22

# MicroSwitch
switch_return = 23
switch_limit = 24


# Function Setup
def turnOff(num):
    print("Released Motor")
    if(num == 0):
        GPIO.output(ENA, GPIO.HIGH)
    elif(num == 1):
        GPIO.output(ENA, GPIO.LOW)


# Variable initialized
currentAngle = 0
nowPlaying = 0
wasPlaying = 0

# stepMotor
delay = 0.01


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

######## Main ##########


def init():
    global currentAngle
    btnR = GPIO.input(switch_return)
    btnL = GPIO.input(switch_limit)
    while(btnR == 0 or btnL == 0):
        print(str(btnL) + '\t' + str(btnR))
        GPIO.output(DIR, GPIO.HIGH)
        GPIO.output(PLS, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PLS, GPIO.LOW)
        time.sleep(delay)

        btnL = GPIO.input(sensorL)
        btnR = GPIO.input(sensorR)
    currentAngle = 0


# init()
flag = 0
while True:

    GPIO.output(DIR, GPIO.HIGH)
    GPIO.output(PLS, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(PLS, GPIO.LOW)
    time.sleep(delay)
    if flag%400==0:
        print("One Cycle stop for 0.5 sec")
        time.sleep(0.5)

GPIO.cleanup()

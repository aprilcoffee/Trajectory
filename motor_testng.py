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


def goFoward():
    #global nowPlaying
    #global wasPlaying
    #wasPlaying = 0
    GPIO.output(m1, GPIO.LOW)
    GPIO.output(m2, GPIO.LOW)
    r_btn = GPIO.input(23)
    time.sleep(2)
    while(r_btn == 0):
        GPIO.output(m1, GPIO.HIGH)
        GPIO.output(m2, GPIO.LOW)
        time.sleep(0.1)
        r_btn = GPIO.input(23)
    GPIO.output(m1, GPIO.LOW)
    GPIO.output(m2, GPIO.LOW)


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

GPIO.setmode(GPIO.BCM)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)
print("initialized")

######## Main ##########


def init():
    global currentAngle
    btnR = GPIO.input(switch_return)
    btnL = GPIO.input(switch_limit)
    while(btnR == 0 or btnL == 0):
        print(str(btnL) + '\t' + str(btnR))
        GPIO.output(DIR, GPIO.HIGH)
        if btnL == 0:
            GPIO.output(PLSL, GPIO.HIGH)
        if btnR == 0:
            GPIO.output(PLSR, GPIO.HIGH)
        time.sleep(delay)
        if btnL == 0:
            GPIO.output(PLSL, GPIO.LOW)
        if btnR == 0:
            GPIO.output(PLSR, GPIO.LOW)
        time.sleep(delay)
        btnL = GPIO.input(sensorL)
        btnR = GPIO.input(sensorR)
    currentAngle = 0


# init()
flag = 0
while True:
    println("Runtime")

    GPIO.output(DIR, GPIO.HIGH)
    GPIO.output(PLS, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(PLS, GPIO.LOW)
    time.sleep(delay)
    if flag%3==0:
        time.sleep(1)

GPIO.cleanup()

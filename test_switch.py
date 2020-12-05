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


def init():
    global currentPosition
    btnR = GPIO.input(switch_return)
    btnL = GPIO.input(switch_limit)
    while(btnR == 0):
        #print(str(btnL) + '\t' + str(btnR))
        GPIO.output(DIR, GPIO.HIGH)
        GPIO.output(PLS, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PLS, GPIO.LOW)
        time.sleep(delay)

        btnL = GPIO.input(switch_limit)
        btnR = GPIO.input(switch_return)
    currentPosition = 0


def foward():
    global currentPosition
    global turn_limit
    btn = GPIO.input(switch_limit)
    while(btn == 0 and currentPosition <= turn_limit):
        currentPosition = currentPosition+1
        GPIO.output(DIR,GPIO.LOW)
        GPIO.output(PLS,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PLS,GPIO.LOW)
        time.sleep(delay)
        btn = GPIO.input(switch_limit)

######## Main ##########

proc = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--layer','0','--aspect-mode','fill','/home/pi/Desktop/Trajectory/house.mp4'])

GPIO.output(DIR,GPIO.LOW)
while True:
    btnR = GPIO.input(switch_return)
    btnL = GPIO.input(switch_limit)
    print('home:\t'+str(btnR)+"\tbtnL"+str(btnL))
    

    GPIO.output(DIR,GPIO.LOW)
    GPIO.output(DIR,GPIO.LOW)
    GPIO.output(DIR,GPIO.LOW)

    GPIO.output(PLS, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(PLS, GPIO.LOW)
    time.sleep(delay)

GPIO.cleanup()

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



# Variable initialized
currentPosition = 0
nowPlaying = 0
wasPlaying = 0
turn_limit = 200 #limitation of the moving Motor

# stepMotor
delay = 0.01 # *2 = delay of steps

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


def init():
    global currentAngle
    btnR = GPIO.input(switch_return)
    btnL = GPIO.input(switch_limit)
    while(btnR == 0):
        print(str(btnL) + '\t' + str(btnR))
        GPIO.output(DIR, GPIO.HIGH)
        GPIO.output(PLS, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PLS, GPIO.LOW)
        time.sleep(delay)

        btnL = GPIO.input(switch_limit)
        btnR = GPIO.input(switch_return)
    currentPosition = 0


def foward():
    global currentAngle
    btn = GPIO.input(switch_limit)
    while(btn == 0 or currentPosition == turn_limit):
        #currentPosition += 1
        GPIO.output(DIR,GPIO.LOW)
        GPIO.output(PLS,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PLS,GPIO.LOW)
        time.sleep(delay)

        btn = GPIO.input(switch_limit)

######## Main ##########


init()
currentPosition = 0

# proc1 = subprocess.Popen(
#     args=['
#     omxplayer',
#     '--no-osd',
#     '--loop',
#     '-b',
#     '--layer','1',
#     '--aspect-mode', 'fill',
#      'tomotor2.mp4'])

print 'proc\'s pid = ', proc1.pid


while True:
    foward();

    # proc2 = subprocess.Popen(
    #     args=['
    #     omxplayer',
    #     '--no-osd',
    #     '--loop',
    #     '-b',
    #     '--layer','2',
    #     '--aspect-mode', 'fill',
    #      'tomotor2.mp4'])
    # time.sleep(0.5)
    # subprocess.call(['pkill', '-P', str(proc1.pid)])


    init();
    # proc1 = subprocess.Popen(
    #     args=['
    #     omxplayer',
    #     '--no-osd',
    #     '--loop',
    #     '-b',
    #     '--layer','1',
    #     '--aspect-mode', 'fill',
    #      'tomotor2.mp4'])
    # time.sleep(0.5)
    # subprocess.call(['pkill', '-P', str(proc2.pid)])


    # flag += 1
    # GPIO.output(DIR, GPIO.HIGH)
    # GPIO.output(PLS, GPIO.HIGH)
    # time.sleep(delay)
    # GPIO.output(PLS, GPIO.LOW)
    # time.sleep(delay)
    # if flag%500==0:
    #     print("One Cycle stop for 0.5 sec")
    #     time.sleep(0.5)


GPIO.cleanup()

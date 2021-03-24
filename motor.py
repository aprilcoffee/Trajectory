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
turn_limit = runSecond*830

# stepMotor
delay = 0.0005 # *2 = delay of steps

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
    while(btnR != 0):
    #while(currentPosition >= -1660):
        #print(str(btnL) + '\t' + str(btnR))
        #currentPosition = currentPosition-=1
        GPIO.output(DIR, GPIO.HIGH)
        GPIO.output(PLS, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PLS, GPIO.LOW)
        time.sleep(delay)
        btnR = GPIO.input(switch_return)
    currentPosition = 0
def initRun():
    global currentPosition
    btnR = GPIO.input(switch_return)
    #while(btnR == 0):
    while(currentPosition >= -415):
        #print(str(btnL) + '\t' + str(btnR))
        currentPosition = currentPosition-1
        GPIO.output(DIR, GPIO.HIGH)
        GPIO.output(PLS, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PLS, GPIO.LOW)
        time.sleep(delay)
        btnR = GPIO.input(switch_return)
    currentPosition = 0

def foward():
    global currentPosition
    global turn_limit
    btn = GPIO.input(switch_limit)
    while(currentPosition <= turn_limit and btn!=0):
        #while(btn == 0 and currentPosition <= turn_limit):
        currentPosition = currentPosition+1
        GPIO.output(DIR,GPIO.LOW)
        GPIO.output(PLS,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PLS,GPIO.LOW)
        time.sleep(delay)
        btn = GPIO.input(switch_limit)

######## Main ##########


init()
currentPosition = 0

proc = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--layer','0','--aspect-mode','fill','/home/pi/Desktop/Trajectory/black.mp4'])

proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--layer','1','--aspect-mode','fill','/home/pi/Desktop/Trajectory/house.mp4'])
time.sleep(10)


#print 'proc\'s pid = ', proc1.pid


while True:
    print("go forward")
    foward()
    time.sleep(10)
    print("go home")

    #proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--layer','2','--aspect-mode', 'fill','/home/pi/Desktop/Trajectory/go_home.mp4'])
    #time.sleep(0.5)
    #subprocess.call(['pkill', '-P', str(proc1.pid)])

    init()
    currentPosition=0
    subprocess.call(['pkill','-P',str(proc1.pid)])
    proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--layer','1','--aspect-mode', 'fill','/home/pi/Desktop/Trajectory/house.mp4'])
    time.sleep(10)
    #subprocess.call(['pkill', '-P', str(proc2.pid)])


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

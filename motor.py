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
    btnL = GPIO.input(switch_limit)
    btnBT = btnR
    while(btnR == 1 or btnBT ==1):
        #print("going Home:\t" +  '\t' + str(btnR))
        GPIO.output(DIR, GPIO.HIGH)
        GPIO.output(PLS, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PLS, GPIO.LOW)
        time.sleep(delay)
        btnBT = btnR
        #btnL = GPIO.input(switch_limit)
        btnR = GPIO.input(switch_return)
    currentPosition = 0


def foward():
    global currentPosition
    global turn_limit
    btnL = GPIO.input(switch_limit)
    btnR = GPIO.input(switch_return)
    btnBT = btnL
    while((btnL == 1 or btnBT==1) and currentPosition <= turn_limit):
        #print("going Forward:\t" + str(btnL))
        currentPosition = currentPosition+1
        GPIO.output(DIR,GPIO.LOW)
        GPIO.output(PLS,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(PLS,GPIO.LOW)
        time.sleep(delay)
        
        btnBT = btnL
        btnL = GPIO.input(switch_limit)
        #btnR = GPIO.input(switch_return)
######## Main ##########


init()
currentPosition = 0

proc = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--layer','0','--aspect-mode','fill','/home/pi/Desktop/Trajectory/black.mp4'])
proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--layer','1','--aspect-mode','fill','/home/pi/Desktop/Trajectory/house.mp4'])
time.sleep(2)


#print 'proc\'s pid = ', proc1.pid


while True:
    print("going turn")
    foward();
    time.sleep(10)
    print("going home")

    #proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--layer','2','--aspect-mode', 'fill','/home/pi/Desktop/Trajectory/go_home.mp4'])
    #time.sleep(0.5)
    #subprocess.call(['pkill', '-P', str(proc1.pid)])

    init();
    currentPosition=0
    subprocess.call(['pkill','-P',str(proc1.pid)])
    proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--layer','1','--aspect-mode', 'fill','/home/pi/Desktop/Trajectory/house.mp4'])
    time.sleep(2)
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

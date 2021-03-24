import time
import os
import signal
import sys
import subprocess
import multiprocessing
import types
from omxplayer.player import OMXPlayer


player = OMXPlayer('/home/pi/Desktop/Trajectory/house.mp4')

player.play()
while True:

    #proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--layer','1','--aspect-mode', 'fill','/home/pi/Desktop/Trajectory/house.mp4'])
    time.sleep(2)
    

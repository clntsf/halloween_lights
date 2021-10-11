from math import sin, pi
import neopixel
from microbit import *

# --- CONFIG --- #
TPS = 20
secondsToDecay = 2

ticksLeft = 0
ticksMax = TPS * secondsToDecay

vibrationThreshold = 20

BASE_ORANGE = (90,30,0)   # Base color to be used
DIFF_ORANGE = (30,10,0)    # Darker Orange
COLOR_DIFF = tuple([(BASE_ORANGE[j]-DIFF_ORANGE[j]) for j in range(3)])

STRIP_SIZE = 10                             # Number of LEDs on strip
np = neopixel.NeoPixel(pin0, STRIP_SIZE)  # init neopixel

# dummy functions for sound input
def getSoundLevel(): pass

tick=0
while True:
    soundLevel = getSoundLevel()        # get the sound level

    # if sound is detected above a certain preset threshold reset the decay timer
    if soundLevel > vibrationThreshold:
        ticksLeft = ticksMax
    
    # run if the decay timer is not expired
    if ticksLeft > 0:
        # set the RGB values of the strip
        for i in range(STRIP_SIZE):
            np[i] = tuple([round(BASE_ORANGE[j]-COLOR_DIFF[j]*sin(pi*(tick%360)/180+(tick%360)*pi/18)) for j in range(3)])

        tick+=1; ticksLeft -= 1; np.show()  # decay the timer, display the LED strip
        if ticksLeft == 0: np.clear()       # if the decay is over clear the LED strip
        
    else: np.clear()        # clear the LED strip
    sleep(1000//TPS)        # sleep for a tick
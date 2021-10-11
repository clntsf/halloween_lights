# Add your Python code here. E.g.
from microbit import *
from math import sin, pi
import neopixel

# --- CONFIG --- #
tick=0
TPS = 20
secondsToDecay = 2
ticksLeft = 0
ticksMax = TPS * secondsToDecay

vibrationThreshold = 20

BASE_ORANGE = (90,30,0)   # Base color to be used
DIFF_ORANGE = (30,10,0)    # Darker Orange
COLOR_DIFF = tuple([(BASE_ORANGE[j]-DIFF_ORANGE[j]) for j in range(3)])

STRIP_SIZE = 10                             # Number of LEDs on strip
np = neopixel.NeoPixel(pin0, STRIP_SIZE)

# function to set the LED RGB colors for the neopixel strip on a given tick (Colin)
def fillNeopixelRGB(tick):
    for i in range(STRIP_SIZE):
            np[i] = tuple([round(BASE_ORANGE[j]-COLOR_DIFF[j]*sin(pi*(tick%360)/180+(tick%360)*pi/18)) for j in range(3)])
    
    return

# functions to play and stop sound output (Javkhlan)
def playSoundOutput():
    return None

def stopSoundOutput():
    return None

# main loop
while True:

    soundLevel = microphone.sound_level()

    if soundLevel > vibrationThreshold:
        if ticksLeft == 0: playSoundOutput()
        ticksLeft = ticksMax

    if ticksLeft > 0:

        fillNeopixelRGB(tick)

        tick+=1; ticksLeft -= 1; np.show()
        if ticksLeft == 0:
            np.clear()
            stopSoundOutput()
        
    else: np.clear()
    sleep(1000//TPS)
# --- CONFIG --- #
TPS = 50
secondsToDecay = 1

ticksLeft = 0
ticksMax = TPS * secondsToDecay

vibrationThreshold = .5 # arbitrary, will need tuning

# --- DUMMY FUNCTIONS --- #

# increments output state
def doAction():
    pass
# resets/clears output state
def stopAction():
    pass
# gets input from vibration sensor
def getVibration():
    return 0
# waits for _ ms
def sleep(ms: int):
    pass

# main loop
while True:
    vibrationLevel = getVibration()

    # if input is above vibration threshold, reset the decay timer to max
    if vibrationLevel > vibrationThreshold:
        ticksLeft = ticksMax

    # if the decay timer is not out, continue to perform the action and decay by 1
    if ticksLeft > 0:
        doAction()
        ticksLeft -= 1

    # if the timer is fully decayed reset the outputs
        if ticksLeft == 0:
            stopAction()

    # sleep for the duration of the tick
    sleep(1000//TPS)
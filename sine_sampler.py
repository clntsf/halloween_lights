from math import sin, pi
from PIL import Image, ImageDraw

# --- CONFIG --- #
BASE_ORANGE = (255,149,0)   # Base color to be used

# Scaling Properties
MIN_HUE_SCALE = .9
MAX_HUE_SCALE = 1.4

STRIP_SIZE = 10                             # Number of LEDs on strip
SAMPLE_DETAIL = 2                           # Controls how 'zoomed in' the resulting color cycles appear
SAMPLES = SAMPLE_DETAIL * STRIP_SIZE        # Controls actual number of samples

STRIPS = 30                                 # Number of cycles to output into image

# Sample from a fitted sinewave
def sineSample(x):
    return (sin(pi*((x%360)-90)/180)+1)*(MAX_HUE_SCALE-MIN_HUE_SCALE)/2 + MIN_HUE_SCALE

# Scale base rgb by the sample
def scaleColor(rgb, scale):
    return tuple([min(255,round(n*scale)) for n in rgb])

# get an array of length SAMPLES containing the cycle rgb values
def getRGBVals():
    return [scaleColor(BASE_ORANGE,sineSample(n*360/(SAMPLES-1))) for n in range(SAMPLES)]

npRGB = getRGBVals()
# get LED RGB values for a certain step in the cycle
def fillSinewave(tick):
    return [npRGB[(i+tick)%SAMPLES] for i in range(STRIP_SIZE)]

# Setup output image with margins
img = Image.new(mode="RGB", size=(3*STRIPS+3, 2*STRIP_SIZE+4))
draw = ImageDraw.Draw(img)

# Draws the cycles
x=2; y=2
for t in range(30):
    for rgb in fillSinewave(t):
        draw.rectangle([x,y,x+1,y+1],rgb)
        y+=2
    x+=3; y=2

# Saves and displays image
img.save("materials/color_cycles.png")
img.show()  
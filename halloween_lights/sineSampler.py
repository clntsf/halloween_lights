from math import sin, pi
from PIL import Image, ImageDraw

# --- CONFIG --- #
BASE_COLOR = (255,149,0)   # Base color to be used

TILE_SIZE = 1
TILE_GAPH = 0
TILE_MARGIN = 4

# Scaling Properties
MIN_HUE_SCALE = .9
MAX_HUE_SCALE = 1.4

STRIP_SIZE = 90                             # Number of LEDs on strip
SAMPLE_DETAIL = 5                           # Controls how 'zoomed in' the resulting color cycles appear
SAMPLES = SAMPLE_DETAIL * STRIP_SIZE        # Controls actual number of samples

GCOLOR_1 = (255,0,0)
GCOLOR_2 = (0,255,255)

STRIPS = 90                                 # Number of cycles to output into image

MODE = 1

# Sample from a fitted sinewave
def sineSample(x):
    return (sin(pi*((x%360)-90)/180)+1)*(MAX_HUE_SCALE-MIN_HUE_SCALE)/2 + MIN_HUE_SCALE

# Scale base rgb by the sample
def scaleColor(rgb, scale):
    return tuple([min(255,round(n*scale)) for n in rgb])

# get an array of length SAMPLES containing the cycle rgb values
def getRGB():
    return [scaleColor(BASE_COLOR,sineSample(n*360/(SAMPLES-1))) for n in range(SAMPLES)]

# get LED RGB values for a certain step in the cycle
def fillSinewave(colors, tick):
    return [colors[(i+tick)%SAMPLES] for i in range(STRIP_SIZE)]

# Setup output image with margins
img = Image.new(mode="RGB", size=((TILE_SIZE+TILE_GAPH)*STRIPS+(2*TILE_MARGIN-TILE_GAPH), TILE_SIZE*STRIP_SIZE+2*TILE_MARGIN))
draw = ImageDraw.Draw(img)

colors = getRGB()
# Draws the cycles
x=TILE_MARGIN; y=TILE_MARGIN
for t in range(STRIPS):
    for rgb in fillSinewave(colors, t):
        draw.rectangle([x,y,x+(TILE_SIZE-1),y+(TILE_SIZE-1)],rgb)
        y+=TILE_SIZE
    x+=TILE_SIZE+TILE_GAPH; y=TILE_MARGIN

# Saves and displays image
img.save("materials/color_cycles.png")
img.show()
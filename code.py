import time
import board
import neopixel
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn

# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.A5
pixel_board = board.NEOPIXEL

# The number of NeoPixels
num_pixels = 30
num_board = 10

# potentiometers connected to A1, power & ground
red = AnalogIn(board.A1)
green = AnalogIn(board.A4)
blue = AnalogIn(board.A2)
white = AnalogIn(board.A3)

# buttons to trigger special patterns
button = DigitalInOut(board.A6)
button.direction = Direction.INPUT

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRBW
ORDER_BOARD = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.99, auto_write=False, pixel_order=ORDER
)
pixels_board = neopixel.NeoPixel (
    pixel_board, num_board, brightness=1.0, auto_write=False, pixel_order=ORDER_BOARD
)


def val(pin):

    # divides voltage (65535) to get a value between 0 and 255

    return pin.value / 257

def wheel(pos):

    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.

    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):

    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def rainbow_board(wait):

    for j in range(255):
        for i in range(num_board):
            pixel_index = (i * 256 // num_board) + j
            pixels_board[i] = wheel(pixel_index & 255)
        pixels_board.show()
        time.sleep(wait)

def police(wait):

    pixels[0] = (255, 0, 0)
    pixels[1] = (0, 0, 0)
    pixels[2] = (255, 0, 0)
    pixels[3] = (0, 0, 0)
    pixels[4] = (255, 0, 0)
    pixels[5] = (0, 0, 0)
    pixels[6] = (255, 0, 0)
    pixels[7] = (0, 0, 0)
    pixels[8] = (255, 0, 0)
    pixels[9] = (0, 0, 0)
    pixels[10] = (255, 0, 0)
    pixels[11] = (0, 0, 0)
    pixels[12] = (255, 0, 0)
    pixels[13] = (0, 0, 0)
    pixels[14] = (255, 0, 0)
    pixels[15] = (0, 0, 0)
    pixels[16] = (255, 0, 0)
    pixels[17] = (0, 0, 0)
    pixels[18] = (255, 0, 0)
    pixels[19] = (0, 0, 0)
    pixels[20] = (255, 0, 0)
    pixels[21] = (0, 0, 0)
    pixels[22] = (255, 0, 0)
    pixels[23] = (0, 0, 0)
    pixels[24] = (255, 0, 0)
    pixels[25] = (0, 0, 0)
    pixels[26] = (255, 0, 0)
    pixels[27] = (0, 0, 0)
    pixels[28] = (255, 0, 0)
    pixels[29] = (0, 0, 0) 
    pixels.show()
    time.sleep(wait)
    pixels[0] = (0, 0, 0)
    pixels[1] = (0, 0, 255)
    pixels[2] = (0, 0, 0)
    pixels[3] = (0, 0, 255)
    pixels[4] = (0, 0, 0)
    pixels[5] = (0, 0, 255)
    pixels[6] = (0, 0, 0)
    pixels[7] = (0, 0, 255)
    pixels[8] = (0, 0, 0)
    pixels[9] = (0, 0, 255)
    pixels[10] = (0, 0, 0)
    pixels[11] = (0, 0, 255)
    pixels[12] = (0, 0, 0)
    pixels[13] = (0, 0, 255)
    pixels[14] = (0, 0, 0)
    pixels[15] = (0, 0, 255)
    pixels[16] = (0, 0, 0)
    pixels[17] = (0, 0, 255)
    pixels[18] = (0, 0, 0)
    pixels[19] = (0, 0, 255)
    pixels[20] = (0, 0, 0)
    pixels[21] = (0, 0, 255)
    pixels[22] = (0, 0, 0)
    pixels[23] = (0, 0, 255)
    pixels[24] = (0, 0, 0)
    pixels[25] = (0, 0, 255)
    pixels[26] = (0, 0, 0)
    pixels[27] = (0, 0, 255)
    pixels[28] = (0, 0, 0)
    pixels[29] = (0, 0, 255)
    pixels.show()
    time.sleep(wait)

pixels_board.fill((0, 0, 255))
pixels_board.show()

while True:

    #pixels_board.fill((0, 0, 255))
    #pixels_board.fill(((int(val(red))), (int(val(green))), (int(val(blue)))))
    #pixels_board.show()
    
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill(((int(val(red))), (int(val(green))), (int(val(blue))), (int(val(white)))))
    # pixels.show()
   
    if button.value:
        
        #rainbow_cycle(0.001) # rainbow cycle with 1ms delay per step
        police(0.3)
        
    else:       

        pixels.fill(((int(val(red))), (int(val(green))), (int(val(blue))), (int(val(white))))) 
        pixels.show()

 #  rainbow_board(0.001)
 #  police(0.5)



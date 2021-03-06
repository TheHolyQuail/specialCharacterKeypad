# libraries for display and pin control
# import os
import time
import busio
import board
import displayio
# import terminalio
import adafruit_displayio_ssd1306
import adafruit_imageload
import math

# libraries for USB HID
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
# from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# custom library for typing special characters
from typeSym import (type_arrowUp, type_arrowDown, type_arrowUpDown
                     , type_oneHalf, type_squared, type_arrowRight
                     , type_arrowLeft, type_arrowRightLeft, type_ae
                     , type_degree, type_lowerTao, type_lowerBeta
                     , type_lowerSigma, type_lowerPhi, type_lowerDelta
                     , type_thorn, type_infinity, type_pi
                     , type_lowerMu, type_capitalOmega, type_capitalSigma
                     , type_theta, type_upperPhi, type_lowerEpsilon
                     , type_lowerAlpha, type_plusMinus, type_aproxEqual
                     , type_greaterOrEqual, type_lesserOrEqual, type_implies
                     , type_squareRoot, type_notEqual, type_oOperator
                     , type_dotProduct, type_defineEqual, type_intersection
                     , type_union, type_parallel, type_notParallel
                     , type_perpendicular, type_not, type_proves
                     , type_emptySet, type_bold, type_italic
                     , type_pageBreak, type_pasteNoFormat, type_subscript
                     , type_shortcutList, type_strikethrough, type_insertFootnote
                     , type_insertComment, type_superscript, unicodeSearch
                     , openPowershell, openSnipSketch, type_parentheses
                     , type_curllyBrackets, type_squareBrackets, type_doubleQuotes
                     , type_singleQuotes, type_commaSpace, unTab, commentCode)


# library for potentiometer
import analogio

# keyboard and button setup ##############################
# creating keyboard
Keyboard = Keyboard(usb_hid.devices)
Layout = KeyboardLayoutUS(Keyboard)

# declaring button pins
btn0_pin = board.GP15
btn1_pin = board.GP5
btn2_pin = board.GP4
btn3_pin = board.GP3
btn4_pin = board.GP2
btn5_pin = board.GP14
btn6_pin = board.GP13
btn7_pin = board.GP12
btn8_pin = board.GP11
btn9_pin = board.GP10

# setting pin settings
btn0 = digitalio.DigitalInOut(btn0_pin)
btn0.direction = digitalio.Direction.INPUT
btn0.pull = digitalio.Pull.UP

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.UP

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.UP

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.UP

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.UP

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.UP

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.UP

# potentiometer setup ####################################
pot = analogio.AnalogIn(board.GP26)
potPosition = 0
previousPotPosition = 0

def get_voltage(pin):
    # return (pin.value * 3.3) / 65536
    return (pin.value)/100

potValue = get_voltage(pot)

# character typing function setup ########################
"""
def type_a():
    Keyboard.press(Keycode.A)
    time.sleep(0.1)??
    Keyboard.release(Keycode.A)
"""
currentBitmap = 0

# display setup ##########################################
WIDTH = 128
HEIGHT = 64
CENTER_X = int(WIDTH/2)
CENTER_Y = int(HEIGHT/2)

displayio.release_displays()

SDA = board.GP8
SCL = board.GP9
i2c = busio.I2C(SCL, SDA)

if(i2c.try_lock()):
    print("i2c.scan(): " + str(i2c.scan()))
    i2c.unlock()
print()

display_bus = displayio.I2CDisplay(i2c, device_address=60)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

"""
???displayio??? drivers will also work with CircuitPython to display error messages
and other output to the display when the user code is not using it.
"""
print("Raspberry Pi Pico/CircuitPython ")
print("SSD1306 displayio (adafruit_displayio_ssd1306)")
time.sleep(.1)

# ================================================
"""
bitmap1, palette = adafruit_imageload.load("/bitmaps/bitmapTest2.bmp",
                                         bitmap=displayio.Bitmap,
                                         palette=displayio.Palette)
"""
# 0:, 1:, 2:, 3:, 4:, 5:, 6:, 7:, 8:, 9:
arrows, palette = adafruit_imageload.load("/bitmaps/arrows.bmp",
                                          bitmap=displayio.Bitmap,
                                          palette=displayio.Palette)

# 0:, 1:, 2:, 3:, 4:, 5:, 6:, 7:, 8:, 9:
logic1, palette = adafruit_imageload.load("/bitmaps/logicSymbols1.bmp",
                                          bitmap=displayio.Bitmap,
                                          palette=displayio.Palette)

# 0:, 1:, 2:, 3:, 4:, 5:, 6:, 7:, 8:, 9:
logic2, palette = adafruit_imageload.load("/bitmaps/logicSymbols2.bmp",
                                          bitmap=displayio.Bitmap,
                                          palette=displayio.Palette)

# 0:, 1:, 2:, 3:, 4:, 5:, 6:, 7:, 8:, 9:
mathOperators1, palette = adafruit_imageload.load("/bitmaps/mathCommonOperators1.bmp",
                                                  bitmap=displayio.Bitmap,
                                                  palette=displayio.Palette)

# 0:, 1:, 2:, 3:, 4:, 5:, 6:, 7:, 8:, 9:
mathSymbols1, palette = adafruit_imageload.load("/bitmaps/mathCommonSymbols1.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

# 0:, 1:, 2:, 3:, 4:, 5:, 6:, 7:, 8:, 9:
mathSymbols2, palette = adafruit_imageload.load("/bitmaps/mathCommonSymbols2.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

# 0:, 1:, 2:, 3:, 4:, 5:, 6:, 7:, 8:, 9:
gDocShortcuts, palette = adafruit_imageload.load("/bitmaps/gDocShortcuts.bmp",
                                                 bitmap=displayio.Bitmap,
                                                 palette=displayio.Palette)

# 0:, 1:, 2:, 3:, 4:, 5:, 6:, 7:, 8:, 9:
code1, palette = adafruit_imageload.load("/bitmaps/code1.bmp",
                                                 bitmap=displayio.Bitmap,
                                                 palette=displayio.Palette)

# Create TileGrids to hold the bitmaps
# tile_grid1 = displayio.TileGrid(bitmap1, pixel_shader=palette)

arrowsGrid = displayio.TileGrid(arrows, pixel_shader=palette)
logicGrid1 = displayio.TileGrid(logic1, pixel_shader=palette)
logicGrid2 = displayio.TileGrid(logic2, pixel_shader=palette)
mOperatorGrid1 = displayio.TileGrid(mathOperators1, pixel_shader=palette)
mSymbolGrid1 = displayio.TileGrid(mathSymbols1, pixel_shader=palette)
mSymbolGrid2 = displayio.TileGrid(mathSymbols2, pixel_shader=palette)
gDocShortGrid = displayio.TileGrid(gDocShortcuts, pixel_shader=palette)
codeGrid1 = displayio.TileGrid(code1, pixel_shader=palette)

# Create a Group to hold the TileGrids
group = displayio.Group(max_size=5)

# Add the TileGrid to the Group
# group.append(tile_grid2)
group.append(arrowsGrid)

# Add the Group to the Display
display.show(group)

# Loop forever so you can enjoy your image
while True:
    time.sleep(0.1)

    # check potentiometer and update position (potentiometer values range from ~10 to ~640)
    if math.fabs(get_voltage(pot) - potValue) > 10:
        potValue = get_voltage(pot)

        if get_voltage(pot) > 608:
            # set keyboard to code1
            potPosition = 7

            group.pop(0)
            group.append(codeGrid1)
            display.show(group)
            
        elif get_voltage(pot) > 538:
            # set keyboard to google doc shortcuts
            potPosition = 6

            group.pop(0)
            group.append(gDocShortGrid)
            display.show(group)

        elif get_voltage(pot) > 448:
            # set keyboard to logic symbols 1
            potPosition = 5

            group.pop(0)
            group.append(logicGrid1)
            display.show(group)

        elif get_voltage(pot) > 358:
            # set keyboard to logic symbols 2
            potPosition = 4

            group.pop(0)
            group.append(logicGrid2)
            display.show(group)

        elif get_voltage(pot) > 268:
            # set keyboard to math operators 1
            potPosition = 3

            group.pop(0)
            group.append(mOperatorGrid1)
            display.show(group)

        elif get_voltage(pot) > 178:
            # set keyboard to math symbols 1
            potPosition = 2

            group.pop(0)
            group.append(mSymbolGrid1)
            display.show(group)

        elif get_voltage(pot) > 88:
            # set keyboard to math symbols 2
            potPosition = 1

            group.pop(0)
            group.append(mSymbolGrid2)
            display.show(group)

        else:
            # set keyboard to arrows and exponents
            potPosition = 0

            group.pop(0)
            group.append(arrowsGrid)
            display.show(group)

# ----------------------------------------------------------

    if potPosition == 0:
        if not btn0.value:
            # type "???"
            type_arrowUp()

        if not btn1.value:
            # type "???"
            type_arrowDown()

        if not btn2.value:
            # type "???"
            type_arrowUpDown()

        if not btn3.value:
            # type "??"
            type_oneHalf()

        if not btn4.value:
            # type "??"
            type_squared()

        if not btn5.value:
            # type "???"
            type_arrowRight()

        if not btn6.value:
            # type "???"
            type_arrowLeft()

        if not btn7.value:
            # type "???"
            type_arrowRightLeft()

        if not btn8.value:
            # type "??"
            type_ae()

        if not btn9.value:
            # type "??"
            type_degree()

# ----------------------------------------------------------

    elif potPosition == 1:
        if not btn0.value:
            # type ""
            unicodeSearch()

        if not btn1.value:
            # type "??"
            type_lowerTao()

        if not btn2.value:
            # type ""
            unicodeSearch()

        if not btn3.value:
            # type ""
            unicodeSearch()

        if not btn4.value:
            # type "??"
            type_lowerBeta()

        if not btn5.value:
            # type "??"
            type_lowerSigma()

        if not btn6.value:
            # type "??"
            type_lowerPhi()

        if not btn7.value:
            # type "??"
            type_lowerDelta()

        if not btn8.value:
            # type ""
            unicodeSearch()

        if not btn9.value:
            # type "??"
            type_thorn()

# ----------------------------------------------------------

    elif potPosition == 2:
        if not btn0.value:
            # type "???"
            type_infinity()

        if not btn1.value:
            # type "??"
            type_pi()

        if not btn2.value:
            # type ""
            unicodeSearch()

        if not btn3.value:
            # type "??"
            type_lowerMu()

        if not btn4.value:
            # type "??"
            type_capitalOmega()

        if not btn5.value:
            # type "??"
            type_capitalSigma()

        if not btn6.value:
            # type "??"
            type_theta()

        if not btn7.value:
            # type "??"
            type_upperPhi()

        if not btn8.value:
            # type "??"
            type_lowerEpsilon()

        if not btn9.value:
            # type "??"
            type_lowerAlpha()

# ----------------------------------------------------------

    elif potPosition == 3:
        if not btn0.value:
            # type "??"
            type_plusMinus()

        if not btn1.value:
            # type "???"
            type_aproxEqual()

        if not btn2.value:
            # type "???"
            type_greaterOrEqual()

        if not btn3.value:
            # type "???"
            type_lesserOrEqual()

        if not btn4.value:
            # type "???>"
            type_implies()

        if not btn5.value:
            # type "???("
            type_squareRoot()

        if not btn6.value:
            # type "!="
            type_notEqual()

        if not btn7.value:
            # type "???"
            type_oOperator()

        if not btn8.value:
            # type "???"
            type_dotProduct()

        if not btn9.value:
            # type "???"
            type_defineEqual()

# ----------------------------------------------------------

    elif potPosition == 4:
        if not btn0.value:
            # type "???"
            type_intersection()

        if not btn1.value:
            # type "U"
            type_union()

        if not btn2.value:
            # type ""
            unicodeSearch()

        if not btn3.value:
            # type ""
            unicodeSearch()

        if not btn4.value:
            # type ""
            unicodeSearch()

        if not btn5.value:
            # type ""
            unicodeSearch()

        if not btn6.value:
            # type ""
            unicodeSearch()

        if not btn7.value:
            # type "||"
            type_parallel()

        if not btn8.value:
            # type "???"
            type_notParallel()

        if not btn9.value:
            # type "???"
            type_perpendicular()

# ----------------------------------------------------------

    elif potPosition == 5:
        if not btn0.value:
            # type ""
            unicodeSearch()

        if not btn1.value:
            # type ""
            unicodeSearch()

        if not btn2.value:
            # type ""
            unicodeSearch()

        if not btn3.value:
            # type "??"
            type_not()

        if not btn4.value:
            # type "???"
            type_proves()

        if not btn5.value:
            # type ""
            unicodeSearch()

        if not btn6.value:
            # type ""
            unicodeSearch()

        if not btn7.value:
            # type ""
            unicodeSearch()

        if not btn8.value:
            # type ""
            unicodeSearch()

        if not btn9.value:
            # type "??"
            type_emptySet()

# ----------------------------------------------------------

    elif potPosition == 6:
        if not btn0.value:
            # ctrl+b
            type_bold()

        if not btn1.value:
            # ctrl+i
            type_italic()

        if not btn2.value:
            # t
            type_pageBreak()

        if not btn3.value:
            # t
            type_pasteNoFormat()

        if not btn4.value:
            # t
            type_subscript()

        if not btn5.value:
            # t
            type_shortcutList()

        if not btn6.value:
            # t
            type_strikethrough()

        if not btn7.value:
            # t
            type_insertFootnote()

        if not btn8.value:
            # t
            type_insertComment()

        if not btn9.value:
            # t
            type_superscript()

# ----------------------------------------------------------

    elif potPosition == 7:
        if not btn0.value:
            # type parentheses and back arrow into them.
            type_parentheses()

        if not btn1.value:
            # type curlly brackets and back arrow into them.
            type_curllyBrackets()

        if not btn2.value:
            # type square brackets and back arrow into them.
            type_squareBrackets()

        if not btn3.value:
            # type double quotes and back arrow into them.
            type_doubleQuotes()

        if not btn4.value:
            # type single quotes and back arrow into them.
            type_singleQuotes()

        if not btn5.value:
            # type a comma follwed with a space
            type_commaSpace()

        if not btn6.value:
            # un-tab shortcut
            unTab()

        if not btn7.value:
            # comment code shortcut
            commentCode()

        if not btn8.value:
            # open power shell application
            openPowershell()

        if not btn9.value:
            # open snip and sketch application
            openSnipSketch()

# ---------------------------------------------------

    else:
        if not btn0.value:
            # type "??"
            type_pi()

        if not btn1.value:
            # type "??"
            type_pi()

        if not btn2.value:
            # type "??"
            type_pi()

        if not btn3.value:
            # type "??"
            type_pi()

        if not btn4.value:
            # type "??"
            type_pi()

        if not btn5.value:
            # type "??"
            type_pi()

        if not btn6.value:
            # type "??"
            type_pi()

        if not btn7.value:
            # type "??"
            type_pi()

        if not btn8.value:
            # type "??"
            type_pi()

        if not btn9.value:
            # type "??"
            type_pi()

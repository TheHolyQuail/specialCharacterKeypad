# importing necessary functions
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# setting up an HID keyboard
Keyboard = Keyboard(usb_hid.devices)
Layout = KeyboardLayoutUS(Keyboard)

# the functions for typing special characters
# test:
def type_a():
    # types: "a"
    Keyboard.press(Keycode.A)
    time.sleep(0.02)
    Keyboard.release(Keycode.A)

# open the unicode search menu if there is no general use alt code
def unicodeSearch():
    Keyboard.press(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.04)
    Keyboard.release(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.02)
    # type "charmap"
    Keyboard.press(Keycode.C)
    time.sleep(0.02)
    Keyboard.release(Keycode.C)
    Keyboard.press(Keycode.H)
    time.sleep(0.02)
    Keyboard.release(Keycode.H)
    Keyboard.press(Keycode.A)
    time.sleep(0.02)
    Keyboard.release(Keycode.A)
    Keyboard.press(Keycode.R)
    time.sleep(0.02)
    Keyboard.release(Keycode.R)
    Keyboard.press(Keycode.M)
    time.sleep(0.02)
    Keyboard.release(Keycode.M)
    Keyboard.press(Keycode.A)
    time.sleep(0.02)
    Keyboard.release(Keycode.A)
    Keyboard.press(Keycode.P)
    time.sleep(0.02)
    Keyboard.release(Keycode.P)
    time.sleep(0.02)
    Keyboard.press(Keycode.ENTER)
    time.sleep(0.02)
    Keyboard.release(Keycode.ENTER)
    time.sleep(0.02)

# arrows
def type_arrowLeft():
    # types: ←
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_arrowRight():
    # types: →
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_SIX)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_SIX)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_arrowRightLeft():
    # types: ↔
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_arrowUp():
    # types: ↑
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_arrowDown():
    # types: ↓
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_arrowUpDown():
    # types: ↕
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_oneHalf():
    # types: ½
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_ae():
    # types: æ
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_degree():
    # types: °
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_squared():
    # types: ²
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

# logicSymbols1
# no type_thereExists

# no type_notThereExists

# no type_forAll

def type_not():
    # types: ¬
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_proves():
    # types: ├
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

# no type_elementOf():

# no type_notElementOf():

# no type_logicalAnd():

# no type_logicalOR():

def type_emptySet():
    # types: Ø
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_SIX)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_SIX)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)


# logicSymbols2
def type_intersection():
    # types: ∩
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_union():
    # types: U
    Keyboard.press(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.U)
    time.sleep(0.02)
    Keyboard.release(Keycode.U)
    time.sleep(0.02)
    Keyboard.release(Keycode.SHIFT)

# no type_subset():

# no type_subsetOrEqual():

# no type_notSubset():

# no type_integral():

# no type_therefore():

def type_parallel():
    # types: ||
    Keyboard.press(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.BACKSLASH)
    time.sleep(0.02)
    Keyboard.release(Keycode.BACKSLASH)
    time.sleep(0.02)
    Keyboard.press(Keycode.BACKSLASH)
    time.sleep(0.02)
    Keyboard.release(Keycode.BACKSLASH)
    time.sleep(0.02)
    Keyboard.release(Keycode.SHIFT)

def type_notParallel():
    # types: ╫
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_perpendicular():
    # types: ┴
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

# mathCommonOperators1

def type_plusMinus():
    # types: ±
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_aproxEqual():
    # types: ≈
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_greaterOrEqual():
    # types: ≥
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_lesserOrEqual():
    # types: ≤
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_implies():
    # types: ═>
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.SHIFT, Keycode.PERIOD)
    time.sleep(0.02)
    Keyboard.release(Keycode.SHIFT, Keycode.PERIOD)

def type_squareRoot():
    # types:
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.SHIFT, Keycode.NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.SHIFT, Keycode.NINE)

def type_notEqual():
    # types:
    Keyboard.press(Keycode.SHIFT, Keycode.ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.SHIFT, Keycode.ONE)
    time.sleep(0.02)
    Keyboard.press(Keycode.EQUALS)
    time.sleep(0.02)
    Keyboard.release(Keycode.EQUALS)

def type_oOperator():
    # types: ○
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_dotProduct():
    # types: •
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_defineEqual():
    # types: ≡
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

# mathCommonSymbols1
def type_infinity():
    # types: ∞
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_SIX)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_SIX)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_pi():
    # types: π
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

# no type_upperDelta():

def type_lowerMu():
    # types: µ
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_capitalOmega():
    # types: Ω
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_capitalSigma():
    # types: Σ
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_theta():
    # types: Θ
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_upperPhi():
    # types: Φ
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_lowerEpsilon():
    # types: ε
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_EIGHT)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_lowerAlpha():
    # types: α
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FOUR)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

# mathCommonSymbols2

# no lowerOmega

def type_lowerTao():
    # types: τ
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ONE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

# no lowerLambda

# no lowerRho

def type_lowerBeta():
    # types: ß
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_lowerSigma():
    # types: σ
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_lowerPhi():
    # types: φ
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_SEVEN)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_lowerDelta():
    # types: δ
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_THREE)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

# no type_proportionalTo

def type_thorn():
    # types: Þ
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_ZERO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.press(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.KEYPAD_TWO)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

# google doc shortcuts:
def type_bold():
    # ctrl+b
    Keyboard.press(Keycode.CONTROL)
    time.sleep(0.02)
    Keyboard.press(Keycode.B)
    time.sleep(0.02)
    Keyboard.release(Keycode.B)
    time.sleep(0.02)
    Keyboard.release(Keycode.CONTROL)

def type_italic():
    # ctrl+i
    Keyboard.press(Keycode.CONTROL)
    time.sleep(0.02)
    Keyboard.press(Keycode.I)
    time.sleep(0.02)
    Keyboard.release(Keycode.I)
    time.sleep(0.02)
    Keyboard.release(Keycode.CONTROL)

def type_strikethrough():
    # alt+shift+5
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.FIVE)
    time.sleep(0.02)
    Keyboard.release(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)

def type_superscript():
    # ctrl+.
    Keyboard.press(Keycode.CONTROL)
    time.sleep(0.02)
    Keyboard.press(Keycode.PERIOD)
    time.sleep(0.02)
    Keyboard.release(Keycode.PERIOD)
    time.sleep(0.02)
    Keyboard.release(Keycode.CONTROL)

def type_subscript():
    # ctrl+,
    Keyboard.press(Keycode.CONTROL)
    time.sleep(0.02)
    Keyboard.press(Keycode.COMMA)
    time.sleep(0.02)
    Keyboard.release(Keycode.COMMA)
    time.sleep(0.02)
    Keyboard.release(Keycode.CONTROL)

def type_insertComment():
    # ctrl+alt+m
    Keyboard.press(Keycode.CONTROL)
    time.sleep(0.02)
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.M)
    time.sleep(0.02)
    Keyboard.release(Keycode.M)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.release(Keycode.CONTROL)

def type_insertFootnote():
    # ctrl+alt+m
    Keyboard.press(Keycode.CONTROL)
    time.sleep(0.02)
    Keyboard.press(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.press(Keycode.F)
    time.sleep(0.02)
    Keyboard.release(Keycode.F)
    time.sleep(0.02)
    Keyboard.release(Keycode.ALT)
    time.sleep(0.02)
    Keyboard.release(Keycode.CONTROL)

def type_pasteNoFormat():
    # ctrl+shift+v
    Keyboard.press(Keycode.CONTROL)
    time.sleep(0.02)
    Keyboard.press(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.V)
    time.sleep(0.02)
    Keyboard.release(Keycode.V)
    time.sleep(0.02)
    Keyboard.release(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.release(Keycode.CONTROL)

def type_pageBreak():
    # ctrl+enter
    Keyboard.press(Keycode.CONTROL)
    time.sleep(0.02)
    Keyboard.press(Keycode.ENTER)
    time.sleep(0.02)
    Keyboard.release(Keycode.ENTER)
    time.sleep(0.02)
    Keyboard.release(Keycode.CONTROL)

def type_shortcutList():
    # ctrl+/
    Keyboard.press(Keycode.CONTROL)
    time.sleep(0.02)
    Keyboard.press(Keycode.FORWARD_SLASH)
    time.sleep(0.02)
    Keyboard.release(Keycode.FORWARD_SLASH)
    time.sleep(0.02)
    Keyboard.release(Keycode.CONTROL)
    

# code shortcuts 1
def type_parentheses():
    # type parentheses and back arrow into them
    Keyboard.press(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.NINE)
    time.sleep(0.02)
    Keyboard.release(Keycode.NINE)
    time.sleep(0.02)
    Keyboard.press(Keycode.ZERO)
    time.sleep(0.02)
    Keyboard.release(Keycode.ZERO)
    Keyboard.release(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.LEFT_ARROW)
    time.sleep(0.02)
    Keyboard.release(Keycode.LEFT_ARROW)

def type_curllyBrackets():
    # type curlly brackets and back arrow into them
    Keyboard.press(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.LEFT_BRACKET)
    time.sleep(0.02)
    Keyboard.release(Keycode.LEFT_BRACKET)
    time.sleep(0.02)
    Keyboard.press(Keycode.RIGHT_BRACKET)
    time.sleep(0.02)
    Keyboard.release(Keycode.RIGHT_BRACKET)
    Keyboard.release(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.LEFT_ARROW)
    time.sleep(0.02)
    Keyboard.release(Keycode.LEFT_ARROW)

def type_squareBrackets():
    # type squre brackets and back arrow into them
    Keyboard.press(Keycode.LEFT_BRACKET)
    time.sleep(0.02)
    Keyboard.release(Keycode.LEFT_BRACKET)
    time.sleep(0.02)
    Keyboard.press(Keycode.RIGHT_BRACKET)
    time.sleep(0.02)
    Keyboard.release(Keycode.RIGHT_BRACKET)
    time.sleep(0.02)
    Keyboard.press(Keycode.LEFT_ARROW)
    time.sleep(0.02)
    Keyboard.release(Keycode.LEFT_ARROW)

def type_doubleQuotes():
    # type double quotes and back arrow into them
    Keyboard.press(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.QUOTE)
    time.sleep(0.02)
    Keyboard.release(Keycode.QUOTE)
    time.sleep(0.02)
    Keyboard.press(Keycode.QUOTE)
    time.sleep(0.02)
    Keyboard.release(Keycode.QUOTE)
    Keyboard.release(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.LEFT_ARROW)
    time.sleep(0.02)
    Keyboard.release(Keycode.LEFT_ARROW)

def type_singleQuotes():
    # type single quotes and back arrow into them
    Keyboard.press(Keycode.QUOTE)
    time.sleep(0.02)
    Keyboard.release(Keycode.QUOTE)
    time.sleep(0.02)
    Keyboard.press(Keycode.QUOTE)
    time.sleep(0.02)
    Keyboard.release(Keycode.QUOTE)
    time.sleep(0.02)
    Keyboard.press(Keycode.LEFT_ARROW)
    time.sleep(0.02)
    Keyboard.release(Keycode.LEFT_ARROW)

def type_commaSpace():
    # type a comma follwed by a space
    Keyboard.press(Keycode.COMMA)
    time.sleep(0.02)
    Keyboard.release(Keycode.COMMA)
    time.sleep(0.02)
    Keyboard.press(Keycode.SPACE)
    time.sleep(0.02)
    Keyboard.release(Keycode.SPACE)

def unTab():
    # shortcut to delete tab spaces on multiple lines
    Keyboard.press(Keycode.SHIFT)
    time.sleep(0.02)
    Keyboard.press(Keycode.TAB)
    time.sleep(0.02)
    Keyboard.release(Keycode.TAB)
    time.sleep(0.02)
    Keyboard.release(Keycode.SHIFT)

def commentCode():
    # shortcut ot comment code in most IDEs
    # ctrl+/
    Keyboard.press(Keycode.CONTROL)
    time.sleep(0.02)
    Keyboard.press(Keycode.FORWARD_SLASH)
    time.sleep(0.02)
    Keyboard.release(Keycode.FORWARD_SLASH)
    time.sleep(0.02)
    Keyboard.release(Keycode.CONTROL)

def openPowershell():
    # open powershell
    Keyboard.press(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.04)
    Keyboard.release(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.02)
    # type "powershell"
    Keyboard.press(Keycode.P)
    time.sleep(0.02)
    Keyboard.release(Keycode.P)
    Keyboard.press(Keycode.O)
    time.sleep(0.02)
    Keyboard.release(Keycode.O)
    Keyboard.press(Keycode.W)
    time.sleep(0.02)
    Keyboard.release(Keycode.W)
    Keyboard.press(Keycode.E)
    time.sleep(0.02)
    Keyboard.release(Keycode.E)
    Keyboard.press(Keycode.R)
    time.sleep(0.02)
    Keyboard.release(Keycode.R)
    Keyboard.press(Keycode.S)
    time.sleep(0.02)
    Keyboard.release(Keycode.S)
    Keyboard.press(Keycode.H)
    time.sleep(0.02)
    Keyboard.release(Keycode.H)
    Keyboard.press(Keycode.E)
    time.sleep(0.02)
    Keyboard.release(Keycode.E)
    Keyboard.press(Keycode.L)
    time.sleep(0.02)
    Keyboard.release(Keycode.L)
    Keyboard.press(Keycode.L)
    time.sleep(0.02)
    Keyboard.release(Keycode.L)
    time.sleep(0.02)
    Keyboard.press(Keycode.ENTER)
    time.sleep(0.02)
    Keyboard.release(Keycode.ENTER)
    time.sleep(0.02)
    
def openSnipSketch():
    # open snip and sketch
    Keyboard.press(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S)
    time.sleep(0.04)
    Keyboard.release(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S)
    time.sleep(0.02)
    
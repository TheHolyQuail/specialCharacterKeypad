# specialCharacterKeypad
This project is a custom keypad using 10 Cherry MX keys as input, a potentiometer to change key values, and 128x64 OLED screen based key value readout all powered by the Raspberry Pi Pico. 
It is focused on allowing quick access to common symbols and letters used in math and science that are not present on the standard US keyboard.

The keypad CAD and ECAD were designed in Fusion 360 and the RP2040 is programed in Curcuitpython taking advantage of the libraries: time, busio, board, displayio, adafruit_displayio_ssd1306 (since the OLED used is based on the ssd1306), adafruit_imageload, math, digitalio, usb_hid, and parts of adafruit_hid.

The custom code is split into two files code.py which contains the loop and keyboard state control and typeSym.py which houses the functions used to send keystrokes to the host computer.

More a more detailed descriptions and assembly/programming instructions are availible on maker.io (link: )
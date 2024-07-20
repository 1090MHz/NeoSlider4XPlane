import sys
import time
import struct
import usb_hid
import adafruit_hid
import board
import neopixel
import analogio
import touchio

# Device setup
touch = touchio.TouchIn(board.TOUCH)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 2, brightness=1)
slider = analogio.AnalogIn(board.POTENTIOMETER)  # ranges from 0-65535
gamepad_device = adafruit_hid.find_device(usb_hid.devices, usage_page=0x01, usage=0x05)

def send_gamepad_report(button_value, slider_value):
    report = bytearray(2)
    struct.pack_into("<Bbb", report, 0, button_value, slider_value)
    gamepad_device.send_report(report)

def hsv2rgb(h: int, s: int, v: int) -> tuple:
    h, s, v = h / 255.0, s / 255.0, v / 255.0
    i = int(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i = i % 6
    if i == 0: return (int(v*255), int(t*255), int(p*255))
    if i == 1: return (int(q*255), int(v*255), int(p*255))
    if i == 2: return (int(p*255), int(v*255), int(t*255))
    if i == 3: return (int(p*255), int(q*255), int(v*255))
    if i == 4: return (int(t*255), int(p*255), int(v*255))
    if i == 5: return (int(v*255), int(p*255), int(q*255))

# Initial color setup
hue_a, sat_a, val_a = 0, 255, 255
hue_b, sat_b, val_b = 127, 255, 255
pixels[0] = hsv2rgb(hue_a, sat_a, val_a)
pixels[1] = hsv2rgb(hue_b, sat_b, val_b)

last_slider_value = 0
last_button = 0

while True:
    button_value = touch.value
    if last_button != button_value:
        last_button = button_value
        send_gamepad_report(button_value, last_slider_value - 128)

    slider_value = slider.value // 256  # Adjust to 0-255 range
    if abs(slider_value - last_slider_value) > 2:
        last_slider_value = slider_value
        pixels[0] = hsv2rgb(slider_value, sat_a, val_a)
        pixels[1] = hsv2rgb(slider_value, sat_b, val_b)
        send_gamepad_report(button_value, slider_value - 128)
        time.sleep(0.01)
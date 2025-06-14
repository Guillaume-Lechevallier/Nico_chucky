import board
import digitalio
import time

# Initialize GPIO12 as an output for the LED
led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT

try:
    # Turn on the LED
    led.value = True
    time.sleep(5)
finally:
    # Ensure the LED is turned off after the delay
    led.value = False

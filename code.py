import board
import digitalio
import time

# LED on GPIO12 that will blink
led1 = digitalio.DigitalInOut(board.GP12)
led1.direction = digitalio.Direction.OUTPUT

# Red LED on GPIO13 that stays on for 10 seconds
led2 = digitalio.DigitalInOut(board.GP13)
led2.direction = digitalio.Direction.OUTPUT

BLINK_INTERVAL = 12.5  # seconds
_HALF_PERIOD = BLINK_INTERVAL / 2

start = time.monotonic()
led2.value = True

try:
    while True:
        led1.value = True
        time.sleep(_HALF_PERIOD)
        led1.value = False
        time.sleep(_HALF_PERIOD)

        if time.monotonic() - start >= 10:
            led2.value = False
except KeyboardInterrupt:
    pass
finally:
    led1.value = False
    led2.value = False

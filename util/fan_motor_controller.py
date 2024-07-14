import board
import digitalio
from util.debug import Debug


class FanMotorController:
    def __init__(self, fan_pin: board.pin, debug: Debug):
        self.debug = debug
        self.relay = digitalio.DigitalInOut(fan_pin)
        self.relay.direction = digitalio.Direction.OUTPUT
        self.running = False
        self.relay.value = False

    def fan_on(self):
        self.running = True
        if not self.relay.value: # Only print once when value changes
            self.debug.print_debug("fan", "Fan ON")
        self.relay.value = True

    def fan_off(self):
        self.running = False
        if self.relay.value:  # Only print once when value changes
            self.debug.print_debug("fan", "Fan OFF")
        self.relay.value = False

import os
import time
import board
#from traceback import format_exception

from util.debug import Debug
from util.fan_motor_controller import FanMotorController
# from util.simple_timer import Timer
from util.temperature import TemperatureReader

loop_count = 0
temp_avg = 0

debug = Debug()
fan_motor = FanMotorController(board.D1, debug)

debug.check_debug_enable()
debug.print_debug("code","CircuitPython version " + str(os.uname().version))

temperature = TemperatureReader(debug)
# timer = Timer()
# timer.start_timer(properties.defaults["send_interval"])

avg = 0
while True:
    loop_count += 1
    debug.check_debug_enable()
    temp, humidity = temperature.read()
    temp_avg += temp
    try:
        if loop_count % 10 is 0: # Read temp 10 times and compute avg temp
            avg = int(temp_avg/loop_count)
            # timer.reset_timer(properties.defaults["send_interval"])
            loop_count = 0
            temp_avg = 0
            time.sleep(.1)
            debug.print_debug("code", "avg temp: %2d" % (avg))
            if avg > 80:
                fan_motor.fan_on()
            else:
                fan_motor.fan_off()
        time.sleep(2)

    except Exception as e:
        # error = str(format_exception(e))
        error = str(e)
        debug.print_debug("code","Exception in main: "+error)

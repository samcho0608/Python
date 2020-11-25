import time
import keyboard
from PIL import ImageGrab


def screenshot():
    current_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(current_time))

keyboard.add_hotkey("ctrl+shift+s", screenshot) # if u want to use ctrl shift s
# keyboard.add_hotkey("F9", screenshot) # use F9 key to take a screenshot and save it

keyboard.wait("esc") # run program till the user presses esc
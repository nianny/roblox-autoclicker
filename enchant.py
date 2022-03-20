import time
import pyautogui
from pynput import keyboard


# time.sleep(5)
# print(pyautogui.position())
def on_press(key):
    try:
        print(type(key), key.char, type(key.char)) 
        # print('alphanumeric key {0} pressed'.format(
        #     key.char))

        if key.char == 'm':
            pyautogui.click()
            # time.sleep(0.1)
            pyautogui.click()
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    pass


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


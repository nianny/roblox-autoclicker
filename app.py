import pyautogui
import keyboard
import time
# keyboard.add_hotkey("ctrl+p", lambda: print("ctrl+p pressed"))
# pyautogui.click()

# import keyboard
# def running():
    # rk = keyboard.record(until ='z')
    # pyautogui.mouseDown();

# print(pyautogui.position())
# keyboard.add_hotkey("q", lambda: pyautogui.click())

# keyboard.add_hotkey("w", lambda: pyautogui.click(657, 550))
# keyboard.add_hotkey("o", lambda: pyautogui.click(764, 550))
# keyboard.add_hotkey("p", lambda: pyautogui.click(869, 550))
  
# # It records all the keys until escape is pressedeeee
# keyboard.wait('esc')
  
# It replay back the all keys
# keyboard.play(rk, speed_factor = 1)
time.sleep(2)


#     pyautogui.click()
#     keyboard.press("e")
#     time.sleep(0.75)

# pyautogui.press("d")
pyautogui.keyDown("d")
time.sleep(0.001)
pyautogui.keyUp("d")

# time.sleep(2)
# keyboard.press("space")


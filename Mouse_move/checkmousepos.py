import pyautogui
import time


if "__main__" == __name__:
    try:
        while True:
            print(pyautogui.position())
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stop")

import pyautogui
import time
import random

# MAC ONLY
# I increase the failsafe time because my mac can get laggy sometimes. Read more on https://pyautogui.readthedocs.io/en/latest/
pyautogui.DARWIN_CATCH_UP_TIME = 0.1


def end_turn():
    pyautogui.moveTo(2220, 700)
    pyautogui.doubleClick()


def end_turn_last_moment():
    while True:
        end_turn()
        random_time = random.uniform(70, 73.5)
        # The more your opponent stalls the higher you make this variable. Range: [0 - 75]
        opponent_turn_time = 50
        time.sleep(random_time + opponent_turn_time)


end_turn_last_moment()

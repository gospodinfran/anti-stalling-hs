from pyautogui import moveTo, locateCenterOnScreen, doubleClick
from time import sleep
from random import uniform
from PIL import Image
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--locate", action="store_true")
args = parser.parse_args()

# Automatically locates end turn and enemy turn buttons
USE_SCREEN_LOCATE = args.locate

if USE_SCREEN_LOCATE:
    end_turn = Image.open("end_turn.png")
    end_turn_pos = locateCenterOnScreen(end_turn, confidence=.8)
    if end_turn:
        print("Found button.")


def end_turn():
    if USE_SCREEN_LOCATE:
        moveTo(end_turn)
    else:
        moveTo(2200, 600)
    doubleClick()


def end_turn_last_moment():
    end_turn()
    random_time = uniform(68, 72.5)
    # The more your opponent stalls the higher you make this variable. Range: [0 - 75]
    opponent_turn_time = 50
    sleep(random_time + opponent_turn_time)


while True:
    end_turn_last_moment()

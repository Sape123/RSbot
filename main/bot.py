import pyautogui
import time
from random import randint


def main():

    while True:

        choptrees()
        droplogs()


def get_coords():
    juuso = 0
    while True:

        currentMouseX, currentMouseY = pyautogui.position()

        if juuso != currentMouseX:
            print(currentMouseX)
            print(currentMouseY)
        juuso = currentMouseX

def choptrees():

    treelocation = pyautogui.locateOnScreen('bigmoney.png')

    try:
        pyautogui.moveTo(treelocation[0],treelocation[1])
        time.sleep(.600)
        pyautogui.click()
        time.sleep(20)

    except TypeError:
        print("no trees to be found")


def droplogs():

    loglocation = pyautogui.locateOnScreen('log.png')

    try:
        pyautogui.moveTo(loglocation[0], loglocation[1])
        pyautogui.rightClick()
        pyautogui.click('drop.png')
    except TypeError:
        print("no logs in inv")



main()
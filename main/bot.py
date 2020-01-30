import pyautogui
from random import randint
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from lxml import html
import cv2

def main():



    while True:
        logout()
        choptrees()
        droplogs()


def get_coords():
    mouse = 0
    while True:

        currentMouseX, currentMouseY = pyautogui.position()

        if mouse != currentMouseX:
            print(currentMouseX)
            print(currentMouseY)
        mouse = currentMouseX

def choptrees():

    treelocation = pyautogui.locateOnScreen('bigshow.png', confidence=0.9)

    try:
        pyautogui.moveTo(treelocation[0],treelocation[1])
        time.sleep(.600)
        pyautogui.click()
        time.sleep(5)

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


def logout():
    minimap = pyautogui.screenshot('konsta.png', region=(3603, 62, 130, 120))
    print(pyautogui.locateOnScreen('vihu.png', region=(3603, 62, 130, 120), confidence=1))


main()
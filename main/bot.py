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


def webscrape():

    url = "https://oldschoolrunescape.fandom.com/wiki/Burnt_chicken"
    response = requests.get(url)
    content = html.fromstring(response.content)
    time.sleep(1)
    pyautogui.write('noobsnoobsnoobs', interval=0.25)
    pyautogui.press('enter')




main()
import select
import sys
import time
import pynput
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

def fun():
    time.sleep(3)
    keyboard.type('pls beg')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls hunt')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls fish')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls dig')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls search')
    keyboard.press(Key.enter)
    time.sleep(2)
    mouse.position = (300,740)
    time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(1)
    mouse.position = (300,790)
    time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(3)
    keyboard.type('pls hl')
    keyboard.press(Key.enter)
    time.sleep(2)
    mouse.position = (300,740)
    time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(1)
    mouse.position = (300,790)
    time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(3)
    keyboard.type('pls dep all')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls use horse')
    keyboard.press(Key.enter)

num = 1000 #Bassically the number of times u want this code to run. One round is 35 seconds

for i in range(0,num):
    fun()

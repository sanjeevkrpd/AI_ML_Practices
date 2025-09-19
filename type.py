import pyautogui as py
import time as t


t.sleep(3)


for i in range(100):
    py.typewrite("i want my order today")
    py.press("enter")

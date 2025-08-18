import pyautogui as py
import time as t

# Wait 3 seconds before starting
t.sleep(3)

# Type and send "hii" 10 times
for i in range(10):
    py.typewrite("hii")
    py.press("enter")

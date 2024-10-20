import random
import pywhatkit as kit
kit.sendwhatmsg("+91XXXXXXXXXXX","skills",24,00 )#enter phone number and time

#@python.coder
import pyautogui as pg
import time
skills=(' java', 'c',' python')
time.sleep(8)
for i in range(50):
    a=random.choice(skills)
    pg.write("iam good in"+a)
    pg.press('enter')

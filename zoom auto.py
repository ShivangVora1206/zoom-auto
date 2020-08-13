import pyautogui
import subprocess
import pyperclip as p
from time import sleep

x = 1920
y = 1080
print("----------------------zoom automation--------------------------")
#meetid = input("ENTER YOUR MEETING ID ")
meetid = p.paste()
if meetid == str(0):
    exit
else:
    pw = input("ENTER MEETING PASSWORD ")
    subprocess.run(r"C:\Users\shang\AppData\Roaming\Zoom\bin\Zoom.exe")
    sleep(0.5)
    pyautogui.click(x/2.5, y/2.4)
    sleep(1)
    pyautogui.typewrite(meetid)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    sleep(0.5)
    pyautogui.press("tab")
    pyautogui.press("enter")
    sleep(0.5)
    pyautogui.press("tab")
    pyautogui.press("enter")
    sleep(4)
    pyautogui.typewrite(pw)
    pyautogui.press("enter")
    sleep(4)
    pyautogui.click(x/1.263, y/8.2)
    exit        




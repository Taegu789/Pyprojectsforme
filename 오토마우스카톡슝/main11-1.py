import pyautogui
import os
import pyperclip
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# py 파일의 실행경로로 이동하기 위해 (dirname), 현재경로 __file__로 이동한다.

picposition = pyautogui.locateOnScreen('k1.png')
print(picposition)

clickposition = pyautogui.center(picposition)
pyautogui.doubleClick(clickposition)

pyperclip.copy("도죠~~~~!")
pyautogui.hotkey("ctrl","v")

pyautogui.write(["enter"])
time.sleep(1.0)

pyautogui.write(["escape"])
time.sleep(1.0)

pyautogui.write(["enter"])
time.sleep(1.0)

pyautogui.write(["escape"])
time.sleep(1.0)


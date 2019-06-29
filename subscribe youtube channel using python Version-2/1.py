import pyautogui
import time

pyautogui.hotkey('win' , 'r')
pyautogui.typewrite('firefox')
pyautogui.hotkey('enter')
time.sleep(5)
pyautogui.click(x=358, y=57, clicks=1, button='left')
pyautogui.typewrite('https://www.youtube.com/user/PewDiePie')
pyautogui.hotkey('enter')
time.sleep(3)
pyautogui.leftClick(x=1155, y=365)
time.sleep(1)
pyautogui.leftClick(x=1155, y=365)

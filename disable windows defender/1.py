import pyautogui
import time


pyautogui.hotkey('win')
pyautogui.typewrite('windows defender')
pyautogui.hotkey('enter')
time.sleep(5)
pyautogui.click(x=458, y=283, clicks=2 , button='left')
time.sleep(2)
pyautogui.click(x=305, y=637, clicks=1 , button='left')
time.sleep(2)
pyautogui.click(x=288, y=388, clicks=1 , button='left')

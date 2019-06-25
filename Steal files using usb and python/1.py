from pynput.keyboard import Key, Controller
import time


keyboard = Controller()

keyboard.press(Key.cmd)
keyboard.press('r')
time.sleep(1)
keyboard.release(Key.cmd)
keyboard.release('r')
time.sleep(1)
keyboard.type('cmd')
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type('cd desktop')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type('1.bat')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

from pynput.keyboard import Key, Controller
import time



keyboard = Controller()

keyboard.press(Key.cmd)
keyboard.press('r')
time.sleep(1)
keyboard.release(Key.cmd)
keyboard.release('r')
time.sleep(1)
keyboard.type('firefox')
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(5)
keyboard.type('https://www.youtube.com/user/PewDiePie')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(6)
keyboard.press(Key.cmd)
keyboard.press('r')
time.sleep(1)
keyboard.release(Key.cmd)
keyboard.release('r')
time.sleep(1)
keyboard.type('cmd')
time.sleep(7)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type('cd desktop')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type('python mouse.py')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(10)




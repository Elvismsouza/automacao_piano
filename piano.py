import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(1027, 385, duration=1)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not keyboard.is_pressed('1'):
    if pyautogui.pixelMatchesColor(920, 236, (0, 0, 0)):
        click(920, 236)
    if pyautogui.pixelMatchesColor(992, 240, (0, 0, 0)):
        click(992, 240)
    if pyautogui.pixelMatchesColor(1067, 243, (0, 0, 0)):
        click(1067, 243)
    if pyautogui.pixelMatchesColor(1138, 240, (0, 0, 0)):
        click(1138, 240)

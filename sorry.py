## for obvious reasons don't run this if you don't want your inputs locked##
import time 
import ctypes 
import pyautogui 
ctypes.windll.user32.BlockInput(True) 
time.sleep(180) 
ctypes.windll.user32.BlockInput(False)
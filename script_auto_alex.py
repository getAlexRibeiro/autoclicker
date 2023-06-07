import pyautogui
import time
import keyboard
from random import random


isPressed = True
current_x, current_y = pyautogui.size()
target_x = current_x //2
target_y = (current_y //2) - 100
num_clicks = 10000
delay = random() + 5
time.sleep(5)

while isPressed == True:
	for i in range(num_clicks):
		pyautogui.click(target_x, target_y)
		time.sleep(delay)
		if keyboard.is_pressed('f'):
			isPressed = False

import pyautogui
import time
import keyboard
import random


x_box, y_box = 1791, 690
x_fill, y_fill = 1791, 723



isPressed = True
current_x, current_y = pyautogui.size()
target_x = current_x // 2
target_y = current_y // 2

num_clicks = 7

delay_click = random.randint(1,5)
delay_fill = random.randint(100,120)


for i in range(delay_fill):
	time.sleep(1)
	pyautogui.click(x_box, y_box, button='right')
	time.sleep(1)
	pyautogui.click(x_fill, y_fill)
	for j in range(num_clicks):
		time.sleep(1)
		pyautogui.click(target_x, target_y)
		time.sleep(delay_click)

	if keyboard.is_pressed('f'):
		break

import pyautogui
import time
import keyboard
import random


def minar():
    # Coordenadas para res 1920x1080
    x_box, y_box = 1791, 690

    stop = True
    current_x, current_y = pyautogui.size()
    target_x = current_x // 2
    target_y = current_y // 2

    # delay_click = random.randint(1, 20)ff
    # delay_fill = random.randint(1, 10)
    while stop:
        for j in range(random.randint(1, 10)):
            if keyboard.is_pressed('F'):
                stop = False
                break
            pyautogui.click(x_box, y_box)
            pyautogui.click(x_box, y_box)
        time.sleep(random.randint(1, 5))
        pyautogui.click(target_x, target_y)

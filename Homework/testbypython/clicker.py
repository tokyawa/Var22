import keyboard
import mouse
import time

isclick = False

def set_clicker():
    global isclick
    if isclick: 
        isclick = False
        print("кликер откл")
    else: 
        isclick = True
        print("кликер вкл")

keyboard.add_hotkey('Alt + w', set_clicker)

while True: 
    if isclick:
        mouse.double_click(button = 'left')
        time.sleep(0.1)
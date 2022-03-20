import keyboard
import pyautogui

keys = ['f1', 'f10', 'f11', 'f12', 'f2','f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']

#key = keyboard.read_key()

print("The Macro is Working :)")
print("Press "'f12'" to exit")

#F1 WILL BE BAG 1
#F2 WILL BE BAG 2
#F3 WILL BE BAG 3
def firstkey():
    pyautogui.moveTo(21,64)
    pyautogui.click(button='left')
    pyautogui.click(button='right')
    pyautogui.moveTo(638,479)

def secondkey():
    pyautogui.moveTo(21,119)
    pyautogui.click(button='left')
    pyautogui.click(button='right')
    pyautogui.moveTo(638,479)

def thirdkey():
    pyautogui.moveTo(21,175)
    pyautogui.click(button='left')
    pyautogui.click(button='right')
    pyautogui.moveTo(638,479)

#pyautogui.moveTo(21,119)
def play():
    while True:
        if (keyboard.read_key() == "f1"):
            firstkey()
        if (keyboard.read_key() == "f2"):
            secondkey()
        if (keyboard.read_key() == "f3"):
            thirdkey()
        if (keyboard.read_key() == 'f12'):
            return
            

play()
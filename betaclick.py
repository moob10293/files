import pyautogui,sys,random,turtle
from pynput import keyboard

pyautogui.FAILSAFE=True

click_speed=eval(input('how fast do you want your autoclicker to click? '))

if click_speed==0:
    click_speed=0.1

pyautogui.PAUSE=click_speed

click_times=eval(input('how many times do you want your autoclicker to click? '))

if click_times==0:
    click_times=10

'''

pyautogui.FAILSAFE=True

ht=eval(input('how long do you want the autoholder to press and hold?'))

if ht==0:
    ht=5
float(ht)

pyautogui.PAUSE=0.1

'''

def run():
    global click_times
    for x in range(click_times):
        pyautogui.click()

    '''
    global ht
    pyautogui.mouseDown()
    time.sleep(ht)
    pyautogui.mouseUp()
    
    '''

def click(k):
    print('debug')
    if k==keyboard.KeyCode(char=']'):
        run()
    if k == keyboard.Key.esc:
        sys.exit()
l=keyboard.Listener(on_press=click)
l.start()
input('')
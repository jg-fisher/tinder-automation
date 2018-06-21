import pyautogui
import time
import keyboard
import screenshot
import count_img

def position():
    pyautogui.displayMousePosition()

def py_click(x,y):
    pyautogui.click(x,y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    print('Clicked')

x = 244
y = 770

time.sleep(2)

interval = 0

while 1:
    try:
        if keyboard.is_pressed('q'):
            sys.exit()
        else:
            pass
    except:
        break

    if interval % 5 == 0 and interval is not 0:
        py_click(322, 78)
        time.sleep(2)

        #back to swiping
        #py_click(211, 81)

        y_message_delta = 240
        message = 'hey babe'
        while y_message_delta < 565:
            # click thread
            py_click(129, y_message_delta)
            time.sleep(2)
            # type message
            py_click(70, 778)
            time.sleep(1)
            py_click(70, 778)
            message = [l for l in message]
            for l in message:
                pyautogui.press(l)
                print('pressed {}'.format(l))
                time.sleep(.25)
            time.sleep(.5)
            # send
            py_click(412, 780)
            time.sleep(2)
            # go back
            py_click(14, 82)
            # pixel interval for messages
            y_message_delta += 25
            # 70, 778
        y_message_delta = 240

        

    screenshot.capture()
    py_click(x, y)
    time.sleep(.5)
    interval += 1
    print(interval)

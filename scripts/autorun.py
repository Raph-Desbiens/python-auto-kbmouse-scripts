import pyautogui, keyboard, time

end = False
autorun_enabled = False
flip_spacebar = True
press_time = time.time()
run_time = time.time()


while(not end):

    if keyboard.is_pressed('1'):
        autorun_enabled = True
        pyautogui.keyDown('shift')
        pyautogui.keyDown('w')
    elif keyboard.is_pressed('0'):
        autorun_enabled = False
        pyautogui.keyUp('shift')
        pyautogui.keyUp('w')
        pyautogui.keyUp('space')

    if autorun_enabled:
        if (time.time() - press_time) > 3:
            press_time = time.time()
            pyautogui.keyUp('space')
            pyautogui.keyDown('space')

        if (time.time() - run_time) > 60.0:
            run_time = time.time()
            pyautogui.press('f1')
            pyautogui.press('up')
            pyautogui.press('enter')
            pyautogui.press('f1')

    
    if keyboard.is_pressed('-'):
        end = True
        pyautogui.keyUp('shift')
        pyautogui.keyUp('w')
        pyautogui.keyUp('space')
    

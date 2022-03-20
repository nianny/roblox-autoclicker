import pyautogui as p
import time

time.sleep(2)

for i in range(20):
    #Reset Character
    p.press('esc')
    time.sleep(0.1)
    p.press('r')
    time.sleep(0.1)
    p.press('enter')
    time.sleep(0.1)
    time.sleep(10)


    #Move to cannon
    p.keyDown('w')
    time.sleep(0.75)
    p.keyUp('w')
    p.keyDown('d')
    time.sleep(8)
    # p.keyUp('d')
    time.sleep(0.01)


    # p.press('space')
    p.keyDown('space')
    time.sleep(0.1)
    p.keyUp('space')


    time.sleep(0.01)
    # p.keyDown('d')
    time.sleep(0.75)
    # p.keyUp('d')

    p.keyDown('space')
    time.sleep(0.1)
    p.keyUp('space')

    # p.keyDown('d')
    time.sleep(0.75)
    p.keyUp('d')


    #fire cannon
    p.press('e')
    time.sleep(0.67)
    p.press('space')
    time.sleep(0.01)
    p.press('space')
    p.keyDown('d')
    p.keyDown('s')
    time.sleep(10)
    p.keyUp('d')
    p.keyUp('s')

    #go to spin spot
    p.keyDown('w')
    p.keyDown('a')
    time.sleep(2)
    p.keyUp('w')
    p.keyUp('a')



    #place sprinklers
    time.sleep(0.5)
    p.keyDown('space')
    time.sleep(0.01)
    p.keyUp('space')
    time.sleep(0.3)
    p.press('1')

    p.keyDown('w')
    time.sleep(0.5)
    p.keyUp('w')

    time.sleep(0.5)
    p.keyDown('space')
    time.sleep(0.01)
    p.keyUp('space')
    time.sleep(0.3)
    p.press('1')

    p.keyDown('a')
    time.sleep(0.5)
    p.keyUp('a')

    time.sleep(0.5)
    p.keyDown('space')
    time.sleep(0.01)
    p.keyUp('space')
    time.sleep(0.3)
    p.press('1')

    p.keyDown('s')
    time.sleep(0.5)
    p.keyUp('s')

    time.sleep(0.5)
    p.keyDown('space')
    time.sleep(0.01)
    p.keyUp('space')
    time.sleep(0.3)
    p.press('1')

    p.mouseDown()
    p.keyDown('d')
    for i in range(300):
        time.sleep(0.3)
        p.keyDown('w')
        p.keyUp('d')

        
        time.sleep(0.3)
        p.keyDown('a')
        p.keyUp('w')

        
        time.sleep(0.3)
        p.keyDown('s')
        p.keyUp('a')

        
        time.sleep(0.3)
        p.keyDown('d')
        p.keyUp('s')
    p.keyUp('d')
    p.mouseUp()




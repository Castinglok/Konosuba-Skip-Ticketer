import pyautogui
import keyboard
import win32api, win32con
import time

#Sleep Timer
SleepTime = 0.8

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def lookForReplay():

    counter = 0

    #first click to minimize ide
    click(1810,14)
    while keyboard.is_pressed('q') == False:
        try:
            Next_POS = pyautogui.locateCenterOnScreen('pictures/next.png', confidence = 0.95)
            Replay_POS = pyautogui.locateCenterOnScreen('pictures/replay.png', confidence = 0.7)
            Confirm_POS = pyautogui.locateCenterOnScreen('pictures/ok.png', confidence = 0.95)
            rankup_POS = pyautogui.locateCenterOnScreen('pictures/rankup.png', confidence = 0.95)
            affinity_POS = pyautogui.locateCenterOnScreen('pictures/affinity.png', confidence = 0.95)

            if(Confirm_POS != None):
                click(Confirm_POS[0], Confirm_POS[1])
                time.sleep(SleepTime)
            if(Replay_POS != None):
                click(Replay_POS[0], Replay_POS[1])
                counter += 1
                time.sleep(SleepTime)
            if(Next_POS != None and Replay_POS == None):
                click(Next_POS[0], Next_POS[1])
                time.sleep(SleepTime)
            if(rankup_POS != None):
                click(rankup_POS[0], rankup_POS[1])
                time.sleep(SleepTime)
            if(affinity_POS != None):
                click(affinity_POS[0], affinity_POS[1])
                time.sleep(SleepTime)

        except:
            continue
    print("Replays: " + str(counter))

lookForReplay()
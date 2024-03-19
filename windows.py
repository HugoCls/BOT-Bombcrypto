import win32gui
import pygetwindow
from time import sleep
import modules.clavier_souris as cs
import pyautogui

def get_window_titles():
    ret = []
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            txt = win32gui.GetWindowText(hwnd)
            if txt:
                ret.append((hwnd,txt))

    win32gui.EnumWindows(winEnumHandler, None)
    fenetres=[]
    for i in range(len(ret)):
        fenetres.append(ret[i][1])
    return(fenetres)


def dimensions(fenetre):
    windows=pygetwindow.getWindowsWithTitle(fenetre)
    for win in windows:
        print(win.size)


def repositionner(fenetre,x,y):
    win = pygetwindow.getWindowsWithTitle(fenetre)[0]
    x,y=int(x),int(y)
    win.moveTo(x,y)


def redimensionner(windows,x,y):
    for win in windows:
        if win.size!=(x,y):
            win.resizeTo(x,y)


def desktop(state):
    with pyautogui.hold("win"):
        with pyautogui.hold("ctrl"):
            if state=="next":
                pyautogui.press("right")
            else:
                pyautogui.press("left")


def positionner_bombcrypto(windows):
    (sizes,positions)=([],[])
    redimensionner(windows,680,518)
    for i in range(len(windows)):
        #print(windows[i])
        win=windows[i]
        #print(win.topleft, win.size)
        x,y=-5+(i%3)*670,(i//3)*500
        if win.topleft!=(x,y):
            win.moveTo(x,y)
        sizes.append(win.size)
        positions.append(win.topleft)
    return(sizes,positions)


def rotate(windows,j):
    redimensionner(windows,1061,765)
    for i in range(len(windows)):
        #print(windows[i])
        win=windows[i]
        #print(win.topleft, win.size)
        x,y=-2400.,-47
        #x,y=1756,-47
        if j==1:
            if i==0:
                x,y=1494,-47
        else:
            if i==4:
                x,y=-5,-47
        if i==1:
            x,y=1074,-47
        elif i==2:
            x,y=-5,672
        elif i==3:
            x,y=1074,672
        win.moveTo(x,y)


def get_windows(title):
    windows=pygetwindow.getWindowsWithTitle(title)
    return(windows)


def premier_plan_bombcrypto():
    windows=get_windows('Bombcrypto - Google Chrome')
    first_plan(windows)


def first_plan(windows):
    (x,y)=cs.curseur()
    for window in windows:
        print(window.hwnd)
        window.activate()
        sleep(0.01)
    cs.move(x,y)


def mettre_arriere_plan(windows):
    for i in range(10):
        window=windows[i%2]
        (x,y)=window.size
        window.resizeTo(x,y)
        sleep(0.1)
        

def fenetre_premier_plan():
    window = win32gui.GetForegroundWindow()
    active_window_name = win32gui.GetWindowText(window)
    return(active_window_name)


def position(fenetre):
    windows=pygetwindow.getWindowsWithTitle(fenetre)
    for win in windows:
        print(win.topleft)

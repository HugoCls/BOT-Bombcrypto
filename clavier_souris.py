from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import ctypes
import keyboard as kb
import autopy
import win32gui
from PIL import ImageGrab
from time import sleep
import random as rd
import pyautogui
import time
import matchtemplate as templ
keyboard = KeyboardController()
mouse = MouseController()
pyautogui.FAILSAFE = False

# Alphabetic keys
A, Z, E, R, T, Y, U, I, O, P, Q, S, D, F, G, H, J, K, L, M, W, X, C, V, B, N = (
    0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19,
    0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27,
    0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31
)

# Special characters
ENTER, VIRGULE, POINT, DEUX_POINTS, EXCLAMATION, MAJ, CTRL, SPACE, TAB, ALT = (
    0x1C, 0x32, 0x33, 0x34, 0x35, 0x36, 0x1D, 0x39, 0x0F, 0x38
)

# Function keys
F5 = 0x3F

PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0,
                        ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def scroll(n):
    n=int(n)
    mouse.scroll(0, n)


def clic_droit():
    mouse.press(Button.right)
    mouse.release(Button.right)

def clic_gauche():
    mouse.press(Button.left)
    #sleep(rd.uniform(0.00000001,0.00001))
    mouse.release(Button.left)

def appuyer(lettre):
    PressKey(lettre)
    ReleaseKey(lettre)

def alt_tab():
    PressKey(ALT)
    PressKey(TAB)
    ReleaseKey(TAB)
    ReleaseKey(ALT)

def ctrl(lettre):
    with keyboard.pressed(Key.ctrl):
        appuyer(lettre)

def maj(lettre):
    with keyboard.pressed(Key.shift):
        appuyer(lettre)

def alt(lettre):
    with keyboard.pressed(Key.alt):
        appuyer(lettre)

def windows(lettre):
    PressKey(WINDOWS)
    appuyer(lettre)
    ReleaseKey(WINDOWS)

def ecrire(texte):
    for i in range(len(texte)):
        appuyer(texte[i])

def write(text):
    kb.write(text)

def move(x,y):
    x,y=int(x),int(y)
    pyautogui.moveTo(x,y)

def move_humanly(x,y,t):
    x,y=int(x),int(y)
    pyautogui.moveTo(x,y,t)

def curseur():
    return(pyautogui.position())

def pixel(x,y):
    x,y=int(x),int(y)
    return(win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x , y))

def pixelRGB(x,y):
    image = ImageGrab.grab()
    color = image.getpixel((x, y))
    return(color)

def balayage_x(xmin,xmax,y,nb_valeurs,couleur):
    couleur_trouvee=0
    epsilon=(xmax-xmin)/nb_valeurs
    x=xmin
    for k in range(nb_valeurs):
        move(x,y)
        if couleur_trouvee==0:
            if pixel(x,y)==couleur:
                move(x,y)
                clic_gauche()
                couleur_trouvee+=1
            else:
                x+=epsilon
    return(couleur_trouvee==1)

def balayage_y(x,ymin,ymax,nb_valeurs,couleur):
    couleur_trouvee=0
    epsilon=(ymax-ymin)/nb_valeurs
    y=ymin
    for k in range(nb_valeurs):
        move(x,y)
        if couleur_trouvee==0:
            if pixel(x,y)==couleur:
                move(x,y)
                clic_gauche()
                couleur_trouvee+=1
            else:
                y+=epsilon
    return(couleur_trouvee==1)

def get_balayage_y(x,ymin,ymax,nb_valeurs,couleur):
    epsilon=(ymax-ymin)/nb_valeurs
    y=ymin
    for k in range(nb_valeurs):
        if pixel(x,y)==couleur:
            return(int(y))
        y+=epsilon
    return(0)
def select(xa,ya,xb,yb):
    move(xa,ya)
    mouse.press(Button.left)
    autopy.mouse.smooth_move(xb,yb)
    mouse.release(Button.left)
"""
def random_move(x,y,t0):
    (x0,y0)=curseur()
    x,y=int(x),int(y)
    d=templ.distance(x0,y0,x,y)
    #print((x0,y0),(x,y))
    N=int(d/100)+1
    if (x,y)==(x0,y0):
        None
    else:
        j=8
        x_tot=0
        a=(y-y0)/(x-x0)
        b=y0-a*x0
        def f(x):
            return(round(a*x+b))
        if d>=500:
            move(x0+0.75*(x-x0),y0+0.75*(y-y0))
            random_move(x,y,t0)
            return(time.time()-t0)
        else:
            while abs(x_tot)<abs(x-x0):
                x_tot+=(x-x0)/N
                move_humanly(x0+x_tot+rd.uniform(-10,10),f(x0+x_tot)+rd.uniform(-10,10),rd.uniform(0.1,0.2))
            move_humanly(x+rd.uniform(-3,3),y+rd.uniform(-3,3),rd.uniform(0.1,0.2))
            return(time.time()-t0)
"""
def random_sleep(t):
    deltat=rd.uniform(0,0.1)
    (x,y)=curseur()
    tps=time.time()
    j=2
    while time.time()-tps<t+deltat:
        deltax,deltay=rd.randint(-5,5),rd.randint(-5,5)
        tho=(t+deltat)/rd.randint(min(j,4),6)
        move_humanly(x+deltax,y+deltay,tho)
        j+=1
    #print(time.time()-tps)
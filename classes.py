import random as rd
import clavier_souris as cs
import colors
import time
import pyautogui
from time import sleep


class Hero():
    def __init__(self):
        self.work_state=False
        self.rest_state=False
        self.home_state=False
        self.hp_percentage=0
        self.work_topleft=(100,150)

    def infos(self):
        return(str(self.work_state)+' | '+str(self.rest_state)+' | '+str(self.home_state)+' | '+str(self.hp_percentage))

    def set_work(self,state):
        self.work_state=state
        #print('New work_state is:'+str(state))

    def set_rest(self,state):
        self.rest_state=state
        #print('New rest_state is:'+str(state))

    def set_home(self,state):
        self.home_state=state
        #print('New house_state is:'+str(state))

    def set_hp_percentage(self,percentage):
        self.hp_percentage=percentage
        #print('New hp_percentage is:'+str(percentage))

    def send_to_work(self,trueorfalse):
        if trueorfalse:
            w,h=69,44
            (x,y)=self.work_topleft
            dx=rd.randint(10,w-10)
            dy=rd.randint(10,h-10)
            cs.move(x+dx,y+dy)
            cs.clic_gauche()
            """
            t=time.time()
            while cs.pixelRGB(x+dx,y+dy)==(237, 215, 186) or time.time()-t>=2:
                cs.random_sleep(0.05)
            """
        self.set_work(trueorfalse)

    def send_to_rest(self,trueorfalse):
        if trueorfalse:
            w,h=69,44
            (x,y)=self.work_topleft
            x+=75
            dx=rd.randint(10,w-10)
            dy=rd.randint(10,h-10)
            cs.move(x+dx,y+dy)
            cs.clic_gauche()
        self.set_rest(trueorfalse)

    def send_to_home(self,trueorfalse):
        if trueorfalse:
            w,h=69,44
            (x,y)=self.work_topleft
            x+=150
            if not colors.gray(x+w/2,y+4*(h/5)):
                dx=rd.randint(2,w-2)
                dy=rd.randint(2,h-2)
                cs.move(x+dx,y+dy)
                cs.clic_gauche()
                self.set_home(trueorfalse)
            else:
                self.send_to_rest(True)
                self.set_home(False)


class Browser():
    def __init__(self,win,t_heroes,init_topleft,init_size,i):
        self.win=win
        self.t_heroes=t_heroes
        self.init_size=init_size
        self.init_topleft=init_topleft
        self.i=i
        self.t_F5=time.time()+1800

    def infos(self):
        return(str(self.win)+' | '+str(self.t_heroes))

    def get_win(self):
       return(self.win)

    def get_t_heroes(self):
        return(self.t_heroes)

    def change_t_heroes(self,t):
        self.t_heroes=t

    def maximize(self):
        #print('OK')
        self.win.moveTo(2087,0)
        #print('Moved')
        self.win.resizeTo(1920,1080)
        #print('Resized')
        pyautogui.moveTo(2800,800)
        pyautogui.click(button='left')
        #print('Clicked center')
        sleep(0.1)
        for i in range(4):
            cs.ctrl(cs.PLUS)
            sleep(0.05)
        #print('Maximized')
        sleep(0.1)

    def minimize(self):
        (x,y)=self.init_topleft
        (w,h)=self.init_size
        self.win.moveTo(x,y)
        #print('Moved')
        self.win.resizeTo(w,h)
        #print('Resized')
        pyautogui.moveTo(int(x+w/2),int(y+h/2))
        pyautogui.click(button='left')
        #print('Clicked center')
        sleep(0.1)
        for i in range(4):
            cs.ctrl(cs.MINUS)
            sleep(0.05)
        #print('Minimized')
        sleep(0.1)

    def center(self):
        (x,y)=self.init_topleft
        (w,h)=(36,114)
        cs.move(x+w,y+h)
        cs.clic_gauche()
        sleep(0.1)
        for i in range(3):
            pyautogui.press('right')
        pyautogui.press('down')
import clavier_souris as cs
import detects as dt
import time
import errors
from time import sleep


def auto_refresh():
    while dt.find('new map'):
        cs.sleep(0.5)
    for k in range(4):
        if dt.find('arrow'):
            cs.sleep(0.5)
    while dt.find('treasure hunt'):
        cs.sleep(0.5)


def F5_all(N):
    for i in range(N):
        dt.find_the_one('chrome_refresh',i)
        cs.sleep(0.5)


def connect():
    tconnexion=time.time()
    if dt.find('ok'):
        errors.ADD(2)
        cs.sleep(0.5)
    while dt.check('bombcrypto connexion')==True and dt.check('connect')==False:
        if time.time()-tconnexion>=40:
            print('Connect | Expired')
            cs.ctrl(cs.F5)
    while dt.check('bombcrypto mainscreen') or dt.check('busy_fox') or dt.check('sign') or dt.check('fox_connect'):
        if dt.check('busy_fox')==True and dt.check('sign')==False and dt.check('fox_connect')==False:
            dt.find('busy_fox')
            cs.sleep(1.5)
        t0=time.time()
        if dt.find('connect') or dt.find('fox_connect'):
            cs.sleep(0.2)
            if dt.find('fox_connect'):
                errors.ADD(2)
                t=time.time()
                while dt.check('sign')==False and time.time()-t<=5:
                    cs.sleep(0.2)
        dt.find('sign')
        dt.find('fox_connect')
        print('Connect | '+str(int(time.time()-t0))+'s')
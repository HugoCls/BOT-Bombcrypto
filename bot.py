import time
import detects as dt
import refresh as fresh
import heroes as h
import historic
import errors
import clavier_souris as cs
import windows as wd
import classes as C
from time import sleep
import zzz
import time
import historic

def infinite_loop():
    t_historic=time.time()-300
    browsers=[]
    windows=wd.pygetwindow.getWindowsWithTitle('Bombcrypto - Google')
    N=len(windows)
    (sizes,positions)=wd.positionner_bombcrypto(windows)
    for i in range(N):
        size=sizes[i]
        topleft=positions[i]
        browsers.append(C.Browser(windows[i],time.time(),topleft,size,i))

    trefresh=time.time()
    #ERROR THINGS
    errors.RESET()
    t_errors=time.time()
    last_count=int(errors.COUNT())
    #COUNTS
    map_count=0
    loop_count=0
    while True:
        loop_count+=1
        dt.find('actualiser')
        if dt.find('new map'):
            map_count+=1
            #historic.printt("Map | "+str(map_count))
        if dt.find('close'):
            cs.sleep(0.5)
        while dt.find('treasure hunt'):
            cs.sleep(0.5)

        fresh.connect()

        if time.time()-trefresh>=3*60:
            dt.find_all('arrow')
            sleep(0.1)
            dt.find_all('treasure hunt')
            trefresh=time.time()

        for i in range(N):
           br=browsers[i]
           if zzz.count(br)>=4:
               br.maximize()
               loop()
               br.minimize()
               wd.positionner_bombcrypto(windows)
               sleep(0.2)
               br.center()
               br.t_heroes=time.time()
               cs.sleep(0.5)
               break

        if time.time()-t_historic>=300:
            historic.screen()
            t_historic=time.time()

        err_count=int(errors.COUNT())
        if err_count!=last_count:
            last_count=err_count
            if err_count>=6:
                historic.printt('Errors | Critical | '+str(err_count))

        if err_count>=30:
            historic.printt("BOT STOPPED <@397738036592508931> BOT STOPPED")
            break

        if time.time()-t_errors>=500:
            historic.printt("Errors | 500s | "+errors.COUNT())
            errors.RESET()
            t_errors=time.time()
            cs.sleep(0.5)

def loop():
    j=0
    while dt.find('new map 100%'):
        cs.sleep(0.5)
    if dt.find('arrow 100%'):
        cs.sleep(0.5)
    if dt.find('heroes 100%'):
        cs.sleep(0.5)
    t_upgrade=time.time()
    while dt.check('upgrade 100%')==False and time.time()-t_upgrade<=20:
        cs.sleep(0.1)
        if dt.check('new map 100%'):
            j=1
            break
    if j==1:
        return(None)
    h.heroes_entirely()

    if dt.find('treasure hunt 100%'):
        cs.sleep(0.5)
    if dt.find('treasure hunt 100%'):
        cs.sleep(0.5)
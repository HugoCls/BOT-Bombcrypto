import datetime
import os
from PIL import ImageGrab
historic_path=os.getcwd()+'\data\Discord_BOT\historic.txt'

def printt(text):
    fichier=open(historic_path,'a')
    now = datetime.datetime.now()
    mins=str(now.minute)
    if len(mins)==1:
        mins='0'+mins
    hour=str(now.hour)+':'+mins
    fichier.write(hour+' | '+text)
    print(hour+' | '+text)
    fichier.close()

def screen():
    box = (0,0,2022,1040)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\Discord BOT\\screenshot.png', 'PNG')

def error():
    fichier=open(historic_path,'r')
    txt=fichier.read()
    fichier.close()
    if len(txt)==0:
        return(False)
    else:
        L = list(txt)
        N=L.count('$')
        if N>=10:
            l=len(L)-1
            piv=len(L)-1
            m=0
            while m<=10:
                if L[piv]=='$':
                    m+=1
                piv-=1
            L_cut=L[piv+1:l]
            txt_cut=''.join(str(e) for e in L_cut)
            return(txt_cut.count('Connect')>=5)

        else:
            return(False)
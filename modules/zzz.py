import modules.ocr as ocr
import modules.matchtemplate as templ
import cv2
import os

zzz_zzz = cv2.imread(os.getcwd()+'\\data\\images\\zzz zzz 67%.png',0)
zzz_zz = cv2.imread(os.getcwd()+'\\data\\images\\zzz zz 67%.png',0)
zzz_z = cv2.imread(os.getcwd()+'\\data\\images\\zzz z 67%.png',0)

def count(br):
    (x,y)=br.init_topleft
    (w,h)=br.init_size
    #(x,y,x+w,x+h)
    L=[]
    for i in range(5):
        img_gray=templ.screen_img()
        #box=img_gray[y:y+h, x:x+w]
        Lzzz,wz,hz=templ.matchtemplate_fast_cibled(img_gray,zzz_zzz,0.8)
        Lzz,wz,hz=templ.matchtemplate_fast_cibled(img_gray,zzz_zz,0.8)
        Lz,wz,hz=templ.matchtemplate_fast_cibled(img_gray,zzz_z,0.8)

        for i in range(len(Lzzz)):
            (xz,yz)=Lzzz[i]
            if x<=xz<=x+w and y<=yz<=y+h:
                L.append(Lzzz[i])
        for i in range(len(Lzz)):
            (xz,yz)=Lzz[i]
            if x<=xz<=x+w and y<=yz<=y+h:
                L.append(Lzz[i])
        for i in range(len(Lz)):
            (xz,yz)=Lz[i]
            if x<=xz<=x+w and y<=yz<=y+h:
                L.append(Lz[i])
        #print(Lzzz,Lzz,Lz,'\n',L,'\n')
        
    L=templ.points_in_couple_list(L)
    print('ZZZ | Screen ',br.i,' | ',len(L))
    return(len(L))
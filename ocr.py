from PIL import Image,ImageGrab
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import pyautogui
import cv2
import numpy as np

def screen(name):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(name, image)


def ocr_text(im_path):
    img = Image.open(im_path)
    text = pytesseract.image_to_string(img, lang = 'fra',config=' --oem 3 -c tessedit_char_whitelist=0123456789')
    return(text)


def ocr_PIL(img):
    text = pytesseract.image_to_string(img, lang = 'fra')
    return(text)


def ocr_box(x1,y1,x2,y2,eta):
    screenGrab(x1, y1, x2, y2)
    if eta!=None:
        img=cv2.imread(os.getcwd() + '\\screenshot.png')
        if eta=='bw':
            img=bw_img(img)
        if eta=='invert':
            img=invert_img(img)
        if eta=='grayscale':
            img=grayscale_img(img)
        if eta=='gray':
            img=gray_img(img)
        cv2.imwrite(os.getcwd() + '\\screenshot.png',img)
    text=ocr_text(os.getcwd() + '\\screenshot.png')
    return(text)


def show_box(x1,y1,x2,y2,eta):
    screenGrab(x1,y1,x2,y2)

    img=cv2.imread(os.getcwd() + '\\screenshot.png')
    if eta=='bw':
        img=bw_img(img)
    if eta=='invert':
        img=invert_img(img)
    if eta=='grayscale':
        img=grayscale_img(img)
    if eta=='gray':
        img=gray_img(img)
    cv2.imshow("lol",img)
    cv2.waitKey(0)


def screenGrab(x1,y1,x2,y2):
    box = (x1,y1,x2,y2)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\data\\images\\screenshot.png', 'PNG')


"""Couleur négative"""
def invert(im_path):
    img=cv2.imread(im_path)
    inverted_image=cv2.bitwise_not(img)
    return inverted_image


def invert_img(img):
    inverted_image=cv2.bitwise_not(img)
    return inverted_image


"""Nuances de gris"""
def grayscale(im_path):
    img=cv2.imread(im_path)
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


def grayscale_img(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


def gray(im_path):
    img=cv2.imread(im_path)
    gray_image=grayscale(img)
    return gray_image


def gray_img(img):
    gray_image=grayscale_img(img)
    return gray_image


"""Noir et Blanc"""
def bw(im_path):
    img=gray(im_path)
    tresh,im_bw = cv2.threshold(img,200,230,cv2.THRESH_BINARY)
    return im_bw


def bw_img(img):
    img=gray_img(img)
    tresh,im_bw = cv2.threshold(img,200,230,cv2.THRESH_BINARY)
    return im_bw


"""Suppression du bruit"""
def noise_removal(img):
    kernel=np.ones((1,1),np.uint8)
    image=cv2.dilate(img,kernel,iterations=1)
    kernel=np.ones((1,1),np.uint8)
    image=cv2.erode(img,kernel,iterations=1)
    image=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
    image=cv2.medianBlur(img,3)
    return img
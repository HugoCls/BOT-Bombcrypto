# Bombcrypto BOT Project

# Table of Contents
1. [Project Introduction](#project-introduction)
2. [Technical Overview](#technical-overview)
    - [Maximizing Gameplay](#maximizing-gameplay)
        - [The Optimized Loop](#the-optimized-loop)
        - [Browser Management](#browser-management)
    - [Automating Gameplay](#automating-gameplay)
        - [Computer Vision & Automated Input Generation](#computer-vision-&-automated-input-generation)
        - [Captchas & Server Crash Handling](#captchas-&-server-crash-handling)
        - [Supervision and Monitoring](#supervision-and-monitoring)

# Project Introduction

**Bombcrypto** is a game following the **"Play-to-Earn"** model, featuring a group of bomb heroes in search of the BCOIN. The game operates on the **Binance blockchain**, with the **BCOIN token** serving as the primary in-game currency on the **BNB Chain**. The project aimed to **maximize BCOIN generation** by **automating all game tasks**, implementing optimized rules, and more.

> [!NOTE]
> On November 29, 2021, BCOIN reached its peak value of $8.2 before plummeting significantly.

# Technical Overview

> [!IMPORTANT]
> This project was developed during my early coding journey (Nov 2020 - Jan 2021), and therefore, the syntax, variable naming conventions, etc., reflect that learning stage.

## Maximizing Gameplay

### The optimized loop

Basically, in Bombcrypto you have heroes who work alone in this zone made up of chests and obstacles. 

<p align="center">
    <img src="https://i.ytimg.com/vi/bw097WMyiUo/maxresdefault.jpg" alt="Bombcrypto map" style="width:50%;">
</p>

Your heroes move around the map by dropping bombs that explode the chests, and when there are no more chests a pop-up appears and you have to click on it to get them working again in a new map.

<p align="center">
    <img src="https://i.ytimg.com/vi/Slw3Pm9Ayek/maxresdefault.jpg" alt="Houses" style="width:40%;">
</p>

When your heroes are tired, they need to sleep, and you can either let them rest peacefully (you can see it with zzz on top of their heads), or place them in a house to get a quick rest. (houses also cost BCOIN, at that time their price was between 1,2k-$250k)

<p align="center">
    <img src="https://www.altcoinbuzz.io/wp-content/uploads/2022/06/1-29-1024x565.png" alt="Houses" style="width:40%;">
</p>

Therefore are two parameters to optimise:
- Always have 15 heroes working while the others rest in houses
- Launch new Maps as soon as they've finished

Whenever you're not on the map screen, the heroes aren't working, so every interaction in the script has to be as quick as possible, otherwise you lose money.

### Browser Management

With **investment in multiple accounts** being **the most cost-effective**, effective management of multiple browser instances was essential to maximise playability.

Each browser was checked independently to ensure optimum performance and avoid computer vision errors.

This included:
- Connection to Metamask and independent management of the chrome extension on different browsers
- Layout of multiple google chrome browsers on a single screen
- Management of relative coordinates to link a state to an action for the right browser

The game loop was then performed one by one for each browser.

<p align="center">
    <img src="https://raw.githubusercontent.com/hugocls/BOT-Bombcrypto/main/data/images/readme/browser_management.png" alt="Description de l'image" style="width:100%;">
</p>

> [!NOTE]
> If I had to do it again today, I'd use multithreading/multiprocessing and better management of the different game instances.

## Automating Gameplay

### Computer Vision & Automated Input Generation

The project utilized computer vision for automatic generation of keyboard and mouse inputs.

For keyboard input I used ```autopy```, ```pywinauto```, ```pyautogui```...

For image recognition, I used ```matchTemplate``` function from ```OpenCV```, which recognises an image template in a larger image.

Technically, it calculates the correlation between a template and regions of an image to find occurrences of the template.

<p align="center">
    <img src="https://raw.githubusercontent.com/hugocls/BOT-Bombcrypto/main/data/images/readme/matchtemplate_.png" alt="Description de l'image" style="width:100%;">
</p>

All other computer vision functions have been created by hand using colour, image processing and other means using ```matchTemplate``` or equivalents.

You can see my whole library of templates at the following path: ```tree/main/data/images```.

### Captchas & Server Crash Handling

There were often server problems, which forced us to create systems to detect server crashes, without which our bot could remain blocked for hours, refreshing the page.

In addition, anti-bot captcha systems were put in place, which we easily bypassed using hand-created functions. 

<p float="left">
    <img src="https://raw.githubusercontent.com/HugoCls/Captcha-Solving/main/Bombcrypto-Puzzle/images/README_IMAGES/captcha_not_done.png" alt="Captcha 1" style="width: 40%;">
    <img src="https://raw.githubusercontent.com/HugoCls/Captcha-Solving/main/Bombcrypto-Numbers-Revealed/images/README_IMAGES/captcha_img.png" alt="Captcha 2" style="width: 39%;">
</p>

I refer you to my repository dedicated solely to this at this address: [Captcha-Solving](https://github.com/HugoCls/Captcha-Solving)

<p align="left">
	<img src="https://github.com/HugoCls/BOT-Bombcrypto/blob/main/data/images/readme/captcha.gif?raw=true" alt="Captcha" style="width: 100%;">
</p>	

### Supervision and Monitoring

Supervision and monitoring mechanisms were developed to maintain oversight of the automation system. 
This included sending periodic screenshots, logging detailed action records locally, and providing important information logs on Discord for real-time monitoring.

<table>
  <tr>
    <th>Running logs</th>
    <th>Working efficiency</th>
    <th>Visual feedback</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/HugoCls/BOT-Bombcrypto/blob/main/data/images/readme/logs (5).png" alt="Logs" style="width: 100%;">
    </td>
    <td>
      <img src="https://github.com/HugoCls/BOT-Bombcrypto/blob/main/data/images/readme/logs (2).png" alt="Logs" style="width: 100%;">
    </td>
    <td>
      <img src="https://github.com/HugoCls/BOT-Bombcrypto/blob/main/data/images/readme/logs (1).png" alt="Logs" style="width: 100%;">
    </td>
  </tr>
  <tr>
</table>

---

This README provides an overview of the Bombcrypto Automation Project, focusing on its technical aspects and methodologies utilized for efficient gameplay automation. Further details and enhancements may be added as the project evolves.

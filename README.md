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

<div style="text-align: center;">
    <img src="https://i.ytimg.com/vi/bw097WMyiUo/maxresdefault.jpg" alt="Bombcrypto map" style="width:50%;">
</div>

Your heroes move around the map by dropping bombs that explode the chests, and when there are no more chests a pop-up appears and you have to click on it to get them working again in a new map.

<div style="text-align: center;">
    <img src="https://i.ytimg.com/vi/Slw3Pm9Ayek/maxresdefault.jpg" alt="Houses" style="width:40%;">
</div>

When your heroes are tired, they need to sleep, and you can either let them rest peacefully (you can see it with zzz on top of their heads), or place them in a house to get a quick rest. (houses also cost BCOIN, at that time their price was between 1,2k-$250k)

<div style="text-align: center;">
    <img src="https://www.altcoinbuzz.io/wp-content/uploads/2022/06/1-29-1024x565.png" alt="Houses" style="width:40%;">
</div>

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

<div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/hugocls/BOT-Bombcrypto/main/data/images/readme/browser_management.png" alt="Description de l'image" style="width:50%;">
</div>

> [!NOTE]
> If I had to do it again today, I'd use multithreading and better management of the different game instances.


## Automating Gameplay

### Computer Vision & Automated Input Generation

The project utilized computer vision for automatic generation of keyboard and mouse inputs, browser management, Metamask connections, server crash handling, and most importantly, the creation and management of optimal game loops for each browser.

Automated input generation played a crucial role in executing game actions efficiently. This included simulating keyboard and mouse inputs to interact with the game interface seamlessly.



Integration with Metamask facilitated seamless transactions within the game environment, allowing for the smooth transfer of BCOIN tokens and other in-game assets.

### Captchas & Server Crash Handling

Robust mechanisms were implemented to handle server crashes gracefully, ensuring minimal disruption to gameplay and maximizing uptime of the automation system.

### Supervision and Monitoring

Supervision and monitoring mechanisms were developed to maintain oversight of the automation system. This included sending periodic screenshots, logging detailed action records locally, and providing important information logs on Discord for real-time monitoring.

---

This README provides an overview of the Bombcrypto Automation Project, focusing on its technical aspects and methodologies utilized for efficient gameplay automation. Further details and enhancements may be added as the project evolves.

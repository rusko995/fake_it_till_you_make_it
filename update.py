# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:03:26 2020

@author: Asus
"""
#
import pyautogui 
from pynput.keyboard import Key, Controller
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
keyboard = Controller()


def windows_update():
    driver.get('https://fakeupdate.net/win8/')
    pyautogui.moveTo(930, 110, duration = 1) 
    pyautogui.click(930, 110) 
    keyboard.press(Key.f11)
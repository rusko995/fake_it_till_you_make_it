# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:03:26 2020

@author: Asus
"""
#
import pyautogui
import pynput
from pynput.keyboard import Key, Controller
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def windows_update():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    keyboard = Controller()
    driver.get('https://fakeupdate.net/win8/')
    pyautogui.moveTo(1280, 150, duration=1)
    pyautogui.click(1280, 150)
    keyboard.press(Key.f11)

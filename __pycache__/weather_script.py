# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 08:32:48 2022

Copyright 2022 - 2023 The MathWorks, Inc.

"""
# weather_script.py

def display_info(location):
    print("Displaying temperature for: "+ location)
    return location

def get_temp():
    import random
    x = random.random()*50
    x = round(x,2)
    print("The temperature is "+str(x))  
    return x

# Exercise: Update the location
w = display_info("Boston")
t = get_temp()


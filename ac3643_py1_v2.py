#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:55:42 2019

@author: sofiacalatrava


Comment added on Thu Sep 9th
"""

import random 

count = 0 

x = random.randint(1,10)

while count < 5:
    
    player = input("Please select and type a number from 1 to 10 (inclusive): ")
    
    player = int(player)
    
    diff = abs(x - player)
    
    count += 1
    
    if diff > 5 and player != x and\
    count < 5 : 
        print("not even close.")
        
    if (diff >= 3) and\
    (diff <= 5) and player != x and\
    count < 5:
        print("close.")
            
    if diff < 3 and player != x and\
    count < 5:
        print("almost there.")
        
    if player != x and count < 5: 
        print("Try Again.")
    
    if count == 5 and player != x:
        print("Out of tries. The game is lost.")
    
    if player == x:
        print("Player Guessed Correctly.")
        count = 5
        

print("Game Over.")
        
    
        
    


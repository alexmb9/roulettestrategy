#putting on red, doubling strategy
#10 seconds per spin

#importing library for rng
#importing graphing library

import numpy as np
import matplotlib.pyplot as plt
import random

from matplotlib.ticker import NullFormatter  # useful for `logit` scale

won_total = 0
loss_total = 0
doubler = 0.01
spin_result = 0
game_stack = 100000
overall_stack = 1000000

for x in range(100000):
    game_stack = 100000 
    if overall_stack - game_stack < 0:
        print("rip")
        break
    
    overall_stack = overall_stack - game_stack
    for x in range(50):
        spin_result=random.randint(0,36)

        if game_stack - doubler <= 0:
            doubler = 0.01
            break

        elif spin_result%2==1:
            game_stack = game_stack + doubler 
            won_total = won_total + 1
            doubler = 0.01

        else:
            loss_total = loss_total + 1
            game_stack = game_stack - doubler
            doubler = doubler*2

    #print("Game result", game_stack)
    overall_stack = overall_stack + game_stack
print(overall_stack)
        
        
        
    




# -*- coding: utf-8 -*-

import hydraulic
import Thermal_Functions as thermal
#import matplotlib.pyplot as plt
#import geometric as geom
#import draw as draw
#import numpy as np
#import optimise 

L = 180e-3
N_baffle = 7
pitch_type = "square"
Y = 13e-3
bundle_array = [4,4,4,4]
N_shell = 1
N_pass = 2
L_header = 0.025
breadth_gap = 0.01
B_end = 27.25e-3

geometry = {'L': L,'N_baffle': N_baffle,'pitch_type': pitch_type,'Y': Y,'bundle_array': bundle_array, 'N_shell': N_shell, 'N_pass': N_pass, 'L_header': L_header, 'breadth_gap': breadth_gap, 'B_end':B_end}

print(thermal.Q(geometry,2018))










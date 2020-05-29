# -*- coding: utf-8 -*-

import hydraulic
import Thermal_Functions as thermal
#import configure
from designs import *
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


year = "2020"

for i in designs_2020:
    K1 = 5.21461099 
    K2 = 4.4899305 
    K3 = 1.29030439
    C1 = 1.18
    C2 = 0.87
    C3 = 1.19
    Q = thermal.Q(designs_2020.get(i),year,K_baffle_bend=K3,K_nozzle=K1,K_turn=K2,Calibration1=C1,Calibration2=C2,Calibration3=C3)
    E = thermal.E(designs_2020.get(i),year,K_baffle_bend=K3,K_nozzle=K1,K_turn=K2,Calibration1=C1,Calibration2=C2,Calibration3=C3)
    print("{}: Q={}W, E={}%".format(i,int(round(Q,0)),int(round(E*100,0))))
    print("Max: {}W, Min: {}W".format(Q*1.17,Q*0.83))
    hydraulic.hydraulic_plot_c(designs_2020.get(i),year,K_baffle_bend=K3,K_nozzle=K1)











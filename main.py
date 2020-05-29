# -*- coding: utf-8 -*-

import hydraulic
import Thermal_Functions as thermal
#import configure
from designs import *
import matplotlib.pyplot as plt
import geometric as geom
#import draw as draw
#import numpy as np
#import optimise 

#L = 180e-3
#N_baffle = 7
#pitch_type = "square"
#Y = 13e-3
#bundle_array = [4,4,4,4]
#N_shell = 1
#N_pass = 2
#L_header = 0.025
#breadth_gap = 0.01
#B_end = 27.25e-3
#
#geometry = {'L': L,'N_baffle': N_baffle,'pitch_type': pitch_type,'Y': Y,'bundle_array': bundle_array, 'N_shell': N_shell, 'N_pass': N_pass, 'L_header': L_header, 'breadth_gap': breadth_gap, 'B_end':B_end}



#K1 = 5.30261345
#K2 = 4.52516239
#K3 = 1.38894101
#C1 = 1.36
#C2 = 0.87
#C3 = 1.17
#print("{} kg".format(geom.f_mass_total(BTC,display=False)))
#print("{} W".format(thermal.Q(BTC,2020,K_turn=K1, K_nozzle=K2, K_baffle_bend=K3, Calibration1=C1,Calibration2=C2, Calibration3=C3)))
#print("{} kg/s cold".format(hydraulic.iterate_c(BTC,2020, K_nozzle=K2, K_baffle_bend=K3)))
#print("{} kg/s hot".format(hydraulic.iterate_h(BTC,2020,K_turn=K1, K_nozzle=K2)))

As = []; Qs = []

for j in Designs:
    for i in Designs.get(j):
        K1 = 4.609375
        K2 = 3.9421875
        K3 = 1.346875
        C1 = 1.082
        C2 = 0.86
        C3 = 1.21
        As.append(hydraulic.give_A_sh(Designs.get(j).get(i)))
        Qs.append(thermal.Q(Designs.get(j).get(i), j, K_turn=K1, K_nozzle=K2, K_baffle_bend=K3, Calibration1=C1,Calibration2=C2, Calibration3=C3))
        
plt.scatter(As,Qs)
plt.xlim(xmin=0,xmax=0.0012)
plt.grid()
plt.xlabel("$A_{sh}$ ($m^2$)")
plt.ylabel("Heat Rate (W)")
plt.show()













# Nelder-Meald . K_turn: 3.9421875  K_nozzle: 4.609375 .. K_baffle_bend: 1.346875 ... Calibration1: 4.72854947 . Calibration2: 0.59867577 . Calibration3: 0.86864792
# Powell ....... K_turn: 5.21461099 K_nozzle: 4.4899305 . K_baffle_bend: 1.29030439 . Calibration1: 2.28059139 . Calibration2: 6.18911879 . Calibration3: 0.99914682

#year = "2020"
#
#for i in designs_2020:
#    K1 = 4.609375
#    K2 = 3.9421875
#    K3 = 1.346875
#    C1 = 1.082
#    C2 = 0.86
#    C3 = 1.21
#    Q = thermal.Q(designs_2020.get(i), year, K_turn=K1, K_nozzle=K2, K_baffle_bend=K3, Calibration1=C1,Calibration2=C2, Calibration3=C3)
#    E = thermal.E(designs_2020.get(i), year, K_turn=K1, K_nozzle=K2, K_baffle_bend=K3, Calibration1=C1,Calibration2=C2, Calibration3=C3)
#    print("{}: Q={}W, E={}%".format(i,int(round(Q,0)),int(round(E*100,0))))
#    print("Max: {}W, Min: {}W".format(Q*1.17,Q*0.83))
#    hydraulic.hydraulic_plot_c(designs_2020.get(i),year,K_baffle_bend=K3,K_nozzle=K1)











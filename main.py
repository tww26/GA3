# -*- coding: utf-8 -*-

import hydraulic
import Thermal_Functions as thermal
import configure
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


year = "2017"
#print(configure.K_config(geometry,2020))
geometry = Designs.get('designs_2017').get('A')
m_dot_c = hydraulic.iterate_c(geometry, year)
m_dot_h = hydraulic.iterate_h(geometry, year)
Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)

print(Re_sh)
print(Re_tube)

#print(thermal.iterate_thermal(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry))

#hydraulic.hydraulic_plot_c(geometry,2017)










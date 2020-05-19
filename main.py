# -*- coding: utf-8 -*-

import hydraulic
import Thermal_Functions as thermal
import matplotlib.pyplot as plt
import geometric as geom
import draw as draw
import numpy as np
import optimise 

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

B_ends = np.linspace(20e-3,30e-3,51)
Qs = []
Qs_constant = []

# What Q was originally planned to be
geometry['B_end'] =geometry.get('L')/(geometry.get('N_baffle')+1)
m_dot_c = hydraulic.iterate_c(geometry)
m_dot_h = hydraulic.iterate_h(geometry)
Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)
Q0 = thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry)

for i in B_ends:
    # Set B_end
    geometry['B_end']=i
    # Calculate values
    m_dot_c = hydraulic.iterate_c(geometry)
    m_dot_h = hydraulic.iterate_h(geometry)
    Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
    Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)
    # Calculate Q
    Q = thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry)
    # Append to list
    Qs.append(Q)
    Qs_constant.append(Q0)
    
plt.plot(B_ends, Qs)
plt.plot(B_ends, Qs_constant, linestyle="--")
plt.ylabel('Heat Transfer (W)')
plt.xlabel('End Baffle Spacing (m)')
plt.title('Effect of variation of end baffle spacing on heat transfer of Group B chosen design')
plt.grid()
plt.show()








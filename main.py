# -*- coding: utf-8 -*-

import hydraulic
import Thermal_Functions as thermal
import matplotlib.pyplot as plt
import geometric as geom
import draw as draw
import numpy as np

L = 180e-3
N_baffle = 7
pitch_type = "square"
Y = 13e-3
bundle_array = [4,4,4,4]
N_shell = 1
N_pass = 2
L_header = 0.025
breadth_gap = 0.01

geometry = {'L': L,'N_baffle': N_baffle,'pitch_type': pitch_type,'Y': Y,'bundle_array': bundle_array, 'N_shell': N_shell, 'N_pass': N_pass, 'L_header': L_header, 'breadth_gap': breadth_gap}


#draw.cross_section(geometry)
#"""PLAYING WITH DESIGN VARIABLES"""
#
m_dot_c = hydraulic.iterate_c(geometry)
m_dot_h = hydraulic.iterate_h(geometry)
Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)
#
#print(m_dot_c)
#print(m_dot_h)
#hydraulic.hydraulic_plot_c(geometry)
#hydraulic.hydraulic_plot_h(geometry)
print(thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry))
print(thermal.F_Q_NTU(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry))
#
#print()
#print(geom.check_constraints(geometry))
#print(geom.troubleshoot_geometry(geometry))
#
#geom.check_mass_total(geometry,display=True)
#geom.check_L_total(geometry,display=True)
#geom.check_L_tube_total(geometry,display=True)




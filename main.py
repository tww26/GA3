# -*- coding: utf-8 -*-

import hydraulic
import Thermal_Functions as thermal

"""DEFINE STATIC DESIGN VARIABLES"""
L = 350e-3
N_baffle = 9
pitch_type = "square"
Y = 10e-3
bundle_array = [1, 3, 5, 3, 1]
geometry = {'L':L,'N_baffle':N_baffle,'pitch_type':pitch_type,'Y':Y,'bundle_array':bundle_array}



m_dot_c = hydraulic.iterate_c(geometry)
m_dot_h = hydraulic.iterate_h(geometry)
Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)

hydraulic.hydraulic_plot_h(geometry)

#print(thermal.F_Q(m_dot_c, m_dot_h, Re_tube, Re_sh))



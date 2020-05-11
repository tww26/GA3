# -*- coding: utf-8 -*-

#from Definitions import *
import hydraulic
import Thermal_Functions as thermal

m_dot_c = hydraulic.iterate_c()
m_dot_h = hydraulic.iterate_h()
Re_sh = hydraulic.give_Re_sh(m_dot_c)
Re_tube = hydraulic.give_Re_tube(m_dot_h)

print(thermal.F_Q(m_dot_c, m_dot_h, Re_tube, Re_sh))


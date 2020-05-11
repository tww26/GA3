# -*- coding: utf-8 -*-

import hydraulic
import Thermal_Functions as thermal
import matplotlib.pyplot as plt

"""DEFINE STATIC DESIGN VARIABLES"""
L = 350e-3
N_baffle = 9
pitch_type = "square"
Y = 10e-3
bundle_array = [1,3,5,3,1]
N_shell = 1

geometry = {'L':L,'N_baffle':N_baffle,'pitch_type':pitch_type,'Y':Y,'bundle_array':bundle_array, 'N_shell':N_shell}


"""PLAYING WITH DESIGN VARIABLES"""

hydraulic.hydraulic_plot_c(geometry)

#N_baffle = 0
#L = 0.1
#Xplot = []; Qplot = []
#for j in range(5):
#    geometry['N_baffle'] = N_baffle
#    L = 0.1
#    for i in range(31):
#        geometry['L'] = L
#        Xplot.append(L)
#        # Find new Q
#        m_dot_c = hydraulic.iterate_c(geometry)
#        m_dot_h = hydraulic.iterate_h(geometry)
#        Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
#        Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)
#        Qplot.append(thermal.F_Q(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry))
#        L += 0.01
#    plt.plot(Xplot,Qplot,label="No.Baffles={}".format(N_baffle))
#    Xplot = []
#    Qplot = []
#    N_baffle += 4
#    
#plt.legend()    
#plt.xlabel("No. Baffles")
#plt.ylabel("Q(W)")
#plt.title("Effect of L and Number of Baffles Variation")
#plt.show()



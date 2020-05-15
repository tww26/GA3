# -*- coding: utf-8 -*-

import hydraulic
import Thermal_Functions as thermal
import matplotlib.pyplot as plt
import geometric as geom

L = 170e-3
N_baffle = 10
pitch_type = "square"
Y = 12e-3
bundle_array = [1,3,5,3,1]
N_shell = 2
N_pass = 2
L_header = 0.1
breadth_gap = 0.01

geometry = {'L': L,'N_baffle': N_baffle,'pitch_type': pitch_type,'Y': Y,'bundle_array': bundle_array, 'N_shell': N_shell, 'N_pass': N_pass, 'L_header': L_header, 'breadth_gap': breadth_gap}


"""PLAYING WITH DESIGN VARIABLES"""

m_dot_c = hydraulic.iterate_c(geometry)
m_dot_h = hydraulic.iterate_h(geometry)
Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)

hydraulic.hydraulic_plot_c(geometry)
hydraulic.hydraulic_plot_h(geometry)
print(thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry))


#hydraulic.hydraulic_plot_c(geometry)

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
#        Qplot.append(thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry))
#        L += 0.01
#    plt.plot(Xplot,Qplot,label="No.Baffles={}".format(N_baffle))
#    Xplot = []
#    Qplot = []
#    N_baffle += 4
#    
#plt.legend()    
#plt.xlabel("L (m)")
#plt.ylabel("Q(W)")
#plt.title("Effect of L and Number of Baffles Variation for 1-pass 1-shell [1,3,5,3,1] square bundle array with Y = 1.2cm")
#plt.show()

#Arrays = [[1,3,5,3,1],[4,4,4],[2,3,4,3,2],[3,3,3,3],[1,5,5,1]]
#
#for i in Arrays:
#    geometry['bundle_array'] = i
#    N_baffle = 0
#    Xplot = []; Qplot = []
#    for j in range(21):
#        geometry['N_baffle'] = N_baffle
#        Xplot.append(N_baffle)
#
#        m_dot_c = hydraulic.iterate_c(geometry)
#        m_dot_h = hydraulic.iterate_h(geometry)
#        Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
#        Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)
#
#        Qplot.append(thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry))
#
#        N_baffle += 1
#
#    plt.plot(Xplot,Qplot,label="{}".format(i))
#
##plt.plot(Xplot,Qplot,label="No.Baffles={}".format(N_baffle))
#plt.ylabel("Q (W)")
#plt.legend()
#plt.title("1-pass,1-shell square Y=12mm, L=300mm")
#plt.xlabel("Number of Baffles")
##plt.ylim(ymin=0)
#plt.plot()

m_dot_c = hydraulic.iterate_c(geometry)
m_dot_h = hydraulic.iterate_h(geometry)
Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)

print(thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry), thermal.F_T_out_hot(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry), thermal.F_T_out_cold(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry))

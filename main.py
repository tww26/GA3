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

#geometry = {'L': L,'N_baffle': N_baffle,'pitch_type': pitch_type,'Y': Y,'bundle_array': bundle_array, 'N_shell': N_shell, 'N_pass': N_pass, 'L_header': L_header, 'breadth_gap': breadth_gap}

value1 = optimise.NTUvsLMTD(1,1)
print('1/6')
value2 = optimise.NTUvsLMTD(2,1)
print('2/6')
value3 = optimise.NTUvsLMTD(4,1)
print('3/6')
value4 = optimise.NTUvsLMTD(1,2)
print('4/6')
value5 = optimise.NTUvsLMTD(2,2)
print('5/6')
value6 = optimise.NTUvsLMTD(4,2)
print('6/6')

LMTD11 = value1[0]
NTU11 = value1[1]
differences11 = value1[2]
reldifferences11 = value1[3]

LMTD21 = value2[0]
NTU21 = value2[1]
differences21 = value2[2]
reldifferences21 = value2[3]

LMTD41 = value3[0]
NTU41 = value3[1]
differences41 = value3[2]
reldifferences41 = value3[3]

LMTD12 = value4[0]
NTU12 = value4[1]
differences12 = value4[2]
reldifferences12 = value4[3]

LMTD22 = value5[0]
NTU22 = value5[1]
differences22 = value5[2]
reldifferences22 = value5[3]

LMTD42 = value6[0]
NTU42 = value6[1]
differences42 = value6[2]
reldifferences42 = value6[3]

plt.scatter(LMTD11,NTU11,label='1-pass,1-shell', s=1.5)
plt.scatter(LMTD21,NTU21,label='2-pass,1-shell', s=1.5)
plt.scatter(LMTD41,NTU41,label='4-pass,1-shell', s=1.5)
plt.scatter(LMTD12,NTU12,label='1-pass,2-shell', s=1.5)
plt.scatter(LMTD22,NTU22,label='2-pass,2-shell', s=1.5)
plt.scatter(LMTD42,NTU42,label='4-pass,2-shell', s=1.5)
plt.title('LMTD vs NTU heat transfers')
plt.legend()
plt.ylabel('e-NTU heat transfer (W)')
plt.xlabel('LMTD heat transfer (W)')
plt.grid()
plt.show()

plt.scatter(LMTD11,NTU11,label='1-pass,1-shell', s=1.5)
plt.scatter(LMTD21,NTU21,label='2-pass,1-shell', s=1.5)
plt.scatter(LMTD41,NTU41,label='4-pass,1-shell', s=1.5)
plt.scatter(LMTD12,NTU12,label='1-pass,2-shell', s=1.5)
plt.scatter(LMTD22,NTU22,label='2-pass,2-shell', s=1.5)
plt.scatter(LMTD42,NTU42,label='4-pass,2-shell', s=1.5)
plt.ylabel('e-NTU heat transfer (W)')
plt.xlabel('LMTD heat transfer (W)')
plt.title('LMTD vs NTU heat transfers')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.grid()
plt.show()

plt.scatter(LMTD11,reldifferences11,label='1-pass,1-shell', s=1.5)
plt.scatter(LMTD21,reldifferences21,label='2-pass,1-shell', s=1.5)
plt.scatter(LMTD41,reldifferences41,label='4-pass,1-shell', s=1.5)
plt.scatter(LMTD12,reldifferences12,label='1-pass,2-shell', s=1.5)
plt.scatter(LMTD22,reldifferences22,label='2-pass,2-shell', s=1.5)
plt.scatter(LMTD42,reldifferences42,label='4-pass,2-shell', s=1.5)
plt.ylabel('NTU heat transfer %error from LMTD method')
plt.xlabel('LMTD heat transfer (W)')
plt.title('NTU Error in Q vs LMTD Q')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.grid()
plt.show()

plt.scatter(LMTD11,reldifferences11,label='1-pass,1-shell', s=1.5)
plt.scatter(LMTD21,reldifferences21,label='2-pass,1-shell', s=1.5)
plt.scatter(LMTD41,reldifferences41,label='4-pass,1-shell', s=1.5)
plt.scatter(LMTD12,reldifferences12,label='1-pass,2-shell', s=1.5)
plt.scatter(LMTD22,reldifferences22,label='2-pass,2-shell', s=1.5)
plt.scatter(LMTD42,reldifferences42,label='4-pass,2-shell', s=1.5)
plt.ylabel('NTU heat transfer %error from LMTD method')
plt.xlabel('LMTD heat transfer (W)')
plt.title('NTU Error in Q vs LMTD Q')
plt.legend()
plt.grid()
plt.show()






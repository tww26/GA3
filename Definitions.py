# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:02:39 2020

@author: Tomos
"""

"""For Parametric Definitions, import design fraiables from main???"""

"""_________________________________________________________________________________________________________"""
"""____________________________________________Definitions__________________________________________________"""
"""_________________________________________________________________________________________________________"""

# All constants are in SI units (m, kg, Pa, K)

"""Geometric Constants"""

D_inner = 64e-3
D_outer = 70e-3
d_inner = 6e-3
d_outer = 8e-3
d_nozzle = 20e-3

t_baffle = 1.5e-3
t_endplate = 4.5e-3

""""Component Mass Properties"""

# rhol (mass per unit length) - kg/m
# rhoA (mass per unit area) - kg/m**2
# mass - kg

rhol_tube = 0.20      # copper tube
rhol_pipe = 0.650     # acrylic pipe (as specified in handout)
mass_nozzle = 0.025
rhoA_plate = 6.375
rhoA_baffle = 2.39


"""Geometric Constraints"""

L_tube_total_max = 6
L_shell_total_max = 0.5
L_total_max = 0.40
mass_total_max = 1



"""Thermal and Hydraulic Constants"""

rho_water = 990.1
cp = 4179
lambda_water = 0.632
lambda_tube = 386
mu = 6.51e-4
Pr = 4.31
Rf = 0

T_in_hot = 333.15
T_in_cold = 293.15


"""__________________________________________________________________"""


"""Global Input Variables"""

"""OLD - NOW IN MAIN/PARA Design Variables"""

#L = 350e-3
#N_baffle = 9
#pitch_type = "square"
#Y = 10e-3
#bundle_array = [1, 3, 5, 3, 1]
#F = 1


"""__________________________________________________________________"""


"""Parametric Definitions NOW DEFINED IN PARA"""

#N_row = len(bundle_array)
#N_tube = sum(bundle_array)
#
#L_sh = L + 3e-3
#L_tube = L + 12e-3
#A = np.pi * d_inner * L * N_tube
#
#B = L / (N_baffle + 1)
#if pitch_type == "square" or pitch_type == "Square":
#    a = 0.34
#else:
#    a = 0.2
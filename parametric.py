# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:41:06 2020

@author: Tomos
"""
   
import numpy as np
from Definitions import *
    
def N_row(geometry):
    """Returns the number of non-zero values in the array and divides by shell count to give:
        - the number of tube rows within each shell"""
        
    # Number of rows total - omitting any zero rows
    N_row = len(geometry.get('bundle_array'))-geometry.get('bundle_array').count(0)
    # Number of rows per shell
    N_row *= (1/geometry.get('N_shell'))
    
    return(N_row)
    
def N_tube(geometry):
    """This is absolute - not per pass or shell or anything"""
    return(sum(geometry.get('bundle_array')))
    
def A(geometry):
    return(np.pi * d_inner * geometry.get('L') * N_tube(geometry))
    
"""A_sh is defined in hydraulic.py"""
    
def F(geometry):
    """1 UNTIL WE ADD MANY PASSES"""
    return(1)
    
def a(geometry):
    if geometry.get('pitch_type') == "square" or geometry.get('pitch_type') == "Square":
        a_value = 0.34
    else:
        a_value = 0.2
    return(a_value)
    
def B(geometry):
    """IN FUTURE NEED TO CHANGE THIS FOR THICKNESS ACCOUNTING"""
    # All baffles equally spaced apart
    
    N_baffle = geometry.get('N_baffle')
    L = geometry.get('L')
    
    # The end baffles are there and we'd rather use middle ones
    if "B_end" in geometry and N_baffle > 4:
        L_new = L - 2*geometry.get('B_end')
        B = L_new/(N_baffle-1)
        return(B)
        
    # All baffles equally spaced
    else:
        return(L/(N_baffle+1))
        


def A_end_plate(geometry):
    r = 0.5 * D_outer
    A_outer = np.pi * r ** 2                                # Area of circle enclosed by D_outer
    return A_outer

def A_tube_plate(geometry):
    l = geometry.get('breadth_gap')
    r = 0.5*D_outer

    A_outer = np.pi * r ** 2                                 # Area of circle enclosed by D_outer
    A_tube = 0.25 * np.pi * d_outer ** 2
    A_tube_total = N_tube(geometry) * A_tube

    return (A_outer - A_tube_total)


def A_baffle(geometry):
    l = geometry.get('breadth_gap')
    r = 0.5 * D_inner
    A_inner = np.pi * r**2                                   # Area of circle enclosed by D_inner
    theta = 2 * np.arcsin(((2*l/r)-((l**2)/(r**2)))**0.5)
    A_tube = 0.25*np.pi*d_outer**2

    # TO BE AMENDED: Need to account for tubes in the baffle gap
    A_tube_total = N_tube(geometry) * A_tube

    A_gap = 0.5 * (theta - np.sin(0.5*theta)) * r**2

    return(A_inner - A_tube_total - A_gap)
    
def L_sh(geometry):
    return(geometry.get('L') + 3e-3)
    
def L_tube(geometry):
    return(geometry.get('L') + 12e-3)

def L_pipe(geometry):
    return(L_sh(geometry) + 2*geometry.get('L_header') + 0.06)

def L_total(geometry):
    # L_total = L + (2 * L_header) + (2 * L_endplate) + (2 * L_tubeplate)
    return(geometry.get('L') + 2*(geometry.get('L_header')) + 18e-3)


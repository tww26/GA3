# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:41:06 2020

@author: Tomos
"""
   
import numpy as np
from Definitions import *
    
def N_row(geometry):
    return(len(geometry.get('bundle_array')))
    
def N_tube(geometry):
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
    return(geometry.get('L')/(geometry.get('N_baffle')+1))
    
def L_sh(geometry):
    return(geometry.get(L) + 3e-3)
    
def L_tube(geometry):
    return(geometry.get(L) + 12e-3)
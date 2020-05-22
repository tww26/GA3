# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:53:10 2020

@author: Tomos
"""

import Thermal_Functions as thermal
import numpy as np

"""FIRST CONFIGURATION: K VALUE CONFIGURTAION"""
def K_config(geometry,year):
    """Varies the value of K_nozzle, K_turn (pass), and K_baffle_bend, and returns Q"""
    
    K_nozzle_list = np.linspace(0.5,2,16)
    K_turn_list = np.linspace(0.5,2,16)
    K_baffle_bend_list = np.linspace(0.5,2,16)
    
    Qmax = 0
    Qmin = 10e5
    Qlist = []
    
    for x in K_nozzle_list:
        for y in K_turn_list:
            for z in K_baffle_bend_list:
                Q = thermal.Q(geometry,year,K_baffle_bend=z,K_nozzle=x,K_turn=y)
                Qlist.append(Q)
                if Q>Qmax:
                    Qmax=Q
                if Q<Qmin:
                    Qmin=Q
    
    Qave = sum(Qlist)/len(Qlist)
    
    return (Qmin,Qave,Qmax)
                    
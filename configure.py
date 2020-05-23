# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:53:10 2020

@author: Tomos
"""

import Thermal_Functions as thermal
import numpy as np
from designs import *

"""FIRST CONFIGURATION: K VALUE CONFIGURTAION"""
def K_config_1(geometry,year):
    """Varies the value of K_nozzle, K_turn (pass), and K_baffle_bend, and returns Q max, ave, min"""
    
    K_nozzle_list = np.linspace(0,1.5,4)
    K_turn_list = np.linspace(0,1.5,4)
    K_baffle_bend_list = np.linspace(0,3,7)
    Calibration1_list = np.linspace(0.9,1.2,4)
    Calibration2_list = np.linspace(0.9,1.2,4)
    Calibration3_list = np.linspace(0.9,1.2,4)
    
    Qmax = 0
    Qmin = 10e5
    Qlist = []
    
    for u in Calibration1_list:
        for v in Calibration2_list:
            for w in Calibration3_list:
                for x in K_nozzle_list:
                    for y in K_turn_list:
                        for z in K_baffle_bend_list:
                            Q = thermal.Q(geometry,year,K_baffle_bend=z,K_nozzle=x,K_turn=y,Calibration1=u,Calibration2=v,Calibration3=w)
                            Qlist.append(Q)
                            if Q>Qmax:
                                Qmax=Q
                            if Q<Qmin:
                                Qmin=Q
    
    Qave = sum(Qlist)/len(Qlist)
    
    return (Qmin,Qave,Qmax)
            
def K_config_2(geometry,year):
    """Varies the value of K_nozzle, K_turn (pass), and K_baffle_bend, to find closest Q to answer"""
    
    K_nozzle_list = np.linspace(0,1.5,4)
    K_turn_list = np.linspace(0,1.5,4)
    K_baffle_bend_list = np.linspace(0,1.5,4)
    Calibration1_list = np.linspace(0.9,1.2,4)
    Calibration2_list = np.linspace(0.9,1.2,4)
    Calibration3_list = np.linspace(0.9,1.2,4)
    
    Difference = 10e4
    Optimal_Constants = (1,1,1,1,1)
    count1 = 0
    
    for u in Calibration1_list:
        for v in Calibration2_list:
            print("{}/{} for one design".format(count1, len(Calibration2_list)*len(Calibration1_list)))
            count1 += 1
            for w in Calibration3_list:
                for x in K_nozzle_list:
                    for y in K_turn_list:
                        for z in K_baffle_bend_list:
                            Q = thermal.Q(geometry,year,K_baffle_bend=z,K_nozzle=x,K_turn=y,Calibration1=u,Calibration2=v,Calibration3=w)
                            if abs(Q-geometry.get('Q')) < Difference:
                                Difference = abs(Q-geometry.get('Q'))
                                Optimal_Constants = (x,y,z,u,v,w)
                                
    print("{}/{} for one design".format(count1, len(Calibration2_list)*len(Calibration1_list)))
    return (Optimal_Constants)      

for i in Designs:
    for j in Designs.get(i):
        print(K_config_2(Designs.get(i).get(j),Designs.get(i).keys()))
        print()
                    
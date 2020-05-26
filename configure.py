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
    
    K_nozzle_list = [3.676678]
    K_turn_list = [1.89314558]
    K_baffle_bend_list = [1.76628]
    Calibration1_list = np.linspace(1,1.1,11)
    Calibration2_list = np.linspace(1,1.1,11)
    Calibration3_list = np.linspace(1.1,1.12,11)
    
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
                                
    return (Optimal_Constants)   

def K_config_2_ave():
    """Prints the Average of the best values"""
    
    # Define some lists
    Values_list = []
    Optimal_Constants = [0,0,0]
    
    # Values list filled with tuples
    for i in Designs:
        for j in Designs.get(i):
            Values_list.append(K_config_2(Designs.get(i).get(j),Designs.get(i).keys()))
    
    # Optimal_constants filled with sums of values
    for k in Values_list:
        for l in range(3):
            Optimal_Constants[l]+=k[l+3]
            
    # Optimal constanta filled with averages      
    count = 0
    for m in Optimal_Constants:
        Optimal_Constants[count]=m/len(Values_list)
        count += 1
        
    return Optimal_Constants

def K_config_3():
    """Finds the optimum of the average, not vice versa"""
    
    K_nozzle_list = [3.676678]
    K_turn_list = [1.89314558]
    K_baffle_bend_list = [1.76628]
    Calibration1_list = np.linspace(1.25,1.35,3)
    Calibration2_list = np.linspace(0.9,0.95,11)
    Calibration3_list = np.linspace(1.15,1.3,3)
    
    Absolute_Difference = 10e4
    Percent_Difference = 100
    count1 = 0
    
    for u in Calibration1_list:
        for v in Calibration2_list:
            print("{}/{} complete".format(count1, len(Calibration2_list)*len(Calibration1_list)))
            count1 += 1
            for w in Calibration3_list:
                for x in K_nozzle_list:
                    for y in K_turn_list:
                        for z in K_baffle_bend_list:
                            Difference_list = []
                            Percent_Difference_list = []
                            for i in Designs:
                                for j in Designs.get(i):
                                    Q = thermal.Q(Designs.get(i).get(j),Designs.get(i).keys(),K_baffle_bend=z,K_nozzle=x,K_turn=y,Calibration1=u,Calibration2=v,Calibration3=w)
                                    Difference_list.append(abs(Q-Designs.get(i).get(j).get('Q')))
                                    Percent_Difference_list.append(100*abs(Q-Designs.get(i).get(j).get('Q'))/Designs.get(i).get(j).get('Q'))
                                    
                            # Average design for those constants
                            Ave_Difference = sum(Difference_list)/len(Difference_list)
                            # Average % design for those constants
                            Ave_Percent_Difference = sum(Percent_Difference_list)/len(Percent_Difference_list)
                            
                            # Store best average vaues
                            if Ave_Difference < Absolute_Difference:
                                Absolute_Difference = Ave_Difference
                                lowest_1 = int(round(Ave_Difference,0))
                                Optimal_Constants_1 = (x,y,z,u,v,w)
                                
                            if Ave_Percent_Difference < Percent_Difference:
                                Percent_Difference = Ave_Percent_Difference
                                lowest_2 = round(Ave_Percent_Difference,2)
                                Optimal_Constants_2 = (x,y,z,u,v,w)
                                

    return (("Ave Absolute Difference = {}".format(lowest_1),Optimal_Constants_1,"Lowest Ave % difference is {}%".format(lowest_2),Optimal_Constants_2))
            
print(K_config_3())
            
                        
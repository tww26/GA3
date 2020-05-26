# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:09:23 2020

@author: Tomos
"""

import matplotlib.pyplot as plt
from Definitions import *
from designs import *
import Thermal_Functions as thermal

def cross_section(geometry):
    """Plot the cross-section"""
    
    pitch_type=geometry.get('pitch_type')
    Y=geometry.get('Y')
    bundle_array=geometry.get('bundle_array')

    fig, ax = plt.subplots()
    plt.ylim(-0.05,0.05)
    plt.xlim(-0.05,0.05)
    
    #ax.add_artist(plt.Circle((0, 0), D_inner/2, facecolor=none))
    
    if pitch_type == 'square':
        for i in range(len(bundle_array)):
            for j in range(bundle_array[i]):
                x = (0.5+(bundle_array[i]*0.5-1)-j)*Y
                y = (0.5+(len(bundle_array)*0.5-1)-i)*Y
                ax.add_artist(plt.Circle((x,y), d_outer/2,color='r'))
    else:
        for i in range(len(bundle_array)):
            for j in range(bundle_array[i]):
                x = x = (0.5+(bundle_array[i]*0.5-1)-j)*Y
                y = (0.5+(len(bundle_array)*0.5-1)-i)*Y*0.866
                ax.add_artist(plt.Circle((x,y), d_outer/2,color='r'))
                
    ax.add_artist(plt.Circle((0, 0), D_inner/2, edgecolor='r',fill=False))

def plot_difference():
    """Plots and prints the differences between the designs of the different years"""
    
    N_17 = len(Designs.get('2017'))
    N_18 = len(Designs.get('2018'))
    N_19 = len(Designs.get('2019'))
    
    # Initialise some lists
    Q_calcs = [] # What we predict
    Q_actual = []
    
    # Fill the lists
    for i in Designs.get('2017'):
        if i != 'Year':
            Q_actual.append(Designs.get('2017').get(i).get('Q'))
            Q_calcs.append(thermal.Q(Designs.get('2017').get(i),'2017',K_baffle_bend=1.73710938,K_nozzle=2.0296875,K_turn=0.68613281,Calibration1=1.17,Calibration2=0.87,Calibration3=1.18))
            
    for i in Designs.get('2018'):
        if i != 'Year':
            Q_actual.append(Designs.get('2018').get(i).get('Q'))
            Q_calcs.append(thermal.Q(Designs.get('2018').get(i),'2018',K_baffle_bend=1.73710938,K_nozzle=2.0296875,K_turn=0.68613281,Calibration1=1.17,Calibration2=0.87,Calibration3=1.18))
            
    for i in Designs.get('2019'):
        if i != 'Year':
            Q_actual.append(Designs.get('2019').get(i).get('Q'))
            Q_calcs.append(thermal.Q(Designs.get('2019').get(i),'2019',K_baffle_bend=1.73710938,K_nozzle=2.0296875,K_turn=0.68613281,Calibration1=1.17,Calibration2=0.87,Calibration3=1.18))
    
    
    #Plot a y = x line
    MaxQ = []
    MaxQ.append(max(Q_calcs))
    MaxQ.append(max(Q_actual))
    MaxQ = int(max(MaxQ))
    MinQ = []
    MinQ.append(min(Q_calcs))
    MinQ.append(min(Q_actual))
    MinQ = int(min(MinQ))
    x = range(MinQ,MaxQ)
    y = range(MinQ,MaxQ)
    plt.scatter(x,y,color='k',s=0.5)
    #plt.plot([MinQ,MinQ],[MaxQ,MaxQ])#,linestyle="--")
    
    # Plot the lists
    plt.scatter(Q_actual[0:N_17],Q_calcs[0:N_17],label="2017")
    plt.scatter(Q_actual[N_17:N_17+N_18],Q_calcs[N_17:N_17+N_18],label="2018")
    plt.scatter(Q_actual[N_17+N_18:],Q_calcs[N_17+N_18:],label="2019")

    # Plotting magic
    plt.title('Measuring difference of Pair 4 code to actual value')
    plt.ylabel('Pair 4 Predicted Heat Transfer (W)')
    plt.xlabel('Measured Heat Transfer (W)')
    plt.legend()
    plt.grid()
    plt.plot()
    
    # Print some results
    print("% Differences")
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        print(percent_diff)
  
plot_difference()


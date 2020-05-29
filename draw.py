# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:09:23 2020

@author: Tomos
"""

import matplotlib.pyplot as plt
from Definitions import *
from designs import *
import Thermal_Functions as thermal
import hydraulic
import numpy as np

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
    Q_calcs_1 = [] # What we predict
    Q_actual_1 = []
    Q_calcs_2 = [] # What we predict
    Q_actual_2 = []
    Q_calcs_3 = [] # What we predict
    Q_actual_3 = []

    
    # Values
    K1 = 5.21461099
    K2 = 4.4899305
    K3 = 1.29030439
    C1 = 1.18
    C2 = 0.87
    C3 = 1.19
    
    # Fill the lists per Design category
    for i in Designs:
        for j in Designs.get(i):
            category = Designs.get(i).get(j).get('category')
            if category == 1:
#                Q_calcs_1.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_1.append(thermal.Q(Designs.get(i).get(j),i, method ="LMTD", K_turn=K1, K_nozzle=K2, K_baffle_bend=K3, Calibration1=C1,Calibration2=C2, Calibration3=C3))
                Q_actual_1.append(Designs.get(i).get(j).get('Q'))
            elif category == 2:
#                Q_calcs_2.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_2.append(thermal.Q(Designs.get(i).get(j),i, method ="LMTD", K_turn=K1, K_nozzle=K2, K_baffle_bend=K3, Calibration1=C1,Calibration2=C2, Calibration3=C3))
                Q_actual_2.append(Designs.get(i).get(j).get('Q'))
            else:
#                Q_calcs_3.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_3.append(thermal.Q(Designs.get(i).get(j),i, method ="LMTD", K_turn=K1, K_nozzle=K2, K_baffle_bend=K3, Calibration1=C1,Calibration2=C2, Calibration3=C3))
                Q_actual_3.append(Designs.get(i).get(j).get('Q'))
    
    
    #Plot a y = x line
    MaxQ = []
    MaxQ.append(max(Q_calcs_1))
    MaxQ.append(max(Q_actual_1))
    MaxQ.append(max(Q_calcs_2))
    MaxQ.append(max(Q_actual_2))
    MaxQ.append(max(Q_calcs_3))
    MaxQ.append(max(Q_actual_3))
    MaxQ = int(max(MaxQ))
    MinQ = []
    MinQ.append(min(Q_calcs_1))
    MinQ.append(min(Q_actual_1))
    MinQ.append(min(Q_calcs_2))
    MinQ.append(min(Q_actual_2))
    MinQ.append(min(Q_calcs_3))
    MinQ.append(min(Q_actual_3))
    MinQ = int(min(MinQ))
    x = range(MinQ,MaxQ)
    y = range(MinQ,MaxQ)
    plt.scatter(x,y,color='k',s=0.5)
    
    # Plot the lists
    plt.scatter(Q_actual_1,Q_calcs_1,label="Category 1",color='b')
    plt.scatter(Q_actual_2,Q_calcs_2,label="Category 2",color='b')
    plt.scatter(Q_actual_3,Q_calcs_3,label="Category 3",color='b')

    # Plotting magic
    plt.title('Measuring difference of Pair 4 code to actual value')
    plt.ylabel('Pair 4 Predicted Heat Transfer (W)')
    plt.xlabel('Measured Heat Transfer (W)')
    #plt.legend()
    plt.grid()
    plt.plot()
    
    # Print some results
    print("Category 1 % Differences")
    avgdiff = []
    Q_actual = Q_actual_1
    Q_calcs = Q_calcs_1
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))
    print()
    print("Category 2 % Differences")
    avgdiff = []
    Q_actual = Q_actual_2
    Q_calcs = Q_calcs_2
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))
    print()
    print("Category 3 % Differences")
    print()
    avgdiff = []
    Q_actual = Q_actual_3
    Q_calcs = Q_calcs_3
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))

def plot_mc_difference():
    """Plots and prints the differences between the designs of the different years"""

    # Initialise some lists
    Q_calcs_1 = [] # What we predict
    Q_actual_1 = []
    Q_calcs_2 = [] # What we predict
    Q_actual_2 = []
    Q_calcs_3 = [] # What we predict
    Q_actual_3 = []


    # Values
    K1 = 5.21461099
    K2 = 4.4899305
    K3 = 1.29030439

    # Fill the lists per Design category
    for i in Designs:
        for j in Designs.get(i):
            category = Designs.get(i).get(j).get('category')
            if category == 1:
#                Q_calcs_1.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_1.append(hydraulic.iterate_c(Designs.get(i).get(j),i,K_baffle_bend=K3,K_nozzle=K2))
                Q_actual_1.append(Designs.get(i).get(j).get('m_dot_cold'))
            elif category == 2:
#                Q_calcs_2.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_2.append(hydraulic.iterate_c(Designs.get(i).get(j),i,K_baffle_bend=K3,K_nozzle=K2))
                Q_actual_2.append(Designs.get(i).get(j).get('m_dot_cold'))
            else:
#                Q_calcs_3.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_3.append(hydraulic.iterate_c(Designs.get(i).get(j),i,K_baffle_bend=K3,K_nozzle=K2))
                Q_actual_3.append(Designs.get(i).get(j).get('m_dot_cold'))


    #Plot a y = x line
    MaxQ = []
    MaxQ.append(max(Q_calcs_1))
    MaxQ.append(max(Q_actual_1))
    MaxQ.append(max(Q_calcs_2))
    MaxQ.append(max(Q_actual_2))
    MaxQ.append(max(Q_calcs_3))
    MaxQ.append(max(Q_actual_3))
    MaxQ = max(MaxQ)
    MinQ = []
    MinQ.append(min(Q_calcs_1))
    MinQ.append(min(Q_actual_1))
    MinQ.append(min(Q_calcs_2))
    MinQ.append(min(Q_actual_2))
    MinQ.append(min(Q_calcs_3))
    MinQ.append(min(Q_actual_3))
    MinQ = min(MinQ)
    x = np.linspace(MinQ,MaxQ,101)
    y = np.linspace(MinQ,MaxQ,101)
    plt.scatter(x,y,color='k',s=0.5)

    # Plot the lists
    plt.scatter(Q_actual_1,Q_calcs_1,label="Category 1",color='b')
    plt.scatter(Q_actual_2,Q_calcs_2,label="Category 2",color='b')
    plt.scatter(Q_actual_3,Q_calcs_3,label="Category 3",color='b')

    # Plotting magic
    plt.title('Measuring difference of Pair 4 code to actual value')
    plt.ylabel('Pair 4 Predicted Cold Mass Flow Rate (kg/s)')
    plt.xlabel('Measured Cold Mass Flow Rate (kg/s)')
    #plt.legend()
    plt.grid()
    plt.plot()

    # Print some results
    print("Category 1 % Differences")
    avgdiff = []
    Q_actual = Q_actual_1
    Q_calcs = Q_calcs_1
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))
    print()
    print("Category 2 % Differences")
    avgdiff = []
    Q_actual = Q_actual_2
    Q_calcs = Q_calcs_2
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))
    print()
    print("Category 3 % Differences")
    print()
    avgdiff = []
    Q_actual = Q_actual_3
    Q_calcs = Q_calcs_3
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))

def plot_mh_difference():
    """Plots and prints the differences between the designs of the different years"""

    # Initialise some lists
    Q_calcs_1 = [] # What we predict
    Q_actual_1 = []
    Q_calcs_2 = [] # What we predict
    Q_actual_2 = []
    Q_calcs_3 = [] # What we predict
    Q_actual_3 = []


    # Values
    K1 = 5.21461099
    K2 = 4.4899305
    K3 = 1.29030439

    # Fill the lists per Design category
    for i in Designs:
        for j in Designs.get(i):
            category = Designs.get(i).get(j).get('category')
            if category == 1:
#                Q_calcs_1.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_1.append(hydraulic.iterate_h(Designs.get(i).get(j),i,K_nozzle=K2,K_turn=K1))
                Q_actual_1.append(Designs.get(i).get(j).get('m_dot_hot'))
            elif category == 2:
#                Q_calcs_2.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_2.append(hydraulic.iterate_h(Designs.get(i).get(j),i,K_nozzle=K2,K_turn=K1))
                Q_actual_2.append(Designs.get(i).get(j).get('m_dot_hot'))
            else:
#                Q_calcs_3.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_3.append(hydraulic.iterate_h(Designs.get(i).get(j),i,K_nozzle=K2,K_turn=K1))
                Q_actual_3.append(Designs.get(i).get(j).get('m_dot_hot'))


    #Plot a y = x line
    MaxQ = []
    MaxQ.append(max(Q_calcs_1))
    MaxQ.append(max(Q_actual_1))
    MaxQ.append(max(Q_calcs_2))
    MaxQ.append(max(Q_actual_2))
    MaxQ.append(max(Q_calcs_3))
    MaxQ.append(max(Q_actual_3))
    MaxQ = max(MaxQ)
    MinQ = []
    MinQ.append(min(Q_calcs_1))
    MinQ.append(min(Q_actual_1))
    MinQ.append(min(Q_calcs_2))
    MinQ.append(min(Q_actual_2))
    MinQ.append(min(Q_calcs_3))
    MinQ.append(min(Q_actual_3))
    MinQ = min(MinQ)
    x = np.linspace(MinQ,MaxQ,101)
    y = np.linspace(MinQ,MaxQ,101)
    plt.scatter(x,y,color='k',s=0.5)

    # Plot the lists
    plt.scatter(Q_actual_1,Q_calcs_1,label="Category 1",color='b')
    plt.scatter(Q_actual_2,Q_calcs_2,label="Category 2",color='b')
    plt.scatter(Q_actual_3,Q_calcs_3,label="Category 3",color='b')

    # Plotting magic
    plt.title('Measuring difference of Pair 4 code to actual value')
    plt.ylabel('Pair 4 Predicted Hot Mass Flow Rate (kg/s)')
    plt.xlabel('Measured Hot Mass Flow Rate (kg/s)')
    #plt.legend()
    plt.grid()
    plt.show()

    # Print some results
    print("Category 1 % Differences")
    avgdiff = []
    Q_actual = Q_actual_1
    Q_calcs = Q_calcs_1
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))
    print()
    print("Category 2 % Differences")
    avgdiff = []
    Q_actual = Q_actual_2
    Q_calcs = Q_calcs_2
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))
    print()
    print("Category 3 % Differences")
    print()
    avgdiff = []
    Q_actual = Q_actual_3
    Q_calcs = Q_calcs_3
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))

def plot_mass_difference():
    """Plots and prints the differences between the designs of the different years"""

    # Initialise some lists
    Q_calcs_1 = [] # What we predict
    Q_actual_1 = []
    Q_calcs_2 = [] # What we predict
    Q_actual_2 = []
    Q_calcs_3 = [] # What we predict
    Q_actual_3 = []


    # Values
    K1 = 5.21461099
    K2 = 4.4899305
    K3 = 1.29030439
    C1 = 1.18
    C2 = 0.87
    C3 = 1.19

    # Fill the lists per Design category
    for i in Designs:
        for j in Designs.get(i):
            category = Designs.get(i).get(j).get('category')
            if category == 1:
#                Q_calcs_1.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_1.append(thermal.Q(Designs.get(i).get(j),i,K_baffle_bend=K3,K_nozzle=K2,K_turn=K1,Calibration1=C1,Calibration2=C2,Calibration3=C3))
                Q_actual_1.append(Designs.get(i).get(j).get('Q'))
            elif category == 2:
#                Q_calcs_2.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_2.append(thermal.Q(Designs.get(i).get(j),i,K_baffle_bend=K3,K_nozzle=K2,K_turn=K1,Calibration1=C1,Calibration2=C2,Calibration3=C3))
                Q_actual_2.append(Designs.get(i).get(j).get('Q'))
            else:
#                Q_calcs_3.append(thermal.Q(Designs.get(i).get(j),i))
                Q_calcs_3.append(thermal.Q(Designs.get(i).get(j),i,K_baffle_bend=K3,K_nozzle=K2,K_turn=K1,Calibration1=C1,Calibration2=C2,Calibration3=C3))
                Q_actual_3.append(Designs.get(i).get(j).get('Q'))

    
    #Plot a y = x line
    MaxQ = []
    MaxQ.append(max(Q_calcs_1))
    MaxQ.append(max(Q_actual_1))
    MaxQ.append(max(Q_calcs_2))
    MaxQ.append(max(Q_actual_2))
    MaxQ.append(max(Q_calcs_3))
    MaxQ.append(max(Q_actual_3))
    MaxQ = max(MaxQ)
    MinQ = []
    MinQ.append(min(Q_calcs_1))
    MinQ.append(min(Q_actual_1))
    MinQ.append(min(Q_calcs_2))
    MinQ.append(min(Q_actual_2))
    MinQ.append(min(Q_calcs_3))
    MinQ.append(min(Q_actual_3))
    MinQ = min(MinQ)
    x = np.linspace(MinQ,MaxQ,101)
    y = np.linspace(MinQ,MaxQ,101)
    plt.scatter(x,y,color='k',s=0.5)

    # Plot the lists
    plt.scatter(Q_actual_1,Q_calcs_1,label="Category 1",color='b')
    plt.scatter(Q_actual_2,Q_calcs_2,label="Category 2",color='b')
    plt.scatter(Q_actual_3,Q_calcs_3,label="Category 3",color='b')

    # Plotting magic
    plt.title('Measuring difference of Pair 4 code to actual value')
    plt.ylabel('Pair 4 Predicted Heat Transfer (W)')
    plt.xlabel('Measured Heat Transfer (W)')
    #plt.legend()
    plt.grid()
    plt.show()

    # Print some results
    print("Category 1 % Differences")
    avgdiff = []
    Q_actual = Q_actual_1
    Q_calcs = Q_calcs_1
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))
    print()
    print("Category 2 % Differences")
    avgdiff = []
    Q_actual = Q_actual_2
    Q_calcs = Q_calcs_2
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))
    print()
    print("Category 3 % Differences")
    print()
    avgdiff = []
    Q_actual = Q_actual_3
    Q_calcs = Q_calcs_3
    for i in range(len(Q_actual)):
        percent_diff = 100*(Q_calcs[i]-Q_actual[i])/Q_actual[i]
        avgdiff.append(abs(percent_diff))
        print(percent_diff)
    avgdiff = sum(avgdiff)/len(avgdiff)
    print("AVERAGE ABS: {}%".format(avgdiff))


plot_mh_difference()
plot_mc_difference()


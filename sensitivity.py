# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:01:33 2020

@author: Tomos
"""

import matplotlib.pyplot as plt
import numpy as np
from designs import *
import hydraulic
import Thermal_Functions as thermal

def sensitivity_m_dot_c(geometry,year):
    """Plots the sensitivity of a certain value or function
    FOR ONE VALUE AT A TIME"""
    
    # Find base values
    m_dot_base  = hydraulic.iterate_c(geometry,year)
    Q_base      = thermal.Q(geometry,year)
    
    # Initialise empty list
    QList       = []
    
    # Find other values needed
    m_dot_const = hydraulic.iterate_h(geometry,year)
    Re_const    = hydraulic.give_Re_tube(m_dot_const,geometry)
    
    # Find factors we multiply by
    factors     = np.linspace(0.5,1.5,101)
    
    # Multiply by 
    for j in factors:
        
        NewVal  = m_dot_base*j
        NewRe   = hydraulic.give_Re_sh(NewVal,geometry)
        NewQ    = thermal.F_Q_LMTD(NewVal,m_dot_const,Re_const,NewRe,geometry)
        
        QList.append(NewQ/Q_base)
        
    return(QList)
    
def plot_sensitivity_m_dot_c():
    """Plots affect on m_dot_c of all the different vals"""
    
    factors = np.linspace(0.5,1.5,101)
    
    for i in Designs:
        count=1
        for j in Designs.get(i):
            geometry = Designs.get(i).get(j)
            year = i
            plt.plot(factors,sensitivity_m_dot_c(geometry,year),label="{} design {}".format(year,count))
            count += 1
    
    plt.title("Effect of shell mass flow rate on heat rate, all other inputs and parameters constant")
    plt.xlabel("Proportion of calculated mass flow rate")
    plt.ylabel("Proportion of calculated heat rate")
    plt.legend()
    plt.grid()
    plt.show()
    
def sensitivity_m_dot_h(geometry,year):
    """Plots the sensitivity of a certain value or function
    FOR ONE VALUE AT A TIME"""
    
    # Find base values
    m_dot_base  = hydraulic.iterate_h(geometry,year)
    Q_base      = thermal.Q(geometry,year)
    
    # Initialise empty lists
    QList       = []
    
    # Find other values needed
    m_dot_const = hydraulic.iterate_c(geometry,year)
    Re_const    = hydraulic.give_Re_sh(m_dot_const,geometry)
    
    # Find factors we multiply by
    factors     = np.linspace(0.5,1.5,101)
    
    # Multiply by 
    for j in factors:
        
        NewVal  = m_dot_base*j
        NewRe   = hydraulic.give_Re_tube(NewVal,geometry)
        NewQ    = thermal.F_Q_LMTD(m_dot_const,NewVal,NewRe,Re_const,geometry)
        
        QList.append(NewQ/Q_base)
        
    return(QList)
    
def plot_sensitivity_m_dot_h():
    """Plots affect on m_dot_h of all the different vals"""
    
    factors = np.linspace(0.5,1.5,101)
    
    for i in Designs:
        count=1
        for j in Designs.get(i):
            geometry = Designs.get(i).get(j)
            year = i
            plt.plot(factors,sensitivity_m_dot_c(geometry,year),label="{} design {}".format(year,count))
            count += 1
    
    plt.title("Effect of shell mass flow rate on heat rate, all other inputs and parameters constant")
    plt.xlabel("Proportion of calculated mass flow rate")
    plt.ylabel("Proportion of calculated heat rate")
    plt.legend()
    plt.grid()
    plt.show()
    
def plot_combined_m_dot_sensitivity():
    """Plots effect of varying both"""
    
    factors = np.linspace(0.5,1.5,101)
    
    for i in Designs:
        count=1
        for j in Designs.get(i):
            geometry = Designs.get(i).get(j)
            year = i
            plt.plot(factors,sensitivity_m_dot_h(geometry,year),label="Tube-side variation for {} design {}".format(year,count))
            plt.plot(factors,sensitivity_m_dot_c(geometry,year),label="Shell-side variation for {} design {}".format(year,count),linestyle="--")
            count += 1
    
    plt.title("Effect of shell mass flow rate on heat rate, all other inputs and parameters constant")
    plt.xlabel("Proportion of calculated mass flow rate")
    plt.ylabel("Proportion of calculated heat rate")
    plt.legend()
    plt.grid()
    plt.show()
    
def sensitivity_Y(geometry,year):
    """Plots the sensitivity of a certain value or function
    FOR ONE VALUE AT A TIME"""
    
    # Find base values
    Y_base      = geometry.get('Y')
    Q_base      = thermal.Q(geometry,year)
    
    # Initialise empty lists
    QList       = []
    
    # Find factors we multiply by
    factors     = np.linspace(1,1.5,51)
    
    # Multiply by 
    for j in factors:
        
        NewVal  = Y_base*j
        geometry['Y'] = NewVal
        NewQ    = thermal.Q(geometry,year)
        
        QList.append(NewQ/Q_base)
        
    return(QList)

def plot_sensitivity_pitch():
    """Plots affect on m_dot_h of all the different vals"""
    
    factors = np.linspace(1,1.5,51)
    
    for i in Designs:
        count=1
        for j in Designs.get(i):
            geometry = Designs.get(i).get(j)
            year = i
            plt.plot(factors,sensitivity_Y(geometry,year),label="{} design {}".format(year,count))
            count += 1
    
    plt.title("Effect of shell mass flow rate on heat rate, all other inputs and parameters constant")
    plt.xlabel("Proportion of calculated mass flow rate")
    plt.ylabel("Proportion of calculated heat rate")
    #plt.legend()
    plt.grid()
    plt.show()
    
plot_sensitivity_m_dot_c()
plot_sensitivity_m_dot_h()
#plot_combined_m_dot_sensitivity()
plot_sensitivity_pitch()
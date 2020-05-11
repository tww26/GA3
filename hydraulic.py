# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:44:10 2020

@author: Tomos
"""

import numpy as np
import matplotlib.pyplot as plt
from Definitions import *

"""
Start by defining the Characteristic dP-massflowrate relationship from graphs
"""

def dp_flowrate(m_dot,temp):
    """Uses a dP-Flowrate data curve-fit for hot and cold to determine the pressure drop from the mass flow rate
    NOTE: Doesn't tell you if the flowrate is beyond what we can expect to work at all!!!"""
    
    # Calculate flowrate in L/s 
    Q = (m_dot / rho_water) * 1000
    
    # if Cold
    if temp == "cold":
        dP = -1.07*Q**2 + 0.0995*Q + 0.584
    
    # if Hot
    else:
        dP = -0.52*Q**2 - 0.769*Q + 0.677
        
    # dP in Pa not bar
    dP *= 100000
    
    return(dP)
    
"""
HOT STREAM CALCULATIONS
"""

def Find_sigma():
    """Returns sigma, the ratio of free area
    geometric parameters defined externally"""
    
    numerator = 0.25 * np.pi * N_tube * d_inner**2
    denominator = 0.25 * np.pi * D_inner**2
    
    sigma = numerator / denominator
    
    return(sigma)

def Find_Kc(sigma,Re="infinite"):
    """Finds Kc from Figure 7 crude curve fit; assumes turbulent flow.
    Re can be 3000,5000,10000 and "infinite" otherwise..."""
    
    # Apply linear fit by observation
    if Re == 10000:
        Kc = -0.4*sigma + 0.5
    elif Re == 5000:
        Kc = -0.4*sigma + 0.52
    elif Re == 3000:
        Kc = -0.4*sigma + 0.54
        
    # Else infinite
    else:
        Kc = -0.4*sigma + 0.4
        
    return(Kc)

def Find_Ke(sigma,Re="infinite"):
    """Finds Ke from Figure 7 crude curve fit; assumes turbulent flow.
    Re can be 3000,5000,10000 and "infinite" otherwise..."""
    
    # Re = 3000,5000,10000 all very similar
    if Re == 10000:
        Ke = sigma**2 - 2.1*sigma + 1
    
    # From infinite Re curve
    else:
        Ke = 0.949*sigma**2 - 1.94*sigma + 0.994
        
    return(Ke)

def Find_f(Re):
    """Finds the friction factor using approximation from worked example"""
    
    f = (1.82*np.log10(Re)-1.64)**(-2)
    
    return(f)

# Now combine the above functions to give a pressure drop
def total_dP_hot(m_dot_h):
    """Given massflowrate, Calculates velocities, Re and Kc, Ke 
    (assumes design variables D_inner,d_inner,N_tube set elsewhere)
    THEN
    Sums pressure drop (Pa) in tubes as the sum of:
        1. Friction in tubes
        2. Entry and Exit losses (assuming infinite Re)
        3. Nozzle losses"""
    
    # Calculate tube velocity
    m_dot_tube = m_dot_h / N_tube
    v_tube = m_dot_tube / (rho_water * np.pi * 0.25 * d_inner**2)
    
    # Calculate nozzle velocity
    v_nozzle_h = m_dot_h / (rho_water * np.pi * 0.25 * d_nozzle**2)
    
    # Calculate Re for tubes
    Re_tube = (v_tube*rho_water*d_inner)/mu
    
    # Re assumed infinite by nozzle (from Friday 8/5/20 MS Teams call)
    
    # Calculate Ke, Kc assuming infinite Re
    sigma = Find_sigma()
    Kc = Find_Kc(sigma)
    Ke = Find_Ke(sigma)
    
    
    # dP FROM TUBE FRICTION
    # This is for one tube, and it's all we need since they're in //
    f = Find_f(Re_tube)
    dP_tube = f*(L/d_inner)*0.5*rho_water*v_tube**2
    
    # dP FROM NOZZLE
    # Assume one dynamic head (x2 for 2 nozzles)
    dP_nozzle = 2*0.5*rho_water*v_nozzle_h**2
    
    # dP FROM ENTRY/EXIT
    # In-Out Pressure Head
    dP_inout = 0.5*rho_water*(v_tube**2)*(Kc+Ke)
    
    return(dP_tube+dP_nozzle+dP_inout)

def give_Re_tube(m_dot_h):
    """Does what is says on the tin"""
    # Calculate tube velocity
    m_dot_tube = m_dot_h / N_tube
    v_tube = m_dot_tube / (rho_water * np.pi * 0.25 * d_inner**2)
    # Calculate Re for tubes
    Re_tube = (v_tube*rho_water*d_inner)/mu
    
    return Re_tube

"""
COLD STREAM CALCULATIONS
"""

def give_A_sh():
    """Gives A_sh. Defined inits own function as this is something that could be tweaked as we improve A_sh"""
    
    # Calculate A_sh 
    """NOTE this is something to revisit since some debate about whether its accurate"""
    # Using Eq 6 from notes:
    A_sh = (D_inner / Y) * (Y - d_outer) * B
    # Try our own A_sh (1)
    """UNFINISHED Takes the busiest row of tubes and calculates the gap area looking down - this will only work for single shell..."""
    # A_sh = 
    
    return(A_sh)

def total_dP_cold(m_dot_c):
    """Given mass flowrate, calculates velocities and Re
    (assumes some design variables)
    THEN
    Sums pressure drops in the shell:
        1. Drop across shell
        2. Drop across nozzle
    NOTE that in future we may like to look at bends
    """
    
    # Calculate A_sh
    A_sh = give_A_sh()
    
    # Calculate v_sh
    v_sh = m_dot_c / (rho_water*A_sh)
    
    # Calculate Re_sh
    Re_sh = (v_sh * A_sh * rho_water) / mu
    
    #calculate v_nozzle cold
    v_nozzle_c = m_dot_c / (rho_water * 0.25 * d_nozzle**2 *np.pi)
    
    # dP FROM SHELL
    # Equation 9 from notes - NOTE DUBIOUS
    dP_shell = 4 * a * Re_sh**(-0.15) * N_row * rho_water * v_sh**2
    
    # dP FROM NOZZLE
    # Assume one dynamic head (x2 for 2 nozzles)
    dP_nozzle = 2*0.5*rho_water*v_nozzle_c**2
    
    return(dP_nozzle + dP_shell)

def give_Re_sh(m_dot_c):
    """What the name says..."""
    
    A_sh = give_A_sh()
    
    # Calculate v_sh
    v_sh = m_dot_c / (rho_water*A_sh)
    
    # Calculate Re_sh
    Re_sh = (v_sh * A_sh * rho_water) / mu
    
    return(Re_sh)
    
"""
ITERATION & PLOTTING
"""
    

def hydraulic_plot_h():
    """Plots dP-massflowrate curves from both the given characteristics and the calculations for hot flow"""
    
    # Starts mass flowrate at 0
    m_dot = 0
    
    m_dots = []
    dp_graph = []
    dp_calc = []
    
    for i in range (125):
        
        m_dot += 0.005
        m_dots.append(m_dot)
        dp_calc.append(total_dP_hot(m_dot))
        dp_graph.append(dp_flowrate(m_dot,"hot"))
    
    plt.plot(m_dots,dp_graph,label = "from fig.6 graph")
    plt.plot(m_dots,dp_calc,label = "from calculations")
    plt.xlabel("mass flowrate (prop to flowrate)")
    plt.ylabel("pressure drop (Pa)")
    plt.grid()
    plt.title("Hot Flow")
    plt.legend()
    plt.axis()
    plt.show()
    
    return(m_dot)

def hydraulic_plot_c():
    """Plots dP-massflowrate curves from both the given characteristics and the calculations for hot flow"""
    
    # Starts mass flowrate at 0
    m_dot = 0
    
    m_dots = []
    dp_graph = []
    dp_calc = []
    
    for i in range (160):
        
        m_dot += 0.005
        m_dots.append(m_dot)
        dp_calc.append(total_dP_cold(m_dot))
        dp_graph.append(dp_flowrate(m_dot,"cold"))
    
    plt.plot(m_dots,dp_graph,label = "from fig.6 graph")
    plt.plot(m_dots,dp_calc,label = "from calculations")
    plt.xlabel("mass flowrate (prop to flowrate)")
    plt.ylabel("pressure drop (Pa)")
    plt.grid()
    plt.title("Cold Flow")
    plt.legend()
    plt.axis()
    plt.show()
    
    return(m_dot)


def iterate_c():
    """Iterates to find the massflowrate of hot flow"""
    
    # Starts mass flowrate at 0
    m_dot = 0
    m_dot_final = 0
    difference = 100000
    
    for i in range (160):
        
        m_dot += 0.005
        if abs(total_dP_cold(m_dot)-dp_flowrate(m_dot,"cold")) < difference:
            difference = abs(total_dP_cold(m_dot)-dp_flowrate(m_dot,"cold"))
            m_dot_final = m_dot
            
    return(m_dot_final)

def iterate_h():
    """Iterates to find the massflowrate of hot flow"""
    
    # Starts mass flowrate at 0
    m_dot = 0
    m_dot_final = 0
    difference = 100000
    
    for i in range (125):
        
        m_dot += 0.005
        if abs(total_dP_hot(m_dot)-dp_flowrate(m_dot,"hot")) < difference:
            difference = abs(total_dP_hot(m_dot)-dp_flowrate(m_dot,"hot"))
            m_dot_final = m_dot
            
    return(m_dot_final)
    
# Define everything that it needs
"""
Testing for the sake of GitKraken

rho_water = 1000
mu = 0.000651
d_inner = 0.006
d_outer = 0.008
d_nozzle = 0.02
Y = 0.014
D_inner = 0.064
a = 0.34
L = 0.35
B = 0.035
N_tube = 12
N_row = 6



hydraulic_plot_h()
print(iterate_h())
hydraulic_plot_c()
print(iterate_c())
"""
   
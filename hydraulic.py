# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:44:10 2020

@author: Tomos
"""

import numpy as np
import matplotlib.pyplot as plt
from Definitions import *
import parametric as para

"""
Start by defining the Characteristic dP-massflowrate relationship from graphs
"""

def dp_flowrate(m_dot,temp,year):
    """Uses a dP-Flowrate data curve-fit for hot and cold to determine the pressure drop from the mass flow rate
    NOTE: Doesn't tell you if the flowrate is beyond what we can expect to work at all!!!"""
    
    # Calculate flowrate in L/s 
    Q = (m_dot / rho_water) * 1000
    
    # 2019 or 2020 values
    
    if year == 2020 or year == 2019:
    
        # if Cold
        if temp == "cold":
            dP = -1.07*Q**2 + 0.0995*Q + 0.584
        
        # if Hot
        else:
            dP = -0.52*Q**2 - 0.769*Q + 0.677
            
        # dP in Pa not bar
        dP *= 100000
        
    elif year == 2018:
        
        # if Cold
        if temp == "cold":
            dP = -0.594*Q**2 - 1.37*Q + 0.833
        
        # if Hot
        else:
            dP = -1.31*Q**2 - 0.553*Q + 0.691
            
        # dP in Pa not bar
        dP *= 100000
      
    # 2017!!
    else:

        # if Cold
        if temp == "cold":
            dP = -3.35*Q**2 + 0.159*Q + 0.816
        
        # if Hot
        else:
            dP = -1.18*Q**2 - 0.597*Q + 0.638
            
        # dP in Pa not bar
        dP *= 100000
    
    return(dP)
    
"""
HOT STREAM CALCULATIONS
"""

def Find_sigma(geometry):
    """Returns sigma, the ratio of free area
    geometric parameters defined externally"""
    
    # Define design variable
    N_tube = para.N_tube(geometry)
    N_pass = geometry.get('N_pass')
    
    numerator = 0.25 * np.pi * (N_tube/N_pass) * d_inner**2
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
def total_dP_hot(m_dot_h,geometry,K_turn=1,K_nozzle=1):
    """Given massflowrate, Calculates velocities, Re and Kc, Ke 
    (assumes design variables D_inner,d_inner,N_tube set elsewhere)
    THEN
    Sums pressure drop (Pa) in tubes as the sum of:
        1. Friction in tubes
        2. Entry and Exit losses (assuming infinite Re)
        3. Nozzle losses"""
    
    # Define design variables
    N_tube = para.N_tube(geometry)
    N_pass = geometry.get('N_pass')
    L = geometry.get('L')
    
    # Calculate tube velocity
    m_dot_tube = m_dot_h / (N_tube / N_pass)
    v_tube = m_dot_tube / (rho_water * np.pi * 0.25 * d_inner**2)
    
    # Calculate nozzle velocity
    v_nozzle_h = m_dot_h / (rho_water * np.pi * 0.25 * d_nozzle**2)
    
    # Calculate Re for tubes
    Re_tube = (v_tube*rho_water*d_inner)/mu
    
    # Re assumed infinite by nozzle (from Friday 8/5/20 MS Teams call)
    
    # Calculate Ke, Kc assuming infinite Re
    sigma = Find_sigma(geometry)
    Kc = Find_Kc(sigma)
    Ke = Find_Ke(sigma)
    
    
    """dP FROM TUBE FRICTION"""
    # This is for one tube, and it's all we need in 1-pass since they're in //
    f = Find_f(Re_tube)
    dP_tube = f*(L/d_inner)*0.5*rho_water*v_tube**2
    # Times the number of passes
    dP_tube *= N_pass
    
    """dP FROM NOZZLE"""
    # Assume one dynamic head (x2 for 2 nozzles)
    dP_nozzle = 2*0.5*K_nozzle*rho_water*v_nozzle_h**2
    
    """dP FROM ENTRY/EXIT"""
    # In-Out Pressure Head
    dP_inout = 0.5*rho_water*(v_tube**2)*(Kc+Ke)
    # Generalise for multiple passes
    dP_inout *= N_pass

    """dP FROM TURN - atm only 180 degree turns between passes"""
    v_turn = m_dot_tube / (rho_water * (N_tube/N_pass) * np.pi * 0.25 * d_inner**2)
    dP_turn = 0.5*rho_water*(v_turn**2)*K_turn
    # Times number of passes - 1
    dP_turn *= (N_pass-1)
    
    return(dP_tube + dP_nozzle + dP_inout + dP_turn)

def give_Re_tube(m_dot_h,geometry):
    """Does what is says on the tin"""
    # Define design variables
    N_tube = para.N_tube(geometry)
    N_pass = geometry.get('N_pass')
    
    # Calculate tube velocity
    # (generalised for N_pass)
    m_dot_tube = m_dot_h / (N_tube / N_pass)
    v_tube = m_dot_tube / (rho_water * np.pi * 0.25 * d_inner**2)
    
    # Calculate Re for tubes
    Re_tube = (v_tube*rho_water*d_inner)/mu
    
    return Re_tube

"""
COLD STREAM CALCULATIONS
"""

def give_A_sh(geometry):
    """Gives A_sh. Defined in its own function as this is something that could be tweaked as we improve A_sh"""
    
    # Define design variables
    Y = geometry.get('Y')
    B = para.B(geometry)
    
    # Calculate A_sh 
    """NOTE this is something to revisit since some debate about whether its accurate"""
    # Using Eq 6 from notes:
    A_sh = (D_inner / Y) * (Y - d_outer) * B
    # Try our own A_sh (1)
    """UNFINISHED Takes the busiest row of tubes and calculates the gap area looking down - this will only work for single shell..."""
    # A_sh = 
    
    return(A_sh)

def total_dP_cold(m_dot_c,geometry,K_baffle_bend=1,K_nozzle=1):
    """Given mass flowrate, calculates velocities and Re
    (assumes some design variables)
    THEN
    Sums pressure drops in the shell:
        1. Drop across shell
        2. Drop across nozzle
    NOTE that in future we may like to look at bends!!!
    """
    # Define design variables
    N_row = para.N_row(geometry)
    a = para.a(geometry)
    N_baffle = geometry.get('N_baffle')
    N_shell = geometry.get('N_shell')
    
    # Calculate A_sh
    A_sh = give_A_sh(geometry)
    
    # Calculate v_sh
    v_sh = m_dot_c / (rho_water*A_sh)
    
    # Calculate Re_sh
    Re_sh = (v_sh * d_outer * rho_water) / mu
    
    #calculate v_nozzle cold
    v_nozzle_c = m_dot_c / (rho_water * 0.25 * d_nozzle**2 *np.pi)
    
    """dP FROM SHELL BUNDLE PASSES"""
    # Equation 9 from notes - NOTE DUBIOUS
    #ALSO INITIALLY I HAD THIS AS FOR THE WHOLE THING, BUT ISN'T IT PER PASS OF BUNDLES?
    dP_shell = 4 * a * Re_sh**(-0.15) * N_row * rho_water * v_sh**2
    # Multiply by number of passes in a shell
    dP_shell *= (N_baffle + 1) 
    # Multiply by number of shells
    # Note when N_row is used that N_shell has no effect since N_row is per shell
    dP_shell *= N_shell
    
    """dP FROM BAFFLE BENDS"""
    # One baffle bend
    dP_bends = K_baffle_bend* 0.5*rho_water*v_sh**2
    # One shell's worth of baffle bends
    dP_bends *= N_baffle
    # Total baffle bends
    dP_bends *= N_shell
    
    """dP FROM NOZZLE"""
    dP_nozzle = 0.5*K_nozzle*rho_water*v_nozzle_c**2
    # Two Nozzles
    dP_nozzle *= 2
    
    return(dP_nozzle + dP_shell + dP_bends)

def give_Re_sh(m_dot_c,geometry):
    """What the name says..."""
    
    A_sh = give_A_sh(geometry)
    
    # Calculate v_sh
    v_sh = m_dot_c / (rho_water*A_sh)
    
    # Calculate Re_sh
    Re_sh = (v_sh * d_outer * rho_water) / mu
    
    return(Re_sh)
    
"""
ITERATION & PLOTTING
"""
    

def hydraulic_plot_h(geometry,year,K_turn=1,K_nozzle=1):
    """Plots dP-massflowrate curves from both the given characteristics and the calculations for hot flow"""
    
    # Starts mass flowrate at 0
    m_dot = 0
    
    m_dots = []
    dp_graph = []
    dp_calc = []
    
    for i in range (125):
        
        m_dot += 0.005
        m_dots.append(m_dot)
        dp_calc.append(total_dP_hot(m_dot,geometry,K_turn,K_nozzle))
        dp_graph.append(dp_flowrate(m_dot,"hot",year))
    
    plt.plot(m_dots,dp_graph,label = "from pump characteristics")
    plt.plot(m_dots,dp_calc,label = "from calculations")
    plt.xlabel("mass flowrate (prop to flowrate)")
    plt.ylabel("pressure drop (Pa)")
    plt.grid()
    plt.title("Hot Flow")
    plt.legend()
    plt.axis()
    plt.show()
    
    return(m_dot)

def hydraulic_plot_c(geometry,year,K_baffle_bend=1,K_nozzle=1):
    """Plots dP-massflowrate curves from both the given characteristics and the calculations for hot flow"""
    
    # Starts mass flowrate at 0
    m_dot = 0
    
    m_dots = []
    dp_graph = []
    dp_calc = []
    
    for i in range (160):
        
        m_dot += 0.005
        m_dots.append(m_dot)
        dp_calc.append(total_dP_cold(m_dot,geometry,K_baffle_bend,K_nozzle))
        dp_graph.append(dp_flowrate(m_dot,"cold",year))
    
    plt.plot(m_dots,dp_graph,label = "from pump characteristics")
    plt.plot(m_dots,dp_calc,label = "from calculations")
    plt.xlabel("mass flowrate (prop to flowrate)")
    plt.ylabel("pressure drop (Pa)")
    plt.grid()
    plt.title("Cold Flow")
    plt.legend()
    plt.axis()
    plt.show()
    
    return(m_dot)


def iterate_c(geometry,year,K_baffle_bend=1,K_nozzle=1):
    """Iterates to find the massflowrate of cold flow"""
    # NOTE - I've had this give same ans for 1-2 Baffles?
    
    # Starts mass flowrate at 0
    m_dot = 0
    m_dot_final = 0
    difference = 100000
    
    for i in range (1600):
        
        m_dot += 0.0005
        if abs(total_dP_cold(m_dot,geometry,K_baffle_bend,K_nozzle)-dp_flowrate(m_dot,"cold",year)) < difference:
            difference = abs(total_dP_cold(m_dot,geometry,K_baffle_bend,K_nozzle)-dp_flowrate(m_dot,"cold",year))
            m_dot_final = m_dot
            
    return(m_dot_final)

def iterate_h(geometry,year,K_turn=1,K_nozzle=1):
    """Iterates to find the massflowrate of hot flow"""
    
    # Starts mass flowrate at 0
    m_dot = 0
    m_dot_final = 0
    difference = 100000
    
    for i in range (1250):
        
        m_dot += 0.0005
        if abs(total_dP_hot(m_dot,geometry,K_turn,K_nozzle)-dp_flowrate(m_dot,"hot",year)) < difference:
            difference = abs(total_dP_hot(m_dot,geometry,K_turn,K_nozzle)-dp_flowrate(m_dot,"hot",year))
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
   
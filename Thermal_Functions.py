# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:02:05 2020

@author: Tomos
"""

import numpy as np
from Definitions import *
import parametric as para
import hydraulic



"""_________________________________________________________________________________________________________"""
"""___________________________________Thermal Function Definitions__________________________________________"""
"""_________________________________________________________________________________________________________"""


"""___________________________________________LMTD Method___________________________________________________"""
"""_________________________________________________________________________________________________________"""

# The following functions relate to the LMTD method to find the heat transfer through iteration of outlet temperatures.

"""____________LMTD Method: INTERNAL Functions: functions to be used by other thermal functions_____________"""

def evaluate_c(geometry):
    if geometry.get('pitch_type') == "square":
        return 0.15
    else:
        return 0.2


def f_Nu_inner(Re_inner, Pr):
    Nu_inner = 0.023 * (Re_inner**0.8) * (Pr**0.3)
    return Nu_inner


def f_h_inner(lambda_water, d_inner, Nu_inner):
    h_inner = (Nu_inner * lambda_water) / d_inner
    return h_inner


def f_Nu_outer(Re_outer, Pr, c):
    Nu_outer = c * (Re_outer**0.6) * (Pr**0.3)
    return Nu_outer


def f_h_outer(lambda_water, d_outer, Nu_outer):
    h_outer = (Nu_outer * lambda_water) / d_outer
    return h_outer


def f_U(h_inner, h_outer, d_inner, d_outer, lambda_tube):
    U = (1/h_inner + d_inner*np.log(d_outer/d_inner)/(2*lambda_tube) + d_inner/(d_outer * h_outer) + Rf)**-1
    return U


def f_Q_dot_cold(m_dot_c, cp, T_in_cold, T_out_cold):
    Q_dot_cold = m_dot_c * cp * (T_out_cold - T_in_cold)
    return Q_dot_cold


def f_Q_dot_hot(m_dot_h, cp, T_in_hot, T_out_hot):
    Q_dot_hot = m_dot_h * cp * (T_in_hot - T_out_hot)
    return Q_dot_hot


def f_dTlm(T_in_hot, T_out_hot, T_in_cold, T_out_cold):
    if (T_in_hot - T_out_cold) / (T_out_hot - T_in_cold) == 1:
        T_out_cold -= 0.01
        print('IT HAPPENED!!!')
    if T_in_hot - T_out_cold == 0:
        T_out_cold -= 0.01
        print('THE OTHER ONE HAPPENED!!!')
    dTlm = ((T_in_hot - T_out_cold) - (T_out_hot - T_in_cold)) / np.log((T_in_hot - T_out_cold) / (T_out_hot - T_in_cold))
    return dTlm


def f_Q_dot_temp(U, A, F, dTlm):
    Q_dot_temp = U * A * F * dTlm
    return Q_dot_temp


def f_T_out_cold(Q_dot_cold, m_dot_c, cp, T_in_cold):
    T_out_cold = Q_dot_cold / (m_dot_c * cp) + T_in_cold
    return T_out_cold


def f_T_out_hot(Q_dot_hot, m_dot_h, cp, T_in_hot):
    T_out_hot = T_in_hot - Q_dot_hot / (m_dot_h * cp)
    return T_out_hot

def f_F(T_in_cold, T_out_cold, T_in_hot, T_out_hot, geometry):

    if geometry.get('N_shell')==1 and geometry.get('N_pass')==1:
        F=1
        return F

    else:

        #     dTlm = ((T_in_hot - T_out_cold) - (T_out_hot - T_in_cold)) / np.log((T_in_hot - T_out_cold) / (T_out_hot - T_in_cold))
        dT1 = T_in_hot - T_out_cold
        dT2 = T_out_hot - T_in_cold
        # T1 = T_in_hot
        # T2 = T_out_hot
        # t1 = T_in_cold
        # t2 = T_out_cold

        P1 = (T_out_hot - T_in_hot) / (T_in_cold - T_in_hot)
        R1 = (T_in_cold - T_out_cold) / (T_out_hot - T_in_hot)

        S = (R1**2 + 1)**0.5 / (R1 -1)
        W = ((1 - P1*R1) / (1-P1))**(1/geometry.get('N_shell'))

        F = S * np.log(W) / np.log((1 + W - S + S*W)/(1 + W + S - S*W))

        return F

"""_____________________LMTD Method: ITERATION to Determine T_out_cold and T_out_hot___________________________"""

    #F_Q(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry)
def iterate_thermal(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry):

    # These variables will not change during the iteration - Design Point Dependent Constants - Pass into
    # iterate_hydraulic():
    Nu_inner = f_Nu_inner(Re_inner, Pr)
    h_inner = f_h_inner(lambda_water, d_inner, Nu_inner)
    
    # Design Variable - Affected
    c = evaluate_c(geometry)
    A = para.A(geometry)
#    F = para.F(geometry)

    # Affected in turn by the above...
    Nu_outer = f_Nu_outer(Re_outer, Pr, c)
    # And in turn affected by the above...
    h_outer = f_h_outer(lambda_water, d_outer, Nu_outer)
    U = f_U(h_inner, h_outer, d_inner, d_outer, lambda_tube)
    
    # Initialisation: these values serve as initial guess to iterate from
    T_out_hot_init = 305
    T_out_cold_init = 295

    T_out_hot = T_out_hot_init
    T_out_cold = T_out_cold_init

    # These variables will change during the iteration.
    F = f_F(T_in_cold, T_out_cold, T_in_hot, T_out_hot, geometry)
    Q_dot_cold = f_Q_dot_cold(m_dot_c, cp, T_in_cold, T_out_cold)
    Q_dot_hot = f_Q_dot_hot(m_dot_h, cp, T_in_hot, T_out_hot)
    dTlm = f_dTlm(T_in_hot, T_out_hot, T_in_cold, T_out_cold)
    Q_dot_temp = f_Q_dot_temp(U, A, F, dTlm)

    i = 0

    while i < 100:

        if i%10==0:
            """
            print("Q_dot_cold:", round(Q_dot_cold, 1), "Q_dot_hot:", round(Q_dot_hot, 1), "Q_dot_temp:",
                  round(Q_dot_temp, 0),
                  "__", "T_out_cold:", round(T_out_cold, 5), "T_out_hot:", round(T_out_hot, 5), "__", "T_in_cold:",
                  T_in_cold,
                  "T_in_hot:", T_in_hot)
            """
        Q_dot_cold = Q_dot_temp
        Q_dot_hot = Q_dot_temp

        T_out_cold = f_T_out_cold(Q_dot_cold, m_dot_c, cp, T_in_cold)
        T_out_hot = f_T_out_hot(Q_dot_hot, m_dot_h, cp, T_in_hot)

        """
        if T_out_hot > 333.15 or T_out_hot < 294.15:
            print("T_out_hot out of range")
            break

        if T_out_cold > 333.15 or T_out_cold < 294.15:
            print("T_out_cold out of range")
            break
        """

        F = f_F(T_in_cold, T_out_cold, T_in_hot, T_out_hot, geometry)
        dTlm = f_dTlm(T_in_hot, T_out_hot, T_in_cold, T_out_cold)

        Q_dot_temp = f_Q_dot_temp(U, A, F, dTlm)

        i += 1

    Results = {'Q_dot_cold': Q_dot_cold, 'Q_dot_hot': Q_dot_hot, 'Q_dot_temp': Q_dot_temp, 'T_out_cold': T_out_cold,
               'T_out_hot': T_out_hot, 'dTlm': dTlm, 'T_out_cold_init ': T_out_cold_init, 'T_out_hot_init': T_out_hot_init}

    """
    print("Worked Solution")
    print("Q_dot_cold:", round(8221.2, 1), "Q_dot_hot:", round(8221.2, 1), "Q_dot_temp:", round(8221.2, 0),
      "__", "T_out_cold:", round(273.15 + 23.93, 1), "T_out_hot:", round(273.15 + 55.42, 1), "__", "T_in_cold:",
      T_in_cold, "T_in_hot:", T_in_hot)
    """

    return Results

"""_____________________LMTD Method: EXTERNAL Functions: functions to be used in main_________________________"""

def F_Q_LMTD(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry):
    results = iterate_thermal(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry)
    # Give average of heat rates
    Q = (results['Q_dot_cold'] + results['Q_dot_hot'] + results['Q_dot_temp']) / 3
    return Q


def F_T_out_cold(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry):
    results = iterate_thermal(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry)
    return results['T_out_cold']


def F_T_out_hot(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry):
    results = iterate_thermal(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry)
    return results['T_out_hot']


def F_E_LMTD(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry):

    if m_dot_h > m_dot_c:
        m_dot = m_dot_c
    else:
        m_dot = m_dot_h

    E = F_Q_LMTD(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry) / (m_dot * cp * (T_in_hot - T_in_cold))

    return E




"""_____________________________________________E-NTU Method________________________________________________"""
"""_________________________________________________________________________________________________________"""

# The following functions relate to the E-NTU method which is a method of obtaining the heat transfer by first
# first determining the heat exchanger effectiveness, E.

"""_____________________________________E-NTU Method: INTERNAL Functions____________________________________"""

def f_C_min(m_dot_c, m_dot_h):
# Returns the minimum heat capacity
    if m_dot_h > m_dot_c:
       C_min = m_dot_c * cp
    else:
        C_min = m_dot_h * cp
    return C_min


def f_C_max(m_dot_c, m_dot_h):
# Returns the maximum heat capacity
    if m_dot_h < m_dot_c:
       C_max = m_dot_c * cp
    else:
        C_max = m_dot_h * cp
    return C_max


def f_E_NTU_p(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry):
# Returns the effectiveness for a single shell pass through the NTU method

    Nu_inner = f_Nu_inner(Re_inner, Pr)
    h_inner = f_h_inner(lambda_water, d_inner, Nu_inner)

    # Design Variable - Affected
    c = evaluate_c(geometry)
    A = para.A(geometry)

    # Affected in turn by the above...
    Nu_outer = f_Nu_outer(Re_outer, Pr, c)
    # And in turn affected by the above...
    h_outer = f_h_outer(lambda_water, d_outer, Nu_outer)
    U = f_U(h_inner, h_outer, d_inner, d_outer, lambda_tube)

    C_min = f_C_min(m_dot_c, m_dot_h)
    C_max = f_C_max(m_dot_c, m_dot_h)

    C = C_min / C_max

    NTU = U * A / C_min

    E = 2 * (1 + C + ((1+C**2)**0.5) * (1 + np.exp(-NTU*(1 + C**2)**0.5))/(1 - np.exp(-NTU*(1 + C**2)**0.5)))**-1

    return E


"""_____________________________________E-NTU Method: EXTERNAL Functions___________________________________"""


def F_E_NTU(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry):
# Returns the effectiveness through NTU method
# FUNCTION INCOMPLETE: need a way to determine E_p, the effectiveness per shell pass inorder to be able to generalise
# to multiple shell passes.

    Nu_inner = f_Nu_inner(Re_inner, Pr)
    h_inner = f_h_inner(lambda_water, d_inner, Nu_inner)

    # Design Variable - Affected
    c = evaluate_c(geometry)
    A = para.A(geometry)

    # Affected in turn by the above...
    Nu_outer = f_Nu_outer(Re_outer, Pr, c)
    # And in turn affected by the above...
    h_outer = f_h_outer(lambda_water, d_outer, Nu_outer)
    U = f_U(h_inner, h_outer, d_inner, d_outer, lambda_tube)

    C_min = f_C_min(m_dot_c, m_dot_h)
    C_max = f_C_max(m_dot_c, m_dot_h)

    N_shell = geometry.get('N_shell')
    C = C_min / C_max

    NTU = U * A / C_min

    E_p = f_E_NTU_p(m_dot_c, m_dot_h, Re_inner, Re_outer, geometry)
    """
    if N_shell ==1:
    # if there is one shell then just return the result from f_E_NTU_p
        E = E_p

    else:
        
        if C == 1:
            E = (N_shell * E_p) / (1 + (N_shell - 1) * E_p)

        elif C == 0:
            E = 1 - np.exp(-NTU)

        else:
            # E = ((((1 - E_p * C)/(1 - E_p))**N_shell)-1)/((((1 - E_p * C)/(1 - E_p))**N_shell) - C)       # Holman equation (returns rubbish, need to investigate)
            E = (1 - np.exp(-NTU * (1 - C)))/(1 - C * np.exp(-NTU * (1 - C)))                               # 3A6 Notes: Counter flow, works very nicely
        """
    E = (1 - np.exp(-NTU * (1 - C))) / (1 - C * np.exp(-NTU * (1 - C)))                                     # This uses the equation from 3A6 Notes always.
    return E


def F_Q_NTU(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry):
    E = F_E_NTU(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry)

    if m_dot_h > m_dot_c:
        T_out_cold = T_in_cold + E * (T_in_hot - T_in_cold)
        Q = m_dot_c * cp * (T_out_cold - T_in_cold)
    else:
        T_out_hot = T_in_hot - E * (T_in_hot - T_in_cold)
        Q = m_dot_h * cp * (T_in_hot - T_out_hot)

    return Q

def Q(geometry, year, method="LMTD"):
    """Calculates Q"""
    m_dot_c = hydraulic.iterate_c(geometry, year)
    m_dot_h = hydraulic.iterate_h(geometry, year)
    Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
    Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)
    if method=="LMTD":
        Qval = F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry)
    else:
        Qval = F_Q_NTU(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry)
    return Qval
        
    
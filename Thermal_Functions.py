# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:02:05 2020

@author: Tomos
"""

import numpy as np
from Definitions import *
import parametric as para



"""_________________________________________________________________________________________________________"""
"""___________________________________Thermal Function Definitions__________________________________________"""
"""_________________________________________________________________________________________________________"""

"""___________________Internal Functions: functions to be used by other thermal functions___________________"""

def evaluate_c(pitch_type):
    if pitch_type == "triangle":
        return 0.2
    else:
        return 0.15


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



"""___________________________Iteration to Determine T_out_cold and T_out_hot_______________________________"""

def iterate_hydraulic(m_dot_c, m_dot_h, Re_inner, Re_outer):

    # These variables will not change during the iteration - Design Point Dependent Constants - Pass into
    # iterate_hydraulic():
    c = evaluate_c(pitch_type)
    Nu_inner = f_Nu_inner(Re_inner, Pr)
    h_inner = f_h_inner(lambda_water, d_inner, Nu_inner)
    Nu_outer = f_Nu_outer(Re_outer, Pr, c)
    h_outer = f_h_outer(lambda_water, d_outer, Nu_outer)
    U = f_U(h_inner, h_outer, d_inner, d_outer, lambda_tube)

    # Initialisation: these values serve as initial guess to iterate from
    T_out_hot_init = 315
    T_out_cold_init = 285

    T_out_hot = T_out_hot_init
    T_out_cold = T_out_cold_init

    # These variables will change during the iteration.

    Q_dot_cold = f_Q_dot_cold(m_dot_c, cp, T_in_cold, T_out_cold)
    Q_dot_hot = f_Q_dot_hot(m_dot_h, cp, T_in_hot, T_out_hot)
    dTlm = f_dTlm(T_in_hot, T_out_hot, T_in_cold, T_out_cold)
    Q_dot_temp = f_Q_dot_temp(U, A, F, dTlm)

    i = 0

    while i < 1000:
        """
        if i%100==0:

            print("Q_dot_cold:", round(Q_dot_cold, 1), "Q_dot_hot:", round(Q_dot_hot, 1), "Q_dot_temp:",
                  round(Q_dot_temp, 0),
                  "__", "T_out_cold:", round(T_out_cold, 5), "T_out_hot:", round(T_out_hot, 5), "__", "T_in_cold:",
                  T_in_cold,
                  "T_in_hot:", T_in_hot)
         """
        Q_dot_cold = (0.5 * Q_dot_temp + 0.5 * Q_dot_cold)
        Q_dot_hot = (0.5 * Q_dot_temp + 0.5 * Q_dot_hot)

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


"""_______________________________External Functions: functions to be used in main___________________________"""

def F_Q(m_dot_c, m_dot_h, Re_inner, Re_outer):
    results = iterate_hydraulic(m_dot_c, m_dot_h, Re_inner, Re_outer)
    # Give average of heat rates
    Q = (results['Q_dot_cold'] + results['Q_dot_hot'] + results['Q_dot_temp']) / 3
    return Q


def F_T_out_cold(m_dot_c, m_dot_h, Re_inner, Re_outer):
    results = iterate_hydraulic(m_dot_c, m_dot_h, Re_inner, Re_outer)
    return results['T_out_cold']


def F_T_out_hot(m_dot_c, m_dot_h, Re_inner, Re_outer):
    results = iterate_hydraulic(m_dot_c, m_dot_h, Re_inner, Re_outer)
    return results['T_out_hot']


def F_E(m_dot_c, m_dot_h, Re_inner, Re_outer):

    if m_dot_h > m_dot_c:
        m_dot = m_dot_c
    else:
        m_dot = m_dot_h

    E = F_Q(m_dot_c, m_dot_h, Re_inner, Re_outer) / (m_dot * cp * (T_in_hot - T_in_cold))

    return E











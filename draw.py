# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:09:23 2020

@author: Tomos
"""

import matplotlib.pyplot as plt
from Definitions import *

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
    



# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:16:20 2020
THIS FILE WILL OPTIMISE THE DEISGN
@author: Tomos
"""
import numpy as np
import hydraulic
import Thermal_Functions as thermal
import geometric as geom
import matplotlib.pyplot as plt

#def generate_bundle_arrays(row_max=6, col_max=6):
#    """Generates an exhaustive list of bundle_array configurations, including zeroes
#    NOTE: The maximum col_max is actually 6 as this is written
#    NOTE: This is not a good way to do anything, Tomos - Tomos"""
#    
#    bundle_array_range = []
#    
#    for i in range(row_max+1):
#        bundle_array_range.append([i])
#    if col_max>1:
#        for i in range(row_max+1):
#            for j in range(row_max+1):
#                bundle_array_range.append([i,j])
#    if col_max>2:
#        for i in range(row_max+1):
#            for j in range(row_max+1):
#                for k in range(row_max+1):
#                    bundle_array_range.append([i,j,k])
#    if col_max>3:
#        for i in range(row_max+1):
#            for j in range(row_max+1):
#                for k in range(row_max+1):
#                    for l in range(row_max+1):
#                        bundle_array_range.append([i,j,k,l])
#    if col_max>4:
#        for i in range(row_max+1):
#            for j in range(row_max+1):
#                for k in range(row_max+1):
#                    for l in range(row_max+1):
#                        for m in range(row_max+1):
#                            bundle_array_range.append([i,j,k,l,m])
#    if col_max>5:
#        for i in range(row_max+1):
#            for j in range(row_max+1):
#                for k in range(row_max+1):
#                    for l in range(row_max+1):
#                        for m in range(row_max+1):
#                            for n in range(row_max+1):
#                                bundle_array_range.append([i,j,k,l,m,n])
#    
#    return(bundle_array_range)

def optimise_design():
    """The magic!"""
    
    # Define minima and maxima of the iteration...
    L_range = np.linspace(0.10,0.20,11)
    Y_range = np.linspace(0.009,0.015,7)
    N_baffle_range = np.linspace(0,15,16)
    pitch_type_array = ["square","triangle"]
    N_shell_array = [1,2]
    N_pass_array = [1,2,4]
    
    bundle_array_array = []
    bundle_array_array.append([1,3,5,3,1])
    bundle_array_array.append([3,3,3,3])
    bundle_array_array.append([2,5,2])
    bundle_array_array.append([3,5,5,5,3])
    bundle_array_array.append([2,3,4,3,2])
    bundle_array_array.append([3,5,5,5,5,3])
    bundle_array_array.append([2,4,6,6,4,2])
    bundle_array_array.append([2,4,4,4,4,2])
    bundle_array_array.append([4,5,6,5,4])

    # define some constant designs
    L_header = 0.025
    breadth_gap = 0.01
    
    geometry = {'L_header': L_header,'breadth_gap':breadth_gap}
    optimal_geometry = geometry
    
    # Set the Q to beat
    Q_max = 0
    count = 0
    
    for N_shell in N_shell_array:
        
        # Set pitch_type
        geometry['N_shell']=N_shell
        
        for N_pass in N_pass_array:
            
            # Set pitch_type
            geometry['N_pass']=N_pass
            
            for pitch_type in pitch_type_array:
                
                print("{}/12 way there!".format(count))
                count += 1
                
                # Set pitch_type
                geometry['pitch_type']=pitch_type
                
                for bundle_array in bundle_array_array:
                    
                    # Set bundle_array
                    geometry['bundle_array']=bundle_array
                
                    for L in L_range:
                        
                        # Set L
                        geometry['L']=L
                        
                        for Y in Y_range:
                            
                            # Set Y
                            geometry['Y']=Y
                            
                            for N_baffle in N_baffle_range:
                                
                                # Set N_baffle
                                geometry['N_baffle']=N_baffle
                                
                                if geom.check_constraints(geometry)==True:
                                
                                    # Find values
                                    m_dot_c = hydraulic.iterate_c(geometry)
                                    m_dot_h = hydraulic.iterate_h(geometry)
                                    Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
                                    Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)
                                    
                                    # Save values if they give the highest Q yet
                                    if thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry) > Q_max:
                                        
                                        # This is the new best design
                                        Q_max = thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry)
                                        
                                        # Save new optimal geometry
                                        optimal_N_baffle=N_baffle
                                        optimal_Y=Y
                                        optimal_L=L
                                        optimal_bundle_array = bundle_array
                                        optimal_pitch_type = pitch_type
                                        optimal_N_pass = N_pass
                                        optimal_N_shell = N_shell
                                        
                                else:
                                    pass
                
    optimal_geometry['L']=optimal_L
    optimal_geometry['Y']=optimal_Y
    optimal_geometry['N_baffle']=optimal_N_baffle
    optimal_geometry['bundle_array']=optimal_bundle_array
    optimal_geometry['pitch_type']=optimal_pitch_type
    optimal_geometry['N_shell']=optimal_N_shell
    optimal_geometry['N_pass']=optimal_N_pass

    m_dot_c = hydraulic.iterate_c(optimal_geometry)   
    m_dot_h = hydraulic.iterate_h(optimal_geometry)

    NTU_Q = thermal.F_Q_LMTD(m_dot_c, m_dot_h, hydraulic.give_Re_tube(m_dot_h,optimal_geometry), hydraulic.give_Re_sh(m_dot_c,optimal_geometry), optimal_geometry)
    
    return([Q_max,optimal_geometry.get('N_shell'),optimal_geometry.get('N_pass'),optimal_geometry.get('N_baffle'),optimal_geometry.get('Y'),optimal_geometry.get('L'),optimal_geometry.get('bundle_array'),optimal_geometry.get('pitch_type'),NTU_Q])
    
def NTUvsLMTD(passes,shells):
    """Change N_shell and N_pass manually to always be 1 value"""
    
    # Define minima and maxima of the iteration...
    L_range = np.linspace(0.10,0.20,11)
    Y_range = np.linspace(0.009,0.015,7)
    N_baffle_range = np.linspace(0,15,16)
    pitch_type_array = ["square","triangle"]
    N_shell_array = [shells]
    N_pass_array = [passes]
    
    bundle_array_array = []
    bundle_array_array.append([1,3,5,3,1])
    bundle_array_array.append([3,3,3,3])
    bundle_array_array.append([2,5,2])
    bundle_array_array.append([3,5,5,5,3])
    bundle_array_array.append([2,3,4,3,2])
    bundle_array_array.append([3,5,5,5,5,3])
    bundle_array_array.append([2,4,6,6,4,2])
    bundle_array_array.append([2,4,4,4,4,2])
    bundle_array_array.append([4,5,6,5,4])

    # define some constant designs
    L_header = 0.025
    breadth_gap = 0.01
    
    geometry = {'L_header': L_header,'breadth_gap':breadth_gap}
    
    NTUs = []
    LMTDs = []
    differences=[]
    reldifferences=[]
    
    for N_shell in N_shell_array:
        
        # Set pitch_type
        geometry['N_shell']=N_shell
        
        for N_pass in N_pass_array:
            
            # Set pitch_type
            geometry['N_pass']=N_pass
            
            for pitch_type in pitch_type_array:
                
                # Set pitch_type
                geometry['pitch_type']=pitch_type
                
                for bundle_array in bundle_array_array:
                    
                    # Set bundle_array
                    geometry['bundle_array']=bundle_array
                
                    for L in L_range:
                        
                        # Set L
                        geometry['L']=L
                        
                        for Y in Y_range:
                            
                            # Set Y
                            geometry['Y']=Y
                            
                            for N_baffle in N_baffle_range:
                                
                                # Set N_baffle
                                geometry['N_baffle']=N_baffle
                                
                                if geom.check_constraints(geometry)==True:
                                
                                    # Find values
                                    m_dot_c = hydraulic.iterate_c(geometry)
                                    m_dot_h = hydraulic.iterate_h(geometry)
                                    Re_sh = hydraulic.give_Re_sh(m_dot_c,geometry)
                                    Re_tube = hydraulic.give_Re_tube(m_dot_h,geometry)
                                    
                                    # Compare Values
                                    LMTD = thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry)
                                    NTU = thermal.F_Q_NTU(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry)
                                    
                                    LMTDs.append(LMTD)
                                    NTUs.append(NTU)
                                    differences.append(abs(LMTD-NTU))
                                    reldifferences.append(abs(100*(LMTD-NTU)/LMTD))

                                        
                                else:
                                    pass
                
    
    return([LMTDs,NTUs,differences,reldifferences])
    
    
def plots():
    """Plots some NTU vs LMTD values"""
    value1 = NTUvsLMTD(1,1)
    print('1/5')
    value2 = NTUvsLMTD(2,1)
    print('2/5')
    value3 = NTUvsLMTD(4,1)
    print('3/5')
    value5 = NTUvsLMTD(2,2)
    print('4/5')
    value6 = NTUvsLMTD(4,2)
    print('5/5')
    
    LMTD11 = value1[0]
    NTU11 = value1[1]
    differences11 = value1[2]
    reldifferences11 = value1[3]
    
    LMTD21 = value2[0]
    NTU21 = value2[1]
    differences21 = value2[2]
    reldifferences21 = value2[3]
    
    LMTD41 = value3[0]
    NTU41 = value3[1]
    differences41 = value3[2]
    reldifferences41 = value3[3]
    
    LMTD22 = value5[0]
    NTU22 = value5[1]
    differences22 = value5[2]
    reldifferences22 = value5[3]
    
    LMTD42 = value6[0]
    NTU42 = value6[1]
    differences42 = value6[2]
    reldifferences42 = value6[3]
    
    plt.scatter(LMTD11,NTU11,label='1-pass,1-shell', s=1.5)
    plt.scatter(LMTD21,NTU21,label='2-pass,1-shell', s=1.5)
    plt.scatter(LMTD41,NTU41,label='4-pass,1-shell', s=1.5)
    plt.scatter(LMTD22,NTU22,label='2-pass,2-shell', s=1.5)
    plt.scatter(LMTD42,NTU42,label='4-pass,2-shell', s=1.5)
    plt.title('LMTD vs NTU heat transfers')
    plt.legend()
    plt.ylabel('e-NTU heat transfer (W)')
    plt.xlabel('LMTD heat transfer (W)')
    plt.grid()
    plt.show()
    
    plt.scatter(LMTD11,NTU11,label='1-pass,1-shell', s=1.5)
    plt.scatter(LMTD21,NTU21,label='2-pass,1-shell', s=1.5)
    plt.scatter(LMTD41,NTU41,label='4-pass,1-shell', s=1.5)
    plt.scatter(LMTD22,NTU22,label='2-pass,2-shell', s=1.5)
    plt.scatter(LMTD42,NTU42,label='4-pass,2-shell', s=1.5)
    plt.ylabel('e-NTU heat transfer (W)')
    plt.xlabel('LMTD heat transfer (W)')
    plt.title('LMTD vs NTU heat transfers')
    plt.legend()
    plt.yscale('log')
    plt.xscale('log')
    plt.grid()
    plt.show()
    
    plt.scatter(LMTD11,reldifferences11,label='1-pass,1-shell', s=1.5)
    plt.scatter(LMTD21,reldifferences21,label='2-pass,1-shell', s=1.5)
    plt.scatter(LMTD41,reldifferences41,label='4-pass,1-shell', s=1.5)
    plt.scatter(LMTD22,reldifferences22,label='2-pass,2-shell', s=1.5)
    plt.scatter(LMTD42,reldifferences42,label='4-pass,2-shell', s=1.5)
    plt.ylabel('NTU heat transfer %error from LMTD method')
    plt.xlabel('LMTD heat transfer (W)')
    plt.title('NTU Error in Q vs LMTD Q')
    plt.legend()
    plt.yscale('log')
    plt.xscale('log')
    plt.grid()
    plt.show()
    
    plt.scatter(LMTD11,reldifferences11,label='1-pass,1-shell', s=1.5)
    plt.scatter(LMTD21,reldifferences21,label='2-pass,1-shell', s=1.5)
    plt.scatter(LMTD41,reldifferences41,label='4-pass,1-shell', s=1.5)
    plt.scatter(LMTD22,reldifferences22,label='2-pass,2-shell', s=1.5)
    plt.scatter(LMTD42,reldifferences42,label='4-pass,2-shell', s=1.5)
    plt.ylabel('NTU heat transfer %error from LMTD method')
    plt.xlabel('LMTD heat transfer (W)')
    plt.title('NTU Error in Q vs LMTD Q')
    plt.legend()
    plt.grid()
    plt.show()
    
    return 1
    
#result = optimise_design()
#print("Q = {}W".format(result[0]))
#print("e-NTU Q = {}W".format(result[8]))
#print("{}-shell".format(result[1]))
#print("{}-pass".format(result[2]))
#print("{} baffles".format(result[3]))
#print("Y={}mm".format(result[4]*1000))
#print("L={}cm".format(result[5]*100))
#print("Bundle Array: {}".format(result[6]))
#print("Pitch is {}".format(result[7]))
    
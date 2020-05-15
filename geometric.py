from Definitions import *
import parametric as para
import matplotlib.pyplot as plt


"""Andrew Fns"""
# Check total mass
# Check total length
# Check total required length of tubing
# Check bundle fits within shell
# Check nozzle fits

"""Tomos Fns"""
# Check bundle divides by shell and pass
# Check L > Baffles
# Check even baffles for >1 shell



def check_L_total(geometry):
    L_total = para.L_total(geometry)
    if L_total <= L_total_max:
        #print('pass: ', round(L_total, 3), '<', L_total_max)
        return True

    else:
        #print('L_total to large: ', round(L_total, 3), '>', L_total_max)
        return False


def check_L_tube_total(geometry):
    L_tube_total = para.L_tube(geometry) * geometry.get('N_tube')
    if L_tube_total <= L_tube_total_max:
        #print('pass: ', round(L_tube_total, 3), '<', L_tube_total_max)
        return True

    else:
        #print('L_tube_total to large: ', round(L_tube_total, 3), '>', L_tube_total_max)
        return False


def check_L_vs_baffle(geometry):
    """Checks if L is greater than total baffle length"""
    N_baffle = geometry.get('N_baffle')
    L = geometry.get('L')
    # I have my functions as pass / fail being True / False - Tomos
    if N_baffle*0.0015 > L:
        return False
    else:
        return True

def check_mass_total(geometry):
    """"TO BE FULLY GENERALISED TO n-shell m-pass"""
    # A_baffle needs to take into account non-intersecting tubes
    # Add flow separaters for mulitishell

    mass_tube_total = rhol_tube * para.L_tube(geometry) * para.N_tube(geometry)

    mass_pipe_total = rhol_pipe * para.L_pipe(geometry)

    mass_baffle_total = rhoA_baffle * geometry.get('N_baffle') * para.A_baffle(geometry)

    mass_nozzle_total = 4 * mass_nozzle

    mass_plate_total = 2 * rhoA_plate * para.A_tube_plate(geometry) + 2 * rhoA_plate * para.A_end_plate(geometry)

    mass_total = mass_pipe_total + mass_tube_total + mass_baffle_total + mass_nozzle_total + mass_plate_total

#    if 1 == 1:
#        print('mass_tube_total: ... ', mass_tube_total)
#        print('mass_pipe_total: ... ', mass_pipe_total)
#        print('mass_baffle_total: . ', mass_baffle_total)
#        print('mass_nozzle_total: . ', mass_nozzle_total)
#        print('mass_plate_total: .. ', mass_plate_total)
#        print('________________________________________')
#        print('mass_total: ....... ',  mass_total)
#        print('________________________________________')

    if mass_total <= mass_total_max:
        #print('pass: ', round(mass_total, 3), '<', mass_total_max)
        return True

    else:
        #print('mass_total to large: ', round(mass_total, 3), '>', mass_total_max)
        return False


#    if 1 == 0:                                                  # TO AMEND: Change to only print if ask for in argument
#        print('mass_tube_total: ', mass_tube_total)
#        print('mass_pipe_total: ', mass_pipe_total)
#        print('mass_baffle_total: ', mass_baffle_total)
#        print('mass_nozzle_total: ', mass_nozzle_total)
#        print('mass_plate_total: ', mass_plate_total)
#        print('________________________________________')
#        print('mass_total: ',  mass_total)


def check_bundle_fit(geometry):
    """Check the tube bundle fits within the radius of the HX casing
        ATM we use a very simplistic check:
        - does it fit vertically?
        - does it fit horizontally?"""
        
    bundle_array = geometry.get('bundle_array')
    Y = geometry.get('Y')
    
    vertical = d_outer*max(bundle_array) + (Y-d_outer)*(max(bundle_array)-1)
    horizontal = d_outer*len(bundle_array) + (Y-d_outer)*(len(bundle_array)-1)
    
    if horizontal < D_inner and vertical < D_inner:
        return True
    else:
        return False   


def check_tube_intersect(geometry):
    """Checks that a divider doesn't intersect the tubes, for N_shell or N_pass > 1, by virtue of not fitting between tubes
    ANOTHER function checks that the tube bundle dvides either side of a divider"""
    
    # Definitions
    bundle_array = geometry.get('bundle_array')
    N_pass = geometry.get('N_pass')
    N_shell = geometry.get('N_shell')
    N_row = para.N_row(geometry)
    t_sep = 4.5e-3                  #thickness of separater

    # Only needed if N_shell > 1 or N_pass > 1
    
    if N_shell > 1 or N_pass > 1:
    
        #Two different requirements depending on whether the number of rows is even or odd.
    
        if N_row % 2 == 0:
            if geometry.get('Y') > d_outer + t_sep:
                return True
            else:
                return False
    
        else:
            if geometry.get('Y') > 0.5 * (d_outer + t_sep):
                return True
            else:
                return False
            
    else:
        return True


def check_pitch_distance(geometry):
    """Checks tubes don't intersect each other"""
    if geometry.get('Y') > d_outer:
        return True
    else:
        return False

def check_N_baffle(geometry):
    """This function checks that there are an even number of baffles if there's >1 shell"""
    N_baffle = geometry.get('N_baffle')
    if N_baffle % 2 > 0: #i.e odd number
        return False
    else:
        return True

def check_tube_division(geometry):
    """This function checks if the tubes will divide into N_shell or N_pass"""

    N_shell= geometry.get('N_shell')
    N_pass = geometry.get('N_pass')
    N_tube = para.N_tube(geometry)
    N_row = para.N_row(geometry) # This is per shell remember
    pitch_type = geometry.get('pitch_type')
    bundle_array = geometry.get('bundle_array')

    (len(bundle_array)/2)-1

    # check first that there's equal tubes either side of the halfway point (checks %2 rows later)
    if len(bundle_array)%2 < 1:
        if sum(bundle_array[0:int(((len(bundle_array)/2)))]) != sum(bundle_array[(int((len(bundle_array)/2))):]) and N_pass%2<1:
            return False
        else:
            pass

    # Check equal no of tubes per pass
    if N_tube % N_pass > 1:
        return False

    else:

        if N_shell == 1 and N_pass == 1:
            # No worries for the simple case
            return True

        elif N_shell == 1 and N_pass == 2:
            # Need number of non zero rows to be divisible by 2
            if N_row % 2 > 0:
                return False
            else:
                return True

        elif N_shell == 2 and N_pass < 3: # i.e 1 or 2 pass
            # Just need N_row (which is per shell) to be whole
            if N_row % 1 > 0:
                return False
            else:
                return True

        elif N_shell < 3 and N_pass == 4:

            if N_row % 1 > 0 and N_Shell == 2:
                return False

            elif N_row % 2 > 0 and N_shell == 1:
                return False

            else:
                # Need to check if columns divide
                if pitch_type == 'square':

                    even_rows = True
                    for i in bundle_array:
                        if i%2 > 1:
                            even_rows = False

                    if even_rows == True:
                        return True
                    else:
                        return False

                else:
                    """You can't have 4-pass triangular"""
                    return False

        else:
            # There are weird numbers of shell vs pass
            return False


def check_constraints(geometry):

    c1 = check_mass_total(geometry)
    c2 = check_L_total(geometry)
    c3 = check_L_total(geometry)
    c4 = check_L_vs_baffle(geometry)
    c5 = check_N_baffle(geometry)
    c6 = check_tube_division(geometry)
    c7 = check_pitch_distance(geometry)
    c8 = check_tube_intersect(geometry)
    c9 = check_bundle_fit(geometry)

    if c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8 and c9 == True:
        return True
    else:
        return False
    
def troubleshoot_geometry(geometry):
    
    c1 = check_mass_total(geometry)
    c2 = check_L_total(geometry)
    c3 = check_L_total(geometry)
    c4 = check_L_vs_baffle(geometry)
    c5 = check_N_baffle(geometry)
    c6 = check_tube_division(geometry)
    c7 = check_pitch_distance(geometry)
    c8 = check_tube_intersect(geometry)
    c9 = check_bundle_fit(geometry)
    
    return([1,c1,2,c2,3,c3,4,c4,5,c5,6,c6,7,c7,8,c8,9,c9])







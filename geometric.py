from Definitions import *
import parametric as para

# Check total mass
# Check total length
# Check total required length of tubing
# Check bundle fits within shell
# Check nozzle fits



def check_L_total(geometry):
    L_total = para.L_total(geometry)
    if L_total <= L_total_max:
        print('pass: ', round(L_total, 3), '<', L_total_max)
        return 'pass'

    else:
        print('L_total to large: ', round(L_total, 3), '>', L_total_max)
        return 'fail'


def check_L_tube_total(geometry):
    L_tube_total = para.L_tube(geometry) * geometry.get('N_tube')
    if L_tube_total <= L_tube_total_max:
        print('pass: ', round(L_tube_total, 3), '<', L_tube_total_max)
        return 'pass'

    else:
        print('L_tube_total to large: ', round(L_tube_total, 3), '>', L_tube_total_max)
        return 'fail'


def check_mass_total(geometry):
    """"TO BE FULLY GENERALISED TO n-shell m-pass"""
    # Consider number of nozzles required
    # A_baffle needs to take into account non-intersecting tubes
    # Add flow separaters for mulitishell

    mass_tube_total = rhol_tube * para.L_tube(geometry) * para.N_tube(geometry)

    mass_pipe_total = rhol_pipe * para.L_pipe(geometry)

    mass_baffle_total = rhoA_baffle * geometry.get('N_baffle') * para.A_baffle(geometry)

    mass_nozzle_total = 4 * mass_nozzle

    mass_plate_total = 2 * rhoA_plate * para.A_tube_plate(geometry) + 2 * rhoA_plate * para.A_end_plate(geometry)

    mass_total = mass_pipe_total + mass_tube_total + mass_baffle_total + mass_nozzle_total + mass_plate_total

    if 1 == 1:
        print('mass_tube_total: ... ', mass_tube_total)
        print('mass_pipe_total: ... ', mass_pipe_total)
        print('mass_baffle_total: . ', mass_baffle_total)
        print('mass_nozzle_total: . ', mass_nozzle_total)
        print('mass_plate_total: .. ', mass_plate_total)
        print('________________________________________')
        print('mass_total: ....... ',  mass_total)
        print('________________________________________')

    if mass_total <= mass_total_max:
        print('pass: ', round(mass_total, 3), '<', mass_total_max)
        return 'pass'

    else:
        print('mass_total to large: ', round(mass_total, 3), '>', mass_total_max)
        return 'fail'


    if 1 == 1:                                                  # TO AMEND: Change to only print if ask for in argument
        print('mass_tube_total: ', mass_tube_total)
        print('mass_pipe_total: ', mass_pipe_total)
        print('mass_baffle_total: ', mass_baffle_total)
        print('mass_nozzle_total: ', mass_nozzle_total)
        print('mass_plate_total: ', mass_plate_total)
        print('________________________________________')
        print('mass_total: ',  mass_total)



def check_constraints(geometry):

    if check_mass_total(geometry)=='pass' and check_L_total(geometry)=='pass' and check_L_total(geometry)=='pass':
        print('constraints satisfied')
        return 'pass'

    else:
        print('ERROR: constraints not satisfied')
        return 'fail'





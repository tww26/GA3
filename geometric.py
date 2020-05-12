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



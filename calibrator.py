import Definitions
import Thermal_Functions as thermal
import designs as des
import hydraulic
import numpy as np
import scipy
from scipy import optimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


L = 180e-3
N_baffle = 7
pitch_type = "square"
Y = 13e-3
bundle_array = [4,4,4,4]
N_shell = 1
N_pass = 2
L_header = 0.025
breadth_gap = 0.01
B_end = 27.25e-3

geometry = {'L': L,'N_baffle': N_baffle,'pitch_type': pitch_type,'Y': Y,'bundle_array': bundle_array, 'N_shell': N_shell, 'N_pass': N_pass, 'L_header': L_header, 'breadth_gap': breadth_gap, 'B_end':B_end}

def f_dQ_squared(year, group):

    year = str(year)

    Q_measured = des.Designs[year][group]['Q']

    geometry = {'L': des.Designs[year][group]['L'],
                'N_baffle': des.Designs[year][group]['N_baffle'],
                'pitch_type': des.Designs[year][group]['pitch_type'],
                'Y': des.Designs[year][group]['Y'],
                'bundle_array': des.Designs[year][group]['bundle_array'],
                'N_shell': des.Designs[year][group]['N_shell'],
                'N_pass': des.Designs[year][group]['N_pass'],
                'L_header': des.Designs[year][group]['L_header'],
                'breadth_gap': des.Designs[year][group]['breadth_gap'],
                'B_end': des.Designs[year][group]['B_end']}

    m_dot_c = hydraulic.iterate_c(geometry, year)
    m_dot_h = hydraulic.iterate_h(geometry, year)
    Re_sh = hydraulic.give_Re_sh(m_dot_c, geometry)
    Re_tube = hydraulic.give_Re_tube(m_dot_h, geometry)

    Q_model = thermal.F_Q_LMTD(m_dot_c, m_dot_h, Re_tube, Re_sh, geometry)
    dQ = Q_model - Q_measured
    dQ_squared = dQ**2

    return dQ_squared

def f_sum_dQ_squared():

    sum_dQ_squared = 0

    for year in des.Designs.keys():
        for group in des.Designs[year].keys():
            sum_dQ_squared += f_dQ_squared(year, group)

    return sum_dQ_squared

def f_dm_hot_squared(year, group, K_turn, K_nozzle):

    year = str(year)

    m_dot_hot_measured = des.Designs[year][group]['m_dot_hot']

    geometry = {'L': des.Designs[year][group]['L'],
                'N_baffle': des.Designs[year][group]['N_baffle'],
                'pitch_type': des.Designs[year][group]['pitch_type'],
                'Y': des.Designs[year][group]['Y'],
                'bundle_array': des.Designs[year][group]['bundle_array'],
                'N_shell': des.Designs[year][group]['N_shell'],
                'N_pass': des.Designs[year][group]['N_pass'],
                'L_header': des.Designs[year][group]['L_header'],
                'breadth_gap': des.Designs[year][group]['breadth_gap'],
                'B_end': des.Designs[year][group]['B_end']}

    m_dot_hot_model = hydraulic.iterate_h(geometry, year, K_turn, K_nozzle)

    dm_dot_hot = m_dot_hot_model - m_dot_hot_measured
    dm_dot_hot_squared = dm_dot_hot**2

    return dm_dot_hot_squared

def f_sum_dm_dot_hot_squared(K_turn, K_nozzle):
    """When this function is used for the minimise methods the input should be K_h, otherwise K_turn and K_nozzle (for plotting)"""

    sum_dm_dot_hot_squared = 0

    for year in des.Designs.keys():
        for group in des.Designs[year].keys():
            sum_dm_dot_hot_squared += f_dm_hot_squared(year, group, K_turn, K_nozzle)

    return sum_dm_dot_hot_squared

def f_sum_dm_dot_hot_sqaured_array(K_h):
    K_turn = K_h[0]
    K_nozzle = K_h[1]
    return f_sum_dm_dot_hot_squared(K_turn, K_nozzle)

def f_dm_dot_cold_squared(year, group, K_baffle_bend, K_nozzle):

    year = str(year)

    m_dot_cold_measured = des.Designs[year][group]['m_dot_cold']

    geometry = {'L': des.Designs[year][group]['L'],
                'N_baffle': des.Designs[year][group]['N_baffle'],
                'pitch_type': des.Designs[year][group]['pitch_type'],
                'Y': des.Designs[year][group]['Y'],
                'bundle_array': des.Designs[year][group]['bundle_array'],
                'N_shell': des.Designs[year][group]['N_shell'],
                'N_pass': des.Designs[year][group]['N_pass'],
                'L_header': des.Designs[year][group]['L_header'],
                'breadth_gap': des.Designs[year][group]['breadth_gap'],
                'B_end': des.Designs[year][group]['B_end']}

    m_dot_cold_model = hydraulic.iterate_c(geometry,year,K_baffle_bend,K_nozzle)

    dm_dot_cold = m_dot_cold_model - m_dot_cold_measured
    dm_dot_cold_squared = dm_dot_cold**2

    return dm_dot_cold_squared

def f_sum_dm_dot_cold_squared(K_c):

    K_baffle_bend = K_c[0]
    if len(K_c) == 2:
        K_nozzle = K_c[1]
    else:
        K_nozzle = 4.48993054

    sum_dm_dot_cold_squared = 0

    for year in des.Designs.keys():
        for group in des.Designs[year].keys():
            sum_dm_dot_cold_squared += f_dm_dot_cold_squared(year, group, K_baffle_bend, K_nozzle)

    return sum_dm_dot_cold_squared



"""______________________WORKING CODE______________________________"""

"""Using N-M and Powell to determine K_turn and K_nozzle from hot"""
# print(scipy.optimize.minimize(f_sum_dm_dot_hot_sqaured_array, [4,4], method="Nelder-Mead"))
# print(scipy.optimize.minimize(f_sum_dm_dot_hot_sqaured_array, [4,4], method="Powell"))

"""Using N-M and Powell to determine K_baffle_bend only from cold"""
# print(scipy.optimize.minimize(f_sum_dm_dot_cold_squared, [1], method="Nelder-Mead"))
# print(scipy.optimize.minimize(f_sum_dm_dot_cold_squared, [1], method="Powell"))

"""Using N-M and Powell to determine Ks independently of each other"""
# print(scipy.optimize.minimize(f_sum_dm_dot_hot_squared, [1,1], method="Nelder-Mead"))
# print(scipy.optimize.minimize(f_sum_dm_dot_hot_squared, [1,1], method="Powell"))
#
# print(scipy.optimize.minimize(f_sum_dm_dot_cold_squared, [1,1], method="CG"))
# print(scipy.optimize.minimize(f_sum_dm_dot_cold_squared, [1,1], method="CG"))

"""Surface plot - THIS WORKS NOW"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

tempf = np.vectorize(f_sum_dm_dot_hot_squared)



fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
K_turn = np.arange(0, 8, .4)
K_nozzle = np.arange(0, 8, .4)
X, Y = np.meshgrid(K_turn, K_nozzle)

Z = tempf(X, Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.04f'))
ax.set_xlabel('K_turn')
ax.set_ylabel('K_nozzle')
ax.set_zlabel('Cost Function')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

"""__________________PLOTTING EXPERIMENTS________________________"""

"""Trying and failing to plot the cost function over the K_h space"""
# K_h_bounds = [(0, 2), (0, 2)]
#
# K_turn = np.arange(0.5, 1, 0.1)
# K_nozzle = np.arange(0.5, 1, 0.1)
# K_turn_grid, K_nozzle_grid = np.meshgrid(K_turn, K_nozzle)
# K_h_stack = np.stack([K_turn_grid, K_nozzle_grid])
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.view_init(45, -45)
# ax.plot_surface(K_turn_grid, K_nozzle_grid, f_sum_dm_dot_hot_squared(K_h_stack), cmap='terrain')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('eggholder(x, y)')
# plt.show()

"""Example surface plot"""
# def eggholder(x):
#     return (-(x[1] + 47) * np.sin(np.sqrt(abs(x[0]/2 + (x[1]  + 47))))
#             -x[0] * np.sin(np.sqrt(abs(x[0] - (x[1]  + 47)))))
#
# bounds = [(-512, 512), (-512, 512)]
#
# x = np.arange(-512, 513)
# y = np.arange(-512, 513)
# xgrid, ygrid = np.meshgrid(x, y)
# xy = np.stack([xgrid, ygrid])
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.view_init(45, -45)
# ax.plot_surface(xgrid, ygrid, eggholder(xy), cmap='terrain')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('eggholder(x, y)')
# plt.show()

"""Trisurface plot"""
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,5,10)
# y = np.linspace(0,5,10)
# z = []
#
# for xv in x:
#     for yv in y:
#         z.append(f_sum_dm_dot_hot_squared(xv, yv))
#
# z = np.array(z)
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
#
# plt.show()

"""____________________MINIMISING EXPERIMENTS______________________"""

"""Trying to get CG method to work"""
#print(scipy.optimize.minimize(f_sum_dm_dot_hot_sqaured_array, [0.1,0.1], method="CG", jac=False, options={'gtol': 1e-20}, tol=1e-20))

#dK_nozzle = 1e-6
#print((f_sum_dm_dot_hot_squared(0.1, 0.1 + dK_nozzle)-f_sum_dm_dot_hot_squared(0.1, 0.1-dK_nozzle))/(2*dK_nozzle))

"""Trying to use shgo"""
# K_h_bounds = [(0, 2), (0, 2)]
# print(optimize.shgo(f_sum_dm_dot_hot_squared, K_h_bounds))

"""Trying to get other optimisation methods to work"""
# print(scipy.optimize.minimize(f_sum_dm_dot_cold_squared, [1,1], method="BFGS"))
# print(scipy.optimize.minimize(f_sum_dm_dot_cold_squared, [1,1], method="L-BFGS-B"))




"""
print('________________Cost Function Evaluation________________')
print('f_sum_dm_dot_cold_squared :', f_sum_dm_dot_cold_squared())
print('f_sum_dm_dot_hot_squared :', f_sum_dm_dot_hot_squared())
print('f_sum_dQ_squared: ', f_sum_dQ_squared())
print('________________________________________________________')
"""









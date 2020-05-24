import Definitions
import parametric as para

# Note that N_baffle is the number of baffles per shell.

"""2020 Design"""

Year = 2020

A = {'L': 132e-3,
     'N_baffle': 3.5,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [4,6,6,4],
     'N_shell': 2,
     'N_pass': 4,
     'L_header': 36.5e-3,
     'L_turner': 20.5e-3,
     'breadth_gap': 0.0175,
     'B_end': 0}

B = {'L': 180e-3,
     'N_baffle': 7,
     'pitch_type': 'square',
     'Y': 12.5e-3,
     'bundle_array': [4,4,4,4],
     'N_shell': 1,
     'N_pass': 2,
     'L_header': 26.5e-3,
     'L_turner': 20.5e-3,
     'breadth_gap': 0.010,
     'B_end': 0}

C = {'L': 169e-3,
     'N_baffle': 6,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [4,4,4,4],
     'N_shell': 2,
     'N_pass': 4,
     'L_header': 50e-3,
     'L_turner': 21e-3,
     'breadth_gap': 0.012,
     'B_end': 0}

D = {'L': 124e-3,
     'N_baffle': 5,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [2,4,6,6,4,2],
     'N_shell': 2,
     'N_pass': 4,
     'L_header': 50e-3,
     'L_turner': 21e-3,
     'breadth_gap': 0.021,
     'B_end': 0}

E = {'L': 105e-3,
     'N_baffle': 7,
     'pitch_type': 'square',
     'Y': 10.4e-3, # this is very approximate
     'bundle_array': [4,4,6,6,4,4],
     'N_shell': 1,
     'N_pass': 4,
     'L_header': 51e-3,
     'L_turner': 30e-3,
     'breadth_gap': 0.0193,
     'B_end': 0}

designs_2020 = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E}


"""2019 Designs"""

Year = 2019

A = {'L': 209e-3,
     'N_baffle': 12,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [4,4,4,4],
     'N_shell': 2,
     'N_pass': 4,
     'L_header': 50e-3,
     'L_turner': 20e-3,
     'breadth_gap': 0.01134,
     'B_end': 0,
     'Q': 12610,
     'm_dot_hot': 0.29604,
     'm_dot_cold': 0.41287
     }

B = {'L': 214e-3,
     'N_baffle': 11,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [2,4,4,4],
     'N_shell': 2,
     'N_pass': 2,
     'L_header': 52e-3,
     'L_turner': 20e-3,
     'breadth_gap': 0.014,
     'B_end': 0,
     'Q': 12705,
     'm_dot_hot': 0.4574262,
     'm_dot_cold': 0.3712875
     }

C = {'L': 210e-3,
     'N_baffle': 6,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [4,4,4,4],
     'N_shell': 1,
     'N_pass': 2,
     'L_header': 53e-3,
     'L_turner': 24e-3,
     'breadth_gap': 0.01734,
     'B_end': 0,
     'Q': 14495,
     'm_dot_hot': 0.4643569,
     'm_dot_cold': 0.5861392
     }

D = {'L': 214e-3,
     'N_baffle': 11,
     'pitch_type': 'triangular', #circular
     'Y': 12.25, #approximate
     'bundle_array': [2,4,4,4,4,2],
     'N_shell': 2,
     'N_pass': 4,
     'L_header': 50e-3,
     'L_turner': 20e-3,
     'breadth_gap': 0.0064,
     'B_end': 0,
     'Q': 15945,
     'm_dot_hot': 0.34802015,
     'm_dot_cold': 0.5693075
     } # circular pitch type, need to revisit

"""E = {'L': 200e-3,
     'N_baffle': 8,
     'pitch_type': 'triangular',
     'Y': 11.5e-3,
     'bundle_array': [4,5,5,4],
     'N_shell': 1,
     'N_pass': 2,
     'L_header': 55e-3,
     'L_turner': 25e-3,
     'breadth_gap': 0.01122,
     'B_end': 0,
     'Q': 17305} # MUST NOT USE!!! DESIGN INCLUDED VORTEX GENERATORS, INCREASING Q"""

# Group E used vortex generators and so their data was replaced by Dr Longley's design

E = {'L': 350e-3,
     'N_baffle': 14,
     'pitch_type': 'triangular',
     'Y': 12e-3,
     'bundle_array': [4,5,4],
     'N_shell': 1,
     'N_pass': 1,
     'L_header': 50e-3,
     'L_turner': 50e-3,
     'breadth_gap': 0.01734,
     'B_end': 0,
     'Q': 16060,
     'm_dot_hot': 0.485149,
     'm_dot_cold': 0.5198025
     }

designs_2019 = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E}


"""2018 Designs"""

Year = 2018

A = {'L': 129e-3,
     'N_baffle': 8,
     'pitch_type': 'triangular', # concentric circles
     'Y': 12.25e-3, #approximate
     'bundle_array': [4,6,6,4],
     'N_shell': 2,
     'N_pass': 4,
     'L_header': 50e-3,
     'L_turner': 20.5e-3,
     'breadth_gap': 0.01907,
     'B_end': 0,
     'Q': 11090,
     'm_dot_hot': 0.3534657,
     'm_dot_cold': 0.3297033
     } #circular pitch

B = {'L': 218e-3,
     'N_baffle': 6,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [2,4,6,6,4,2],
     'N_shell': 2,
     'N_pass': 2,
     'L_header': 50e-3,
     'L_turner': 21e-3,
     'breadth_gap': 0.019,
     'B_end': 0,
     'Q': 11610,
     'm_dot_hot': 0.4574262,
     'm_dot_cold': 0.2891092
     }

C = {'L': 156e-3,
     'N_baffle': 5,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [4,4,4,4],
     'N_shell': 2,
     'N_pass': 2,
     'L_header': 50e-3,
     'L_turner': 21e-3,
     'breadth_gap': 0.015,
     'B_end': 0,
     'Q': 11620,
     'm_dot_hot': 0.4594064,
     'm_dot_cold': 0.31831715
     }

designs_2018 = {'A': A, 'B': B, 'C': C}


"""2017 Designs"""

Year = 2017

A = {'L': 249e-3,
     'N_baffle': 12,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [4,4],
     'N_shell': 1,
     'N_pass': 1,
     'L_header': 38e-3,
     'L_turner': 38e-3,
     'breadth_gap': 0.016,
     'B_end': 0,
     'Q': 9668,
     'm_dot_hot': 0.456,
     'm_dot_cold': 0.44825
     }

B = {'L': 221e-3,
     'N_baffle': 12,
     'pitch_type': 'triangular',
     'Y': 15e-3,
     'bundle_array': [2,4,4,4],
     'N_shell': 2,
     'N_pass': 2,
     'L_header': 38e-3,
     'L_turner': 20e-3,
     'breadth_gap': 0.02585,
     'B_end': 0,
     'Q': 13813.5,
     'm_dot_hot': 0.422,
     'm_dot_cold': 0.304325
     }

C = {'L': 180e-3,
     'N_baffle': 8,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [3,4,4,3],
     'N_shell': 1,
     'N_pass': 2,
     'L_header': 38e-3,
     'L_turner': 21e-3,
     'breadth_gap': 0.016,
     'B_end': 0,
     'Q': 11767,
     'm_dot_hot': 0.4285,
     'm_dot_cold': 0.4169
     }

D = {'L': 136e-3,
     'N_baffle': 6,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [3,2,4,2,4,2,3],
     'N_shell': 1,
     'N_pass': 4,
     'L_header': 38e-3,
     'L_turner': 21e-3,
     'breadth_gap': 0.016,
     'B_end': 0,
     'Q': 13925.5,
     'm_dot_hot': 0.355,
     'm_dot_cold': 0.44255
     }

E = {'L': 120e-3,
     'N_baffle': 7,
     'pitch_type': 'triangular',
     'Y': 10e-3,
     'bundle_array': [2,4,6,6,4,2],
     'N_shell': 1,
     'N_pass': 4,
     'L_header': 28e-3,
     'L_turner': 28e-3,   # guessed
     'breadth_gap': 0.0163,
     'B_end': 0,
     'Q': 14866.5,
     'm_dot_hot': 0.385,
     'm_dot_cold': 0.377
     }

designs_2017 = {'A': A, 'B': B, 'C': C, 'D': D}



"""Dictionary of designs from all years"""

Designs = {'2017': designs_2017, '2018': designs_2018,'2019': designs_2019}



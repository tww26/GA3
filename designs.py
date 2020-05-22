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

designs_2020 = {'Year': Year, 'A': A, 'B': B, 'C': C, 'D': D, 'E': E}

"""2019 Designs"""

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

designs_2019 = {'Year': Year, 'A': A, 'B': B, 'C': C, 'D': D, 'E': E}

"""2018 Designs"""

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

designs_2018 = {'Year': Year, 'A': A, 'B': B, 'C': C, 'D': D, 'E': E}

"""2017 Designs"""

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

E = {'L': 180e-3,
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

designs_2017 = {'Year': Year, 'A': A, 'B': B, 'C': C, 'D': D, 'E': E}



"""Dictionary of designs from all years"""

Designs = {'designs_2017': designs_2017, 'designs_2018': designs_2018,'designs_2019': designs_2019 ,'designs_2020': designs_2020}


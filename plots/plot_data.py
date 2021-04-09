# Defining constants for generating plot data & plotting
# Constants are for when this variable isn't the one being varied

dest_directory = 'plots/data/'

# min -> max of range when varying the number of airports
min_vary_v = 5
max_vary_v = 365
const_num_flights = 500

# min -> max of range when varying the number of flights
min_vary_e = 50
max_vary_e = 3000
const_num_airports = 365

# setting up the respective ranges for the two plots to be generated
seq_vary_v = range(min_vary_v, max_vary_v + 1, 10)
seq_vary_e = range(min_vary_e, max_vary_e + 1, 150)

import random
import string
import time

import dill

from plots.plot_data import *
from algorithm import FlightOptimizer, FlightNoptimizer
from models.graph import Graph

dest_directory = 'plots/data/'


def setup(max_outgoing, max_airports):
    graph = Graph()
    graph.init_with_data(False, max_outgoing, max_airports, silent=True)
    # select random start and finish airports
    src = random.choice(list(graph.airport_dict.values()))
    while len(src.outgoing_flights) == 0:
        src = random.choice(list(graph.airport_dict.values()))

    dest = random.choice(list(graph.airport_dict.values()))
    while dest.get_code() == src.get_code():
        dest = random.choice(list(graph.airport_dict.values()))

    return src, dest, graph


def generate_data(best_alg: bool, vary: string):
    time_data = []
    run_type = 'Best' if best_alg else 'Worst'
    dest_file_name = f'{dest_directory}vary_{vary}_{run_type.lower()}_data'
    is_v = False

    if vary == 'v':
        r = seq_vary_v
        max_vary = max_vary_v
        is_v = True
    elif vary == 'e':
        r = seq_vary_e
        max_vary = max_vary_e
    else:
        return None

    for i in r:
        print(f"\n== [{i / max_vary * 100:.1f}%] Vary {vary.upper()} {run_type} ==", end='\n\t')
        src, dest, graph = setup(const_num_flights, i) if is_v else setup(i, const_num_airports)

        # We assume a start time of 0 for all test cases
        if best_alg:
            optimizer = FlightOptimizer(src, dest, start_time=0)
        else:
            optimizer = FlightNoptimizer(src, dest, start_time=0)

        start = time.time()
        optimizer.find_best_path(graph)
        end = time.time()
        # save times
        time_data.append(start - end)

    # save the time data
    with open(dest_file_name, 'wb') as f:
        dill.dump(time_data, f)


def run():
    generate_data(True, 'v')
    generate_data(False, 'v')
    generate_data(True, 'e')
    generate_data(False, 'e')


# call run() to generate all 4 data sets
run()

import random
import time

import dill

from algorithm import FlightOptimizer
from load_data import LoadData
from models import Graph

times_x = []
times_y = []

for i in range(5, 365, 10):
    print("x =", i)
    graph = Graph()
    max_outgoing = i
    ld = LoadData(graph, False, 5000, i)
    ld.load()
    # select random start and finish airports
    src = random.choice(list(graph.airport_dict.values()))
    while len(src.outgoing_flights) == 0:
        src = random.choice(list(graph.airport_dict.values()))

    dest = random.choice(list(graph.airport_dict.values()))
    while dest.get_code() == src.get_code():
        dest = random.choice(list(graph.airport_dict.values()))

    # src = graph.get_airport('LAX')
    # dest = graph.get_airport('JFK')
    # vary the start time randomly, too
    # fo = FlightOptimizer(src, dest, random.randint(0, 3000000))
    fo = FlightOptimizer(src, dest, 0)

    start = time.time()
    fo.find_best_path()
    end = time.time()
    # save times
    times_y.append(start - end)
    times_x.append(i)

# save the times data (x values are trivial to regenerate)
with open('times-again.pkl', 'wb') as f:
    dill.dump(times_y, f)

import time

import dill as dill

from load_data import LoadData
from models import Graph

prelim = input("\"load\" or \"open\"\n")
graph = Graph()
max_outgoing = int(input("Enter max # of outgoing flights per airport: "))

if prelim == 'load':
    ld = LoadData(graph, True, max_outgoing)
    ld.load()
else:
    ld = LoadData(graph, False, max_outgoing)
    ld.load()

print(graph)
print('Number of Airports: ', len(graph.airport_dict))
num_edges = 0
for a in graph.airports:
    num_edges += len(a.outgoing_flights)
print('Number of Flights (Edges): ', num_edges)

while True:
    try:
        src_code = input("First Airport Code: ")

        src_airport = graph.get_airport(src_code.upper())
        src_airport.print_flights()

        dest_code = input("Second Airport Code: ")

        dest_airport = graph.get_airport(dest_code.upper())
        dest_airport.print_flights()

        start_time = int(input('Start Time: '))

        if src_airport is None or dest_airport is None:
            print('Something went wrong. Try again.\n')
            continue

        from algorithm import FlightOptimizer

        fo = FlightOptimizer(src_airport, dest_airport, start_time)
        fo.find_best_path()
    except KeyError:
        continue
    except ValueError:
        continue

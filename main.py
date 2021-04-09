from load_data import LoadData
from models.graph import Graph

prelim = input("\"load\" or \"open\"\n")
graph = Graph()
max_outgoing = int(input("Enter max # of outgoing flights per airport: "))

if prelim == 'load':
    graph.init_with_data(True, max_outgoing, max_airports=4)
else:
    graph.init_with_data(False, max_outgoing, max_airports=4)

while True:
    try:
        src_code = input("Src Airport Code: ")

        src_airport = graph.get_airport(src_code.upper())
        src_airport.print_flights()

        dest_code = input("Dest Airport Code: ")

        dest_airport = graph.get_airport(dest_code.upper())
        dest_airport.print_flights()

        start_time = int(input('Start Time (as a seconds timestamp): '))

        from algorithm import FlightOptimizer, FlightNoptimizer

        print("\nBETTER")
        fo = FlightOptimizer(src_airport, dest_airport, start_time)
        fo.find_best_path(graph)

        print("\nWORSE")
        fno = FlightNoptimizer(src_airport, dest_airport, start_time)
        fno.find_best_path(graph)
    except KeyError:
        continue
    except ValueError:
        continue
    except AttributeError:
        continue

from models.airport import Airport
from models.flight import Flight
from models.graph import Graph

# Defining constants (NOTE: Must always have the same values as the fast algorithm)
W_DUR = 0.05
W_PRI = 2
W_WAIT = 0.005


class FlightNoptimizer:

    def __init__(self, src_airport: Airport, dest_airport: Airport, start_time: int):
        self.src_airport = src_airport
        self.dest_airport = dest_airport
        self.dest_airport_code = self.dest_airport.get_code()
        self.start_time = start_time
        self.best_cost = float('inf')

    def calculate_wait_time(self, curr_time, next_flight_dept_time):
        if curr_time is None:
            return next_flight_dept_time
        return next_flight_dept_time - curr_time

    def get_node_cost(self, flight_path: [Flight]):
        node_cost = 0
        curr_time = self.start_time
        for flight in flight_path:
            wait_time = self.calculate_wait_time(curr_time, flight.get_dept_time())
            curr_time = flight.get_dept_time() + flight.get_duration()
            added_cost = W_DUR * flight.get_duration() + W_PRI * flight.get_price() + W_WAIT * wait_time
            node_cost += added_cost

        return node_cost

    def compare_paths(self, paths: [[Flight]]):
        optimal_path = []
        optimal_path_cost = float('Inf')
        print('Found', len(paths), 'paths in total.')
        for path in paths:
            if len(optimal_path) == 0:
                optimal_path = path
                continue

            path_cost = self.get_node_cost(path)
            if path_cost < optimal_path_cost:
                optimal_path = path
                optimal_path_cost = path_cost

        print("Optimal path score:", optimal_path_cost)
        return optimal_path

    def traverse_graph_helper(self, curr_flight: Flight, curr_time: int, flight_history: [Flight],
                              found_flight_paths: [[Flight]]):

        curr_cost = self.get_node_cost(flight_history)
        if curr_flight.destination.get_code() == self.dest_airport_code:
            found_flight_paths.append(flight_history)
            self.best_cost = min(self.best_cost, curr_cost)
            return

        curr_flight.destination.set_status('In Progress')
        curr_flight.destination.min_cost = min(curr_flight.destination.min_cost, curr_cost)

        for flight in curr_flight.destination.get_outgoing_flights():
            if curr_time > flight.get_dept_time():
                continue

            new_flight_history = [*flight_history, flight]
            new_node_cost = self.get_node_cost(new_flight_history)

            if not flight.destination.status == 'Unvisited' and new_node_cost > flight.destination.min_cost:
                continue

            if new_node_cost > self.best_cost:
                continue

            self.traverse_graph_helper(flight, flight.get_dept_time() + flight.get_duration(), new_flight_history,
                                       found_flight_paths)

        curr_flight.destination.set_status('Finished')

    def traverse_graph(self, start_time: int):
        self.src_airport.set_status('In Progress')
        found_flight_paths = []
        for flight in self.src_airport.get_outgoing_flights():
            if start_time > flight.get_dept_time():
                continue
            self.traverse_graph_helper(flight, flight.get_dept_time() + flight.get_duration(), [flight],
                                       found_flight_paths)

        self.src_airport.set_status('Finished')
        return found_flight_paths

    def find_best_path(self, graph: Graph):
        self.best_cost = float('inf')
        for airport in graph.airports:
            airport.set_status('Unvisited')
            airport.min_cost = float('inf')

        found_flight_paths = self.traverse_graph(self.start_time)
        if not found_flight_paths:  # if there were no found paths
            print('Solution could not be found | Slow')
            return

        self.print_path(self.compare_paths(found_flight_paths))

    def print_path(self, path: [Flight]):
        print('------- Solution | Slow -------')
        print('Start at ' + self.src_airport.get_code())
        for flight in path:
            print(flight)
        print('Arrive at ' + self.dest_airport.get_code())

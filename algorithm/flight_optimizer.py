from queue import PriorityQueue


from models.airport import Airport
from models.flight import Flight
from models.graph import Graph
from models.state import State

# Defining constants (NOTE: Must always have the same values as the fast algorithm)
W_DUR = 0.05
W_PRI = 2
W_WAIT = 0.005


class FlightOptimizer:

    def __init__(self, src_airport: Airport, dest_airport: Airport, start_time: int):
        self.src_airport = src_airport
        self.dest_airport = dest_airport
        self.queue = PriorityQueue()
        initial_state = State(src_airport, 0, start_time, [])
        self.queue.put(initial_state)
        self.found_solution = False

    def calculate_new_cost(self, curr_state: State, flight: Flight, wait_time: int):
        added_cost = W_DUR * flight.get_duration() + W_PRI * flight.get_price() + W_WAIT * wait_time
        return curr_state.get_node_cost() + added_cost

    def is_goal_state(self, state: State):
        return state.get_airport().get_code() == self.dest_airport.get_code()

    def print_path(self, state: State):
        flights = state.get_flights_taken()
        print('------- Solution | Fast -------')
        print('Start at ' + self.src_airport.get_code())
        for flight in flights:
            print(flight)
        print('Arrive at ' + self.dest_airport.get_code())

    def find_best_path(self, graph: Graph):
        for airport in graph.airports:
            airport.min_cost = float('inf')

        while not self.queue.qsize() == 0:  # while the queue is not empty
            curr_state = self.queue.get()

            if curr_state.get_airport().min_cost < curr_state.get_node_cost():
                continue
            curr_state.get_airport().min_cost = min(curr_state.get_node_cost(), curr_state.get_airport().min_cost)

            if self.is_goal_state(curr_state):
                self.print_path(curr_state)
                return

            for flight in curr_state.get_airport().get_outgoing_flights():
                # skip processing this flight if the it has already taken off
                if flight.get_dept_time() < curr_state.get_curr_time():
                    continue

                wait_time = flight.get_dept_time() - curr_state.get_curr_time()
                new_node_cost = self.calculate_new_cost(curr_state, flight, wait_time)

                new_node_time = flight.get_dept_time() + flight.get_duration()

                new_flights_taken = [*curr_state.get_flights_taken(), flight]

                next_state = State(flight.destination, new_node_cost, new_node_time, new_flights_taken)
                self.queue.put(next_state)

        print('Solution could not be found | Fast')

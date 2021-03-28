from queue import PriorityQueue

from algorithm import State


# from models import PriorityQueue


class FlightOptimizer:

    def __init__(self, src_airport, dest_airport, start_time):
        self.src_airport = src_airport
        self.dest_airport = dest_airport
        self.queue = PriorityQueue()
        initial_state = State(src_airport, 0, start_time, [])
        self.queue.put(initial_state)
        self.found_solution = False

    def calculate_wait_time(self, curr_time, next_flight_dept_time):
        return next_flight_dept_time - curr_time

    def calculate_new_cost(self, curr_state, flight, wait_time):
        added_cost = 0.5 * flight.get_duration() + 1 * flight.get_price() + 0.2 * wait_time
        return curr_state.get_node_cost() + added_cost

    def is_goal_state(self, state):
        return state.get_airport().get_code() == self.dest_airport.get_code()

    def print_path(self, state):
        self.found_solution = True
        flights = state.get_flights_taken()
        print('------- Solution -------')
        print('Start at ' + self.src_airport.get_code())
        for flight in flights:
            print(flight)
        print('Arrive at ' + self.dest_airport.get_code())

    def find_best_path(self):
        while not self.queue.qsize() == 0:  # while the queue is not empty
            curr_state = self.queue.get()
            print(self.queue.qsize())

            if self.is_goal_state(curr_state):
                self.print_path(curr_state)
                break

            for flight in curr_state.get_airport().get_outgoing_flights():
                # continue if the flight has already taken off
                if flight.get_dept_time() < curr_state.get_curr_time():
                    continue

                # print(curr_state.get_airport().get_code(), "\t|\t", flight.destination.get_code(), "\t", curr_state.get_node_cost())
                wait_time = flight.get_dept_time() - curr_state.get_curr_time()
                new_node_cost = self.calculate_new_cost(curr_state, flight, wait_time)

                new_node_time = flight.get_dept_time() + wait_time + flight.get_duration()

                new_flights_taken = list(curr_state.get_flights_taken())
                new_flights_taken.append(flight)

                next_state = State(flight.destination, new_node_cost, new_node_time, new_flights_taken)
                self.queue.put(next_state)

        if not self.found_solution:
            print('Solution could not be found')

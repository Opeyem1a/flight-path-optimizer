from algorithm import State
from models import PriorityQueue


class FlightOptimizer:

    def __init__(self, src_airport, dest_airport):
        self.src_airport = src_airport
        self.dest_airport = dest_airport
        self.queue = PriorityQueue()
        initial_state = State(src_airport, 0, None, [])
        self.queue.enqueue(initial_state)

    def calculate_wait_time(self, curr_time, next_flight_dept_time):
        # TODO: handle case where next flight is tomorrow
        if curr_time is None:
            """
            ASSUME: there is 0 waitTime for the first flight, you arrive @ the airport right before the flight departs
             //the first loop will have currTime = null so there's no waitTime, just go to the 1st airport when the flight's about to leave
            """
            return 0

        return next_flight_dept_time - curr_time

    def calculate_new_cost(self, curr_state, flight, wait_time):
        # TODO: determine these coefficients somehow
        added_cost = 0.1 * flight.get_duration() + 0.2 * flight.get_price() + 0.3 * wait_time
        return curr_state.get_node_cost() + added_cost

    def is_goal_state(self, state):
        # TODO: make sure that this checks string value equality
        return state.get_airport().get_code() == self.dest_airport.get_code()

    def find_best_path(self):
        while not self.queue.is_empty():
            curr_state = self.queue.dequeue()

            if self.is_goal_state(curr_state):
                break

            for flight in curr_state.get_airport().get_outgoing_flights():
                wait_time = self.calculate_wait_time(curr_state.get_curr_time(), flight.get_dept_time())
                new_node_cost = self.calculate_new_cost(curr_state, flight, wait_time)
                new_node_time = curr_state.currTime + wait_time + flight.duration

                new_flights_taken = list(curr_state.get_flights_taken())
                new_flights_taken.append(flight)

                next_state = State(flight.destination, new_node_cost, new_node_time, new_flights_taken)
                self.queue.enqueue(next_state)

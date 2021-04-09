from models.airport import Airport
from models.flight import Flight


class State:
    def __init__(self, airport: Airport, node_cost: float, curr_time: int, flights_taken: [Flight]):
        self.airport = airport  # the current airport at this state
        self.node_cost = node_cost  # total node cost at this state
        self.curr_time = curr_time  # current time for this state, encoded as a decimal, (0 - 23.99)
        self.flights_taken = flights_taken

    def get_node_cost(self):
        return self.node_cost

    def get_airport(self):
        return self.airport

    def get_curr_time(self):
        return self.curr_time

    def get_flights_taken(self):
        return self.flights_taken

    def __gt__(self, other):
        return self.node_cost > other.node_cost

    def __eq__(self, other):
        return self.node_cost == other.node_cost

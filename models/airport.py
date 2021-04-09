import string

from models.flight import Flight


class Airport:
    def __init__(self, code):
        self.outgoing_flights: [Flight] = []  # array of type Flight
        self.code: string = code
        self.status = 'Unvisited'
        self.min_cost = float('Inf')

    def add_outgoing_flight(self, flight: Flight):
        self.outgoing_flights.append(flight)

    def create_outgoing_flight(self, destination: any, dept_time: int, duration: int, price: float):
        flight = Flight(destination, dept_time, duration, price)
        self.add_outgoing_flight(flight)

    def get_code(self):
        return str(self.code)

    def get_outgoing_flights(self):
        return self.outgoing_flights

    def set_status(self, new_status: string):
        self.status = new_status

    def __str__(self):
        return "Airport" + str(self.code) \
                + " - NumFlights: " + str(len(self.outgoing_flights))

    def print_flights(self):
        print('=== ', str(self.code), ' ===')
        print('> NumFlights:', str(len(self.outgoing_flights)))
        for flight in self.outgoing_flights:
            print('\t', flight.__str__())

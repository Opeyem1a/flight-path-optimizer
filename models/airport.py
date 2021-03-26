from models import Flight


class Airport:
    def __init__(self, code):
        self.outgoing_flights = []  # array of type Flight
        self.code = code

    def add_outgoing_flight(self, flight):
        self.outgoing_flights.append(flight)

    def create_outgoing_flight(self, destination, dept_time, duration, price):
        flight = Flight(destination, dept_time, duration, price)
        self.add_outgoing_flight(flight)

    def get_code(self):
        return self.code

    def get_outgoing_flights(self):
        return self.outgoing_flights

    def __str__(self):
        return "Airport" + str(self.code) \
                + " - NumFlights: " + str(len(self.outgoing_flights))

    def print_flights(self):
        print('=== ', str(self.code), ' ===')
        print('> NumFlights:', str(len(self.outgoing_flights)))
        for flight in self.outgoing_flights:
            print('\t', flight.__str__())

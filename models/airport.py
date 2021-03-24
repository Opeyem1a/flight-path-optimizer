from models.flight import Flight


class Airport:
    def __init__(self, code):
        self.outgoingFlights = []  # array of type Flight
        self.code = code

    def add_outgoing_flight(self, flight):
        self.outgoingFlights.append(flight)

    def create_outgoing_flight(self, destination, deptTime, duration, price):
        flight = Flight(destination, deptTime, duration, price)
        self.add_outgoing_flight(flight)

    def get_code(self):
        return self.code

    def __str__(self):
        return str(self.code)

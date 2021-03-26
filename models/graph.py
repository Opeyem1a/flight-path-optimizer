from models import Airport, Flight


class Graph:
    def __init__(self):
        self.airports = []
        self.airport_dict = {}

    def add_airport(self, airport):
        self.airports.append(airport)
        self.airport_dict[airport.get_code()] = airport

    def get_airport(self, code):
        try:
            return self.airport_dict[code]
        except KeyError:
            return None

    def get_or_create_airport(self, code):
        if self.get_airport(code) is None:
            new_airport = Airport(code)
            self.add_airport(new_airport)

        return self.get_airport(code)

    def add_flight(self, src_code, flight):
        self.get_or_create_airport(src_code).add_outgoing_flight(flight)

    def create_flight(self, src_code, dest_code, dept_time, duration, price):
        dest_airport = self.get_or_create_airport(dest_code)
        flight = Flight(dest_airport, dept_time, duration, price)
        self.add_flight(src_code, flight)

    def __str__(self):
        out = "Airport Graph"
        # TODO: add more details
        for key, airport in self.airport_dict.items():
            out += "\n"+key+"\t"+airport.__str__()

        return out

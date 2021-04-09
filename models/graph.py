import string

from models.airport import Airport
from models.flight import Flight
from load_data import LoadData

class Graph:
    def __init__(self):
        self.airports: [Airport] = []
        self.airport_dict = {}

    def init_with_data(self, is_load=True, max_outgoing=10, max_airports=500, silent=False):
        ld = LoadData(self, is_load, max_outgoing, max_airports, silent)
        ld.load()
        silent or self.print_info()

    def print_info(self):
        # prints array of airport codes so you know your options before selecting & graph info
        print('Options -', self.airport_dict.keys())
        print('Number of Airports (Vertices): ', len(self.airport_dict))
        total_flights = 0
        for a in self.airports:
            total_flights += len(a.outgoing_flights)
        print('Number of Flights (Edges): ', total_flights)

    def add_airport(self, airport: Airport):
        self.airports.append(airport)
        self.airport_dict[airport.get_code()] = airport

    def get_airport(self, code: string):
        try:
            return self.airport_dict[code]
        except KeyError:
            return None

    def get_or_create_airport(self, code: string):
        if self.get_airport(code) is None:
            new_airport = Airport(code)
            self.add_airport(new_airport)

        return self.get_airport(code)

    def add_flight(self, src_code: string, flight: Flight):
        self.get_or_create_airport(src_code).add_outgoing_flight(flight)

    def create_flight(self, src_code: string, dest_code: int, dept_time: int, duration: int, price: float):
        dest_airport = self.get_or_create_airport(dest_code)
        flight = Flight(dest_airport, dept_time, duration, price)
        self.add_flight(src_code, flight)

    def __str__(self):
        out = "Airport Graph"
        # TODO: add more details
        for key, airport in self.airport_dict.items():
            out += "\n" + key + "\t" + airport.__str__()

        return out

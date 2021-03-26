from load_data import LoadData
from models import Graph

graph = Graph()
ld = LoadData(graph)
ld.load()
print(graph)

while True:
    user_input = input("Hit enter to to run the function again.")

    from algorithm import FlightOptimizer
    fo = FlightOptimizer('a', 'b')


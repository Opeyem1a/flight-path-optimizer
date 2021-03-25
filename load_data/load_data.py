import csv
import pandas as pd
import math
import random

from models import Graph


class LoadData:
    def __init__(self, graph):
        self.graph = graph

    def load(self):
        col_list = ['Year', 'Month', 'DayOfWeek', 'FlightDate', 'Marketing_Airline_Network', 'Operating_Airline ',
                    'Flight_Number_Marketing_Airline', 'Flight_Number_Operating_Airline', 'Origin', 'OriginAirportID',
                    'Dest', 'DestAirportID', 'DepTime', 'ArrTime', 'CRSElapsedTime', 'ActualElapsedTime']
        df = pd.read_csv('./data/flight_data.csv', usecols=col_list)

        agg_data = df.groupby(['Marketing_Airline_Network',
                               'Flight_Number_Operating_Airline',
                               'Origin',
                               'Dest',
                               'DayOfWeek']) \
            .agg({'DepTime': ['mean'],
                  'ActualElapsedTime': ['mean'], }) \
            .dropna()

        for index, row in agg_data.iterrows():
            src_code = row.name[2]
            dest_code = row.name[3]
            dept_time = row['DepTime']
            duration = row['ActualElapsedTime']
            # TODO: obviously the price should not be random going forward
            price = random.randint(100, 1000)
            self.graph.create_flight(src_code, dest_code, dept_time, duration, price)

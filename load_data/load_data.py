import csv
import pandas as pd

from models import Graph


class LoadData:
    def __init__(self, graph):
        self.graph = graph

    def load(self):
        col_list = ['Year', 'Month', 'DayOfWeek', 'FlightDate', 'Marketing_Airline_Network', 'Operating_Airline ',
                    'Flight_Number_Marketing_Airline', 'Flight_Number_Operating_Airline', 'Origin', 'OriginAirportID',
                    'Dest', 'DestAirportID', 'DepTime', 'ArrTime', 'CRSElapsedTime', 'ActualElapsedTime']
        df = pd.read_csv('./data/flight_data.csv', usecols=col_list)
        print(df.loc[0, :])
        print(df["Marketing_Airline_Network"].unique())
        print(df["Origin"].unique())
        print(df["Dest"].unique())
        # TODO: make all airport objects

        # TODO: make all flights to connect airports
        #  (just calling add flights should create the required airport objects too)
        # for index, row in df.iterrows():
        #     print(row['Origin'], row['Dest'])

        print(df.groupby(['Origin', 'Dest']).agg())
        # with open('./data/flight_data.csv') as file:
        #     csv_reader = csv.reader(file, delimiter=',')
        #     line_count = 0
        #     for row in csv_reader:
        #         if line_count == 0:
        #             print(f'Column names are {", ".join(row)}')
        #         line_count += 1
        #     print(f'Processed {line_count} lines.')

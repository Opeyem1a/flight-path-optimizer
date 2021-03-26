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

        col_list_price = ['ORIGIN', 'DEST', 'MARKET_FARE']
        df_price = pd.read_csv('./data/flight_price.csv', usecols=col_list_price) \
            .rename(columns={'ORIGIN': 'Origin', 'DEST': 'Dest', 'MARKET_FARE': 'MarketFare'}) \
            .groupby(['Origin',
                      'Dest']) \
            .agg({'MarketFare': ['mean']})

        agg_data = df.groupby(['Marketing_Airline_Network',
                               'Flight_Number_Operating_Airline',
                               'Origin',
                               'Dest',
                               'DayOfWeek'], as_index=False) \
            .agg({'DepTime': ['mean'],
                  'ActualElapsedTime': ['mean'], }) \
            .dropna() \
            .set_index(['Origin', 'Dest'])

        new_data = agg_data.join(df_price, how='inner')

        for index, row in new_data.iterrows():
            src_code = row.name[0]
            dest_code = row.name[1]
            dept_time = row['DepTime']
            duration = row['ActualElapsedTime']
            price = row["MarketFare"]
            self.graph.create_flight(src_code, dest_code, dept_time, duration, price)

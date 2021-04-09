import dill
import pandas as pd
from sklearn.utils import shuffle
import random


class LoadData:
    def __init__(self, graph, is_load, max_outgoing=10, max_airports=365, silent=False):
        self.graph = graph
        self.is_load = is_load
        self.max_outgoing = max_outgoing
        self.max_airports = max_airports
        self.silent = silent

    def load(self):
        self.silent or print('Retrieving data...')
        if self.is_load:
            col_list = ['Operating_Airline ', 'Month', 'DayOfWeek', 'Origin', 'Dest', 'DeptDateTime',
                        'ActualElapsedTime', 'Flight_Number_Marketing_Airline']
            df = pd.read_csv('./data/flight_data_new.csv', usecols=col_list, low_memory=False)
            df = df.dropna()
            df['DeptDateTime'] = pd.to_datetime(df['DeptDateTime'], format='%Y-%m-%d %H:%M')

            col_list_price = ['ORIGIN', 'DEST', 'MARKET_FARE']
            df_price = pd.read_csv('./data/flight_price.csv', usecols=col_list_price, low_memory=False) \
                .rename(columns={'ORIGIN': 'Origin', 'DEST': 'Dest', 'MARKET_FARE': 'MarketFare'}) \
                .groupby(['Origin',
                          'Dest']) \
                .agg({'MarketFare': ['mean']})

            agg_data = df.groupby(['Operating_Airline ',
                                   'Origin',
                                   'Dest',
                                   'Month',
                                   'DayOfWeek',
                                   'Flight_Number_Marketing_Airline'], as_index=False) \
                .agg({'DeptDateTime': ['max'],
                      'ActualElapsedTime': ['mean'], }) \
                .dropna() \
                .set_index(['Origin', 'Dest'])

            new_data = agg_data.join(df_price, how='inner')

            with open('data_df.pkl', 'wb') as f:
                dill.dump(new_data, f)
        else:
            with open('data_df.pkl', 'rb') as f:
                new_data = dill.load(f)

        self.silent or print('Finished retrieving data...')
        throttle_dict = {}
        self.silent or print('Shuffling data...')
        new_data = shuffle(new_data)
        new_data.reset_index()
        print('Loading flight graph...')
        total_rows = len(new_data.index)
        i = 0
        for index, row in new_data.iterrows():
            i += 1
            print(f"\r{i / total_rows * 100:.1f} %", end='')
            src_code = row.name[0]
            dest_code = row.name[1]

            try:
                throttle_dict[str(src_code)] += 1
            except KeyError:
                throttle_dict[str(src_code)] = 1

            try:
                throttle_dict[str(dest_code)] += 1
            except KeyError:
                throttle_dict[str(dest_code)] = 1

            if len(throttle_dict.keys()) > self.max_airports:
                break

            if throttle_dict[str(src_code)] > self.max_outgoing:
                continue

            dept_time = int(pd.Timestamp(row['DeptDateTime'].values[0]).timestamp()) + random.randint(0, 30 * 86400)
            duration = int(row['ActualElapsedTime']) * 60
            price = float(row["MarketFare"])
            self.graph.create_flight(src_code, dest_code, dept_time, duration, price)

        self.silent or print(' - Completed.')
        print()  # just for the new line

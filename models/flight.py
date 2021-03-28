class Flight:
    def __init__(self, destination, dept_time, duration, price):
        self.destination = destination
        self.dept_time = dept_time
        self.duration = duration
        self.price = price

    def get_destination(self):
        return self.destination

    def get_dept_time(self):
        return self.dept_time

    def get_duration(self):
        return self.duration

    def get_price(self):
        return self.price

    def __str__(self):
        from datetime import datetime
        return 'Flight to: ' + self.destination.get_code() \
               + '\tDept Time: ' + datetime.fromtimestamp(self.dept_time).strftime('%Y-%m-%d %H:%M') \
               + '\tDur: ' + str(self.duration) \
               + '\tPrice: $' + str(self.price)

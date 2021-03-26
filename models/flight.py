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

    def set_destination(self, destination):
        self.destination = destination

    def set_dept_time(self, dept_time):
        self.dept_time = dept_time

    def set_duration(self, duration):
        self.duration = duration

    def set_price(self, price):
        self.price = price

class Flight:
    def __init__(self, destination, deptTime, duration, price):
        self.destination = destination
        self.deptTime = deptTime
        self.duration = duration
        self.price = price

    def get_destination(self):
        return self.destination

    def get_deptTime(self):
        return self.deptTime

    def get_duration(self):
        return self.duration

    def get_price(self):
        return self.price

    def set_destination(self, destination):
        self.destination = destination

    def set_deptTime(self, deptTime):
        self.deptTime = deptTime

    def set_duration(self, duration):
        self.duration = duration

    def set_price(self, price):
        self.price = price

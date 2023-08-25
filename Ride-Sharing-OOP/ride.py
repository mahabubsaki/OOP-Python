from datetime import datetime
class Ride:
    def __init__(self,startLocation,endLocation) -> None:
        self.start_location = startLocation
        self.end_location = endLocation
        self.driver = None
        self.start_time = None
        self.rider= None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self,driver):
        self.driver = driver
    def start_ride(self):
        self.start_time = datetime.now()
    def end_ride(self,rider,amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
    def __repr__(self) -> str:
        return f'Ride Details. Started : {self.start_location} to {self.end_location}'

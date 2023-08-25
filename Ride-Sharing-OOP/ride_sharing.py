class Ride_Sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    def add_rider(self,rider):
        self.riders.append(rider)
    def add_driver(self,driver):
        self.drivers.append(driver)
    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}'

from ride import Ride
class Ride_matching:
    def __init__(self,drivers) -> None:
        self.available_drivers = drivers
    def find_driver(self,ride_request):
        if len(self.available_drivers) > 0:
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location,ride_request.end_location)
            driver.accept_ride(ride)
            return ride
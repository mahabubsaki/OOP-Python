from abc import ABC,abstractmethod
from ride_matching import Ride_matching
from ride_request import Ride_Request
class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name = name
        self.email = email
        self.__nid= nid
        self.__id = 0
        self.wallet = 0
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, nid,current_location,initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nid)
    def display_profile(self):
        print(f'Rider with name : {self.name} and email : {self.email}')
    def load_cash(self,amount):
        if(amount > 0):
            self.wallet += amount
    def update_location(self,new_location):
        self.current_location = new_location
    def request_ride(self, ride_sharing, destination):
        if not self.current_ride:
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_matching(ride_sharing.drivers)
            rider = ride_matcher.find_driver(ride_request)
            print(rider)
            self.current_ride = rider
    def show_current_ride(self):
       print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.wallet = 0
        self.current_location = current_location
    def display_profile(self):
        print(f'Driver with name : {self.name} and email : {self.email}')
    def accept_ride(self,ride):
        ride.set_driver(self)

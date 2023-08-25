from abc import ABC,abstractmethod
class Vehicle(ABC):
    speed = {
        'car': 50,
        'bike':60,
        'cng':15
    }
    def __init__(self,vehicle_type,license_plate,rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'Available'
    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    def start_drive(self):
        self.status = 'Unavailable'

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    def start_drive(self):
        self.status = 'Unavailable'

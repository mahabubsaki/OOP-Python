class Phone:
    price = 1900
    color = 'blue'
    brand = 'samsung'

# class methods should always have a self parameter this self parameter is same as this in js

class NewPhone:
    price = 20
    color = "red"
    features = ["camera","speaker","hammer"]

    def call(self):
        print("calling")
    def send_sms(self,phone,sms):
        text = f'sending SMS to : {phone} and message: {sms}'
        return text

#__init__ is same as constructor of js which takes parameter and create objects


class BrandedPhone:
    def __init__(self,brand,price,manufacturer):
        self.brand = brand
        self.price = price
        self.manufactured = manufacturer
    def getMenufacturer(self):
        return self.manufactured


# if we define a property on class and change it this change will reflect on all other object created by that class
class Shop:
    cart = []
    def __init__(self,buyer):
        self.buyer = buyer
    def add_to_cart(self,item):
        self.cart.append(item)
    def get_cart(self):
        return self.cart

# mehzem = Shop("mehzaben")
# nishu =Shop("nishu")

# nishu.add_to_cart("x")
# nishu.add_to_cart("a")
# mehzem.add_to_cart("s")
# mehzem.add_to_cart("a")

# print(mehzem.get_cart())


# mehzem.add_to_cart("shoes") print => ['x', 'a', 's', 'a']


# we can see string representation of a class by __repr__ method. if we print a instance created my class then we will see the string
class Student:
    def __init__(self,name,id,cls) -> None:
        self.name = name
        self.id = id
        self.cls = cls
    
    def __repr__(self) -> str:
        return f'student with name : {self.name}, class : {self.cls} and id : {self.id}'





saki = Student("Saki",12,12)
print(saki)
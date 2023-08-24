

class Company:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fare = []

class Driver:
    def __init__(self,name,license,age) -> None:
        self.name = name
        self.license = license
        self.age = age

class Counter:
    def __init__(self) -> None:
        pass
    def purchase_ticket(self,start,destination):
        pass

class Passenger:
    pass

class Supervisor:
    pass

 
class Device:
    def __init__(self,brand,color,price) -> None:
        self.brand = brand
        self.color = color
        self.price = price
    def run(self):
        return f'brand name is : {self.brand}'
    

# in js we can extend and call super for taking properties from parent. We are doing exactly the same thing here
class Laptop(Device):
    def __init__(self,brand,color,price,memory) -> None:
        super().__init__(brand,color,price)
        self.memory = memory
    def coding(self):
        return f'learning python and practicing'
    def __repr__(self) -> str:
        return f'{self.brand}'

class Phone:
    def __init__(self,brand,color,price,dual_sim) -> None:
        self.dual_sim = dual_sim
    def message(self):
        return f'sending message'
   

# l = Laptop("samsung",color="s",price="s",memory="s")
# print(l)

class Family:
    def __init__(self,address) -> None:
        self.address = address

class School:
    def __init__(self,id,level) -> None:
        self.id = id
        self.level = level

class Sports:
    def __init__(self,game) -> None:
        self.game = game


# we can inherit multiple class like this , but here we cant call super.instead of that we have to call each class with __init__ method to call the parent class

class Student(Family,School,Sports):
    def __init__(self, address,id,level,game) -> None:
        School.__init__(self,id,level)
        Family.__init__(self,address)
        Sports.__init__(self,game)
    def __repr__(self) -> str:
        return f'{self.address} {self.id} {self.level} {self.game}'


# saki = Student("tongi",69,12,"coding")
# print(saki)


#to create a private property in class we can declare the property name with __. This is a way to hide data and control the accessibillity of the data. This is the main concept of encapsulation

class NewBank:
    def __init__(self,holder_name,deposite) -> None:
        self.__holder_name = holder_name
        self.__balance = deposite

# rafsun =NewBank("Saki",200)
# print(rafsun.balance)


# suppose we are inheriting a class and there is a method which we want to be created on all derived class the we have to use abstractmethod


#here Monkey is inheriting the animal class. But we need monkeys own eat method which is already inheriting from animal.to stop this we are doing the following work
from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod # enforcing that eat should be present in all subclass
    def eat(self):
        pass
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self) -> None:
        super().__init__()
    def eat():
        pass


# l = Monkey()

class N:
    n = 2
    def __init__(self,age) -> None:
        self.age = age
        #special + operator method for object adding
    def __add__(self,other):
        return self.age + other.age
    #same as js classes static method but we have to give self as paramter
    @classmethod
    def staticMethod(self):
        self.n+=1
        return 2
      #same as js classes static method but we dont have have to give self as paramter
    @staticmethod
    def staticMethod2():
        return 4
    

# a = N(2)
# b = N(5)
# print(a+b)
# print(N.staticMethod2())

class User:
    def __init__(self,name,age,money) -> None:
        self._name = name
        self._age = age
        self.__money = money
    # this is a method if we want to get back value from this we have to write instance.age() 
    def age(self):
        return self._age
    # this is a property if we want to get back value from this we have to write instance.age same as js class getter
    @property
    def age2(self):
        return self._age
    # this is a method if we want to set value then we have to write instance.setAge(2) 
    def setAge(self,newAge):
        self._age = newAge
    # this is a method if we want to set value then we have to write instance.age2 = 32 .same as js class setter here we have to create getter first and set same name as getter
    @age2.setter
    def age2(self,newAge):
        self._age = newAge



class Family:
    member = []
    @classmethod
    def add_member(self,item):
        self.member.append(item)
    @staticmethod
    def addition(x,y):
        return x+y

# me = Family()
# me.add_member("me")
# my_brother = Family()
# my_brother.add_member("my_brother")
# print(my_brother.member)
# print(my_brother.addition(4,5))

class Vehicl:
    def engine(self):
        print("superclass engine")

class Bus(Vehicl):
    def engine(self):
        print("Bus engine")

class Rickshaw(Vehicl):
    pass


# b = Bus()
# r = Rickshaw()

# b.engine() # Bus engine
# r.engine() #super class engine


class Person:
    def __init__(self,name) -> None:
        self._name = name
    def __repr__(self) -> str:
        return f'name is {self._name}'

class Teacher(Person):
    def __init__(self, name,id) -> None:
        super().__init__(name)
        self._id = id
    def __repr__(self) -> str:
        return f'name is {self._name} and id {self._id}'
class Student(Teacher):
    def __init__(self, name, id,currentClass) -> None:
        super().__init__(name, id)
        self._currentClass = currentClass
    def __repr__(self) -> str:
        return f'name is {self._name} , id is {self._id} and class is {self._currentClass}'


saki = Person("saki")
print(saki) # name is saki
john = Teacher("john",12)
print(john) # name is john and id 12
doe = Student("doe",17,"8th-class")
print(doe) # name is doe , id is 17 and class is 8th-class





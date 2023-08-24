from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Customer(User):
    def __init__(self,name,phone,email,address,money) -> None:
        self.wallet = money
        self.due_amount = 0
        self.__order = None
        super().__init__(name,phone,email,address)
    @property
    def order(self):
        return self.__order
    @order.setter
    def order(self,order):
        self.__order = order
    
    def place_order(self,order):
        self.order = order
        self.due_amount+= order.bill
        print(f'{self.name} placed an order with bill {order.bill}')
    
    def eat_food(self,order):
        print(f'{self.name} item food {order.items}')

    def pay_for_order(self,amount):
        pass

    def give_tips(self,tips_amount):
        pass

    def write_review(self,stars):
        pass
    


class Employee(User):
    def __init__(self, name,phone,email,address,salary,starting_date,department) -> None:
        super().__init__(name,phone,email,address)
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department = department

    def recieve_salary(self):  
        self.due = 0


class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department,cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.cooking_item = cooking_item


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.tips_earning = 0
        super().__init__(name, phone, email, address, salary, starting_date, department)
    
    def take_order(self,order):
        pass

    def transfer_order(self,order):
        pass

    def serve_food(self,order):
        pass
    
    def recived_tips(self,amount):
        self.tips_earning += amount


class Restaurant:
    def __init__(self,name,rent,menu=[]) -> None:
        self.name = name
        self.chef = None
        self.orders =[]
        self.server = None
        self.manager = None
        self.menu = menu
        self.revenue = 0
        self.profit = 0
        self.expense = 0
        self.rent = rent
        self.balance = 0

    def show_employee(self):
        if self.chef is not None:
            print(f'Chef : {self.chef.name} with salary: {self.chef.salary}')
        if self.server is not None:
            print(f'Server : {self.server.name} with salary: {self.server.salary}')
        if self.manager is not None:
            print(f'Manager : {self.manager.name} with salary: {self.manager.salary}')


    def add_order(self,order):
        self.orders.append(order)
    def add_employee(self,employe,employe_type):
        if employe_type == 'chef':
            self.chef =employe
        elif employe_type == 'server':
            self.server = employe
        elif employe_type == 'manager':
            self.manager = employe

    def revieved_payment(self,amount,customer,order):
        if amount >= order.bill:
            self.revenue += amount
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
    

    def pay_expense(self,amount,description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'Not Enough Money for {amount}')
    

    def pay_salary(self,employe):
        if employe.salary < self.balance:
            employe.recieve_salary()


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)



class Food:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
        self.cooking_time = 15


class Burger(Food):
    def __init__(self, name, price,meat,ingredients) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients


class Pizza(Food):
    def __init__(self, name, price,size,toppings) -> None:
        super().__init__(name, price)
        self.size = size 
        self.toppings =toppings


class Drinks(Food):
    def __init__(self, name, price,isCold=True) -> None:
        super().__init__(name, price)
        self.isCold =isCold


class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.burgers = []
        self.drinks = []

    
    def add_menu_item(self,item_type,item):
        if item_type == 'pizza':
            self.pizzas.append(item)
        elif item_type == 'burger':
            self.burgers.append(item)
        elif item_type == 'drinks':
            self.drinks.append(item)
    
    def removePizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
    
    def showMenu(self):
        for pizza in self.pizzas:
            print(f'name : {pizza.name} price: {pizza.price}')
        for burger in self.burgers:
            print(f'name : {burger.name} price: {burger.price}')
        for drink in self.drinks:
            print(f'name : {drink.name} price: {drink.price}')
        


class Order:
    def __init__(self,customer,items) -> None:
        self.customer = customer
        total = 0
        self.items = items
        for item in items:
            total += item.price
        self.bill = total
    


def main():
    menu = Menu()
    pizza_1 = Pizza("Shutki",600,'large',["shutki","onion"])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza("Alu",400,'large',["potato","oil"])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 = Pizza("Dal",500,'large',["dal","oil"])
    menu.add_menu_item('pizza',pizza_3)


    burgur_1 = Burger("Naga",500,"beef",["beef","bun"])
    menu.add_menu_item("burger",burgur_1)
    burgur_2 = Burger("Chicken",500,"chicken",["chicken","bun"])
    menu.add_menu_item("burger",burgur_2)

    coke = Drinks('Coke',50,True)
    menu.add_menu_item('drinks',coke)
    cofee = Drinks('Mocha',300,False)
    menu.add_menu_item("drinks",cofee)
    menu.showMenu()

    restaurent = Restaurant("rustik restaurent",200,menu=menu)
    manager = Manager("kala chan",400,"kala@","tongi",4000,"Jan 1 2020","core")

    restaurent.add_employee(manager,"manager")

    chef =Chef("saki",17,"saki@","tongi",500,"Feb 1 2020","Chef","lol")

    restaurent.add_employee(chef,'chef')

    server = Server("Chotu",6,"nai","restaurent",200,'march 1 2020',"server")

    restaurent.add_employee(server,'server')

    restaurent.show_employee()

    customer_1 = Customer("Sk",141,"SK@GMail.com","banani",5000)
    order_1 = Order(customer_1,[pizza_3,cofee])
    customer_1.pay_for_order(order_1)
    restaurent.add_order(order_1)

    restaurent.revieved_payment(order_1,2000,customer_1)

    customer_2 = Customer("Ska",41,"SKa@GMail.com","banani",50000)
    order_2 = Order(customer_2,[pizza_2,coke])
    customer_2.pay_for_order(order_1)
    restaurent.add_order(order_2)

    restaurent.revieved_payment(order_2,2000,customer_2)


main()
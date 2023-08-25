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
            self.balance -= employe.salary
            self.expense += employe.salary
            employe.recieve_salary()


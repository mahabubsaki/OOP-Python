from menu import Menu
from foods import Pizza,Burger,Drinks
from users import Manager,Chef,Server,Customer
from order import Order
from restaurant import Restaurant
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

    restaurent.revieved_payment(2000,customer_1,order_1)
    print('revenue and balance after first',restaurent.revenue,restaurent.balance)

    customer_2 = Customer("Ska",41,"SKa@GMail.com","banani",50000)
    order_2 = Order(customer_2,[pizza_2,coke])
    customer_2.pay_for_order(order_1)
    restaurent.add_order(order_2)

    restaurent.revieved_payment(2000,customer_2,order_2)
    print('revenue and balance after second',restaurent.revenue,restaurent.balance)

    restaurent.pay_expense(restaurent.rent,"Rent")
    print('revenue and balance after rent',restaurent.revenue,restaurent.balance,restaurent.expense)


main()
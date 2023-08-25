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
        
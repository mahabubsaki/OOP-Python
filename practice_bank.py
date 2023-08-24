class Bank:
    def __init__(self,balance) -> None:
        self.min_withdraw = 100
        self.max_withdraw = 10000
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if(amount > 0):
            self.balance += amount
            return self.balance
    def withdraw(self,amount):
        if(amount > self.min_withdraw and amount < self.max_withdraw and  self.balance - amount > 0):
            self.balance -= amount
            return self.balance
        else:
            return "Invalid with draw"


abc = Bank(15000)

abc.deposit(299)

abc.withdraw(1500)
abc.withdraw(1500)
abc.withdraw(1500)
abc.withdraw(1500)

# print(abc.get_balance())


N, M = map(int, input().split())
A = list(map(int, input().split()))


frq = {}


for num in A:
    if num in frq:
        frq[num] += 1
    else:
        frq[num] = 1


for i in range(1, M + 1):
    if i in frq:
        print(frq[i])
    else:
        print(0)

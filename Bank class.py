class Bank_account:
    def __init__ (self, account_number,balance, date_of_popening,customer_name):
        self.acount_number= account_number
        self.balance= balance
        self.date_of_popening= date_of_popening
        self.customer_name= customer_name
    def deposite(self ,amt):
       self.balance += amt
       return self.balance
    
    def withdrow(self, price):
        self.balance -= price
        return self.balance
    
    def check_balance(self):
        return self.balance
x1=Bank_account(1000, 55.44, "02-01-2020","A")
x2=Bank_account(9003, 55.46, "02-01-2021","b")
print(x1.withdrow(5))
print(x1.deposite(6))

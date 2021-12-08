#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# parent class
class User():
    def _init_(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def Show_details(self):
        print("PERSONAL DETAILS")
        print("")
        print("NAME :-",self.name)
        print("AGE :-",self.age)
        print("GENDER :-",self.gender)
# child class      
class Bank(User):
    def __init__(self,name,age,gender):
        super()._init_(name,age,gender)
        self.balance=0
    def Deposit(self,amount):
        self.amount=amount
        self.balance=self.amount + self.balance
        print("ACCOUNT BALANCE HAS BEEN UPDATED :- ₹",self.balance)
    def Withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("INSUFFICIENT BALANCE :- ₹",self.balance)
        else:
            self.balance=self.balance - self.amount
            print("ACCOUNT BALANCE HAS BEEN UPDATED :- ₹",self.balance)
    def View_balance(self):
        self.Show_details()
        print("ACCOUNT BALANCE :-",self.balance)
b=Bank("shubham",23,"male")
b.Show_details()
b.Deposit(1000)
b.Withdraw(100)
b.View_balance()


# In[ ]:





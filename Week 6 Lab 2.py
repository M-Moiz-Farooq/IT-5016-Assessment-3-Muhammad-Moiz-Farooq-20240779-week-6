'''
Week 6 Lab2
Author: Muhammad Moiz Farooq/20240779
Whitecliffe College, AKL

'''
#class Electric Car
class Car():
    def __init__(self,model,colour,year):
        self.model=model
        self.colour=colour
        self.year=year
    def drive(self):
        print(F"The {self.colour} {self.model} was driving by.")
   
    def stop(self):    
        print(F"The {self.colour} {self.model} stopped.")
    def cardetails(self):
        print(self.colour) 
        print(self.model)  
        print(self.year)
    def carinfo(self):
        print(F"Car Info: {self.colour} {self.year} {self.model} ")
class Electric_car(Car):
    def __init__(self, model, colour, year,batterycapacity):
        super().__init__(model, colour, year)
        self.batterycappacity=batterycapacity
    def carinfo(self):
        super().carinfo()    
        print(F"Battery Capacity:{self.batterycappacity}kwh")
car1=Electric_car("Tesla","Black",2024,75)
car1.drive()
car1.stop()
car1.cardetails()
car1.carinfo()     

# Account Class
class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self._balance=balance
    def deposit(self,ammount):
        if ammount>0:
           self._balance += ammount
           print(F"{ammount} deposited")
        else:
            print("Deposit must be positive")


    def withdraw(self,ammount):
        if 0<ammount<self._balance:
            self._balance -= ammount
            print(F"{ammount} withdrawn")
        else:
            print("Insufficient Balance or Invalid Ammount")
    def getbalance(self):
        return self._balance
account1=Account("Moiz",5000)
account1.deposit(50)
print(account1.getbalance)
account1.withdraw(75)    
print(account1.getbalance)                    

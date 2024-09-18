'''
Week6 Lab 1
Author: Muhammad Moiz Farooq
'''
# Class Person
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(F"Hello, My name is {self.name}, I am {self.age} years old.")
person1=Person("Moiz",19)            
person1.greet()        

# class rectangle
class Rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
rect=Rectangle(4,9)
print(F"Area of the rectangle is: {rect.area()}")
print(F"Perimeter of rectangle is: {rect.perimeter()}")        


# class car
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
        print(F"Car Info: {self.colour} {self.year} {self.model}")

car1=Car("Ferarri","Red",2024)             
car1.drive()
car1.stop()
car1.carinfo()

car1.cardetails()
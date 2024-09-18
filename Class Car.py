'''
Class Car
Author: Muhammad Moiz Farooq/20240779
Whitecliffecollege, AKL

'''
class Car():
    def __init__(self,make,colour,):
        self.make=make
        self.colour=colour
   
    def drive(self):
        print(F"The {self.colour} {self.make} was driving by.")
   
    def stop(self):    
        print(F"The {self.colour} {self.make} stopped.")



car1=Car("toyota","blue") 
car2=Car("honda","white")

car1.drive()
car1.stop()

car2.drive()
car2.stop()
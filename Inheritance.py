'''
Inheritance
Author: Muhammad Moiz Farooq/20240779
Whitecliffe College, AKL

'''
class Animal():
    def __init__(self,name,coloured):
        self.coloured=coloured
        self.name=name
    def speaks(self):    
        print(F"{self.name} makes a sound,")
class Dog(Animal):
    def bark(self):
        print(F"{self.name} barks,")
    def colour(self):
        print(F"{self.name} is {self.coloured} coloured.")    
mydog=Dog("Buddy","gold")
mydog.speaks()
mydog.bark()
mydog.colour()

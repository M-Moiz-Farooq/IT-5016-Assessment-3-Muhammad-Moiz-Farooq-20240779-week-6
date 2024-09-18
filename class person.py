'''
Class Person
Author: Muhammad Moiz Farooq/20240779
Whitecliffe College, AKL
'''


class Person():
    def __init__(self,name,age,) -> None:
        self.name=name
        self.age=age
#creating instances
person1=Person("Moiz",19)
person2=Person("Arsal",23)
person3=Person("Shahryar",18)


#accessing attributes

print(person1.name,":",person1.age)
print(person2.name,":",person2.age)
print(person3.name,":",person3.age)        
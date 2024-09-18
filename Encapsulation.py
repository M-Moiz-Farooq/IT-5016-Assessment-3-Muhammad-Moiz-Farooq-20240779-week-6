'''
Encapsulation
Author: Muhammad Moiz Farooq/20240779
Whitecliffe College, AKL

'''
class Person():
    def __init__(self):
        self.A="James"
        self._B="James Bond"
    def printname(self):
        print(self.A)
        print(self._B)
p = Person()
p.A
p._B

p.printname()



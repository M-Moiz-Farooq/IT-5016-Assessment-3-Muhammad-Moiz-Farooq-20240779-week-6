'''
Vehicle class
Author: Muhammad Moiz Farooq/20240779
Whitecliffe College, AKL

'''
class Vehicle():
      def __init__(self) -> None:
            pass
      def start(self):
            print("Vehicle has started,")
      def stop(self):
            print("Vehicle has stopped.")   
class Car(Vehicle):
      def honk(self):
            print("Honk! Honk!")
myCar=Car()
myCar.start()
myCar.honk()
myCar.stop()
                                             



        
    
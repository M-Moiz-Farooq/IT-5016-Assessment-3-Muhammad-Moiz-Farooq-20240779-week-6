'''
Polymorphism
Autor: Muhmmad Moiz Farooq/20240779
Whitecliffe College, AKL
'''
class Device():
    def turnon(self):
        pass
class TV(Device):
    def turnon(self):
        return "TV is now on"
class Fan(Device):
    def turnon(self):
        return "Fan is now spinning"
class Light(Device):
    def turnon(self):
        return "light is now on"
def activatedevice(device):
    print(device.turnon())
tv=TV()
fan=Fan()
light=Light()
activatedevice(tv)
activatedevice(fan)
activatedevice(light)           
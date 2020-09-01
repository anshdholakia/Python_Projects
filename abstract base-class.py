# from abc import ABCMeta,abstractmethod     #  can be used in older versions
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=4
        self.breath=5

    def printarea(self):
        return self.length*self.breath

rect1=Rectangle()
print(rect1.printarea())
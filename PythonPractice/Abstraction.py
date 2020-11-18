
from abc import ABC, abstractmethod

class House(ABC):
    def sqfeet(self, size):
        print("Square footage: ", size)

    @abstractmethod
    def criteria(self, size):
        pass


class HousingOptions(House):
    #define how to implement criteria function from parent class
    def criteria(self, size):
        print('This house is {} square feet. It fulfills your housing criteria of 1600 square feet.'.format(size))


option1 = HousingOptions()
option1.sqfeet(1800)
option1.criteria(1800)

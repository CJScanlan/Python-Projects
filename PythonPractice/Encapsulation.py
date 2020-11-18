
class Dogs:
    def __init__(self):
        self._breed = "Lab"
        self.__color = "Black"
        self.__name = ""

    def getBreed(self):
        print(self._breed)

    def getColor(self):
        print(self.__color)

    def setName(self, name):
        self.__name = name

    def getName(self):
        print(self.__name)
    

obj = Dogs()
obj.getBreed()
obj.setName("Luna")
obj.getName()


#create parent class
class Pet:
    name = "Unknown"
    age = ""
    pet_type = ""
    color = ""
    food = ""
    
    def __init__(self, name, age, pet_type, color, food):   #used to initialize objects in class
        self.name = name
        self.age = age
        self.pet_type = pet_type
        self.color = color
        self.food = food
        
    def information(self):
        msg = "{} is a {} old {} {} who prefers to eat {}.".format(self.name,self.age,self.color,self.pet_type,self.food)
        return msg



if __name__ == "__main__":
    dog = Pet("Luna", "4 month", "dog", "black", "kibble")   #create new instance of pet class
    print(dog.information())
    cat = Pet("Cheeto", "1 year", "cat", "orange", "kibble")
    print(cat.information())
    hamster = Pet("Tubby", "1 year", "hamster", "tan", "sunflower seeds")
    print(hamster.information())

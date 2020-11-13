
class Student:
    #Define the attributes of the class
    name = "No name provided"
    email = ""
    GPA = 0.0
    class_credits = 0

    def __init__(self, name, email, GPA, class_credits):
        self.name = name
        self.email = email
        self.GPA = GPA
        self.class_credits = class_credits

class Graduate(Student):
    thesis_subject = ""
    thesis_advisor = ""

class UnderGraduate(Student):
    major = ""
    graduation_date = ""



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

    def getInfo(self):
        msg = "\nName: {}\nEmail: {}\nGPA: {}\nClass Credits: {}".format(self.name,self.email,self.GPA,self.class_credits)
        return msg
        

class Graduate(Student):
    thesis_subject = ""
    thesis_advisor = ""

    def getInfo(self):
        msg = "\nName: {}\nEmail: {}\nGPA: {}\nClass Credits: {}\nThesis Subject: {}\nThesis Advisor: {}".format(self.name,self.email,self.GPA,self.class_credits,self.thesis_subject,self.thesis_advisor)
        return msg

class UnderGraduate(Student):
    major = ""
    graduation_date = ""

    def getInfo(self):
        msg = "\nName: {}\nEmail: {}\nGPA: {}\nClass Credits: {}\nMajor: {}\nGraduation Date: {}".format(self.name,self.email,self.GPA,self.class_credits,self.major,self.graduation_date)
        return msg

class Study_Level():
    def __init__(self, Type, NoOfyears, CgpaCriteria):
        self.Type = Type
        self.NoOfyears = NoOfyears
        self.CgpaCriteria = CgpaCriteria

class Student(Study_Level):
    def __init__(self, Type, NoOfyears, CgpaCriteria, Section ):
        self.Section = Section
        Study_Level.__init__(self, Type, NoOfyears, CgpaCriteria)

    def details(self):
        print("My type is {}".format(self.Type))
        print("My no of years are {}".format(self.NoOfyears))
        print("My gpa is {}".format(self.CgpaCriteria))
        print("My section is {}".format(self.Section))
a = Student(input("Tell you Type: "), input("Tell you Years: "),input("Tell you Section: "), input("Tell you Gpa: ") )
a.details()

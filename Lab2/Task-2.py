class Person():
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
    def display(self):
        print(self.Name)
        print(self.Age)
    def details(self):
        print("My name is:  {}".format(self.Name))
        print("My id is: {}".format(self.Age))

class Student(Person):
    def __init__(self, Name, Age, Section):
        self.Section = Section
        Person.__init__(self, Name, Age)

    def details(self):
        print("My name is {}".format(self.Name))
        print("Age: {}".format(self.Age))
        print("Section: {}".format(self.Section))
a = Student('Anoushah', 20 , 593)
a.display()
a.details()

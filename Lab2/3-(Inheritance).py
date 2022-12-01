class Person():
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
    def details(self):
        print("My name is:  {}".format(self.name))
        print("My id is: {}".format(self.idnumber))

class Employee(Person):
    def __init__(self, name, idnumber, salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("ID number: {}".format(self.idnumber))
        print("Salary: {}".format(self.salary))
        print("Post: {}".format(self.post))
a = Employee('Anoushah', 460009 , 1000000, "CEO")
a.display()
a.details()

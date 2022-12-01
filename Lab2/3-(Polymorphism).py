class Human:
    def intro(self):
        print("There are many types of Humans.")

    def Nature(self):
        print("Most of the Humans are toxic")

class Female(Human):
    def Nature(self):
        print("Females are kind-natured.")

class Male(Human):
    def Nature(self):
        print("Males are toxic.")

obj_Human = Human()
obj_Female= Female()
obj_male = Male()

obj_Human.intro()
obj_Human.Nature()

obj_Female.intro()
obj_Female.Nature()

obj_male.intro()
obj_male.Nature()

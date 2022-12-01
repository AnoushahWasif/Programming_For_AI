class Cat:
    attr1 = "Cute"
    attr2 = "Silly"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))
Billy = Cat("Meow")
Tom = Cat("Meeo")
Hellen = Cat("Ohha")
Ridge = Cat("Me-oh")

Billy.speak()
Tom.speak()
Hellen.speak()
Ridge.speak()

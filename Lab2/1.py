class Cat:
    attr1 = "Cute"
    attr2 = "Silly"

    def __init__(self, name):
        self.name = name

# cat type obj (initiation)
Billy = Cat("Rodger")
Tom = Cat("Tommy")
Hellen = Cat("Tommy")
Ridge = Cat("Tommy")

print("Billy is a {}".format(Billy.__class__.attr1))
print("Tom is also a {}".format(Tom.__class__.attr1))
print("Hellen is a {}".format(Hellen.__class__.attr2))
print("Ridge is also {}".format(Ridge.__class__.attr2))

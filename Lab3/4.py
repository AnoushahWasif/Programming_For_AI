class Refrigerator():
    def __init__(self):
        self.__Price = "345"

    def show(self):
        print(self.__Price)
Price = Refrigerator()
Price.show()
Price._Refrigerator__Price = "new"
Price.show()

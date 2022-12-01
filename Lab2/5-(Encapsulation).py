class base:
  def __init__(self):
    self.a = "Multilevel Hierarchy"
    self.__c = "Multilevel Hierarchy"
class derived(base):
  def __init__(self):
    base.__init__(self)
    print("Calling private member of base class: ")
    print(self.__c)

  obj1 = base()
  print(obj1.a)

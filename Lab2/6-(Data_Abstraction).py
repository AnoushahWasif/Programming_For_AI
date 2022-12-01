class myclass:

  __hiddenvariable = 0

  def add(self, increment):
    self.__hiddenvariable += increment
    print(self.__hiddenvariable)

myObject = myclass()
myObject.add(2)
myObject.add(5)
print(myObject._myclass__hiddenvariable)

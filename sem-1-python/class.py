class Person:
  def __init__(self, name, rollNo, mark):
    self.a1 = name
    self.a2 = rollNo
    self.a3 = mark

  def printname(self):
    print(self.a1, self.a2,self.a3)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Tobin K Tomy", "59",120)
x.printname()

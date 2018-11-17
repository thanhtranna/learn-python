class Parent:
  def myMethod(self):
    print('Calling parent method')

class Child(Parent):
  def myMethod(self):
    print('Calling child method')
  # pass

c = Child()
c.myMethod()
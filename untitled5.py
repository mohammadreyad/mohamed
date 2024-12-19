class Person():
    counter=0
    def __init__(self, name="No_name"):
        self.name=name
        type(self).counter=self.counter + 1
        print(name + " has been created!")
    def __del__(self):
        print (self.name + " says bye-bye!")
        type(self).counter=self.counter-1

x = Person()
print("Number of current instances: ", Person.counter)
y = Person()
print("Number of current instances: ", Person.counter)
z = Person()
print("Number of current instances: ", Person.counter)

del x
print("Number of current instances: ", Person.counter)
del y
print("Number of current instances: ", Person.counter)

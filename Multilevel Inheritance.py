class A: 
    def description(self):
        print("Desc from A")
        
class B(A):
    def description(self):
        print("Desc from B")
        
    def Hint(self):
        print("Hint from B")

class C(B): # Child Class
    def Info(self):
        print("Info from C")

obj= C()
obj.description()
obj.Hint()
obj.Info()
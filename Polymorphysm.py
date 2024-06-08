# polymorphism in python

# polymorphism is nothing but same object having differnt behaviours

# Overriding : whenever the parent class and childclass have same method name and same 
# parameter is called polymorhidms ... 

# here is also pareant class and child classs having the same methods 
# but differnt outputs means : same object having differnt behaviors

class ParentClass :
    def print_self(self):
        print('A')
        
class ChildClass :
    def print_self(self):
        print('B')
        
object_A =ParentClass()        # object of parent class
object_B = ChildClass()         # object of childclass

object_A.print_self()      #calling with object 
object_B.print_self()      # calling with object 



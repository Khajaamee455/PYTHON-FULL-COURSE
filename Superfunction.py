# superfuctions in python 

class ParentClass:
    def print_test(self):
        print("This is parent class method")
        
class ChildClass :
    def print_test(self):
        print("This is child class method")
# if u want to call the parent method u can call using super function (same as super keyword in java)
        
        super().print_test()     
child_instance = ChildClass()
child_instance.print_test()
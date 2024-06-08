# match case is intruduced in python 3.10 
# additional feature same as like that switch case in java .
# this is new feature of python old course dont ask about this topic ...

a = 4   # if u change the value like 0 it will print case not found thats the defualt case ...

match a :
    case 1 :
        print("this is case 1")
    case 2 :
        print("this is case 2")
    case 3 :
        print("this is case 3")
    case 4 :
        print("this is case 4")        # this case is matched it will print this
    case _:
        print("case not found")
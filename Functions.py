# funtions in python ..
# we can create a function with def keyword in python

# Example 1 
def hello():  
    print("Hello world")
hello()

# created a function with def keyword inside the function we print hello world 
# out of the fuction we called that function 

# Example 2 
# using return keyword 

def add(x , y):
    print("x is %s , y is %s " %(x,y))
    return x + y 

add(1,3)

# positianal arguments 
def varargs(*args):
    return args
varargs(1,2,3)


# returning multiples
def swap(x,y):
    return y,x
x=1 
y=4
x,y = swap(x,y)
print("x =",x)
print("y=",y)

# defult values 

def add(x , y=10):
    return x + y
print(add(40))
print (add(10 ,20))

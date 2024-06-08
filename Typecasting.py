# types casting in python

x = int(1)  # x will be one 
y = int (8.9) # y will be 8 now 
z = int("3")  # z will be 3 now

print(x)
print(y)
print(z)

# this is how typecasiting works 

f = "10"
# if i print this
print(f)

# what am telling is add 10 more to f 
#print(f+10)    # it will give an error called cannot concatinate with strings 

# if i will convert the f to int and then i will add 10 to it ..

print(int(f) +10)   # now 20 will be the output ...
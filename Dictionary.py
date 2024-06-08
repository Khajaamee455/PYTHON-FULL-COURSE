# dictionarys in python

# this is an empty dictinary
dict1 = {}

print(dict1)
print(type(dict1))

#Note dont confuse with sets 
a = set()  # this is an empty set 
print(a)
print(type(a))

# dict is a key-value paired 
# we can access the dict using keys and get their values like 

dict2 ={"physics":95 , "chemistry": 87 , "mathamatics":89 , "biology":88}

# here physics is key and 95 is value , we can print the values using their keys 

print(dict2.get("physics"))    # getting physics marks means value 95

# if am print 
print(dict2.get("kannada"))   # here i got none

# because kannada is not defied in this dict2....
# their is lot of methods u can explore more like dict2 .get ,key ,etc
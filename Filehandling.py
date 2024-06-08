# file handling in python is easy compare to java file handling 

# if you want to read whats inside the file you just do this 

with open ("file.txt") as file:
    for line in file:
        print(line)
        
# it printing the lines in that file file.txt

# this will print the line with numbers like 1 ,2,3 ,4 ...
file = open('file.txt', 'r')
for i, line in enumerate(file, start=1):
    print("Number %s: %s" % (i, line))


#write a lines in file 
contents = {"Name ":"khaja" , "age":24 , "Colur":"Brown"}
with open ("file.txt" , "w+") as file:
    file.write(str(contents))
    
# reading the file 
with open ("file.txt" , "r+") as file:
    contents = file.read()
    print(contents)
    
    
# write an object in file
import json
contents = {"Name":"khaja ", "age":24 , "language":"kannada"}
with open ("file.txt", "w+") as file:
    contents = file.write(json.dumps(contents))


# reading the json data 

import json
with open ("file.txt" , "r+") as file:
    contents = json.load(file)
print(contents)


# Deleting a file in python

# import os
# os.remove("text.txt")

# checking and deleting the file in python 

import os 
if os.path.exists("mine.txt"):
    os.remove("mine.txt")
else :
    print("file not found")
    

# Deleting hole folder 
import os
os.rmdir("myfolder")

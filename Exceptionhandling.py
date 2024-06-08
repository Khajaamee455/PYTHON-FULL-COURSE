# Exception is nothing but an unwanted / abnormal situation occurs at runtime 
# terminate the programm flow 

# Exception handling is we have an alternative source to handle those exceptions using except and finnaly blocks 

# using these block we can handle the exception and privent the abnormal behaviour of the programme

try :
    raise IndexError("This is an index error")
except IndexError as e:
    pass
except(TypeError ,NameError):
    pass
else:
    print('All good..')
finally:
    print("we can clean the resources ..")
    

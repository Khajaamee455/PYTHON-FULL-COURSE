
#constructor in  python 

class Animal :
    def __init__(self, voice):
        self.voice = voice
cat = Animal ('meow')
print(cat.voice)

dog =Animal('bark')
print(dog.voice)
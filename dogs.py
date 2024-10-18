class Orchestra(object):
    def __init__(self):
        self.dogs = []
    
    def addSinger(self, dogName):
        self.dogs.append(dogName)

    def sing(self):
        for i in self.dogs:
            i.woof()

class Dogs(object):
    def __init__(self, name):
        self.name = name
    def woof(self):
        print("Wooof")



class Cats(object):
    def __init__(self, name):
        self.name = name
    def meow(self):
        print("Meow")


class CatAdapter(Dogs):
    def __init__(self, name):
        super(CatAdapter, self).__init__(name)
        self.cat = Cats(name)

    def bark(self):
        return self.cat.meow()
#method_overloading
class baseclass:
    def __init__(self):
        pass
    def example(self,a,b):
        print("first method of base class")
class child(baseclass):
    def __init__(self):
        pass
    def example(self,a,b,c):
        print("second method")
class child2(baseclass):
    def __init__(self):
        pass
    def example(self,a,b,c,d):
        print("third method")
obj=child()
obj.example(1,2,3)
#method_overriding
class father:
    def printjob(self):
        print("father")
class boy(father):
    def printjob(self):
        print("boy")
c=boy()
c.printjob()


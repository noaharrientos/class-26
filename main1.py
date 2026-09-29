class IOstring():
    def __init__(self):
        self.str1=""
    def getstring(self):
        self.str1=input("Enter a string")
    def printstring(self):
        print(f"Result is {self.str1}")
object1 = IOstring()
object1.getstring()
object1.printstring()
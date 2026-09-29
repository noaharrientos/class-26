class fruits:
    def __init__(self,name,season,texture):
        self.name=name
        self.season=season
        self.texture=texture
    def display(self):
        print(f"The name of the fruit is {self.name}, the season that this fruit is found in is {self.season} and the texture of the fruit is {self.texture}.")
    def __del__(self):
        print(f"This is a destructer getting called")
object1 = fruits("Mango","Summer","Soft")
object1.display()
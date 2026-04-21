# Design a class Lion having method roar() and a class Cub having method play() which inherits class Lion. Use instance of Cub called- simba to access methods roar() and play(). Define public attribute legs, protected attribute ears and private attribute mane of class Lion. Show accessibility of these variables according to their scope.


class Lion:

    def __init__(self):
        self.legs = 4                # Public
        self._ears = 2               # Protected
        self.__mane = "Thick"        # Private

    def roar(self):
        print("Lion roars ")

    # Method to access private variable
    def show_mane(self):
        print("Mane: ", self.__mane)

class Cub(Lion):

    def play(self):
        print("Cub is Playing")

simba = Cub()

simba.roar()
simba.play()

print("\nAccessing Variables: ")

print("Legs: ", simba.legs)
print("Ears: ", simba._ears)

simba.show_mane()


from random import randint

class Bird:

    def __init__(self, world):

        self.world = world
        self.health = self.constitution_roll()

    # Not all birds are created equal lol
    # It would make sense to simulate some variability to the constitution of each bird
    def constitution_roll ():
        base = 100
        variability = 5
        return randint (base - variability, base + variability)

    def eat ():

        self.health += self.food_benifit

    def injured ():

        self.health -= self.injury_cost

    def display ():

        self.health -= self.display_cost

    def die ():

        self.world.birds.remove (self)

    def update():

        pass

    
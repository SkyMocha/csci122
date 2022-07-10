from random import seed

class World:

    def __init__(self, seedNum): # Constructor (Python is weird LOL)

        seed(seedNum)
        print (f'creating world w/ seed num {seedNum}')
        self.birds = []


    def update ():
        
        for b in self.birds: 

            b.update()

    # Gives free food to num random birds
    def free_food (num):

        for i in range (num):

            choice(self.birds).eat()
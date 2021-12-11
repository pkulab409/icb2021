from pgzero.actor import Actor

class SeedBank(Actor):
    def __init__(self):
        Actor.__init__(self,image='others/seedbank')
        self.left,self.top = 40,- self.height
        self.position = False
        self.speed = 5

    def move(self):
        if self.top < 0:
            self.top += self.speed
        else:
            self.top = 0
            self.position = True
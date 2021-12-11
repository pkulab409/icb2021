from pgzero.actor import Actor

class CarImage():
    def __init__(self):
        self.car_image = 1 


class Car(Actor):
    def __init__(self,L):
        Actor.__init__(self,"others/lawnmower")

        self.left = - self.width
        self.L = L
        self.active = False
        self.speed = 4

    def move1(self):
        if self.right < self.L+54:
            self.left += self.speed
        else:
            self.right = self.L+54

    def move2(self):
        self.left += self.speed
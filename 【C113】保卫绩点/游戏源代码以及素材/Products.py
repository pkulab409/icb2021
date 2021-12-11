from random import *
from pgzero.actor import Actor
from pygame import Rect

class ProductsImages():
    def __init__(self):
        # 阳光图片
        self.sun_images = []
        self.sun_images.extend([\
            "plants/sunflower/sunlight_1", \
            "plants/sunflower/sunlight_2", \
            "plants/sunflower/sunlight_3", \
            "plants/sunflower/sunlight_4", \
            "plants/sunflower/sunlight_5", \
            "plants/sunflower/sunlight_6", \
            "plants/sunflower/sunlight_7", \
            "plants/sunflower/sunlight_8", \
            "plants/sunflower/sunlight_9", \
            "plants/sunflower/sunlight_10", \
            "plants/sunflower/sunlight_11", \
            "plants/sunflower/sunlight_12", \
            ])

        # 弹丸图片
        self.bullet_image = "plants/peashooter/bullet"
        self.firebullet_images = []
        self.firebullet_images.extend([\
            "plants/torchwood/fire_bullet1", \
            "plants/torchwood/fire_bullet2" \
            ])


class Sun(Actor):
    def __init__(self, T,L,images,level=1):
        Actor.__init__(self,image='plants/sunflower/sun_1')

        self.images = images.sun_images
        self.top, self.left = T, L
        self.rect1 = Rect(self.left, self.top, self.width, self.height) 
        self.rect2 = Rect(self.left, self.top, self.width, self.height) 
        self.rect1.left,self.rect1.top = randint(125,470), 87 - self.rect1.height
        self.rect2.centerx, self.rect2.centery = self.x, self.top + 30
        self.index_image = 0
        self.num_image = 12
        self.speed1 = 2
        self.speed2 = 1
        self.speed3 = 10
        self.position = randint(335, 480)
        self.count_time = 0
        self.is_supply = True   #系统提供True 向日葵生成False
        self.gather = False
        self.get_position = False
        self.level = level

    def move1(self): #下落
        if self.top < self.position:
            self.top += self.speed1
        else:
            self.top = self.position

    def move2(self):#植物头顶
        if self.top > self.position:
            self.top -= self.speed2
        else:
            self.top = self.position
            
    def move3(self):#gather
        if self.x > 79:
            self.x -= self.speed3
        else:
            self.x = 79
        if self.y > 36:
            self.y -= self.speed3
        else:
            self.y = 36
        if self.x == 79 and self.y == 36:
            self.get_position = True


class Bullet(Actor):
    def __init__(self,bg_size,positon,images,level=1):
        Actor.__init__(self,'plants/peashooter/bullet')

        self.bullet_image = images.bullet_image
        self.firebullet_images = images.firebullet_images
        self.rect = Rect(self.left, self.top, self.width, self.height) 
        self.index_image = 0
        self.num_image = 2
        self.left,self.top = positon[0] + 110 , positon[1] + 70
        self.rect.left,self.rect.top = self.left,self.top
        self.screenwidth = bg_size[0]
        self.shoot = False
        self.speed = 5
        self.is_bullet = True
        self.level = level

    def move(self):
        self.left += self.speed
        if self.left >= self.screenwidth:
            self.shoot = False
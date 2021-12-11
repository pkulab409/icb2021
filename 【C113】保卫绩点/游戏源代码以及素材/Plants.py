from random import *
from pgzero.actor import Actor

class PlantsImages():
    def __init__(self):
        # 向日葵图片
        self.sunflower_card_image = "plants/sunflower/sunflower_card"
        self.sunflower_images = []
        self.sunflower_images.extend([ \
            "plants/sunflower/sunflower1", \
            "plants/sunflower/sunflower2", \
            "plants/sunflower/sunflower3", \
            "plants/sunflower/sunflower4", \
            "plants/sunflower/sunflower5", \
            "plants/sunflower/sunflower6", \
            "plants/sunflower/sunflower7", \
            "plants/sunflower/sunflower8", \
            "plants/sunflower/sunflower9", \
            "plants/sunflower/sunflower10", \
            "plants/sunflower/sunflower11", \
            "plants/sunflower/sunflower12", \
            ])

        # 豌豆射手图片
        self.peashooter_card_image = "plants/peashooter/peashooter_card"
        self.peashooter_images = []
        self.peashooter_images.extend([ \
            "plants/peashooter/peashooter1", \
            "plants/peashooter/peashooter2", \
            "plants/peashooter/peashooter3", \
            "plants/peashooter/peashooter4", \
            "plants/peashooter/peashooter5", \
            "plants/peashooter/peashooter6", \
            "plants/peashooter/peashooter7", \
            "plants/peashooter/peashooter8", \
            "plants/peashooter/peashooter9", \
            "plants/peashooter/peashooter10", \
            "plants/peashooter/peashooter11", \
            "plants/peashooter/peashooter12" \
            ])

        # 坚果图片
        self.wallnut_card_image = "plants/wallnut/wallnut_card"
        self.wallnut_ok_images = []
        self.wallnut_ok_images.extend([ \
            "plants/wallnut/wallnut1", \
            "plants/wallnut/wallnut2", \
            "plants/wallnut/wallnut3", \
            "plants/wallnut/wallnut4", \
            "plants/wallnut/wallnut5", \
            "plants/wallnut/wallnut6", \
            "plants/wallnut/wallnut7", \
            "plants/wallnut/wallnut8", \
            "plants/wallnut/wallnut9", \
            "plants/wallnut/wallnut10", \
            "plants/wallnut/wallnut11", \
            "plants/wallnut/wallnut12", \
            "plants/wallnut/wallnut13", \
            "plants/wallnut/wallnut14", \
            "plants/wallnut/wallnut15", \
            "plants/wallnut/wallnut16" \
            ])
        self.wallnut_c1_images = []
        self.wallnut_c1_images.extend([ \
            "plants/wallnut/wallnut_cracked1_1", \
            "plants/wallnut/wallnut_cracked1_2", \
            "plants/wallnut/wallnut_cracked1_3", \
            "plants/wallnut/wallnut_cracked1_4", \
            "plants/wallnut/wallnut_cracked1_5", \
            "plants/wallnut/wallnut_cracked1_6", \
            "plants/wallnut/wallnut_cracked1_7", \
            "plants/wallnut/wallnut_cracked1_8", \
            "plants/wallnut/wallnut_cracked1_9", \
            "plants/wallnut/wallnut_cracked1_10", \
            "plants/wallnut/wallnut_cracked1_11" \
            ])
        self.wallnut_c2_images = []
        self.wallnut_c2_images.extend([ \
            "plants/wallnut/wallnut_cracked2_1", \
            "plants/wallnut/wallnut_cracked2_2", \
            "plants/wallnut/wallnut_cracked2_3", \
            "plants/wallnut/wallnut_cracked2_4", \
            "plants/wallnut/wallnut_cracked2_5", \
            "plants/wallnut/wallnut_cracked2_6", \
            "plants/wallnut/wallnut_cracked2_7", \
            "plants/wallnut/wallnut_cracked2_8", \
            "plants/wallnut/wallnut_cracked2_9", \
            "plants/wallnut/wallnut_cracked2_10", \
            "plants/wallnut/wallnut_cracked2_11", \
            "plants/wallnut/wallnut_cracked2_12", \
            "plants/wallnut/wallnut_cracked2_13", \
            "plants/wallnut/wallnut_cracked2_14", \
            "plants/wallnut/wallnut_cracked2_15" \
            ])
        self.wallnut_pf_images = []
        self.wallnut_pf_images.extend([ \
            "plants/wallnut/wallnut_pf", \
            "plants/wallnut/wallnut_pf" \
            ])

        # 火炬图片
        self.torchwood_card_image = "plants/torchwood/torchwood_card"
        self.torchwood_images = []
        self.torchwood_images.extend([ \
            "plants/torchwood/torchwood1", \
            "plants/torchwood/torchwood2", \
            "plants/torchwood/torchwood3", \
            "plants/torchwood/torchwood4", \
            "plants/torchwood/torchwood5", \
            "plants/torchwood/torchwood6", \
            "plants/torchwood/torchwood7", \
            "plants/torchwood/torchwood8", \
            "plants/torchwood/torchwood9" \
            ])

        #level up 图片
        self.level_up_card_image = "plants/level_up"

        # 铲子图片
        self.shovel_card_image = "plants/shovel/shovel_card"
        self.shovel_images = []
        self.shovel_images.extend(["plants/shovel/shovel"])



class SunFlower(Actor):
    def __init__(self,images,level=1):
        Actor.__init__(self,"plants/sunflower/sunflower_card")

        self.card_image = images.sunflower_card_image
        self.left,self.top = 125,8
        self.images = images.sunflower_images
        self.shadow_rectx,self.shadow_recty = -10,50
        self.index = 1
        self.level = level
        self.index_image = 0
        self.num_image = 12
        self.price = 45 + level*5
        self.count_time = 0
        self.create_time = randint(12,22)
        self.blood_max = 3 + level*2
        self.blood = 3 + level*2
        self.attacked = False
        self.num_az = 0
    
    def level_up(self):
        self.level += 1
        self.create_time = randint(12,22)
        self.blood_max += 2
        self.blood += 2


class Peashooter(Actor):
    def __init__(self,images,level=1):
        Actor.__init__(self,"plants/peashooter/peashooter_card")

        self.card_image = images.peashooter_card_image
        self.left,self.top = 180,8
        self.images = images.peashooter_images
        self.shadow_rectx, self.shadow_recty = -11, 45
        self.index = 2
        self.level = level
        self.index_image = 0
        self.num_image = 12
        self.price = 80 + level*20
        self.blood_max = 3 + level*2
        self.blood = 3 + level*2
        self.count_time = 0
        self.attacked = False
        self.num_az = 0

    def level_up(self):
        self.level += 1
        self.blood_max += 2
        self.blood += 2
        self.price += 20


class WallNut(Actor):
    def __init__(self,images,level=1):
        Actor.__init__(self,"plants/wallnut/wallnut_card")

        self.card_image = images.wallnut_card_image
        self.left,self.top = 235,8

        self.ok_images = images.wallnut_ok_images
        self.index_ok_image = 0
        self.num_ok_image = 16

        self.c1_images = images.wallnut_c1_images
        self.index_c1_image = 0
        self.num_c1_image = 11

        self.c2_images = images.wallnut_c2_images
        self.index_c2_image = 0
        self.num_c2_image = 15

        self.pf_images = images.wallnut_pf_images
        self.index_pf_image = 0
        self.num_pf_image = 1

        self.shadow_rectx,self.shadow_recty = -10,50
        self.index = 3
        self.level = level
        self.images = self.ok_images
        self.index_image = self.index_ok_image
        self.num_image = self.num_ok_image

        self.price = 35 + level*15
        self.blood_max = 25 + level*20
        self.blood = 25 + level*20
        self.attacked = False
        self.pf = False
        self.num_az = 0

    def level_up(self):
        self.level += 1
        self.price += 15
        self.blood_max += 20
        self.blood += 20
    
    def npf(self):
        self.blood += self.blood_max*2
        self.images = self.pf_images
        self.index_image = self.index_pf_image
        self.num_image = self.num_pf_image


class Torchwood(Actor):
    def __init__(self,images,level=1):
        Actor.__init__(self,"plants/torchwood/torchwood_card")

        self.card_image = images.torchwood_card_image
        self.left, self.top = 290,8
        self.images = images.torchwood_images
        self.shadow_rectx, self.shadow_recty = -8, 60
        self.index = 4
        self.level = level
        self.index_image = 0
        self.num_image = 9
        self.price = 160 + level*15
        self.blood_max = 3 + level*2
        self.blood = 3 + level*2
        self.attacked = False
        self.num_az = 0
    
    def level_up(self):
        self.level += 1
        self.blood_max += 2
        self.blood += 2
        self.price += 15


class Shovel(Actor):
    def __init__(self,images,level=1):
        Actor.__init__(self,"plants/shovel/shovel_card")
        self.card_image = images.shovel_card_image
        self.left, self.top = 483,1
        self.images = images.shovel_images
        self.index = 5
        self.price = 0
        self.level = 1
    
    def level_up(self):
        pass

class Level_up(Actor):
    def __init__(self,images,level=1):
        Actor.__init__(self,"plants/level_up")
        self.card_image = images.level_up_card_image
        self.left, self.top = 345,8
        self.index = 6
        self.level = 1
        if level<=4:
            self.price = 500*self.level
        else:
            self.price = 1000*self.level-2000

    
    def level_up(self):
        self.level += 1
        if self.level<=4:
            self.price += 500
        else:
            self.price += 1000
        
        
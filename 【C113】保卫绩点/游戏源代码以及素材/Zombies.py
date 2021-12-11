from pgzero.actor import Actor
from random import *
import sys
import os

os.chdir(sys.path[0])

class ZombiesImages():
    def __init__(self):
        self.oz1_images = []  # 原始僵尸1图片
        self.oz1_images.extend([ \
            "zombies/zombie1/zombie1_1", \
            "zombies/zombie1/zombie1_2", \
            "zombies/zombie1/zombie1_3", \
            "zombies/zombie1/zombie1_4", \
            "zombies/zombie1/zombie1_5", \
            "zombies/zombie1/zombie1_6", \
            "zombies/zombie1/zombie1_7", \
            "zombies/zombie1/zombie1_8", \
            "zombies/zombie1/zombie1_9", \
            "zombies/zombie1/zombie1_10", \
            "zombies/zombie1/zombie1_11", \
            "zombies/zombie1/zombie1_12", \
            ])

        self.oz2_images = []  # 原始僵尸2图片
        self.oz2_images.extend([ \
            "zombies/ordinaryzombie/zombie2_1", \
            "zombies/ordinaryzombie/zombie2_2", \
            "zombies/ordinaryzombie/zombie2_3", \
            "zombies/ordinaryzombie/zombie2_4", \
            "zombies/ordinaryzombie/zombie2_5", \
            "zombies/ordinaryzombie/zombie2_6", \
            "zombies/ordinaryzombie/zombie2_7", \
            "zombies/ordinaryzombie/zombie2_8", \
            "zombies/ordinaryzombie/zombie2_9", \
            "zombies/ordinaryzombie/zombie2_10", \
            "zombies/ordinaryzombie/zombie2_11", \
            "zombies/ordinaryzombie/zombie2_12", \
            "zombies/ordinaryzombie/zombie2_13", \
            "zombies/ordinaryzombie/zombie2_14", \
            "zombies/ordinaryzombie/zombie2_15", \
            "zombies/ordinaryzombie/zombie2_16", \
            "zombies/ordinaryzombie/zombie2_17", \
            "zombies/ordinaryzombie/zombie2_18", \
            "zombies/ordinaryzombie/zombie2_19", \
            "zombies/ordinaryzombie/zombie2_20", \
            "zombies/ordinaryzombie/zombie2_21", \
            "zombies/ordinaryzombie/zombie2_22", \
            "zombies/ordinaryzombie/zombie2_23", \
            "zombies/ordinaryzombie/zombie2_24", \
            "zombies/ordinaryzombie/zombie2_25", \
            "zombies/ordinaryzombie/zombie2_26", \
            "zombies/ordinaryzombie/zombie2_27", \
            "zombies/ordinaryzombie/zombie2_28", \
            "zombies/ordinaryzombie/zombie2_29", \
            "zombies/ordinaryzombie/zombie2_30", \
            "zombies/ordinaryzombie/zombie2_31" \
            ])

        self.oza_images = []  # 原始僵尸攻击图片
        self.oza_images.extend([ \
            "zombies/zombie1/zombie1attack_1", \
            "zombies/zombie1/zombie1attack_2", \
            "zombies/zombie1/zombie1attack_3", \
            "zombies/zombie1/zombie1attack_4", \
            "zombies/zombie1/zombie1attack_5", \
            "zombies/zombie1/zombie1attack_6", \
            "zombies/zombie1/zombie1attack_7", \
            "zombies/zombie1/zombie1attack_8", \
            "zombies/zombie1/zombie1attack_9", \
            "zombies/zombie1/zombie1attack_10", \
            "zombies/zombie1/zombie1attack_11", \
            "zombies/zombie1/zombie1attack_12", \
            ])
        
        self.cz_images = []  # 帽子僵尸图片
        self.cz_images.extend([ \
            "zombies/zombie2/zombie21", \
            "zombies/zombie2/zombie22", \
            "zombies/zombie2/zombie23", \
            "zombies/zombie2/zombie24", \
            "zombies/zombie2/zombie25", \
            "zombies/zombie2/zombie26", \
            "zombies/zombie2/zombie27", \
            "zombies/zombie2/zombie28", \
            "zombies/zombie2/zombie29", \
            "zombies/zombie2/zombie210", \
            "zombies/zombie2/zombie211", \
            "zombies/zombie2/zombie212", \
            "zombies/zombie2/zombie213", \
            "zombies/zombie2/zombie214", \
            "zombies/zombie2/zombie215", \
            "zombies/zombie2/zombie216", \
            "zombies/zombie2/zombie217", \
            "zombies/zombie2/zombie218", \
            "zombies/zombie2/zombie219", \
            "zombies/zombie2/zombie220", \
            "zombies/zombie2/zombie221" \
            ])

        self.cza_images = []  # 帽子僵尸攻击图片
        self.cza_images.extend([ \
            "zombies/zombie2/zombie2attack1", \
            "zombies/zombie2/zombie2attack2", \
            "zombies/zombie2/zombie2attack3", \
            "zombies/zombie2/zombie2attack4", \
            "zombies/zombie2/zombie2attack5", \
            "zombies/zombie2/zombie2attack6", \
            "zombies/zombie2/zombie2attack7", \
            "zombies/zombie2/zombie2attack8", \
            "zombies/zombie2/zombie2attack9", \
            "zombies/zombie2/zombie2attack10", \
            "zombies/zombie2/zombie2attack11" \
            ])

        self.cznh_images = []  # 帽子僵尸没帽子行走图片
        self.cznh_images.extend([\
            "zombies/zombie2/zombie2_1", \
            "zombies/zombie2/zombie2_2", \
            "zombies/zombie2/zombie2_3", \
            "zombies/zombie2/zombie2_4", \
            "zombies/zombie2/zombie2_5", \
            "zombies/zombie2/zombie2_6", \
            "zombies/zombie2/zombie2_7", \
            "zombies/zombie2/zombie2_8", \
            "zombies/zombie2/zombie2_9", \
            "zombies/zombie2/zombie2_10", \
            "zombies/zombie2/zombie2_11", \
            "zombies/zombie2/zombie2_12", \
            ])

        self.cznha_images = []  #帽子僵尸没帽子攻击图片
        self.cznha_images.extend([\
            "zombies/zombie2/zombieattack_1", \
            "zombies/zombie2/zombieattack_2", \
            "zombies/zombie2/zombieattack_3", \
            "zombies/zombie2/zombieattack_4", \
            "zombies/zombie2/zombieattack_5", \
            "zombies/zombie2/zombieattack_6", \
            "zombies/zombie2/zombieattack_7", \
            "zombies/zombie2/zombieattack_8", \
            "zombies/zombie2/zombieattack_9", \
            "zombies/zombie2/zombieattack_10", \
            "zombies/zombie2/zombieattack_11", \
            "zombies/zombie2/zombieattack_12", \
            ])

        self.bz_images = []  # 铁桶僵尸图片
        self.bz_images.extend([ \
            "zombies/zombie3/zombie3_1", \
            "zombies/zombie3/zombie3_2", \
            "zombies/zombie3/zombie3_3", \
            "zombies/zombie3/zombie3_4", \
            "zombies/zombie3/zombie3_5", \
            "zombies/zombie3/zombie3_6", \
            "zombies/zombie3/zombie3_7", \
            "zombies/zombie3/zombie3_8", \
            "zombies/zombie3/zombie3_9", \
            "zombies/zombie3/zombie3_10", \
            "zombies/zombie3/zombie3_11", \
            "zombies/zombie3/zombie3_12", \
            ])

        self.bza_images = []  # 铁桶僵尸攻击图片
        self.bza_images.extend([ \
            "zombies/zombie3/zombie3attack_1", \
            "zombies/zombie3/zombie3attack_2", \
            "zombies/zombie3/zombie3attack_3", \
            "zombies/zombie3/zombie3attack_4", \
            "zombies/zombie3/zombie3attack_5", \
            "zombies/zombie3/zombie3attack_6", \
            "zombies/zombie3/zombie3attack_7", \
            "zombies/zombie3/zombie3attack_8", \
            "zombies/zombie3/zombie3attack_9", \
            "zombies/zombie3/zombie3attack_10", \
            "zombies/zombie3/zombie3attack_11", \
            "zombies/zombie3/zombie3attack_12" \
            ])

        self.bznh_images = []  # 铁桶僵尸没有帽子行走图片
        self.bznh_images.extend([\
            "zombies/zombie3/zombie_1", \
            "zombies/zombie3/zombie_2", \
            "zombies/zombie3/zombie_3", \
            "zombies/zombie3/zombie_4", \
            "zombies/zombie3/zombie_5", \
            "zombies/zombie3/zombie_6", \
            "zombies/zombie3/zombie_7", \
            "zombies/zombie3/zombie_8", \
            "zombies/zombie3/zombie_9", \
            "zombies/zombie3/zombie_10", \
            "zombies/zombie3/zombie_11", \
            "zombies/zombie3/zombie_12", \
            ])

        self.bznha_images = []  #铁桶僵尸没有帽子攻击图片
        self.bznha_images.extend([\
            "zombies/zombie3/zombieattack_1", \
            "zombies/zombie3/zombieattack_2", \
            "zombies/zombie3/zombieattack_3", \
            "zombies/zombie3/zombieattack_4", \
            "zombies/zombie3/zombieattack_5", \
            "zombies/zombie3/zombieattack_6", \
            "zombies/zombie3/zombieattack_7", \
            "zombies/zombie3/zombieattack_8", \
            "zombies/zombie3/zombieattack_9", \
            "zombies/zombie3/zombieattack_10", \
            "zombies/zombie3/zombieattack_11", \
            "zombies/zombie3/zombieattack_12", \
            ])

        self.fz_images = []  # 举旗僵尸图片
        self.fz_images.extend([ \
            "zombies/zombie4/zombie4_1", \
            "zombies/zombie4/zombie4_2", \
            "zombies/zombie4/zombie4_3", \
            "zombies/zombie4/zombie4_4", \
            "zombies/zombie4/zombie4_5", \
            "zombies/zombie4/zombie4_6", \
            "zombies/zombie4/zombie4_7", \
            "zombies/zombie4/zombie4_8", \
            "zombies/zombie4/zombie4_9", \
            "zombies/zombie4/zombie4_10", \
            "zombies/zombie4/zombie4_11", \
            "zombies/zombie4/zombie4_12" \
            ])

        self.fza_images = []  # 举旗僵尸攻击图片
        self.fza_images.extend([ \
            "zombies/zombie4/zombie4attack_1", \
            "zombies/zombie4/zombie4attack_2", \
            "zombies/zombie4/zombie4attack_3", \
            "zombies/zombie4/zombie4attack_4", \
            "zombies/zombie4/zombie4attack_5", \
            "zombies/zombie4/zombie4attack_6", \
            "zombies/zombie4/zombie4attack_7", \
            "zombies/zombie4/zombie4attack_8", \
            "zombies/zombie4/zombie4attack_9", \
            "zombies/zombie4/zombie4attack_10", \
            "zombies/zombie4/zombie4attack_11", \
            "zombies/zombie4/zombie4attack_11" \
            ])

        self.fzlh_images = []  # 举旗僵尸没有头图片
        self.fzlh_images.extend([ \
            "zombies/zombie4/image1", \
            "zombies/zombie4/image2", \
            "zombies/zombie4/image3", \
            "zombies/zombie4/image4", \
            "zombies/zombie4/image5", \
            "zombies/zombie4/image1", \
            "zombies/zombie4/image7", \
            "zombies/zombie4/image8", \
            "zombies/zombie4/image9", \
            "zombies/zombie4/image10", \
            "zombies/zombie4/image11", \
            "zombies/zombie4/image12" \
            ])
        

        self.zlh_images = []  # 原始僵尸没有头图片
        self.zlh_images.extend([ \
            "zombies/ordinaryzombie/zombielosthead1", \
            "zombies/ordinaryzombie/zombielosthead2", \
            "zombies/ordinaryzombie/zombielosthead3", \
            "zombies/ordinaryzombie/zombielosthead4", \
            "zombies/ordinaryzombie/zombielosthead5", \
            "zombies/ordinaryzombie/zombielosthead6", \
            "zombies/ordinaryzombie/zombielosthead7", \
            "zombies/ordinaryzombie/zombielosthead8", \
            "zombies/ordinaryzombie/zombielosthead9", \
            "zombies/ordinaryzombie/zombielosthead10", \
            "zombies/ordinaryzombie/zombielosthead11", \
            "zombies/ordinaryzombie/zombielosthead12", \
            "zombies/ordinaryzombie/zombielosthead13", \
            "zombies/ordinaryzombie/zombielosthead14", \
            "zombies/ordinaryzombie/zombielosthead15", \
            "zombies/ordinaryzombie/zombielosthead16", \
            "zombies/ordinaryzombie/zombielosthead17", \
            "zombies/ordinaryzombie/zombielosthead18" \
            ])

        self.zh_images = []  # 僵尸的头图片
        self.zh_images.extend([ \
            "zombies/ordinaryzombie/zombiehead1", \
            "zombies/ordinaryzombie/zombiehead2", \
            "zombies/ordinaryzombie/zombiehead3", \
            "zombies/ordinaryzombie/zombiehead4", \
            "zombies/ordinaryzombie/zombiehead5", \
            "zombies/ordinaryzombie/zombiehead6", \
            "zombies/ordinaryzombie/zombiehead7", \
            "zombies/ordinaryzombie/zombiehead8", \
            "zombies/ordinaryzombie/zombiehead9", \
            "zombies/ordinaryzombie/zombiehead10", \
            "zombies/ordinaryzombie/zombiehead11", \
            "zombies/ordinaryzombie/zombiehead12" \
            ])

        self.zlha_images = []  # 原始僵尸没有头攻击图片
        self.zlha_images.extend([ \
            "zombies/ordinaryzombie/zombielostheadattack1", \
            "zombies/ordinaryzombie/zombielostheadattack2", \
            "zombies/ordinaryzombie/zombielostheadattack3", \
            "zombies/ordinaryzombie/zombielostheadattack4", \
            "zombies/ordinaryzombie/zombielostheadattack5", \
            "zombies/ordinaryzombie/zombielostheadattack6", \
            "zombies/ordinaryzombie/zombielostheadattack7", \
            "zombies/ordinaryzombie/zombielostheadattack8", \
            "zombies/ordinaryzombie/zombielostheadattack9", \
            "zombies/ordinaryzombie/zombielostheadattack10", \
            "zombies/ordinaryzombie/zombielostheadattack11" \
            ])
        
        self.fzlha_images = []  # 举旗僵尸没有头攻击图片
        self.fzlha_images.extend([ \
            "zombies/flagzombie/flagzombielostheadattack1", \
            "zombies/flagzombie/flagzombielostheadattack2", \
            "zombies/flagzombie/flagzombielostheadattack3", \
            "zombies/flagzombie/flagzombielostheadattack4", \
            "zombies/flagzombie/flagzombielostheadattack5", \
            "zombies/flagzombie/flagzombielostheadattack6", \
            "zombies/flagzombie/flagzombielostheadattack7", \
            "zombies/flagzombie/flagzombielostheadattack8", \
            "zombies/flagzombie/flagzombielostheadattack9", \
            "zombies/flagzombie/flagzombielostheadattack10", \
            "zombies/flagzombie/flagzombielostheadattack11" \
            ])
        
        self.zd_images = []  # 僵尸死亡图片
        self.zd_images.extend([ \
            "zombies/ordinaryzombie/zombiedie1", \
            "zombies/ordinaryzombie/zombiedie2", \
            "zombies/ordinaryzombie/zombiedie3", \
            "zombies/ordinaryzombie/zombiedie4", \
            "zombies/ordinaryzombie/zombiedie5", \
            "zombies/ordinaryzombie/zombiedie6", \
            "zombies/ordinaryzombie/zombiedie7", \
            "zombies/ordinaryzombie/zombiedie8", \
            "zombies/ordinaryzombie/zombiedie9", \
            "zombies/ordinaryzombie/zombiedie10" \
            ])

        self.die_boom_image = []  # 僵尸死亡爆炸图片
        self.die_boom_image.extend([ \
            "zombies/ordinaryzombie/boom/image1", \
            "zombies/ordinaryzombie/boom/image2", \
            "zombies/ordinaryzombie/boom/image3", \
            "zombies/ordinaryzombie/boom/image4", \
            "zombies/ordinaryzombie/boom/image5", \
            "zombies/ordinaryzombie/boom/image6", \
            "zombies/ordinaryzombie/boom/image7", \
            "zombies/ordinaryzombie/boom/image8", \
            "zombies/ordinaryzombie/boom/image9", \
            "zombies/ordinaryzombie/boom/image10", \
            "zombies/ordinaryzombie/boom/image11", \
            "zombies/ordinaryzombie/boom/image12" \
            ])
        
        self.boom_die_black_images = []  #僵尸死亡被炸成灰
        self.boom_die_black_images.extend([ \
            "zombies/boom_die_black/image1",\
            "zombies/boom_die_black/image2",\
            "zombies/boom_die_black/image3",\
            "zombies/boom_die_black/image4",\
            "zombies/boom_die_black/image5",\
            "zombies/boom_die_black/image6",\
            "zombies/boom_die_black/image7",\
            "zombies/boom_die_black/image8",\
            "zombies/boom_die_black/image9",\
            "zombies/boom_die_black/image10",\
            "zombies/boom_die_black/image11",\
            "zombies/boom_die_black/image12",\
            "zombies/boom_die_black/image13",\
            "zombies/boom_die_black/image14",\
            "zombies/boom_die_black/image15",\
            "zombies/boom_die_black/image16",\
            "zombies/boom_die_black/image17",\
            "zombies/boom_die_black/image18",\
            "zombies/boom_die_black/image19",\
            "zombies/boom_die_black/image20",\
            "zombies/boom_die_black/image21",\
            "zombies/boom_die_black/image22",\
            "zombies/boom_die_black/image23",\
            "zombies/boom_die_black/image24",            
            ])


class OrdinaryZombie(Actor):
    def __init__(self,x,y,images,level=1):
        Actor.__init__(self,image='zombies/ordinaryzombie/zombie_0')

        self.x,self.y = x,y

        self.oz_images = images.oz1_images  # 原始僵尸1图片
        self.index_oz_image = 0
        self.num_oz_image = 12

        self.za_images = images.oza_images  # 原始僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 12

        self.zlh_images = images.zlh_images  # 原始僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 18

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = Actor(self.zh_images[0])
        
        self.zlha_images = images.zlha_images  # 僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11

        self.zd_images = images.zd_images  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10

        self.left, self.y = randint(int(1*self.x),int(1.1*self.x)), self.y - 25
        self.index = 1
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 0.5 + 0.5*level
        self.blood_max = 2+level*8
        self.blood = 2+level*8
        self.level = level
        self.attack = False
        self.willdie = False
        self.die = False
        self.get_win = False
        self.attack_delay = 60

    def move(self):
        self.left -= self.speed+0.2*(self.level-1)


class ConeheadZombie(Actor):
    def __init__(self,x,y,images,level=1):
        Actor.__init__(self,'zombies/zombie2/zombie21')

        self.x,self.y= x,y

        self.oz_images = images.cz_images  # 帽子僵尸图片
        self.index_oz_image = 0
        self.num_oz_image = 11

        self.hoz_images = images.cznh_images  # 帽子僵尸没帽子行走图片
        self.index_hoz_image = 0
        self.num_hoz_image = 12

        self.za_images = images.cza_images  # 帽子僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 11

        self.hza_images = images.cznha_images  # 帽子僵尸没帽子攻击图片
        self.index_hza_image = 0
        self.num_hza_image = 11

        self.zlh_images = images.zlh_images  # 原始僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 18

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = Actor(self.zh_images[0])

        self.zlha_images = images.zlha_images  # 僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11

        self.zd_images = images.die_boom_image  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10

        self.black = False
        self.zd_black_images = images.boom_die_black_images  # 僵尸灰烬图片
        self.index_zd_black_image = 0
        self.num_zd_black_image = 24

        self.left,self.y = randint(int(1*self.x),int(1.2*self.x)), self.y- 25
        self.index = 2
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 0.5 + level*0.5
        self.blood_max = 12 + 15*level 
        self.blood = 12 + 15*level
        self.level = level
        self.hat = True
        self.attack = False
        self.willdie = False
        self.die = False
        self.explosion = False
        self.get_win = False
        self.attack_delay = 60

    def move(self):
        self.left -= self.speed + (self.level-1)*0.2


class BucketheadZombie(Actor):
    def __init__(self,x,y,images,level=1):
        Actor.__init__(self,"zombies/zombie3/zombie3_1")

        self.x, self.y = x,y

        self.oz_images = images.bz_images  # 铁桶僵尸图片
        self.index_oz_image = 0
        self.num_oz_image = 12

        self.hoz_images = images.bznh_images  # 铁桶僵尸没有铁桶行走图片
        self.index_hoz_image = 0
        self.num_hoz_image = 12

        self.za_images = images.bza_images  # 铁桶僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 12

        self.hza_images = images.bznha_images  # 铁桶僵尸没有铁桶攻击图片
        self.index_hza_image = 0
        self.num_hza_image = 12

        self.zlh_images = images.zlh_images  # 原始僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 18

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = Actor(self.zh_images[0])

        self.zlha_images = images.zlha_images  # 僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11

        self.zd_images = images.die_boom_image  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10
        
        self.black = False
        self.zd_black_images = images.boom_die_black_images  # 僵尸灰烬图片
        self.index_zd_black_image = 0
        self.num_zd_black_image = 24

        self.left,self.y = randint(int(1.1*self.x),int(1.3*self.x)), self.y - 25
        self.index = 3
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 0.5 + 0.5*level
        self.blood_max = 30 + 12*level + 2*level**2
        self.blood = 30 + 12*level + 2*level**2
        self.level = level
        self.hat = True
        self.attack = False
        self.willdie = False
        self.die = False
        self.explosion = False
        self.get_win = False
        self.attack_delay = 60

    def move(self):
        self.left -= self.speed + (self.level-1)*0.2


class FlagZombie(Actor):
    def __init__(self,x,y,images,level=1):
        Actor.__init__(self,'zombies/flagzombie/flagzombie1')

        self.x,self.y = x,y

        self.oz_images = images.fz_images  # 举旗僵尸图片
        self.index_oz_image = 0
        self.num_oz_image = 12

        self.za_images = images.fza_images  # 举旗僵尸攻击图片
        self.index_za_image = 0
        self.num_za_image = 11

        self.zlh_images = images.fzlh_images  # 举旗僵尸没有头图片
        self.index_zlh_image = 0
        self.num_zlh_image = 12

        self.zh_images = images.zh_images  # 僵尸的头图片
        self.index_zh_image = 0
        self.num_zh_image = 12
        self.zh_rect = Actor(self.zh_images[0])

        self.zlha_images = images.fzlha_images  # 举旗僵尸没有头攻击图片
        self.index_zlha_image = 0
        self.num_zlha_image = 11

        self.zd_images = images.zd_images  # 僵尸死亡图片
        self.index_zd_image = 0
        self.num_zd_image = 10
        self.zd_rect = Actor(self.zh_images[0])

        self.black = False
        self.zd_black_images = images.boom_die_black_images  # 僵尸灰烬图片
        self.index_zd_black_image = 0
        self.num_zd_black_image = 24

        self.left, self.y = self.x, self.y - 25
        self.index = 4
        self.index_image = self.index_oz_image
        self.num_image = self.num_oz_image
        self.images = self.oz_images
        self.speed = 0.5 + level*0.5
        self.blood_max = 5 + 7*level
        self.blood = 5 + 7*level
        self.level = level
        self.attack = False
        self.willdie = False
        self.die = False
        self.get_win = False
        self.attack_delay = 60

    def move(self):
        self.left -= self.speed
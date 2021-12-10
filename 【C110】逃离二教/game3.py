import random
import pgzrun
import time
#开始模块
def start():
    if keyboard.space:
        START_WORD.x = 1
        sounds.putong.play(-1)
    return START_WORD.x

#移动模块
def move():
    if keyboard.right:
        BOX.x += speed
    if keyboard.left:
        BOX.x -= speed
    if keyboard.up:
        BOX.y -= speed
    if keyboard.down:
        BOX.y += speed
    return BOX.x,BOX.y
def move_act():
    global WALK 
    if keyboard.right:
        WALK = 1
    elif keyboard.left:
        WALK = 2
    elif keyboard.up:
        WALK = 3
    elif keyboard.down:
        WALK = 4
    else:
        WALK = 0
def hero_normal():
    BOX.image= 'hero'
    return BOX.image
def walk():
    if BOX.image == 'hero':
        BOX.image = 'knight rt1'
        clock.schedule_unique(hero_walk11, 0.1)
    return BOX.image
def hero_walk11():
    if BOX.image== 'knight rt1':
        BOX.image= 'knight rt2'
        clock.schedule_unique(hero_walk12, 0.1)
    return BOX.image
def hero_walk12():
    if BOX.image== 'knight rt2':
        BOX.image= 'knight rt3'
        clock.schedule_unique(hero_walk13, 0.1)
    return BOX.image
def hero_walk13():
    if BOX.image== 'knight rt3':
        BOX.image= 'knight rt4'
        clock.schedule_unique(hero_walk14, 0.1)
    return BOX.image
def hero_walk14():
    if BOX.image== 'knight rt4':
        BOX.image= 'knight rt1'
        clock.schedule_unique(hero_walk11, 0.1)
    return BOX.image
def walk2():
    if BOX.image == 'hero':
        BOX.image = 'knight lf1'
        clock.schedule_unique(hero_walk21, 0.1)
    return BOX.image
def hero_walk21():
    if BOX.image== 'knight lf1':
        BOX.image= 'knight lf2'
        clock.schedule_unique(hero_walk22, 0.1)
    return BOX.image
def hero_walk22():
    if BOX.image== 'knight lf2':
        BOX.image= 'knight lf3'
        clock.schedule_unique(hero_walk23, 0.1)
    return BOX.image
def hero_walk23():
    if BOX.image== 'knight lf3':
        BOX.image= 'knight lf4'
        clock.schedule_unique(hero_walk24, 0.1)
    return BOX.image
def hero_walk24():
    if BOX.image== 'knight lf4':
        BOX.image= 'knight lf1'
        clock.schedule_unique(hero_walk21, 0.1)
def walk3():
    if BOX.image == 'hero':
        BOX.image = 'knight bk1'
        clock.schedule_unique(hero_walk31, 0.1)
    return BOX.image
def hero_walk31():
    if BOX.image== 'knight bk1':
        BOX.image= 'knight bk2'
        clock.schedule_unique(hero_walk32, 0.1)
    return BOX.image
def hero_walk32():
    if BOX.image== 'knight bk2':
        BOX.image= 'knight bk3'
        clock.schedule_unique(hero_walk33, 0.1)
    return BOX.image
def hero_walk33():
    if BOX.image== 'knight bk3':
        BOX.image= 'knight bk4'
        clock.schedule_unique(hero_walk34, 0.1)
    return BOX.image
def hero_walk34():
    if BOX.image== 'knight bk4':
        BOX.image= 'knight bk1'
        clock.schedule_unique(hero_walk31, 0.1)
def walk4():
    if BOX.image == 'hero':
        BOX.image = 'knight fd1'
        clock.schedule_unique(hero_walk41, 0.1)
    return BOX.image
def hero_walk41():
    if BOX.image== 'knight fd1':
        BOX.image= 'knight fd2'
        clock.schedule_unique(hero_walk42, 0.1)
    return BOX.image
def hero_walk42():
    if BOX.image== 'knight fd2':
        BOX.image= 'knight fd3'
        clock.schedule_unique(hero_walk43, 0.1)
    return BOX.image
def hero_walk43():
    if BOX.image== 'knight fd3':
        BOX.image= 'knight fd4'
        clock.schedule_unique(hero_walk44, 0.1)
    return BOX.image
def hero_walk44():
    if BOX.image== 'knight fd4':
        BOX.image= 'knight fd1'
        clock.schedule_unique(hero_walk41, 0.1)
#判定进入模块
def IN_BLOCK(i,j):
    IN = False
    x = 225+((i-1)*50)
    y = (j-1)*50 +25
    if BOX.x >= x-10 and BOX.y>= y-10 and BOX.x <= x+10 and BOX.y<= y+10:
        IN = True
    return IN
#地面模块
def ground(i,j):
    GROUND =  Actor('ground')
    GROUND.x =225+((i-1)*50)
    GROUND.y = (j-1)*50+25
    return GROUND

#墙模块
def wall(i,j):
    WALL =  Actor('wall')
    WALL.x =225+((i-1)*50)
    WALL.y = (j-1)*50+25
    return WALL
def wall_stop(i,j):
    a = 0
    x = 210+((i-1)*50)
    y = (j-1)*50+10
    w = 60
    z = 50
    if BOX.x<= x+w and BOX.x>x and BOX.y>y-25+3 and BOX.y<y+z-3:
        BOX.x = x+w
        a =1
    if BOX.x>= x-25 and BOX.x<x+w and BOX.y>y-25+3 and BOX.y<y+z-3:
        BOX.x = x-25
        a =1
    if BOX.y<= y+z and BOX.y >y and BOX.x < x+w-3 and BOX.x>x-25+3:
        BOX.y = y+z
        a =1
    if BOX.y>= y-25 and BOX.y<y+z and BOX.x < x+w-3 and BOX.x>x-25+3:
        BOX.y = y-25
        a =1
    return BOX.x,BOX.y,a
def bosswall_stop(i,j):
    a = 0
    x = 210+((i-1)*50)
    y = (j-1)*50+10
    w = 120
    z = 50
    if BOX.x<= x+w and BOX.x>x and BOX.y>y-25+3 and BOX.y<y+z-3:
        BOX.x = x+w
        a =1
    if BOX.x>= x-25 and BOX.x<x+w and BOX.y>y-25+3 and BOX.y<y+z-3:
        BOX.x = x-25
        a =1
    if BOX.y<= y+z and BOX.y >y and BOX.x < x+w-3 and BOX.x>x-25+3:
        BOX.y = y+z
        a =1
    if BOX.y>= y-25 and BOX.y<y+z and BOX.x < x+w-3 and BOX.x>x-25+3:
        BOX.y = y-25
        a =1
    return BOX.x,BOX.y,a

#上下楼模块
def stairs_up(i,j):
    UP =  Actor('up')
    UP.x =225+((i-1)*50)
    UP.y = (j-1)*50+25
    return UP
def stairs_down(i,j):
    UP =  Actor('down')
    UP.x =225+((i-1)*50)
    UP.y = (j-1)*50+25
    return UP
def Floor_up(i,j,k):
    if IN_BLOCK(i,j) and k == 1:
        FLOOR_READER12.x = 900
    if IN_BLOCK(i,j) and k == 2:
        FLOOR_READER23.x = 900
    if IN_BLOCK(i,j) and k == 3:
        FLOOR_READER34.x = 900
    if IN_BLOCK(i,j) and k == 4:
        FLOOR_READER45.x = 900
    return FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x
def Floor_down(i,j,k):
    if IN_BLOCK(i,j) and k == 1:
        FLOOR_READER12.x = 950
    if IN_BLOCK(i,j) and k == 2:
        FLOOR_READER23.x = 950
    if IN_BLOCK(i,j) and k == 3:
        FLOOR_READER34.x = 950
    if IN_BLOCK(i,j) and k == 4:
        FLOOR_READER45.x = 950
    return FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x
def MAP_X(FLOOR_READER12x,FLOOR_READER23x,FLOOR_READER34x,FLOOR_READER45x):
    if FLOOR_READER12x == 950:
        MAP = FLOOR[1]
        FLOOR_COUNT= '第五层'
    elif FLOOR_READER12x == 900 and FLOOR_READER23x == 950:
        MAP = FLOOR[2]
        FLOOR_COUNT= '第四层'
    elif FLOOR_READER12x == 900 and FLOOR_READER23x == 900 and FLOOR_READER34x == 950:
        MAP = FLOOR[3]
        FLOOR_COUNT= '第三层'
    elif FLOOR_READER12x == 900 and FLOOR_READER23x == 900 and FLOOR_READER34x == 900 and FLOOR_READER45x == 950:
        MAP = FLOOR[4]
        FLOOR_COUNT= '第二层'
    elif FLOOR_READER12x == 900 and FLOOR_READER23x == 900 and FLOOR_READER34x == 900 and FLOOR_READER45x == 900:
        MAP = FLOOR[5]
        FLOOR_COUNT= '大厅'
    return MAP,FLOOR_COUNT

#血怪物1模块
def monster1(i,j):
    if MONSTER_MOVE.x == 0:
        MONSTER1.image = monster_walk11()
    MONSTER1.x =225+((i-1)*50)
    MONSTER1.y = (j-1)*50+25
    MONSTER_MOVE.x = 1
    return MONSTER1,MONSTER_MOVE.x
def monster_walk11():
    if MONSTER1.image== 'slm1':
        MONSTER1.image= 'slm2'
        clock.schedule_unique(monster_walk12, 0.2)
    return MONSTER1.image
def monster_walk12():
    if MONSTER1.image == 'slm2':
        MONSTER1.image = 'slm1'
        clock.schedule_unique(monster_walk11, 0.8)
    return MONSTER1.image
def monster1_fight(i,j,ATTACK):
    x = 210+((i-1)*50)
    y = (j-1)*50+10
    w = 60
    z = 50
    MONSTER_ATTACK = 80
    if BOX.x<= x+w and BOX.x>x and BOX.y>y-25+3 and BOX.y<y+z-3:
        BOX.x = x+w+10
        MONSTER_BLOD.x = MONSTER_BLOD.x - ATTACK.x
        if MONSTER_ATTACK > DEFENCE.x:
            HEALTH.x = HEALTH.x -(MONSTER_ATTACK-DEFENCE.x)
        else:
            HEALTH.x = HEALTH.x - 1
        sounds.hit.play()
    if BOX.x>= x-25 and BOX.x<x+w and BOX.y>y-25+3 and BOX.y<y+z-3:
        BOX.x = x-35
        MONSTER_BLOD.x = MONSTER_BLOD.x - ATTACK.x
        if MONSTER_ATTACK > DEFENCE.x:
            HEALTH.x = HEALTH.x -(MONSTER_ATTACK-DEFENCE.x)
        else:
            HEALTH.x = HEALTH.x - 1
        sounds.hit.play()
    if BOX.y<= y+z and BOX.y >y and BOX.x < x+w-3 and BOX.x>x-25+3:
        BOX.y = y+z+10
        MONSTER_BLOD.x = MONSTER_BLOD.x - ATTACK.x
        if MONSTER_ATTACK > DEFENCE.x:
            HEALTH.x = HEALTH.x -(MONSTER_ATTACK-DEFENCE.x)
        else:
            HEALTH.x = HEALTH.x - 1
        sounds.hit.play()
    if BOX.y>= y-25 and BOX.y<y+z and BOX.x < x+w-3 and BOX.x>x-25+3:
        BOX.y = y-35
        MONSTER_BLOD.x = MONSTER_BLOD.x - ATTACK.x
        if MONSTER_ATTACK > DEFENCE.x:
            HEALTH.x = HEALTH.x -(MONSTER_ATTACK-DEFENCE.x)
        else:
            HEALTH.x = HEALTH.x - 1
        sounds.hit.play()
    return BOX.x,BOX.y,MONSTER_BLOD.x,HEALTH.x
def monster1_dead():
    a = 'monster1'
    if MONSTER_BLOD.x <= 0:
        a = 0
        MONSTER_BLOD.x = 200
    return a,MONSTER_BLOD.x 

#精怪物2模块
def monster2(i,j):
    if MONSTER_MOVE2.x == 0:
        MONSTER2.image = monster_walk21()
    MONSTER2.x =225+((i-1)*50)
    MONSTER2.y = (j-1)*50+25
    MONSTER_MOVE2.x = 1
    return MONSTER2,MONSTER_MOVE2.x
def monster_walk21():
    if MONSTER2.image== 'eye1':
        MONSTER2.image= 'eye2'
        clock.schedule_unique(monster_walk22, 0.5)
    return MONSTER2.image
def monster_walk22():
    if MONSTER2.image == 'eye2':
        MONSTER2.image = 'eye1'
        clock.schedule_unique(monster_walk21, 0.1)
    return MONSTER2.image
def monster2_fight(i,j,ATTACK):
    x = 210+((i-1)*50)
    y = (j-1)*50+10
    w = 60
    z = 50
    MONSTER_ATTACK = 5
    if BOX.x<= x+w and BOX.x>x and BOX.y>y-25+3 and BOX.y<y+z-3:
        BOX.x = x+w+10
        MONSTER_BLOD2.x = MONSTER_BLOD2.x - ATTACK.x
        REASON.x = REASON.x - MONSTER_ATTACK
        sounds.hit.play()
    if BOX.x>= x-25 and BOX.x<x+w and BOX.y>y-25+3 and BOX.y<y+z-3:
        BOX.x = x-35
        MONSTER_BLOD2.x = MONSTER_BLOD2.x - ATTACK.x
        REASON.x = REASON.x - MONSTER_ATTACK
        sounds.hit.play()
    if BOX.y<= y+z and BOX.y >y and BOX.x < x+w-3 and BOX.x>x-25+3:
        BOX.y = y+z+10
        MONSTER_BLOD2.x = MONSTER_BLOD2.x - ATTACK.x
        REASON.x = REASON.x - MONSTER_ATTACK
        sounds.hit.play()
    if BOX.y>= y-25 and BOX.y<y+z and BOX.x < x+w-3 and BOX.x>x-25+3:
        BOX.y = y-35
        MONSTER_BLOD2.x = MONSTER_BLOD2.x - ATTACK.x
        REASON.x = REASON.x - MONSTER_ATTACK
        sounds.hit.play()
    return BOX.x,BOX.y,MONSTER_BLOD2.x,REASON.x
def monster2_dead():
    a = 'monster2'
    if MONSTER_BLOD2.x <= 0:
        a = 0
        MONSTER_BLOD2.x = 150
    return a,MONSTER_BLOD2.x

#药物模块     
def medicine(i,j):
    WATER =  Actor('water')
    WATER.x =225+((i-1)*50)
    WATER.y = (j-1)*50+25
    return WATER
def drink(i,j):
    a = 'medicine'
    if IN_BLOCK(i,j) and HEALTH.x !=1000:
        if 1000 - HEALTH.x <=200:
            HEALTH.x = 1000
        else:
            HEALTH.x = HEALTH.x +200
        a = 'pickup_medicine'
        sounds.drink.play()
    return a,HEALTH.x

#咖啡模块
def coffee(i,j):
    COFFEE =  Actor('coffee')
    COFFEE.x =225+((i-1)*50)
    COFFEE.y = (j-1)*50+25
    return COFFEE
def drink_coffee(i,j):
    a = 'coffee'
    if IN_BLOCK(i,j) and REASON.x !=100:
        if 100 - REASON.x <=15:
            REASON.x = 100
        else:
            REASON.x = REASON.x +15
        HEALTH.x = HEALTH.x -20
        a = 'pickup_coffee'
        sounds.drink.play()
    return a,REASON.x
def on_coffee(i,j):
    REASON_WORD.x = 0
    if IN_BLOCK(i,j):
        REASON_WORD.x = 1
    return REASON_WORD.x
#宝剑模块
def sword1(i,j):
    SWORD1 =  Actor('sword1')
    SWORD1.x =225+((i-1)*50)
    SWORD1.y = (j-1)*50+25
    return SWORD1
def pick_upsword1(i,j):
    a = 'sword1'
    if IN_BLOCK(i,j):
        ATTACK.x = 50
        a = 'pickup_sword1'
        sounds.pick.play()
    return a,ATTACK.x
def on_sword(i,j):
    ATTACK_WORD.x = 0
    if IN_BLOCK(i,j):
        ATTACK_WORD.x = 1
    return ATTACK_WORD.x
#盔甲模块
def armour1(i,j):
    ARMOUR1 =  Actor('armour1')
    ARMOUR1.x =225+((i-1)*50)
    ARMOUR1.y = (j-1)*50+25
    return ARMOUR1
def pick_uparmour1(i,j):
    a = 'armour1'
    if IN_BLOCK(i,j):
        DEFENCE.x = 30
        a = 'pickup_armour1'
        sounds.pick.play()
    return a,DEFENCE.x
def on_armour(i,j):
    DEFENCE_WORD.x = 0
    if IN_BLOCK(i,j):
        DEFENCE_WORD.x = 1
    return DEFENCE_WORD.x
#高数书模块
def mathbook(i,j):
    MATHBOOK =  Actor('mathbook')
    MATHBOOK.x =225+((i-1)*50)
    MATHBOOK.y = (j-1)*50+25
    return MATHBOOK
def pick_upmathbook(i,j):
    a = 'mathbook'
    if IN_BLOCK(i,j):
        REASON.x = REASON.x -20
        MATHBOOK_NEMBER.x = MATHBOOK_NEMBER.x + 1
        a = 'mathbook_open'
    return a,REASON.x,MATHBOOK_NEMBER.x
def on_mathbook(i,j):
    MATH_WORD.x = 0
    if IN_BLOCK(i,j):
        MATH_WORD.x = 1
    return MATH_WORD.x
def bosswall(i,j):
    WALL =  Actor('cp')
    WALL.x =250+((i-1)*50)
    WALL.y = (j-1)*50+25
    return WALL
def bosswall2(i,j):
    WALL =  Actor('tl')
    WALL.x =250+((i-1)*50)
    WALL.y = (j-1)*50+25
    return WALL
def bosswall3(i,j):
    WALL =  Actor('wa')
    WALL.x =250+((i-1)*50)
    WALL.y = (j-1)*50+25
    return WALL
def bosswall4(i,j):
    WALL =  Actor('rt')
    WALL.x =250+((i-1)*50)
    WALL.y = (j-1)*50+25
    return WALL
def accept(i,j):
    WALL =  Actor('ac')
    WALL.x =250+((i-1)*50)
    WALL.y = (j-1)*50+25
    return WALL
def bosswall_dead(i,j,b):
    x = 200+((i-1)*50)
    y = (j-1)*50+25
    w = 120
    z = 50
    if b == 'bosswall':
        s = 'word18'
    if b == 'bosswall2':
        s = 'word17'
    if b == 'bosswall3':
        s = 'word16'
    if b == 'bosswall4':
        s = 'word15'
    if BOX.x<= x+w and BOX.x>x and BOX.y>y-25+3 and BOX.y<y+z-3:
        MATHBOOK_NEMBER.x = MATHBOOK_NEMBER.x - 1
        b = s
        ATTACK.x = ATTACK.x + 2500
        DEFENCE.x = DEFENCE.x + 2455
        if REASON.x <= 85:
            REASON.x = REASON.x +15
        else:
            REASON.x = 100
        BOX.y = BOX.y + 15
    elif BOX.x>= x-25 and BOX.x<x+w and BOX.y>y-25+3 and BOX.y<y+z-3:
        MATHBOOK_NEMBER.x = MATHBOOK_NEMBER.x - 1
        b = s
        ATTACK.x = ATTACK.x + 2500
        DEFENCE.x = DEFENCE.x + 2455
        if REASON.x <= 85:
            REASON.x = REASON.x +15
        else:
            REASON.x = 100
        BOX.y = BOX.y +15
    elif BOX.y<= y+z and BOX.y >y and BOX.x < x+w-3 and BOX.x>x-25+3:
        MATHBOOK_NEMBER.x = MATHBOOK_NEMBER.x - 1
        b = s
        ATTACK.x = ATTACK.x + 2500
        DEFENCE.x = DEFENCE.x + 2455
        if REASON.x <= 85:
            REASON.x = REASON.x +15
        else:
            REASON.x = 100
        BOX.y = BOX.y + 15
    elif BOX.y>= y-25 and BOX.y<y+z and BOX.x < x+w-3 and BOX.x>x-25+3:
        MATHBOOK_NEMBER.x = MATHBOOK_NEMBER.x - 1
        b = s
        ATTACK.x = ATTACK.x + 2500
        DEFENCE.x = DEFENCE.x + 2455
        if REASON.x <= 85:
            REASON.x = REASON.x +15
        else:
            REASON.x = 100
        BOX.y = BOX.y + 15
    return b
#门/锁模块
def door_close(i,j):
    DOOR =  Actor('door1')
    DOOR.x =225+((i-1)*50)
    DOOR.y = (j-1)*50+25
    return DOOR
def door_open(i,j):
    DOOR =  Actor('door12')
    DOOR.x =225+((i-1)*50)
    DOOR.y = (j-1)*50+25
    return DOOR
def Key1(i,j):
    KEYS =  Actor('key1')
    KEYS.x =225+((i-1)*50)
    KEYS.y = (j-1)*50+25
    return KEYS
def Key_pick(i,j):
    a = 'key1'
    if IN_BLOCK(i,j):
        KEYS_NEMBER.x = KEYS_NEMBER.x + 1
        a ='pickup_key1'
        sounds.pick.play()
    return a,KEYS_NEMBER.x
def on_Keys(i,j):
    KEYS_WORD.x = 0
    if IN_BLOCK(i,j):
        KEYS_WORD.x = 1
    return KEYS_WORD.x
def open_door(i,j):
    a = 'door_close'
    x = 210+((i-1)*50)
    y = (j-1)*50+10
    w = 60
    z = 50
    if BOX.x<= x+w and BOX.x>x and BOX.y>y-25+3 and BOX.y<y+z-3:
        KEYS_NEMBER.x = KEYS_NEMBER.x - 1
        a ='door_open'
        sounds.open.play()
    elif BOX.x>= x-25 and BOX.x<x+w and BOX.y>y-25+3 and BOX.y<y+z-3:
        KEYS_NEMBER.x = KEYS_NEMBER.x - 1
        a ='door_open'
        sounds.open.play()
    elif BOX.y<= y+z and BOX.y >y and BOX.x < x+w-3 and BOX.x>x-25+3:
        KEYS_NEMBER.x = KEYS_NEMBER.x - 1
        a ='door_open'
        sounds.open.play()
    elif BOX.y>= y-25 and BOX.y<y+z and BOX.x < x+w-3 and BOX.x>x-25+3:
        KEYS_NEMBER.x = KEYS_NEMBER.x - 1
        a ='door_open'
        sounds.open.play()
    return a, KEYS_NEMBER.x

def door_close2(i,j):
    DOOR =  Actor('door2')
    DOOR.x =225+((i-1)*50)
    DOOR.y = (j-1)*50+25
    return DOOR
def door_open2(i,j):
    DOOR =  Actor('door22')
    DOOR.x =225+((i-1)*50)
    DOOR.y = (j-1)*50+25
    return DOOR
def Key2(i,j):
    KEYS =  Actor('key2')
    KEYS.x =225+((i-1)*50)
    KEYS.y = (j-1)*50+25
    return KEYS
def Key_pick2(i,j):
    a = 'key2'
    if IN_BLOCK(i,j):
        KEYS_NEMBER2.x = KEYS_NEMBER2.x + 1
        a ='pickup_key2'
        sounds.pick.play()
    return a,KEYS_NEMBER2.x
def on_Keys2(i,j):
    KEYS_WORD2.x = 0
    if IN_BLOCK(i,j):
        KEYS_WORD2.x = 1
    return KEYS_WORD2.x
def open_door2(i,j):
    a = 'door_close2'
    x = 210+((i-1)*50)
    y = (j-1)*50+10
    w = 60
    z = 50
    if BOX.x<= x+w and BOX.x>x and BOX.y>y-25+3 and BOX.y<y+z-3:
        KEYS_NEMBER2.x = KEYS_NEMBER2.x - 1
        a ='door_open2'
        sounds.open.play()
    elif BOX.x>= x-25 and BOX.x<x+w and BOX.y>y-25+3 and BOX.y<y+z-3:
        KEYS_NEMBER2.x = KEYS_NEMBER2.x - 1
        a ='door_open2'
        sounds.open.play()
    elif BOX.y<= y+z and BOX.y >y and BOX.x < x+w-3 and BOX.x>x-25+3:
        KEYS_NEMBER2.x = KEYS_NEMBER2.x - 1
        a ='door_open2'
        sounds.open.play()
    elif BOX.y>= y-25 and BOX.y<y+z and BOX.x < x+w-3 and BOX.x>x-25+3:
        KEYS_NEMBER2.x = KEYS_NEMBER2.x - 1
        a ='door_open2'
        sounds.open.play()
    return a, KEYS_NEMBER2.x
#理智惩罚
def mad(k):
    if k == 1:
        MAD.x =0
    if k == 2:
        b = random.randint(1,2)
        if b == 1 :
            ATTACK.x = int(ATTACK.x*(1.5))
            DEFENCE.x = int(DEFENCE.x//2)
            MAD.x = 51
        if b == 2 :
            ATTACK.x = int(ATTACK.x/2)
            DEFENCE.x = int(DEFENCE.x*1.5)
            MAD.x = 52
    elif k == 3:
        b = random.randint(1,2)
        if b == 1:
            DEFENCE.x = int(DEFENCE.x*5)
            ATTACK.x = int(ATTACK.x/10)
            MAD.x = 101
        if b == 2:
            ATTACK.x = int(ATTACK.x*(5))
            DEFENCE.x = int(DEFENCE.x/10)
            MAD.x = 102
    return ATTACK.x,DEFENCE.x,HEALTH.x,MAD.x
def mad_words():
    MAD_words = ''
    if MAD.x == 51:
        MAD_words = '你感到十分的烦躁,有点粗心大意'
    if MAD.x == 52:
        MAD_words = '你感到十分的担忧，有点畏手畏脚'
    if MAD.x == 102:
        MAD_words = '你感到十分的愤怒，想要不惜一切代价撕碎周围的东西'
    if MAD.x == 101:
        MAD_words = '你感到十分的恐惧，想要抓住所有可以保护自己的东西'
    return MAD_words
def end_mad(k):
    if k == 1:
        MAD.x =0
    if k == 2:
        if MAD.x == 51:
            ATTACK.x = int(ATTACK.x/1.5)
            DEFENCE.x = int(DEFENCE.x*2)
            MAD.x = 0
        if MAD.x == 52:
            ATTACK.x = int(ATTACK.x*2)
            DEFENCE.x = int(DEFENCE.x/1.5)
            MAD.x = 0
    if k == 3:
        if MAD.x == 102:
            ATTACK.x = int(ATTACK.x/5)
            DEFENCE.x = int(DEFENCE.x*10)
            MAD.x = 52
        if MAD.x == 101:
            ATTACK.x = int(ATTACK.x*10)
            DEFENCE.x = int(DEFENCE.x/5)
            MAD.x = 51
    return ATTACK.x,DEFENCE.x,HEALTH.x,MAD.x

#语言模块
def word1(i,j,k):
    WORD.x = 0
    if IN_BLOCK(i,j) and k == 1:
        WORD.x = 1
    return WORD.x 
def word2(i,j,k):  
    WORD.x = 0
    if IN_BLOCK(i,j) and k == 2:
        WORD.x = 2
    return WORD.x
def word3(i,j,k):  
    WORD.x = 0
    if IN_BLOCK(i,j) and k == 3:
        WORD.x = 3
    return WORD.x
def word4(i,j,k):  
    WORD.x = 0
    if IN_BLOCK(i,j) and k == 4:
        WORD.x = 4
    return WORD.x
def word5(i,j,k):  
    WORD.x = 0
    if IN_BLOCK(i,j) and k == 5:
        WORD.x = 5
    return WORD.x
def word6(i,j,k):  
    WORD.x = 0
    if IN_BLOCK(i,j) and k == 6:
        WORD.x = 6
    return WORD.x
def word7(i,j,k):  
    WORD.x = 0
    if IN_BLOCK(i,j) and k == 7:
        WORD.x = 7
    return WORD.x
def word8(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 8
    return WORD.x
def word9(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 9
    return WORD.x
def word10(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 10
    return WORD.x
def word11(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 11
    return WORD.x
def word12(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 12
    return WORD.x
def word13(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 13
    return WORD.x
def word14(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 14
    return WORD.x
def word15(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 15
    return WORD.x
def word16(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 16
    return WORD.x
def word17(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 17
    return WORD.x
def word18(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 18
    return WORD.x
def word19(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 19
    return WORD.x
def word20(i,j):  
    WORD.x = 0
    if IN_BLOCK(i,j):
        WORD.x = 20
    return WORD.x
#岩浆模块
def lava(i,j):
    LAVA =  Actor('lava')
    LAVA.x =225+((i-1)*50)
    LAVA.y = (j-1)*50+25
    return LAVA

#boss 模块
def boss(i,j):
    if BOSS_MOVE.x == 0:
        BOSS.image = boss_walk21()
    BOSS.x =200+((i-1)*50)
    BOSS.y = (j-1)*50
    BOSS_MOVE.x = 1
    return BOSS,BOSS_MOVE.x
def boss_walk21():
    if BOSS.image== 'boss1':
        BOSS.image= 'boss2'
        clock.schedule_unique(boss_walk22, 0.2)
    return BOSS.image
def boss_walk22():
    if BOSS.image == 'boss2':
        BOSS.image = 'boss3'
        clock.schedule_unique(boss_walk23, 0.2)
    return BOSS.image
def boss_walk23():
    if BOSS.image == 'boss3':
        BOSS.image = 'boss4'
        clock.schedule_unique(boss_walk24, 0.2)
def boss_walk24():
    if BOSS.image == 'boss4':
        BOSS.image = 'boss1'
        clock.schedule_unique(boss_walk21, 0.2)
    return BOSS.image
def boss_fight(i,j,ATTACK):
    x = 150+((i-1)*50)
    y = (j-1)*50 -50
    w = 120
    z = 100
    BOSS_ATTACK = 10000
    if BOX.x<= x+w and BOX.x>x and BOX.y>y-25+3 and BOX.y<y+z-3:
        BOX.x = x+w+10
        BOSS_BLOD.x =BOSS_BLOD.x - ATTACK.x
        if BOSS_ATTACK > DEFENCE.x:
            HEALTH.x = HEALTH.x -(BOSS_ATTACK-DEFENCE.x)
        else:
            HEALTH.x = HEALTH.x - 1
        sounds.hit.play()
    if BOX.x>= x-25 and BOX.x<x+w and BOX.y>y-25+3 and BOX.y<y+z-3:
        BOX.x = x-35
        BOSS_BLOD.x = BOSS_BLOD.x - ATTACK.x
        if BOSS_ATTACK > DEFENCE.x:
            HEALTH.x = HEALTH.x -(BOSS_ATTACK-DEFENCE.x)
        else:
            HEALTH.x = HEALTH.x - 1
        sounds.hit.play()
    if BOX.y<= y+z and BOX.y >y and BOX.x < x+w-3 and BOX.x>x-25+3:
        BOX.y = y+z+10
        BOSS_BLOD.x =BOSS_BLOD.x - ATTACK.x
        if BOSS_ATTACK > DEFENCE.x:
            HEALTH.x = HEALTH.x -(BOSS_ATTACK-DEFENCE.x)
        else:
            HEALTH.x = HEALTH.x - 1
        sounds.hit.play()
    if BOX.y>= y-25 and BOX.y<y+z and BOX.x < x+w-3 and BOX.x>x-25+3:
        BOX.y = y-35
        BOSS_BLOD.x = BOSS_BLOD.x - ATTACK.x
        if BOSS_ATTACK > DEFENCE.x:
            HEALTH.x = HEALTH.x -(BOSS_ATTACK-DEFENCE.x)
        else:
            HEALTH.x = HEALTH.x - 1
        sounds.hit.play()
    return BOX.x,BOX.y,BOSS_BLOD.x,HEALTH.x
def boss_dead():
    a = 'boss'
    if BOSS_BLOD.x <= 0:
        a = 0
        sounds.boss_music.stop()
    return a,BOSS_BLOD.x
def boss_music():
    sounds.boss.play()
#边界模块
def edg():
    if BOX.x<=225:
        BOX.x = 225
    if BOX.x>=975:
        BOX.x = 975
    if BOX.y<=25:
        BOX.y = 25
    if BOX.y>=575:
        BOX.y = 575
    return BOX.x,BOX.y

#结尾
def end():
    if END_MOVE.x == 0 and BOSS_BLOD.x<=0:
        BACK.image = end1()
        BOSS_MOVE.x = 1
    return BACK.image
def end1():
    if BACK.image == 'backg1':
        BACK.image = 'backg2'
        clock.schedule_unique(end2, 4)
    return BACK.image
def end2():
    if BACK.image == 'backg2':
        BACK.image = 'backg3'
    return BACK.image

# 底板的大小形状设置
WIDTH = 1000
HEIGHT = 800
START_WORD = Rect((0,750),(50,50))
# 主人公的移动速度，大小，颜色
speed = 3
WALK = 0
BOX = Actor('hero')
BOX.height =50
BOX.width =50
BOX.x = 875
BOX.y = 530

ATTACK = Rect((1,750),(50,50))
HEALTH = Rect((1000,750),(50,50))
DEFENCE = Rect((1,750),(50,50))
REASON = Rect((100,750),(50,50))

HEALTH_WORD = Rect((0,750),(50,50))
ATTACK_WORD = Rect((0,750),(50,50))
DEFENCE_WORD = Rect((0,750),(50,50))
REASON_WORD = Rect((0,750),(50,50))
MAD = Rect((0,750),(50,50))
# 地图的形状大小颜色
COLOR1 = 0,0,255
BACKGROUNG = Rect((200,0),(800,600))
BACKGROUNG2 = Rect((5,300),(40,40))
BACKGROUNG3 = Rect((5,345),(40,40))
# 语言栏
COLOR2 = 0,255,0
SPEEK = Rect((0,600),(1000,200))
# 状态栏
COLOR3 = 255,255,255
EQUIPMENT = Rect((0,0),(200,600))

# 设计四个楼层记录器
FLOOR_READER12 = Rect((950,750),(50,50))
FLOOR_READER23 = Rect((950,750),(50,50))
FLOOR_READER34 = Rect((950,750),(50,50))
FLOOR_READER45 = Rect((950,750),(50,50))
MAP_1 = {(1,1):1,(1,2):1,(1,3):1,(1,4):1,(1,5):1,(1,6):1,(1,7):1,(1,8):1,(1,9):1,(1,10):1,(1,11):1,(1,12):1,(2,1):1,(2,2):'up',(2,3):0,(2,4):'key2',(2,5):1,(2,6):0,(2,7):0,(2,8):0,(2,9):0,(2,10):1,(2,11):'mathbook',(2,12):1,(3,1):1,(3,2):0,(3,3):0,(3,4):0,(3,5):1,(3,6):0,(3,7):0,(3,8):0,(3,9):'word1',(3,10):1,(3,11):0,(3,12):1,(4,1):1,(4,2):'medicine',(4,3):0,(4,4):0,(4,5):1,(4,6):0,(4,7):1,(4,8):1,(4,9):'door_close',(4,10):1,(4,11):"coffee",(4,12):1,(5,1):1,(5,2):'medicine',(5,3):'coffee',(5,4):0,(5,5):1,(5,6):0,(5,7):1,(5,8):1,(5,9):'word7',(5,10):1,(5,11):'word6',(5,12):1,(6,1):1,(6,2):1,(6,3):1,(6,4):1,(6,5):1,(6,6):0,(6,7):1,(6,8):1,(6,9):0,(6,10):'word4',(6,11):'monster2',(6,12):1,(7,1):1,(7,2):'medicine',(7,3):'monster2',(7,4):0,(7,5):1,(7,6):0,(7,7):1,(7,8):1,(7,9):0,(7,10):1,(7,11):1,(7,12):1,(8,1):1,(8,2):'monster2',(8,3):'medicine',(8,4):'monster1',(8,5):'monster1',(8,6):0,(8,7):1,(8,8):1,(8,9):0,(8,10):1,(8,11):'medicine',(8,12):1,(9,1):1,(9,2):'coffee',(9,3):'monster2',(9,4):'word11',(9,5):1,(9,6):0,(9,7):1,(9,8):1,(9,9):'monster1',(9,10):1,(9,11):'word5',(9,12):1,(10,1):1,(10,2):'coffee',(10,3):0,(10,4):'medicine',(10,5):1,(10,6):0,(10,7):1,(10,8):1,(10,9):'word2',(10,10):0,(10,11):0,(10,12):1,(11,1):1,(11,2):1,(11,3):1,(11,4):1,(11,5):1,(11,6):0,(11,7):1,(11,8):'sword1',(11,9):0,(11,10):0,(11,11):0,(11,12):1,(12,1):1,(12,2):0,(12,3):0,(12,4):1,(12,5):0,(12,6):0,(12,7):1,(12,8):1,(12,9):0,(12,10):0,(12,11):0,(12,12):1,(13,1):1,(13,2):0,(13,3):0,(13,4):'monster1',(13,5):0,(13,6):0,(13,7):1,(13,8):'armour1',(13,9):0,(13,10):0,(13,11):0,(13,12):1,(14,1):1,(14,2):0,(14,3):0,(14,4):'monster2',(14,5):0,(14,6):0,(14,7):1,(14,8):1,(14,9):0,(14,10):0,(14,11):'word11',(14,12):1,(15,1):1,(15,2):'up',(15,3):0,(15,4):1,(15,5):0,(15,6):0,(15,7):1,(15,8):'key1',(15,9):0,(15,10):0,(15,11):0,(15,12):1,(16,1):1,(16,2):1,(16,3):1,(16,4):1,(16,5):1,(16,6):1,(16,7):1,(16,8):1,(16,9):1,(16,10):1,(16,11):1,(16,12):1}
MAP_2 = {(1,1):1,(1,2):1,(1,3):1,(1,4):1,(1,5):1,(1,6):1,(1,7):1,(1,8):1,(1,9):1,(1,10):1,(1,11):1,(1,12):1,(2,1):1,(2,2):0,(2,3):0,(2,4):1,(2,5):0,(2,6):'mathbook',(2,7):0,(2,8):1,(2,9):'medicine',(2,10):'key1',(2,11):'medicine',(2,12):1,(3,1):1,(3,2):'down',(3,3):0,(3,4):1,(3,5):0,(3,6):0,(3,7):0,(3,8):1,(3,9):0,(3,10):0,(3,11):0,(3,12):1,(4,1):1,(4,2):0,(4,3):0,(4,4):1,(4,5):'coffee',(4,6):0,(4,7):'coffee',(4,8):1,(4,9):0,(4,10):0,(4,11):0,(4,12):1,(5,1):1,(5,2):'monster2',(5,3):1,(5,4):1,(5,5):1,(5,6):'door_close',(5,7):1,(5,8):1,(5,9):1,(5,10):'monster1',(5,11):1,(5,12):1,(6,1):1,(6,2):0,(6,3):0,(6,4):0,(6,5):'monster1',(6,6):'word7',(6,7):0,(6,8):'monster1',(6,9):0,(6,10):0,(6,11):'medicine',(6,12):1,(7,1):1,(7,2):0,(7,3):1,(7,4):1,(7,5):1,(7,6):1,(7,7):1,(7,8):1,(7,9):1,(7,10):1,(7,11):1,(7,12):1,(8,1):1,(8,2):0,(8,3):0,(8,4):'monster1',(8,5):0,(8,6):'monster1',(8,7):'coffee',(8,8):1,(8,9):0,(8,10):'medicine',(8,11):0,(8,12):1,(9,1):1,(9,2):0,(9,3):'monster2',(9,4):0,(9,5):'monster2',(9,6):0,(9,7):0,(9,8):1,(9,9):'coffee',(9,10):0,(9,11):'coffee',(9,12):1,(10,1):1,(10,2):1,(10,3):1,(10,4):1,(10,5):1,(10,6):1,(10,7):0,(10,8):1,(10,9):0,(10,10):0,(10,11):0,(10,12):1,(11,1):1,(11,2):0,(11,3):0,(11,4):0,(11,5):0,(11,6):'monster2',(11,7):'word3',(11,8):1,(11,9):0,(11,10):0,(11,11):0,(11,12):1,(12,1):1,(12,2):'monster1',(12,3):1,(12,4):1,(12,5):1,(12,6):1,(12,7):'door_close2',(12,8):1,(12,9):1,(12,10):'door_close2',(12,11):1,(12,12):1,(13,1):1,(13,2):0,(13,3):'medicine',(13,4):1,(13,5):0,(13,6):0,(13,7):0,(13,8):'monster1',(13,9):0,(13,10):'monster1',(13,11):0,(13,12):1,(14,1):1,(14,2):0,(14,3):0,(14,4):1,(14,5):0,(14,6):0,(14,7):0,(14,8):0,(14,9):'monster1',(14,10):0,(14,11):0,(14,12):1,(15,1):1,(15,2):0,(15,3):'down',(15,4):1,(15,5):'up',(15,6):'medicine',(15,7):0,(15,8):'monster1',(15,9):0,(15,10):'monster1',(15,11):0,(15,12):1,(16,1):1,(16,2):1,(16,3):1,(16,4):1,(16,5):1,(16,6):1,(16,7):1,(16,8):1,(16,9):1,(16,10):1,(16,11):1,(16,12):1}
MAP_3 = {(1,1):1,(1,2):1,(1,3):1,(1,4):1,(1,5):1,(1,6):1,(1,7):1,(1,8):1,(1,9):1,(1,10):1,(1,11):1,(1,12):1,(2,1):1,(2,2):'key2',(2,3):1,(2,4):0,(2,5):0,(2,6):'up',(2,7):1,(2,8):0,(2,9):0,(2,10):'monster2',(2,11):'key1',(2,12):1,(3,1):1,(3,2):'coffee',(3,3):1,(3,4):0,(3,5):0,(3,6):0,(3,7):1,(3,8):0,(3,9):0,(3,10):0,(3,11):'monster1',(3,12):1,(4,1):1,(4,2):0,(4,3):1,(4,4):0,(4,5):0,(4,6):0,(4,7):1,(4,8):0,(4,9):0,(4,10):0,(4,11):0,(4,12):1,(5,1):1,(5,2):0,(5,3):1,(5,4):1,(5,5):0,(5,6):1,(5,7):1,(5,8):'monster1',(5,9):1,(5,10):1,(5,11):0,(5,12):1,(6,1):1,(6,2):0,(6,3):'door_close',(6,4):'monster1',(6,5):0,(6,6):0,(6,7):0,(6,8):0,(6,9):1,(6,10):'coffee',(6,11):0,(6,12):1,(7,1):1,(7,2):0,(7,3):1,(7,4):0,(7,5):0,(7,6):0,(7,7):0,(7,8):0,(7,9):1,(7,10):0,(7,11):'monster1',(7,12):1,(8,1):1,(8,2):'monster1',(8,3):1,(8,4):1,(8,5):1,(8,6):1,(8,7):1,(8,8):1,(8,9):1,(8,10):'monster2',(8,11):0,(8,12):1,(9,1):1,(9,2):'monster1',(9,3):1,(9,4):1,(9,5):1,(9,6):1,(9,7):1,(9,8):1,(9,9):1,(9,10):'monster2',(9,11):0,(9,12):1,(10,1):1,(10,2):'monster1',(10,3):1,(10,4):0,(10,5):0,(10,6):0,(10,7):0,(10,8):0,(10,9):1,(10,10):0,(10,11):'monster1',(10,12):1,(11,1):1,(11,2):0,(11,3):'door_close',(11,4):'monster1',(11,5):0,(11,6):0,(11,7):0,(11,8):0,(11,9):1,(11,10):'medicine',(11,11):0,(11,12):1,(12,1):1,(12,2):0,(12,3):1,(12,4):1,(12,5):0,(12,6):1,(12,7):1,(12,8):'monster1',(12,9):1,(12,10):1,(12,11):0,(12,12):1,(13,1):1,(13,2):'coffee',(13,3):1,(13,4):0,(13,5):0,(13,6):0,(13,7):1,(13,8):0,(13,9):0,(13,10):0,(13,11):0,(13,12):1,(14,1):1,(14,2):'medicine',(14,3):1,(14,4):0,(14,5):0,(14,6):0,(14,7):1,(14,8):0,(14,9):0,(14,10):0,(14,11):'monster2',(14,12):1,(15,1):1,(15,2):'mathbook',(15,3):1,(15,4):'medicine',(15,5):0,(15,6):'down',(15,7):1,(15,8):0,(15,9):0,(15,10):'monster1',(15,11):'key1',(15,12):1,(16,1):1,(16,2):1,(16,3):1,(16,4):1,(16,5):1,(16,6):1,(16,7):1,(16,8):1,(16,9):1,(16,10):1,(16,11):1,(16,12):1}
MAP_4 = {(1,1):1,(1,2):1,(1,3):1,(1,4):1,(1,5):1,(1,6):1,(1,7):1,(1,8):1,(1,9):1,(1,10):1,(1,11):1,(1,12):1,(2,1):1,(2,2):'medicine',(2,3):0,(2,4):0,(2,5):'down',(2,6):0,(2,7):1,(2,8):'medicine',(2,9):'medicine',(2,10):1,(2,11):'mathbook',(2,12):1,(3,1):1,(3,2):'coffee',(3,3):0,(3,4):0,(3,5):0,(3,6):0,(3,7):1,(3,8):'coffee',(3,9):'coffee',(3,10):1,(3,11):0,(3,12):1,(4,1):1,(4,2):1,(4,3):1,(4,4):'monster1',(4,5):'monster2',(4,6):1,(4,7):1,(4,8):0,(4,9):1,(4,10):1,(4,11):0,(4,12):1,(5,1):1,(5,2):0,(5,3):0,(5,4):0,(5,5):0,(5,6):0,(5,7):0,(5,8):0,(5,9):0,(5,10):'monster2',(5,11):'monster2',(5,12):1,(6,1):1,(6,2):0,(6,3):1,(6,4):1,(6,5):1,(6,6):1,(6,7):1,(6,8):1,(6,9):1,(6,10):1,(6,11):1,(6,12):1,(7,1):1,(7,2):0,(7,3):0,(7,4):0,(7,5):1,(7,6):0,(7,7):0,(7,8):0,(7,9):1,(7,10):0,(7,11):0,(7,12):0,(8,1):1,(8,2):0,(8,3):'monster1',(8,4):0,(8,5):1,(8,6):0,(8,7):1,(8,8):'key2',(8,9):1,(8,10):0,(8,11):'word12',(8,12):'up',(9,1):1,(9,2):'medicine',(9,3):1,(9,4):0,(9,5):0,(9,6):'monster2',(9,7):1,(9,8):1,(9,9):1,(9,10):0,(9,11):'word12',(9,12):'up',(10,1):1,(10,2):1,(10,3):1,(10,4):0,(10,5):1,(10,6):0,(10,7):0,(10,8):0,(10,9):1,(10,10):0,(10,11):0,(10,12):0,(11,1):1,(11,2):'medicine',(11,3):1,(11,4):'monster1',(11,5):1,(11,6):0,(11,7):0,(11,8):'door_close',(11,9):1,(11,10):'door_close2',(11,11):1,(11,12):1,(12,1):1,(12,2):0,(12,3):0,(12,4):0,(12,5):1,(12,6):'monster1',(12,7):1,(12,8):0,(12,9):1,(12,10):'word20',(12,11):0,(12,12):1,(13,1):1,(13,2):0,(13,3):1,(13,4):0,(13,5):'monster1',(13,6):'coffee',(13,7):1,(13,8):0,(13,9):0,(13,10):0,(13,11):0,(13,12):1,(14,1):1,(14,2):0,(14,3):1,(14,4):1,(14,5):1,(14,6):1,(14,7):1,(14,8):1,(14,9):1,(14,10):0,(14,11):0,(14,12):1,(15,1):1,(15,2):0,(15,3):'monster1',(15,4):'monster1',(15,5):0,(15,6):'medicine',(15,7):0,(15,8):'key1',(15,9):1,(15,10):'medicine',(15,11):'coffee',(15,12):1,(16,1):1,(16,2):1,(16,3):1,(16,4):1,(16,5):1,(16,6):1,(16,7):1,(16,8):1,(16,9):1,(16,10):1,(16,11):1,(16,12):1}
MAP_5 = {(1,1):'lava',(1,2):'lava',(1,3):'lava',(1,4):'lava',(1,5):'lava',(1,6):'lava',(1,7):'lava',(1,8):'lava',(1,9):'lava',(1,10):'lava',(1,11):0,(1,12):0,(2,1):'lava',(2,2):'lava',(2,3):'lava',(2,4):'lava',(2,5):'lava',(2,6):'lava',(2,7):'lava',(2,8):'lava',(2,9):'lava',(2,10):'lava',(2,11):0,(2,12):0,(3,1):'lava',(3,2):'lava',(3,3):'lava',(3,4):'lava',(3,5):'lava',(3,6):'lava',(3,7):'lava',(3,8):'lava',(3,9):'lava',(3,10):'lava',(3,11):0,(3,12):0,(4,1):'lava',(4,2):'lava',(4,3):'lava',(4,4):'lava',(4,5):'lava',(4,6):'lava',(4,7):'lava',(4,8):'lava',(4,9):'lava',(4,10):'lava',(4,11):0,(4,12):0,(5,1):'lava',(5,2):'lava',(5,3):'lava',(5,4):'lava',(5,5):'lava',(5,6):'lava',(5,7):'lava',(5,8):'lava',(5,9):'lava',(5,10):'lava',(5,11):0,(5,12):0,(6,1):'lava',(6,2):'lava',(6,3):'lava',(6,4):'lava',(6,5):'lava',(6,6):'lava',(6,7):'lava',(6,8):'lava',(6,9):'lava',(6,10):'lava',(6,11):0,(6,12):0,(7,1):'lava',(7,2):'lava',(7,3):'lava',(7,4):'lava',(7,5):'lava',(7,6):'lava',(7,7):'lava',(7,8):'lava',(7,9):'lava',(7,10):'lava',(7,11):0,(7,12):0,(8,1):0,(8,2):0,(8,3):'word19',(8,4):'word18',(8,5):0,(8,6):'word17',(8,7):0,(8,8):'word16',(8,9):0,(8,10):'word15',(8,11):'word14',(8,12):'word13',(9,1):0,(9,2):'boss',(9,3):'word19',(9,4):"bosswall",(9,5):0,(9,6):"bosswall2",(9,7):0,(9,8):"bosswall3",(9,9):0,(9,10):"bosswall4",(9,11):'word14',(9,12):'word13',(10,1):'lava',(10,2):'lava',(10,3):'lava',(10,4):'lava',(10,5):'lava',(10,6):'lava',(10,7):'lava',(10,8):'lava',(10,9):'lava',(10,10):'lava',(10,11):0,(10,12):0,(11,1):'lava',(11,2):'lava',(11,3):'lava',(11,4):'lava',(11,5):'lava',(11,6):'lava',(11,7):'lava',(11,8):'lava',(11,9):'lava',(11,10):'lava',(11,11):0,(11,12):0,(12,1):'lava',(12,2):'lava',(12,3):'lava',(12,4):'lava',(12,5):'lava',(12,6):'lava',(12,7):'lava',(12,8):'lava',(12,9):'lava',(12,10):'lava',(12,11):0,(12,12):0,(13,1):'lava',(13,2):'lava',(13,3):'lava',(13,4):'lava',(13,5):'lava',(13,6):'lava',(13,7):'lava',(13,8):'lava',(13,9):'lava',(13,10):'lava',(13,11):0,(13,12):0,(14,1):'lava',(14,2):'lava',(14,3):'lava',(14,4):'lava',(14,5):'lava',(14,6):'lava',(14,7):'lava',(14,8):'lava',(14,9):'lava',(14,10):'lava',(14,11):0,(14,12):0,(15,1):'lava',(15,2):'lava',(15,3):'lava',(15,4):'lava',(15,5):'lava',(15,6):'lava',(15,7):'lava',(15,8):'lava',(15,9):'lava',(15,10):'lava',(15,11):0,(15,12):0,(16,1):'lava',(16,2):'lava',(16,3):'lava',(16,4):'lava',(16,5):'lava',(16,6):'lava',(16,7):'lava',(16,8):'lava',(16,9):'lava',(16,10):'lava',(16,11):0,(16,12):0}
FLOOR = {1:MAP_1,2:MAP_2,3:MAP_3,4:MAP_4,5:MAP_5}

#设计怪物血量
MONSTER1 =  Actor('slm1')
MONSTER2 =  Actor('eye1')
MONSTER_BLOD = Rect((200,750),(50,50))
MONSTER_MOVE = Rect((0,750),(50,50))
MONSTER_BLOD2 = Rect((150,750),(50,50))
MONSTER_MOVE2 = Rect((0,750),(50,50))
BOSS = Actor('boss1')
BOSS_BLOD = Rect((50000,750),(50,50))
BOSS_MOVE = Rect((0,750),(50,50))
#设计一个钥匙数量槽和剧情触发器
KEYS_NEMBER = Rect((0,750),(50,50))
KEYS_NEMBER2 = Rect((0,750),(50,50))
KEYS_WORD = Rect((0,750),(50,50))
KEYS_WORD2 = Rect((0,750),(50,50))

#设计一个高数书的语言触发器
MATH_WORD = Rect((0,750),(50,50))

#提示语计数器
WORD = Rect((0,750),(50,50))
WORD2 = Rect((0,750),(50,50))
#高数书计数器
MATHBOOK_NEMBER = Rect((4,750),(50,50))
MUSIC_WORDS = Rect((0,750),(50,50))
#最后的滚动字幕
END_MOVE = Rect((0,750),(50,50))
WORDSY = 0
ENDA = 0
BACK = Actor('backg1')
BACK.x = 500
BACK.y = 400
BOARD = Actor('backg4')
BOARD.x = 500
BOARD.y = 400
TIME1 = 0
TIME2 = 0

def update():
# 这一行是楼层判定
    MAP,a = MAP_X(FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x)
#模块加载
    WORD.x = 0
    for i in range(1,17):
        for j in range(1,13):
            if MAP[(i,j)]==1 or MAP[(i,j)] == 'lava':
                BOX.x,BOX.y,CHECK1 = wall_stop(i,j)
            if MAP[(i,j)]== 'monster1':
                BOX.x,BOX.y,MONSTER_BLOD.x,HEALTH.x= monster1_fight(i,j,ATTACK)
                MAP[(i,j)],MONSTER_BLOD.x = monster1_dead()
                BLOCKs,MONSTER_MOVE.x = monster1(i,j)
            if MAP[(i,j)]== 'monster2':
                BOX.x,BOX.y,MONSTER_BLOD2.x,REASON.x= monster2_fight(i,j,ATTACK)
                MAP[(i,j)],MONSTER_BLOD2.x = monster2_dead()
                BLOCKs,MONSTER_MOVE2.x = monster2(i,j)
            if MAP[(i,j)]== 'boss':
                BOX.x,BOX.y,BOSS_BLOD.x,HEALTH.x= boss_fight(i,j,ATTACK)
                MAP[(i,j)],BOSS_BLOD.x = boss_dead()
                BLOCKs,BOSS_MOVE.x = boss(i,j)
            if MAP[(i,j)]== 'medicine':
                MAP[(i,j)],HEALTH.x= drink(i,j)
            if MAP[(i,j)] == 'pickup_medicine' and (WORD.x == 0 or WORD.x == 8):
                WORD.x = word8(i,j)
            if MAP[(i,j)]== 'coffee':
                MAP[(i,j)],REASON.x= drink_coffee(i,j)
            if MAP[(i,j)] == 'pickup_coffee' and (WORD.x == 0 or WORD.x == 9):
                WORD.x = word9(i,j)
            if MAP[(i,j)] =='door_close' and KEYS_NEMBER.x == 0:
                BOX.x,BOX.y,CHECK1 = wall_stop(i,j)
            if MAP[(i,j)] =='door_close' and KEYS_NEMBER.x != 0:
                MAP[(i,j)],KEYS_NEMBER.x= open_door(i,j)
            if MAP[(i,j)] =='door_close2' and KEYS_NEMBER2.x == 0:
                BOX.x,BOX.y,CHECK1 = wall_stop(i,j)
            if MAP[(i,j)] =='door_close2' and KEYS_NEMBER2.x != 0:
                MAP[(i,j)],KEYS_NEMBER2.x= open_door2(i,j)
            if (MAP[(i,j)] =='bosswall' and MATHBOOK_NEMBER.x == 0) or (MAP[(i,j)] =='bosswall2' and MATHBOOK_NEMBER.x == 0) or (MAP[(i,j)] =='bosswall3' and MATHBOOK_NEMBER.x == 0) or (MAP[(i,j)] =='bosswall4' and MATHBOOK_NEMBER.x == 0):
                BOX.x,BOX.y,CHECK1 = bosswall_stop(i-1,j)
                BOX.x,BOX.y,MONSTER_BLOD2.x,REASON.x= monster2_fight(i-1,j,ATTACK)
                BOX.x,BOX.y,MONSTER_BLOD2.x,REASON.x= monster2_fight(i,j,ATTACK)
            if MAP[(i,j)] =='bosswall' and MATHBOOK_NEMBER.x >0:
                b = 'bosswall'
                MAP[(i,j)]= bosswall_dead(i-1,j,b)
                if MAP[(i,j)] == 'word18':
                    MAP[(9,5)]= 'AC'
                    MAP[(9,6)]= 'AC'
                    MAP[(9,7)]= 'AC'
                    MAP[(9,8)]= 'AC'
                    MAP[(9,9)]= 'AC'
                    MAP[(9,10)]= 'AC'
            if MAP[(i,j)] =='bosswall2' and MATHBOOK_NEMBER.x >0:
                b = 'bosswall2'
                MAP[(i,j)]= bosswall_dead(i-1,j,b)
            if MAP[(i,j)] =='bosswall3' and MATHBOOK_NEMBER.x >0:
                b = 'bosswall3'
                MAP[(i,j)]= bosswall_dead(i-1,j,b)
            if MAP[(i,j)] =='bosswall4' and MATHBOOK_NEMBER.x >0:
                b = 'bosswall4'
                MAP[(i,j)]= bosswall_dead(i-1,j,b)
            if MAP[(i,j)] == 'key1':
                MAP[i,j],KEYS_NEMBER.x = Key_pick(i,j)
            if MAP[(i,j)] == 'pickup_key1':
                KEYS_WORD.x = on_Keys(i,j)
            if MAP[(i,j)] == 'key2':
                MAP[i,j],KEYS_NEMBER2.x = Key_pick2(i,j)
            if MAP[(i,j)] == 'pickup_key2':
                KEYS_WORD2.x = on_Keys2(i,j)
            if MAP[(i,j)] == 'sword1':
                if REASON.x>60:
                    MAP[i,j],ATTACK.x = pick_upsword1(i,j)
            if MAP[(i,j)] == 'pickup_sword1':
                ATTACK_WORD.x = on_sword(i,j)
            if MAP[(i,j)] == 'armour1':
                if REASON.x>60:
                    MAP[i,j],DEFENCE.x = pick_uparmour1(i,j)
            if MAP[(i,j)] == 'pickup_armour1':
                DEFENCE_WORD.x = on_armour(i,j)
            if MAP[(i,j)] == 'mathbook':
                MAP[i,j],REASON.x,MATHBOOK_NEMBER.x = pick_upmathbook(i,j)
            if MAP[(i,j)] == 'mathbook_open':
                MATH_WORD.x = on_mathbook(i,j)
            if MAP[(i,j)] == 'word1' and (WORD.x == 0 ):
                ks = 1
                WORD.x = word1(i,j,ks)
            if MAP[(i,j)] == 'word2' and (WORD.x == 0 ):
                ks = 2
                WORD.x = word2(i,j,ks)
            if MAP[(i,j)] == 'word3' and (WORD.x == 0 ):
                ks = 3
                WORD.x = word3(i,j,ks)
            if MAP[(i,j)] == 'word4' and (WORD.x == 0 ):
                ks = 4
                WORD.x = word4(i,j,ks)
            if MAP[(i,j)] == 'word5' and (WORD.x == 0 ):
                ks = 5
                WORD.x = word5(i,j,ks)
            if MAP[(i,j)] == 'word6' and (WORD.x == 0 ):
                ks = 6
                WORD.x = word6(i,j,ks)
            if MAP[(i,j)] == 'word7' and (WORD.x == 0 ):
                ks = 7
                WORD.x = word7(i,j,ks)
            if MAP[(i,j)] == 'word10' and (WORD.x == 0 ):
                WORD.x = word10(i,j)
            if MAP[(i,j)] == 'word11' and (WORD.x == 0 ):
                WORD.x = word11(i,j)
            if MAP[(i,j)] == 'word12' and (WORD.x == 0):
                WORD.x = word12(i,j)
            if MAP[(i,j)] == 'word13' and (WORD.x == 0 ):
                WORD.x = word13(i,j)
            if MAP[(i,j)] == 'word14' and (WORD.x == 0 ):
                WORD.x = word14(i,j)
            if MAP[(i,j)] == 'word15' and (WORD.x == 0 ):
                WORD.x = word15(i,j)
            if MAP[(i,j)] == 'word16' and (WORD.x == 0 ):
                WORD.x = word16(i,j)
            if MAP[(i,j)] == 'word17' and (WORD.x == 0 ):
                WORD.x = word17(i,j)
            if MAP[(i,j)] == 'word18' and (WORD.x == 0 ):
                WORD.x = word18(i,j)
            if MAP[(i,j)] == 'word19' and (WORD.x == 0 ):
                WORD.x = word19(i,j)
            if MAP[(i,j)] == 'word20' and (WORD.x == 0 ):
                WORD.x = word20(i,j)
# 上下楼
            if MAP[(i,j)]=='up' and MAP == FLOOR[1]:
                k = 1
                FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x = Floor_up(i,j,k)
                if FLOOR_READER12 == 900:
                    break
            if MAP == FLOOR[2]and MAP[(i,j)]=='down':
                k = 1
                FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x = Floor_down(i,j,k)
                if FLOOR_READER12 == 950:
                    break
            if MAP[(i,j)]=='up' and MAP == FLOOR[2]:
                k = 2
                FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x = Floor_up(i,j,k)
                if FLOOR_READER23 == 950:
                    break
            if MAP == FLOOR[3] and MAP[(i,j)]=='down':
                k = 2
                FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x = Floor_down(i,j,k)
                if FLOOR_READER23 == 900:
                    break
            if MAP[(i,j)]=='up' and MAP == FLOOR[3]:
                k = 3
                FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x = Floor_up(i,j,k)
                if FLOOR_READER34 == 950:
                    break
            if MAP == FLOOR[4] and MAP[(i,j)]=='down':
                k = 3
                FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x = Floor_down(i,j,k)
                if FLOOR_READER34 == 900:
                    break
            if MAP[(i,j)]=='up' and MAP == FLOOR[4]:
                k = 4
                FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x = Floor_up(i,j,k)
                if FLOOR_READER45 == 950:
                    break
            if MAP == FLOOR[5] and MAP[(i,j)]=='down':
                k = 4
                FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x = Floor_down(i,j,k)
                if FLOOR_READER45 == 900:
                    break
            if MAP == FLOOR[5] and MUSIC_WORDS.x== 0:
                global speed
                sounds.putong.stop()
                sounds.boss_music.play()
                #speed = 1
                MUSIC_WORDS.x =1               
#楼层判定结束 
#理智判定
    if REASON.x <=60 and REASON.x>40 and MAD.x <50:
        MADS = 2
        ATTACK.x,DEFENCE.x,HEALTH.x,MAD.x = mad(MADS)
    if REASON.x <=40 and REASON.x>10 and MAD.x<100:
        MADS = 3
        ATTACK.x,DEFENCE.x,HEALTH.x,MAD.x = mad(MADS)
    if REASON.x <=60 and REASON.x>40 and MAD.x >100:
        MADS = 3
        ATTACK.x,DEFENCE.x,HEALTH.x,MAD.x = end_mad(MADS)
    if REASON.x >60 and MAD.x>50:
        MADS = 2
        ATTACK.x,DEFENCE.x,HEALTH.x,MAD.x = end_mad(MADS)
#移动判定
    BOX.x,BOX.y= move()
    if WALK == 0:
        move_act()
        if WALK ==1:
            BOX.image=walk()
        elif WALK ==2:
            BOX.image=walk2()
        elif WALK ==3:
            BOX.image=walk3()
        elif WALK ==4:
            BOX.image=walk4()
        if WALK == 0:
            BOX.image = 'hero'
    else:
        move_act()
    BOX.x,BOX.y = edg()
    START_WORD.x = start()
    global ENDA
    if BOSS_BLOD.x<=0 and ENDA == 0:
        clock.schedule_unique(end, 6)
        ENDA = 1

def draw():
    MAP , FLOOR_COUNT= MAP_X(FLOOR_READER12.x,FLOOR_READER23.x,FLOOR_READER34.x,FLOOR_READER45.x)
    screen.fill((100,100,100))
    screen.draw.rect(BACKGROUNG, COLOR1)
    screen.draw.rect(SPEEK,COLOR2)
    screen.draw.rect(EQUIPMENT,COLOR3)
    screen.draw.text('我是状态栏',(10,10),fontsize=30,fontname="a",color = 'yellow')
    screen.draw.text('生命值：%d'%HEALTH.x,(10,40),fontsize=30,fontname="a",color = 'yellow')
    screen.draw.text('攻击力：%d'%ATTACK.x,(10,70),fontsize=30,fontname="a",color = 'yellow')
    screen.draw.text('防御力：%d'%DEFENCE.x,(10,100),fontsize=30,fontname="a",color = 'yellow')
    screen.draw.text('精神状态：%d'%REASON.x,(10,130),fontsize=30,fontname="a",color = 'yellow')
    screen.draw.rect(BACKGROUNG2, 'white')
    screen.draw.rect(BACKGROUNG3, 'white')
    KEY1 = Actor('key1(1)')
    KEY1.x =25
    KEY1.y =320
    KEY1.draw()
    KEY2 = Actor('key2 (2)')
    KEY2.x =25
    KEY2.y =365
    KEY2.draw()
    screen.draw.text('    :%d'%KEYS_NEMBER.x,(10,300),fontsize=30,fontname="a",color = 'yellow')
    screen.draw.text('    :%d'%KEYS_NEMBER2.x,(10,350),fontsize=30,fontname="a",color = 'yellow')
    screen.draw.text("#4#2@：%d"%MATHBOOK_NEMBER.x,(10,380),fontsize=30,fontname="a",color = 'yellow')
    screen.draw.text(FLOOR_COUNT,(900,610),fontsize=30,fontname="a",color = 'yellow')
    screen.draw.text("我是装备栏",(10,190),fontsize=30,fontname="a",color = 'yellow')
    if ATTACK.x == 50 or ATTACK.x == 75 or ATTACK.x == 25:
        screen.draw.text('村好剑',(10,220),fontsize=30,fontname="a",color = 'yellow')
    if DEFENCE.x == 30 or DEFENCE.x == 45 or DEFENCE.x == 15:
        screen.draw.text('村好盾',(10,250),fontsize=30,fontname="a",color = 'yellow')
    for i in range(1,17):
        for j in range(1,13):
            if MAP[(i,j)]==0:
                BLOCK = ground(i,j)
                BLOCK.draw()
            if MAP[(i,j)]==1:
                BLOCK = wall(i,j)
                BLOCK.draw()
            if MAP[(i,j)]=='up':
                BLOCK = stairs_up(i,j)
                BLOCK.draw()
            if MAP[(i,j)]=='down':
                BLOCK = stairs_down(i,j)
                BLOCK.draw()
            if MAP[(i,j)]=='monster1':
                BLOCK,MONSTER_MOVE.x = monster1(i,j)
                BLOCK.draw()
            if MAP[(i,j)]=='boss':
                BLOCK,MONSTER_MOVE.x = boss(i,j)
                BLOCK.draw()
            if MAP[(i,j)]=='monster2':
                BLOCK,MONSTER_MOVE2.x = monster2(i,j)
                BLOCK.draw()
            if MAP[(i,j)]=='medicine':
                BLOCK = medicine(i,j)
                BLOCK.draw()
            if MAP[(i,j)]=='coffee':
                BLOCK = coffee(i,j)
                BLOCK.draw()
            if MAP[(i,j)] =='door_close':
                BLOCK = door_close(i,j)
                BLOCK.draw()
            if MAP[(i,j)] =='door_open':
                BLOCK = door_open(i,j)
                BLOCK.draw()
            if MAP[(i,j)] =='door_close2':
                BLOCK = door_close2(i,j)
                BLOCK.draw()
            if MAP[(i,j)] =='door_open2':
                BLOCK = door_open2(i,j)
                BLOCK.draw()
            if MAP[(i,j)] =='key1':
                BLOCK = Key1(i,j)
                BLOCK.draw()
            if MAP[(i,j)] =='key2':
                BLOCK = Key2(i,j)
                BLOCK.draw()
            if MAP[(i,j)] =='pickup_key1' or MAP[(i,j)] =='pickup_key2' or MAP[(i,j)] =='word3' or MAP[(i,j)] =='word4' or MAP[(i,j)] =='word5' or MAP[(i,j)] =='word6' or MAP[(i,j)] =='word7':
                BLOCK = ground(i,j)
                BLOCK.draw()
            if MAP[(i,j)] == 'sword1':
                BLOCK = sword1(i,j)
                BLOCK.draw()
            if MAP[(i,j)] == 'armour1':
                BLOCK = armour1(i,j)
                BLOCK.draw()
            if MAP[(i,j)] == 'mathbook':
                BLOCK = mathbook(i,j)
                BLOCK.draw()
            if MAP[(i,j)] == 'mathbook_open' or MAP[(i,j)]=='pickup_armour1' or MAP[(i,j)]=='pickup_sword1' or MAP[(i,j)]=='pickup_medicine' or MAP[(i,j)] == 'pickup_coffee' or MAP[(i,j)] == 'word1' or MAP[(i,j)] == 'word2':
                BLOCK = ground(i,j)
                BLOCK.draw()
            if MAP[(i,j)] =='word10' or MAP[(i,j)] =='word11'or MAP[(i,j)] =='word12' or MAP[(i,j)] =='word13' or MAP[(i,j)] =='word14' or MAP[(i,j)] =='word15' or MAP[(i,j)] =='word16' or MAP[(i,j)] =='word17' or MAP[(i,j)] =='word18' or MAP[(i,j)] =='word19'or MAP[(i,j)] =='word20':
                BLOCK = ground(i,j)
                BLOCK.draw()
            if MAP[(i,j)]=='lava':
                BLOCK = lava(i,j)
                BLOCK.draw()
            if MAP[(i,j)]=='bosswall':
                BLOCK = bosswall(i-1,j)
                BLOCK.draw()
            if MAP[(i,j)]=='bosswall2':
                BLOCK = bosswall2(i-1,j)
                BLOCK.draw()
            if MAP[(i,j)]=='bosswall3':
                BLOCK = bosswall3(i-1,j)
                BLOCK.draw()
            if MAP[(i,j)]=='bosswall4':
                BLOCK = bosswall4(i-1,j)
                BLOCK.draw()
            if MAP[(i,j)]=='AC':
                BLOCK = accept(i-1,j)
                BLOCK.draw()
    #主角绘画
    BOX.draw()
#文字提示
    if MATH_WORD.x == 1:
        screen.draw.text('你看不清这是什么，但你感觉莫名的有些熟悉',(10,610),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('学不会，学不会，学不会，学不会！！',(10,650),fontsize=40,fontname="a",color = 'red')
        screen.draw.text('@#%#@！@@￥#￥%……#@~@#',(10,650),fontsize=40,fontname="a",color = 'red')
        screen.draw.text('（精神-20）',(10,690),fontsize=40,fontname="a",color = 'red')
    if KEYS_WORD.x == 1:
        screen.draw.text('你在这里捡到了一把沾满铁锈的钥匙,',(10,610),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('也许还能用,也许不能....',(10,660),fontsize=40,fontname="a",color = 'yellow')
    if KEYS_WORD2.x == 1:
        screen.draw.text('一把被严重腐蚀的钥匙,',(10,610),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('也不知道有什么用....',(10,660),fontsize=40,fontname="a",color = 'yellow')
    if DEFENCE_WORD.x == 1:
        screen.draw.text('你记得这面盾，这是村里最好的盾',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if ATTACK_WORD.x == 1:
        screen.draw.text('你记得这柄剑，这是村里最好的剑',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if HEALTH.x <=0 or REASON.x <=0:
        ATTACK.x = 0
        screen.fill((0,0,0))
        screen.draw.text("GAME OVER",(220,200),fontsize=100,fontname="a",color = 'red')
        screen.draw.text("或许是运气不好，请再接再厉！",(220,300),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 1:
        screen.draw.text('以上是基本介绍，请努力逃出去吧！',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 2:
        screen.draw.text('一只...史莱姆？你不敢相信自己的眼睛',(10,610),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('（攻击史莱姆时你的生命值会减少）',(10,650),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('史莱姆：血量：200  攻击力：80',(10,690),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 3:
        screen.draw.text('一扇被严重腐蚀的门，也许需要相似的东西才能打开',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 4:
        screen.draw.text('一只诡异的眼睛悬在半空中',(10,610),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('（驱散注视需要消耗精神值）',(10,650),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('诡异的眼睛：血量：150  攻击力：5（精神）',(10,690),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('注意：精神状态降低到一定程度后会获得负面属性！',(10,745),fontsize=40,fontname="a",color = 'red')
    if WORD.x == 5:
        screen.draw.text('这瓶"热水"可以恢复你的体力（+200）',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 6:
        screen.draw.text('咖啡可以恢复你的精神，但对身体不好',(10,610),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('精神+15；生命-20',(10,650),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 7:
        screen.draw.text('一扇上了锁的门，没有钥匙是出不去的',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 8:
        screen.draw.text('你喝了口水，感觉身心都受到了治愈',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 9:
        screen.draw.text('你喝了一杯咖啡，精神多了！',(10,610),fontsize=40,fontname="a",color = 'red')
    if WORD.x == 10:
        screen.draw.text('你逐渐理解了书中的内容',(10,610),fontsize=60,fontname="a",color = 'GOLD')
    if WORD.x == 11:
        screen.draw.text('你环顾四周，发现自己身处在于地牢之中',(10,610),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('回忆不起自己为什么在这个地方，你知道你还有重要的事情要做。',(10,650),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('设法逃出去吧。',(10,690),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 12:
        screen.draw.text('你感到一阵恶寒',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 13:
        screen.draw.text('"经过74天的%&￥/，你终于来参加了......”',(10,610),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('不可名状的东西说着难以理解的话',(10,650),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text('“现在开始/*@%” 没有回头路了"',(10,690),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 14:
        screen.draw.text('阻拦着你的东西令你头痛欲裂',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 15:
        screen.draw.text('你长舒一口气',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 16:
        screen.draw.text('你逐渐适应了节奏',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 17:
        screen.draw.text('你灵感迸发',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 18:
        screen.draw.text('“我理解了！”',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 19:
        screen.draw.text(' 一口气解决它！',(10,610),fontsize=40,fontname="a",color = 'yellow')
    if WORD.x == 20:
        screen.draw.text(' 开弓没有回头箭，请确保你状态良好',(10,610),fontsize=40,fontname="a",color = 'yellow')
        screen.draw.text(' 并且拿上所有“重要”的东西，即使它们在之前很没用',(10,650),fontsize=40,fontname="a",color = 'yellow')
    MAD_words = mad_words()
    screen.draw.text(MAD_words,(10,700),fontsize=40,fontname="a",color = 'red')
    if START_WORD.x == 0:
        screen.fill((255,255,255))
        screen.draw.text("逃离二教",(220,200),fontsize=100,fontname="a",color = 'red')
        screen.draw.text("吴延景，王梓涵",(220,300),fontsize=40,fontname="a",color = 'brown')
        screen.draw.text("请按空格开始游戏",(220,500),fontsize=30,fontname="a",color = 'black')
    if BOSS_BLOD.x < 0:
        screen.fill((0,0,0))
        global WORDSY
        global TIME2
        TIME2 +=1
        if MUSIC_WORDS.x == 1 and TIME2>100:
            sounds.ed.play()
            MUSIC_WORDS.x = 2
        if TIME2 >100:
            screen.fill((255,255,255))
            BACK.draw()
        global TIME1
        if BACK.image == 'backg3':
            TIME1 += 1
            if TIME1 >= 300:
                BOARD.draw()
                WORDSY +=1
                screen.draw.text("《逃离二教》",(110,890-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text(" ",(110,950-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("脚本：吴延景",(110,1000-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("地图设计：吴延景、王梓涵",(110,1050-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("贴图、素材绘制：吴延景",(110,1100-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("数值设计：王梓涵",(110,1150-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("程序设计与制作：王梓涵",(110,1200-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("本游戏所有素材图片均为作者拍摄、手工绘制",(110,1250-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("音效素材来源：https://www.ear0.com/",(110,1300-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("bgm：",(110,1350-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("Judicare tibi-深澤秀行 魔法使いの夜 オリジナルサ",(110,1400-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("thames troll(wood)-hil-魔法使いの夜 オリジナル",(110,1450-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("《ever after (ED size)-芳賀敬太 / 永田大祐 EVER AFTER",(110,1500-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("～MUSIC FROM　",(110,1550-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("",(110,1600-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("感谢陈斌老师开设本次活动，",(110,1650-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("您的悉心教导，让本作品的创作成为可能",(110,1700-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("",(110,1750-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("感谢各位玩家的游玩，",(110,1800-WORDSY),fontsize=30,fontname="b",color = 'black')
                screen.draw.text("愿拙作能给您带去一丝愉悦",(110,1850-WORDSY),fontsize=30,fontname="b",color = 'black')
                if WORDSY <= 1600:
                    screen.draw.text(" Fin.",(450,1950-WORDSY),fontsize=60,fontname="c",color = 'black')
                else:
                    screen.draw.text(" Fin.",(450,350),fontsize=60,fontname="c",color = 'black')        
pgzrun.go()
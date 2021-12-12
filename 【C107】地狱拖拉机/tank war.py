from easygui import *
uk = ccbox('为了提升游戏体验,请先选择您电脑的键盘类型:','键盘类型',['含有小键盘','不含小键盘'])
wk = not uk
from random import *
from time import *
from math import *
import pgzrun

TITLE = 'TANK WAR'
WIDTH = 1800
HEIGHT = 1200

#控制游戏的物理常数
GRAVITY = 0.4
SPEED = 5
STRENGTH = 8

#directory
x = Actor('bomb')
x.begin = True
x.gaming = False
x.death = False
x.manuals = False

#icons
begin_gaming = Actor('icon_begin',center=(900,650))#从begin传送到gaming
begin_manuals = Actor('icon_manuals',center=(900,900))#从begin传送到manuals
manuals_begin = Actor('icon_delete',(30,30))#从manuals传送到begin
death_gaming = Actor('icon_replay',center=(900,900))#从death传送到gaming


#actors
ground = []
cara = Actor('sheep_1_rt')
balla = Actor('bomb')
tonga = Actor('gun_1',anchor=(12,23))
carb = Actor('sheep_2_lt')
ballb = Actor('bomb')
tongb = Actor('gun_2',anchor=(24,24))

def reset():
    global ground
    ground = [Actor('block_soil',bottomleft=(60*i,1200-60*t)) for i in range(0,30) for t in range(6)]\
             +[Actor('block_grass',bottomleft=(60*i,840)) for i in range(0,30)]\
             +[Actor('block_mout',bottomleft=(60*i,1200-60*t)) for i in range(7,9) for t in range(7,randint(8,11))]\
             +[Actor('block_mout',bottomleft=(60*i,1200-60*t)) for i in range(21,23) for t in range(7,randint(8,11))]\
             +[Actor('block_mout',bottomleft=(60*i,1200-60*t)) for i in range(11,19) for t in range(7,randint(12,19))]\
             +[Actor('block_mout',bottomleft=(60*i,1200-60*t)) for i in range(9,11) for t in range(7,randint(9,13))]\
             +[Actor('block_mout',bottomleft=(60*i,1200-60*t)) for i in range(19,21) for t in range(7,randint(9,13))]
    cara.pos = (150,300)
    cara.win = False
    cara.vy = 0
    cara.jump = False
    carb.pos = (1650,300)
    carb.win = False
    carb.vy = 0
    cara.goright = True
    cara.goleft = True
    carb.goright = True
    carb.goleft = True
    cara.jump = True
    carb.jump = True
    cara.hp = 3
    carb.hp = 3
    cara.dying = False
    carb.dying = False
    cara.rt = True
    carb.lt = True
    cara.image = 'sheep_1_rt.png'
    carb.image = 'sheep_2_lt.png'
    tonga.angle = 0
    tongb.angle = 0
    balla.on = False
    ballb.on = False
reset()

def update():
    if x.gaming:
        update_ground()
        update_tong()
        update_car()
        update_ball()

def update_ground():
    global ground
    for block in ground[:]:
        if balla.on and block.colliderect(balla):
            ground.remove(block)
            balla.on = False
        if ballb.on and block.colliderect(ballb):
            ground.remove(block)
            ballb.on = False

def update_tong():
    #位置追随
    if cara.rt:
        tonga.pos = (cara.x+12,cara.top+5)
    else:
        tonga.pos = (cara.x-12,cara.top+5)
    if carb.lt:
        tongb.pos = (carb.x-12,carb.top+5)
    else:
        tongb.pos = (carb.x+12,carb.top+5)
    #调整角度
    if uk:
        if keyboard.G:
            tonga.angle += 2
        if keyboard.H:
            tonga.angle -= 2
        if keyboard.KP2:
            tongb.angle -= 2
        if keyboard.KP1:
            tongb.angle += 2
    if wk:
        if keyboard.C:
            tonga.angle += 2
        if keyboard.V:
            tonga.angle -= 2
        if keyboard.RIGHTBRACKET:
            tongb.angle -= 2
        if keyboard.LEFTBRACKET:
            tongb.angle += 2

def update_car():
    #基本运动
    carb.y += carb.vy
    cara.y += cara.vy
    cara.vy += GRAVITY
    carb.vy += GRAVITY
    cara.goright = True
    cara.goleft = True
    carb.goright = True
    carb.goleft = True
    cara.jump = False
    carb.jump = False
    #碰撞检测
    for block in ground:
        if cara.x-100<block.x<cara.x+100 and cara.y-100<block.y<cara.y+100:
            if cara.colliderect(Rect([block.left+9,block.top],[42,10])):#up
                cara.vy = - 0.9
            if cara.colliderect(Rect([block.left,block.top+9],[10,42])):#left
                cara.goright = False
            if cara.colliderect(Rect([block.left+9,block.bottom-10],[42,10])):#down
                cara.vy = 0.8
            if cara.colliderect(Rect([block.right-10,block.top+8],[10,42])):#right
                cara.goleft = False
            if cara.colliderect(Rect([block.left+3,block.top-8],[54,12])):#jump
                cara.jump = True
    for block in ground:
        if carb.x-100<block.x<carb.x+100 and carb.y-100<block.y<carb.y+100:
            if carb.colliderect(Rect([block.left+9,block.top],[42,10])):#up
                carb.vy = - 0.9
            if carb.colliderect(Rect([block.left,block.top+9],[10,42])):#left
                carb.goright = False
            if carb.colliderect(Rect([block.left+9,block.bottom-10],[42,10])):#down
                carb.vy = 0.8
            if carb.colliderect(Rect([block.right-10,block.top+9],[10,42])):#right
                carb.goleft = False
            if carb.colliderect(Rect([block.left+3,block.top-8],[54,12])):#jump
                carb.jump = True
    #控制运动
    if uk:
        if keyboard.A and cara.goleft:
            cara.x -= SPEED*(1+cara.dying)
        if keyboard.D and cara.goright:
            cara.x += SPEED*(1+cara.dying)
        if keyboard.LEFT and carb.goleft:
            carb.x -= SPEED*(1+carb.dying)
        if keyboard.RIGHT and carb.goright:
            carb.x += SPEED*(1+carb.dying)
    if wk:
        if keyboard.A and cara.goleft:
            cara.x -= SPEED*(1+cara.dying)
        if keyboard.D and cara.goright:
            cara.x += SPEED*(1+cara.dying)
        if keyboard.J and carb.goleft:
            carb.x -= SPEED*(1+carb.dying)
        if keyboard.L and carb.goright:
            carb.x += SPEED*(1+carb.dying)
    #血量
    if cara.hp == 1:
        cara.dying = True
    if carb.hp == 1:
        carb.dying = True
    if carb.hp == 0 or carb.y > HEIGHT:
        reset()
        sounds.sheep_2.play()
        cara.win = True
        x.death = True
        x.gaming = False
    if cara.hp == 0 or cara.y > HEIGHT:
        reset()
        sounds.sheep_2.play()
        carb.win = True
        x.death = True
        x.gaming = False
    
def update_ball():
    #位置追随
    if not ballb.on:
        ballb.pos = tongb.pos
    if not balla.on:
        balla.pos = tonga.pos
    #基本运动
    if balla.on:
        balla.x += balla.vx
        balla.vy += GRAVITY
        balla.y += balla.vy
        balla.angle = -atan(balla.vy / balla.vx) * (180 / pi)
    if ballb.on:
        ballb.x += ballb.vx
        ballb.vy += GRAVITY
        ballb.y += ballb.vy
        ballb.angle = -atan(ballb.vy / ballb.vx) * (180 / pi)
    #装弹
    if balla.on and balla.y > HEIGHT:
        balla.on = False
    if ballb.on and ballb.y > HEIGHT:
        ballb.on = False
    #击中敌人
    if balla.colliderect(carb) and balla.on:
        carb.hp -= 1
        sounds.sheep.play()
        balla.on = False
    if ballb.colliderect(cara) and ballb.on:
        cara.hp -= 1
        sounds.sheep.play()
        ballb.on = False


def draw():
    screen.clear()
    if x.gaming:
        show_gaming()
    if x.death:
        show_death()
    if x.begin:
        show_begin()
    if x.manuals:
        show_manuals()
        
def show_begin():
    screen.blit('img_palebegin',(0,0))
    screen.blit('tank_war',(440,230))
    begin_gaming.draw()
    begin_manuals.draw()
    
def show_gaming():
    screen.blit('img_background',(0,0))
    for i in range(cara.hp):
        if cara.dying:
            screen.blit('heart1.png',(50+80*i,40+randint(0,3)))
        else:
            screen.blit('heart.png',(50+80*i,40+randint(0,3)))
    for i in range(carb.hp):
        if carb.dying:
            screen.blit('heart1.png',(1700-80*i,40+randint(0,3)))
        else:
            screen.blit('heart.png',(1700-80*i,40+randint(0,3)))
    for block in ground:
        block.draw()
    cara.draw()
    carb.draw()
    if balla.on:
        balla.draw()
    tonga.draw()
    if ballb.on:
        ballb.draw()
    tongb.draw()


def show_death():
    if carb.win:
        screen.blit('img_whitewin',(0,0))
    if cara.win:
        screen.blit('img_blackwin',(0,0))
    death_gaming.draw()

def show_manuals():
    screen.blit('img_palebegin',(0,0))
    if uk:
        screen.blit('img_manuals_uk',(30,100))
    if wk:
        screen.blit('img_manuals_wk',(30,100))
    manuals_begin.draw()


def on_mouse_down(pos):
    if x.death:
        if death_gaming.collidepoint(pos):
            sounds.choose.play()
            sounds.motor.play()
            x.gaming = True
            x.death = False
    if x.begin:
        if begin_gaming.collidepoint(pos):
            sounds.choose.play()
            sounds.motor.play()
            x.gaming = True
            x.begin = False
        if begin_manuals.collidepoint(pos):
            sounds.choose.play()
            x.manuals = True
            x.begin = False
    if x.manuals:
        if manuals_begin.collidepoint(pos):
            sounds.choose.play()
            x.begin = True
            x.manuals = False
def on_key_down(key):
    if x.gaming:
        if uk:
            if key == key.W and cara.jump:
                cara.vy = -STRENGTH*(1+cara.dying/2)
            if key == key.UP and carb.jump:
                carb.vy = -STRENGTH*(1+carb.dying/2)
            if key == key.J:
                balla.time0 = time()
            if key == key.KP3:
                ballb.time0 = time()
            if key == key.A:
                if cara.rt:
                    tonga.angle = 90 - tonga.angle
                cara.rt = False
                if cara.dying:
                    cara.image = 'sheep_11_lt.png'
                else:
                    cara.image = 'sheep_1_lt.png'
            if key == key.D:
                if not cara.rt:
                    tonga.angle = 90 - tonga.angle
                cara.rt = True
                if cara.dying:
                    cara.image = 'sheep_11_rt.png'
                else:
                    cara.image = 'sheep_1_rt.png'
            if key == key.RIGHT:
                if carb.lt:
                    tongb.angle = -90 - tongb.angle
                carb.lt = False
                if carb.dying:
                    carb.image = 'sheep_22_rt.png'
                else:
                    carb.image = 'sheep_2_rt.png'
            if key == key.LEFT:
                if not carb.lt:
                    tongb.angle = -90 - tongb.angle
                carb.lt = True
                if carb.dying:
                    carb.image = 'sheep_22_lt.png'
                else:
                    carb.image = 'sheep_2_lt.png'
        if wk:
            if key == key.W and cara.jump:
                cara.vy = -STRENGTH*(1+cara.dying/2)
            if key == key.I and carb.jump:
                carb.vy = -STRENGTH*(1+carb.dying/2)
            if key == key.B:
                balla.time0 = time()
            if key == key.BACKSLASH:
                ballb.time0 = time()
            if key == key.A:
                if cara.rt:
                    tonga.angle = 90 - tonga.angle
                if cara.dying:
                    cara.image = 'sheep_11_lt.png'
                else:
                    cara.image = 'sheep_1_lt.png'
                cara.rt = False
            if key == key.D:
                if not cara.rt:
                    tonga.angle = 90 - tonga.angle
                if cara.dying:
                    cara.image = 'sheep_11_rt.png'
                else:
                    cara.image = 'sheep_1_rt.png'
                cara.rt = True
            if key == key.L:
                if carb.lt:
                    tongb.angle = -90 - tongb.angle
                if carb.dying:
                    carb.image = 'sheep_22_rt.png'
                else:
                    carb.image = 'sheep_2_rt.png'
                carb.lt = False
            if key == key.J:
                if not carb.lt:
                    tongb.angle = -90 - tongb.angle
                if carb.dying:
                    carb.image = 'sheep_22_lt.png'
                else:
                    carb.image = 'sheep_2_lt.png'
                carb.lt = True

def on_key_up(key):
    if x.gaming:
        if uk:
            if key == key.J:
                if not balla.on:
                    balla.on = True
                    sounds.shoot.play()
                    balla.strength = min(time() - balla.time0 + 0.1,2.5)
                    balla.angle = tonga.angle + 45
                    balla.vx = 50*balla.strength * cos(balla.angle*pi/180)
                    balla.vy = -50*balla.strength * sin(balla.angle*pi/180)
            if key == key.KP3:
                if not ballb.on:
                    ballb.on = True
                    sounds.shoot.play()
                    ballb.strength = min(time() - ballb.time0 + 0.1,2.5)
                    ballb.angle = tongb.angle - 45
                    ballb.vx = -50*ballb.strength * cos(ballb.angle*pi/180)
                    ballb.vy = 50*ballb.strength * sin(ballb.angle*pi/180)
        if wk:
            if key == key.B:
                if not balla.on:
                    balla.on = True
                    sounds.shoot.play()
                    balla.strength = min(time() - balla.time0 + 0.1,2.5)
                    balla.angle = tonga.angle + 45
                    balla.vx = 50*balla.strength * cos(balla.angle*pi/180)
                    balla.vy = -50*balla.strength * sin(balla.angle*pi/180)
            if key == key.BACKSLASH:
                if not ballb.on:
                    ballb.on = True
                    sounds.shoot.play()
                    ballb.strength = min(time() - ballb.time0 + 0.1,2.5)
                    ballb.angle = tongb.angle - 45
                    ballb.vx = -50*ballb.strength * cos(ballb.angle*pi/180)
                    ballb.vy = 50*ballb.strength * sin(ballb.angle*pi/180)


music.play('bgm')
pgzrun.go()lj
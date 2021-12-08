import pgzrun
import pygame
import random
import sys
WIDTH=1000
HEIGHT=562.5
l = open('txts/level.txt',mode='r',encoding='utf-8')
level = l.readlines()
le=int(level[-1])
l.close()
eye1=Actor('eye_open')
eye1.pos=(WIDTH/4,0)
eye2=Actor('eye_open')
eye2.pos=(WIDTH*3/4,0)
player=Actor('you')
player.midbottom=(WIDTH/2,HEIGHT)
player.blood=3000
call=[Actor('call0')]
call[0].midbottom=(WIDTH/2,0)
call[0].vy=3
he=Actor('he')
he.midbottom=(WIDTH/2,0)
f = open('txts/TXT50.txt','r', encoding='utf-8')
TXT=f.readlines()
f.close()
line=0
t=0
t1=0
r1=0
t11=0
e1=0
m1=0
G=0.1
r=0
c=0
h=0
rocks=[]
errs=[]
mes=[]
tans=[]
ends=[]

#定义攻击模式
def rock():#此条没问题
    global r1, t11, m1, e1
    for i in errs:
        errs.remove(i)
    for i in mes:
        mes.remove(i)
    for i in tans:
        tans.remove(i)
    m1=0
    t11=0
    e1=0
    r1+=1
    if r1==30:
        r1=0
        ro=Actor('rock')
        ro.midbottom=(random.randrange(int(WIDTH)),0)
        ro.vy=20
        rocks.append(ro)
    for ro in rocks:
        ro.y+=ro.vy
        if ro.bottom>HEIGHT:
            ro.vy=-10
        if ro.bottom<0:
            rocks.remove(ro)
        if ro.colliderect(player):
            player.blood-=6
    
def tan():#此条没问题
    global t11, m1, e1, r1
    for i in errs:
        errs.remove(i)
    for i in mes:
        mes.remove(i)
    for i in rocks:
        rocks.remove(i)
    m1=0
    e1=0
    r1=0
    if t11==0:
        b1=Actor('me1_0')
        b2=Actor('me1_0')
        b1.midtop=(random.randrange(int(WIDTH)),0)
        b2.midtop=(random.randrange(int(WIDTH)),0)
        b1.move1=1
        b2.move1=-1
        b1.move2=1
        b2.move2=1
        b1.vx=random.randrange(10,15)
        b2.vx=random.randrange(15,20)
        b1.vy=random.randrange(5,10)
        b2.vy=random.randrange(10,15)
        tans.append(b1)
        tans.append(b2)
        t11+=1
    for b in tans:
        if b.left < 0:#弹跳
            b.move1 = 1
        elif b.right > WIDTH:
            b.move1 = -1
        if b.top < 0:#弹跳
            b.move2 = 1
        elif b.bottom > HEIGHT:
            b.move2 = -1
        b.x+=b.vx*b.move1
        b.y+=b.vy*b.move2
        if b.colliderect(player):
            player.blood-=6
            
def me():#此条无问题
    global m1, e1, t11, r1
    for i in errs:
        errs.remove(i)
    for i in tans:
        tans.remove(i)
    for i in rocks:
        rocks.remove(i)
    e1=0
    t11=0
    r1=0
    m1+=1
    if m1==10:
        m1=0
        mm=Actor('me2')
        if random.randrange(1,3)==1:
            mm.y=random.randrange(int(HEIGHT))
            mm.x=0
            mm.vx=15
        else:
            mm.y=random.randrange(int(HEIGHT))
            mm.x=WIDTH
            mm.vx=-15
        mes.append(mm)
    for mm in mes:
        mm.x+=mm.vx
        if (mm.vx<0 and mm.right<0) or (mm.vx>0 and mm.left>WIDTH):
            mes.remove(mm)
        if mm.colliderect(player):
            player.blood-=6
    
def err():#此条嘴有时候会不见
    global e1, G, m1, t11, r1
    for i in mes:
        mes.remove(i)
    for i in tans:
        tans.remove(i)
    for i in rocks:
        rocks.remove(i)
    m1=0
    t11=0
    r1=0
    if e1==0:
        err1=Actor('me3')
        err1.pos=(WIDTH/2,HEIGHT/10)
        err1.vx=0
        err1.vy=0
        err1.m=0
        err1.n=0
        errs.append(err1)
        e1+=1
    elif e1==5:
        e1=1
        er=Actor('err')
        if random.randrange(1,3)==1:
            er.pos=(WIDTH/2,HEIGHT/10)
            er.vx=random.randrange(20)
            er.m=1
            er.vy=0
            er.n=1
        else:
            er.pos=(WIDTH/2,HEIGHT/10)
            er.vx=random.randrange(20)
            er.m=-1
            er.vy=0
            er.n=1
        errs.append(er)
    else:
        e1+=1
    for er in errs:
        er.x+=er.vx*er.m
        er.y+=er.vy
        er.vy+=G*er.n
        if er.bottom>HEIGHT:
            errs.remove(er)
        if er.left < 0:#弹跳
            er.m = 1
        elif er.right > WIDTH:
            er.m = -1
        if er.colliderect(player):
            player.blood-=6

def draw():
    global line,t,c,h
    if line>10:
        screen.clear()
        screen.fill((255,255,255))
        if len(TXT[line])<=16:
            screen.draw.text(TXT[line], (0,0), color=(135,155,180), fontname = 'zpix', fontsize = 50)
        elif len(TXT[line])<=31:
            screen.draw.text(TXT[line][0:15], (0,0), color=(135,155,180), fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT[line][15:-1], (0,50), color=(135,155,180), fontname = 'zpix', fontsize = 50)
        elif len(TXT[line])<=47:
            screen.draw.text(TXT[line][0:15], (0,0), color=(135,155,180), fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT[line][15:30], (0,50), color=(135,155,180), fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT[line][30:-1], (0,100), color=(135,155,180), fontname = 'zpix', fontsize = 50)
        he.draw()
        player.draw()
    else:
        screen.clear()
        if le==-1 and line==1:
            screen.blit('error0',(0,0))
        elif le==-2:
            screen.clear()
            screen.blit('my_win',(0,0))
        else:
            if line==1:
                screen.blit('error1',(0,0))
            elif line==2:
                screen.blit('error2',(0,0))
            elif line==3:
                screen.blit('error3',(0,0))
            elif line==5:
                if c==1:
                    screen.blit('abaaba', (0,0))
                elif keyboard.escape:
                    screen.blit('esc', (0,0))
                eye1.draw()
                eye2.draw()
                BOX1=Rect((WIDTH/2-150,HEIGHT-50),(300,50))
                BOX2=Rect((WIDTH/2-150,HEIGHT-50),(player.blood/10,50))
                screen.draw.filled_rect(BOX1,(166,0,0))
                screen.draw.filled_rect(BOX2,(44,232,245))
                screen.draw.text('YOUR BLOOD', (WIDTH/2-150,HEIGHT-50), color='black', fontname = 'zpix', fontsize = 50)
        if 5<line<=10:
            eye1.draw()
            eye2.draw()
        for ro in rocks:
            ro.draw()
        for b in tans:
            b.draw()
        for er in errs:
            er.draw()
        for mm in mes:
            mm.draw()
        for end in ends:
            end.draw()
        for i in call:
            i.draw()
        he.draw()
        player.draw()
        if t==10001:
            if len(TXT[line])<=16:
                screen.draw.text(TXT[line], (0,0), color=(58,68,102), fontname = 'zpix', fontsize = 50)
            elif len(TXT[line])<=31:
                screen.draw.text(TXT[line][0:15], (0,0), color=(58,68,102), fontname = 'zpix', fontsize = 50)
                screen.draw.text(TXT[line][15:-1], (0,50), color=(58,68,102), fontname = 'zpix', fontsize = 50)
            elif len(TXT[line])<=47:
                screen.draw.text(TXT[line][0:15], (0,0), color=(58,68,102), fontname = 'zpix', fontsize = 50)
                screen.draw.text(TXT[line][15:30], (0,50), color=(58,68,102), fontname = 'zpix', fontsize = 50)
                screen.draw.text(TXT[line][30:-1], (0,100), color=(58,68,102), fontname = 'zpix', fontsize = 50)

def update():
    global line,t,t1, at, r, c, h
    pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if le==-2:
        sounds.my_win.play()
        pass
    elif line==0:
        music.play('say_hi')
        with open('txts/level.txt',mode='w',encoding='utf-8') as l:
            l.write('-1')
        l.close()
        line+=1
    if le==-1 and line==2:
        line=4
    if line==4:
        music.play('playyyyy')
        line=5
    elif line==5:
        eye1.angle = eye1.angle_to(player)
        eye2.angle = eye2.angle_to(player)
        line=5
    if player.left < 0:
        player.left = 0
    elif player.right > WIDTH:
        player.right = WIDTH
    elif player.top < 0:
        player.top = 0
    elif player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if player.top>HEIGHT or player.bottom<0:
        player.blood-=100
    if line==5 or line>10:
        if keyboard.w:
            player.y-=10
        if keyboard.s:
            player.y+=10
        if keyboard.a:
            player.x-=10
        if keyboard.d:
            player.x+=10
    if 7200<t<10000:
        if ends[0].right>=460:
            ends[0].right=460
        else:
            ends[0].x+=3
        if ends[1].left<=540:
            ends[1].left=540
        else:
            ends[1].x-=3
        if ends[2].bottom>=400:
            ends[2].bottom=400
            t=10000
        else:
            ends[2].y+=1
        for i in ends:
            if i.colliderect(player):
                player.blood-=10
    if t1==900:
        t1=0
    if line==5 and t<7200:
        if t1==0:
            r=random.randrange(1,5)
    if r==1:
        err()
    elif r==2:
        rock()
    elif r==3:
        tan()
    elif r==4:
        me()
    if line==5 and t<10000:
        t+=1
        t1+=1
    else:
        t1=0
        r=0
    if t>=6000 and call[0].y<=400:
        call[0].y+=call[0].vy
    if call[0].colliderect(player):
        call[0]=Actor('bloc')
        call[0].midbottom=(WIDTH/2,0)
        call[0].vy=0
        player.blood=3000
        c=1
    if t==7200:
        end1=Actor('your_end1')
        end2=Actor('your_end2')
        end3=Actor('your_true_end')
        end1.midright=(0,HEIGHT/2)
        end2.midleft=(WIDTH,HEIGHT/2)
        end3.midbottom=(WIDTH/2,0)
        ends.append(end1)
        ends.append(end2)
        ends.append(end3)
    if t==10000:
        if h==0:
            he.midtop=ends[2].midbottom
            h+=1
        t+=1
        line+=1
    if player.blood<=0:
        exit()
    if line==10:
        ends[0].x-=9
        ends[1].x+=9
        ends[2].y-=9
        if eye1.bottom<0:
            he.midbottom=(WIDTH*2/3,HEIGHT)
            line+=1
        else:
            eye1.y-=1
            eye2.y-=1
        music.stop()
    if line==34:
        with open('txts/level.txt',mode='w',encoding='utf-8') as l:
            l.write('-2')
        l.close()
        exit()
        
        

def on_key_down(key):
    global line
    if (not line==5) and (not line==10):
        if key == key.SPACE:
            line+=1

pgzrun.go()
import pgzrun
import random
import os

WIDTH = 1200
HEIGHT = 600

bug=[]
bugspeed=[]
ifmt=[]
move=[1, 1, 1, 1]

for i in range(4):
    bug.append(Actor('bug'))
for i in range(25):
    ifmt.append(Actor('information'))
base = Actor('base')
hook = Actor('hook')
line = Actor('line')

hook.get=0
hook.lose=0
hookmove=0
ifmt_num=0
over=0

base.midtop = 600, 0
hook.midtop = line.midbottom = 600, 33
for i in range(25):
    ifmt[i].midtop=1200*random.random(), random.randrange(300,600,25)

for i in range(4):
    bugspeed.append(7*random.random())

for i in range(4):
    bug[i].midtop = 1200*random.random(),150

def draw():
    global ifmt_num, over
    screen.blit('background2', (0, 0))
    screen.draw.text('number of file:%d' % hook.get, (0, 0),fontsize=50)
    for i in range(25):
        ifmt[i].draw()
    if hook.get<15:
        if hook.lose>10:
            screen.clear()
            screen.draw.text('YOU LOSE!', (25,0), color=(200,50,50),fontsize=300)
            screen.draw.text('Press "R" to restart', (110,HEIGHT*2/3), color=(200,50,50),fontsize=150)
            if keyboard.r:
                hook.get=0
                hook.lose=0
                ifmt_num=0
                over=0
        else:
            for i in range(4):
                bug[i].draw()
    if hook.get>=15:
        screen.clear()
        if hook.lose==0:
            screen.blit('perfect2',(0,0))
            screen.draw.text('YOU WIN!', (120,0), color=(18,78,137),fontsize=300)
        else:
            screen.draw.text('YOU WIN!', (120,0), color=(0,0,137),fontsize=300)
        over+=1
        screen.blit('continue', (0,400))
        if keyboard.c:
            exit()
    line.draw()
    base.draw()
    hook.draw()

def update():
    global bugspeed, hookmove
    for i in range(4):
        bug[i].left += move[i]*bugspeed[i]
    if base.left < 0:
        base.left = 0
    elif base.right > WIDTH:
        base.right = WIDTH
    hook.x=base.x
    line.midbottom=hook.midtop
    for i in range(4):
        if bug[i].left < 0:
            move[i] = 1
        elif bug[i].right > WIDTH:
            move[i] = -1
    hook.y += hookmove*5
    catch()
    Return()
    error()

def on_mouse_move(pos):
    if base.left >= 0 and base.right <= WIDTH:
        base.x=pos[0]

def on_mouse_down():
    global hookmove
    if hookmove == 0:
        hookmove=2

def catch():
    global hookmove, ifmt_num
    for i in range(25):
        if ifmt[i].colliderect(hook):
            ifmt_num+=1
            hookmove=-1
            hook.get+=1
            ifmt[i]=Actor('empty')
    if hook.bottom >= HEIGHT:
        hookmove=-1
            
def Return():
    global hookmove
    if hook.colliderect(base):
        hookmove=0

def error():
    global hookmove, over
    if over==0:
        for i in range(4):
            if bug[i].colliderect(hook):
                hook.midtop=(base.x, 30)
                hook.get-=1
                hook.lose+=1
                hookmove=0

pgzrun.go()
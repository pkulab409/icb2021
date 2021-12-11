import pgzrun
import random
import time
dino=Actor('dinol')
dino.pos=90,215
gameover=Actor('gameover')
gameover.pos=500,130
cloud=Actor('cloud')
cloud.pos=50,75
ground=Actor('ground')
ground.pos=0,275
WIDTH=1000
HEIGHT=300
global jumped
global lasttime
global begin_run
global st
global run
global new
global up
global over
over=0
lasttime=0
jumped=0
st=0
up=0
run=10
new=1
names=['cactibig','cactismall','cactismall3']
cacties=[]
begin_run=time.time()
def draw():
    #if over:
    screen.clear()
    screen.fill((255,255,255))
    ground.draw()
    cloud.draw()
    dino.draw()
    #screen.draw.rect(Rect(int(dino.left)+38,dino.y-43,34,30),'green')
    #screen.draw.rect(Rect(int(dino.left)+10,int(dino.y+65)-53,44,13),'red')
    #screen.draw.rect(Rect(int(dino.left)+19,int(dino.y+93)-66,26,21),'yellow')
    if over:
        gameover.draw()
    for cacti in cacties:
        cacti.draw()
def update():
    global new
    global run
    global begin_run
    global lasttime
    global over
    global up
    ground.right-=run
    dele=[]
    global cacties
    crash=0
    for i in range(len(cacties)):
        if cacties[i].image=='cactibig':
            if (Rect(cacties[i].left,cacties[i].y-25,10,36).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left,cacties[i].y-25,10,36).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left,cacties[i].y-25,10,36).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left,cacties[i].y-25,10,36).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)or
                Rect(cacties[i].left+16,cacties[i].y-50,15,79).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left+16,cacties[i].y-50,15,79).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left+16,cacties[i].y-50,15,79).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left+16,cacties[i].y-50,15,79).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)or
                Rect(cacties[i].left+37,cacties[i].y-28,10,34).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left+37,cacties[i].y-28,10,34).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left+37,cacties[i].y-28,10,34).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left+37,cacties[i].y-28,10,34).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)):
                crash=1
        elif cacties[i].image=='cactismall':
            if (Rect(cacties[i].left,cacties[i].y-26,5,30).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left,cacties[i].y-26,5,30).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left,cacties[i].y-26,5,30).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left,cacties[i].y-26,5,30).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)or
                Rect(cacties[i].left+10,cacties[i].y-32,10,70).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left+10,cacties[i].y-32,10,70).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left+10,cacties[i].y-32,10,70).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left+10,cacties[i].y-32,10,70).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)or
                Rect(cacties[i].left+24,cacties[i].y-25,5,34).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left+24,cacties[i].y-25,5,34).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left+24,cacties[i].y-25,5,34).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left+24,cacties[i].y-25,5,34).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)):
                crash=1
            
        else:
            if (Rect(cacties[i].left,cacties[i].y-17,5,30).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left,cacties[i].y-17,5,30).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left,cacties[i].y-17,5,30).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left,cacties[i].y-17,5,30).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)or
                Rect(cacties[i].left+10,cacties[i].y-36,10,70).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left+10,cacties[i].y-36,10,70).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left+10,cacties[i].y-36,10,70).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left+10,cacties[i].y-36,10,70).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)or
                Rect(cacties[i].left+24,cacties[i].y-22,30,34).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left+24,cacties[i].y-22,30,34).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left+24,cacties[i].y-22,30,34).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left+24,cacties[i].y-22,30,34).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)or
                Rect(cacties[i].left+44,cacties[i].y-31,10,70).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left+44,cacties[i].y-31,10,70).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left+44,cacties[i].y-31,10,70).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left+44,cacties[i].y-31,10,70).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)or
                Rect(cacties[i].left+58,cacties[i].y-16,5,30).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left+58,cacties[i].y-16,5,30).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left+58,cacties[i].y-16,5,30).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left+58,cacties[i].y-16,5,30).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)or
                Rect(cacties[i].left+69,cacties[i].y-22,29,30).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left+69,cacties[i].y-22,29,30).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left+69,cacties[i].y-22,29,30).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left+69,cacties[i].y-22,29,30).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)or
                Rect(cacties[i].left+78,cacties[i].y-31,10,70).colliderect(dino.left,int(dino.y+21)-30,61,24) or
                Rect(cacties[i].left+78,cacties[i].y-31,10,70).colliderect(int(dino.left)+38,dino.y-43,34,30) or
                Rect(cacties[i].left+78,cacties[i].y-31,10,70).colliderect(int(dino.left)+10,int(dino.y+65)-53,44,13)or
                Rect(cacties[i].left+78,cacties[i].y-31,10,70).colliderect(int(dino.left)+19,int(dino.y+93)-66,30,21)):
                crash=1
        if crash:    
            up=0
            run=0
            new=0
            over=1
            dino.image='dinoover2'
            begin_run=time.time()
                
                
        cacties[i].right-=run
        if(cacties[i].right==0):
            dele.append(i)
    for i in dele:
        del cacties[i]
    if up<0:
        dino.y-=((time.time()-st)*23)**2
    elif up>0 and dino.y<215:
        dino.y+=((time.time()-(st+0.27))*23)**2
    dino.y=min(dino.y,215)
    if ground.right<=WIDTH:
        ground.left=0
    cloud.right-=run
    if cloud.right<=WIDTH:
        cloud.left=0
    if new and time.time()-lasttime>0.5:#
        if random.randrange(60)==0 :
            lasttime=time.time()
            cacti=Actor(random.choice(names))#random.choice(names)
            cacti.pos=WIDTH,220
            cacties.append(cacti)
    if over==0:
        if int((time.time()-begin_run)*10)%2:
            dino.image='dinor'
        else:
            dino.image='dinol'
def on_key_down(key):
    global st
    if up==0:
        if key.A:
            st=time.time() 
            upjump()
def upjump():
    global up
    global new
    new=0
    up=-1
    clock.schedule_unique(downjump,0.27)
def notjump():
    global up
    global new
    new=1
    up=0
def downjump():
    global up
    global new
    new=0
    up=1
    global st
    clock.schedule_unique(notjump,0.27)
def on_mouse_down(pos):
    global run
    global new
    global over
    global up
    global cacties
    if gameover.collidepoint(pos):
        up=0
        run=10
        new=1
        over=0
        cacties.clear()
        dino.pos=90,215   
pgzrun.go()
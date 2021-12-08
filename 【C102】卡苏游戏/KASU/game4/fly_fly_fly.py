import pgzrun
import random
import easygui as g

clouds = ['cloud1', 'cloud2', 'cloud3', 'cloud4', 'cloud5', 'cloud6', 'cloud7']
back = Actor('skyline')
fly=Actor('fly_machine')
goal=Actor('goal')
fly.midright=(0,400)
goal.midleft=(800,400)
road=0
C=[]
c1=0
v=0
line=0

WIDTH=800
HEIGHT=800
f = open('txts/TXT40.txt','r', encoding='utf-8')
TXT=f.readlines()

def draw():
    #global i
    screen.clear()
    back.draw()
    for cloud in C:
        cloud.draw()
    goal.draw()
    fly.draw()
    if len(TXT[line])<=15:
        screen.draw.text(TXT[line], (10,700), fontname = 'zpix', fontsize = 50)
    elif len(TXT[line])<=30:
        screen.draw.text(TXT[line][0:14], (10,650), fontname = 'zpix', fontsize = 50)
        screen.draw.text(TXT[line][14:-1], (10,700), fontname = 'zpix', fontsize = 50)
    elif len(TXT[line])<=45:
        screen.draw.text(TXT[line][0:14], (10,600), fontname = 'zpix', fontsize = 50)
        screen.draw.text(TXT[line][14:28], (10,650), fontname = 'zpix', fontsize = 50)
        screen.draw.text(TXT[line][28:-1], (10,700), fontname = 'zpix', fontsize = 50)

def update():
    global GRAVITY, c1, v, line 
    #云移动
    c1 += 1
    if c1 == 10:
        c1 = 0
        cloud = Actor(random.choice(clouds))
        cloud.midleft = WIDTH, random.randrange(500)
        cloud.v = random.randrange(5,15)
        C.append(cloud)
    for cloud in C:
        cloud.x -= cloud.v-3+v
        if cloud.right <= 0:
            C.remove(cloud)
    if fly.x>=400:
        back.left-=v/3
        v=3
    else:
        fly.x+=3
        v=0
    if back.right<=800:
        back.left=0
    if line==4:
        choices=['好的','算了']
        choice=g.choicebox('','',choices)
        if choice==choices[0]:
            line=5
        elif choice==choices[1]:
            line=11
    elif line==5:
        music.play('your_love_is_a_drug')
    elif line==10:
        line=12
    elif line==13:
        choices=['背景是……？','背景……我好像在哪见过']
        choice=g.choicebox('','',choices)
        line+=1
    elif line==32:
        g.msgbox("你能跟我讲讲……你的事吗？")
        line+=1
    elif line==35:
        g.msgbox("……QAQ")
        line+=1
    elif line==52:
        g.msgbox("游戏做游戏(笑)")
        line+=1
    if line>=57:
        if fly.x>=goal.x:
            v=0
        else:
            goal.left-=0.5
        if line >60:
            line=61
        if keyboard.c:
            exit()

    
def on_key_down(key):
    global line
    if key == key.SPACE:
        line+=1

pgzrun.go()
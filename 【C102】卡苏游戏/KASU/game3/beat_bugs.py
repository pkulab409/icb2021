import pgzrun
import random

HEIGHT = 600
WIDTH = 500

#创建飞机，判定点，boss,确定初始位置,boss血量
plain = Actor('plain')
point = Actor('point')
bbug = Actor('bugbig')
point.beat=0
plain.pos=point.pos=350/2,1100/2
bbug.pos=350/2,0
bbug.blood=700

#用于储存子弹的子弹库与储存敌方的敌人库
bullet=[]
bugs=[]
sbugs=[]

#各种需要的数据
i=0
s1=s2=0#控制子弹生成和普通敌人生成
sh=1#模拟修饰键效果，按下x时移速降低

up=down=left=right=0
def draw():
    screen.fill((255,255,255))
    screen.blit('background3',(0,0))
    #更新
    if point.beat>=20 and keyboard.r:
        for bug in bugs:
            bugs.remove(bug)
        for sbug in sbugs:
            sbugs.remove(sbug)
        for bul in bullet:
            bullet.remove(bul)
    #画上飞机,敌方
    for bug in bugs:
        bug.draw()
    for sbug in sbugs:
        sbug.draw()
    for bul in bullet:
        bul.draw()
    plain.draw()
    bbug.draw()
    #画右侧栏
    screen.blit('background30',(0,0))
    #画上自己与敌方的血量
    screen.draw.text(*['boss blood: %d' % bbug.blood], (720/2,20/2), color='white', fontsize=50/2)
    screen.draw.text(*['your blood: %d' % (20-point.beat)], (720/2,1000/2), color='white', fontsize=50/2)
    if point.beat >= 20:
        screen.clear()
        screen.blit('lose3', (0, 0))
        screen.draw.text('Press "R" to restart', (90/2,900/2), color=(200,50,50),fontsize=130/2)
        if keyboard.r:
            point.beat=0
            bbug.blood=700
            for bul in bullet:
                bullet.remove(bul)
            for bug in bugs:
                bugs.remove(bug)
            for sbug in sbugs:
                sbugs.remove(sbug)
    #判断结束与胜利状态
    elif bbug.blood<=0:
        screen.clear()
        screen.blit('win3', (0, 0))
        if point.beat<=5:
            screen.blit('perfect3', (0, 0))
        screen.blit('continue', (0,1000/2))
        if keyboard.c:
            exit()
    
def update():
    global up,down,left,right,s1,s2,sh
    #让判定点与机体位置一致，编辑飞机运动
    plain.pos=point.pos
    point.x+=right*4/sh
    point.x-=left*4/sh
    point.y+=down*4/sh
    point.y-=up*4/sh
    #离开界面时归位（限制判定点在屏幕内）
    if point.left < 0:
        point.left = 0
    elif point.right > 700/2:
        point.right = 700/2
    elif point.top < 0:
        point.top = 0
    elif point.bottom > HEIGHT:
        point.bottom = HEIGHT
    #判断结束条件
    if not(point.beat >= 20 or bbug.blood <= 0):
    #让boss转起来
        bbug.angle+=3
    #设置飞机射击
        s1+=1
        if s1==2:
            s1=0
            shot(i)
    #生成敌方
        s2+=1
        if s2==20:
            bug = Actor('bugsmall')
            bug.midtop = random.randrange(700/2), 0
            bugs.append(bug)
            s2=0
        if random.randrange(14)==0:
            sbug = Actor('bugsupersmall')
            sbug.pos =random.randrange(700/2), 0
            sbugs.append(sbug)
            sbug.move=random.randrange(2)
            sbug.xz=random.randrange(0,5)
            sbug.yz=random.randrange(5,10)
        #敌方下降，判断是否碰到玩家或触地
        for bug in bugs:
            bug.y+=random.randrange(10)
            if bug.colliderect(point):
                bugs.remove(bug)
                point.beat+=1
            elif bug.bottom>=HEIGHT:
                bugs.remove(bug)
                point.beat+=1
    #设置小型敌方（敌方子弹）的移动与碰撞
        for sbug in sbugs:
            if sbug.left < 0:#弹跳
                sbug.move = 1
            elif sbug.right > 700/2:
                sbug.move = 0
            sbug.y+=sbug.yz
            if sbug.move==1:
                sbug.x+=sbug.xz
            elif sbug.move==0:
                sbug.x-=sbug.xz
            if sbug.bottom==HEIGHT:
                sbugs.remove(sbug)
            elif sbug.colliderect(point):
                sbugs.remove(sbug)
                point.beat+=1
    #己方子弹移动
        for bul in bullet:
            bul.y-=20
            if bul.bottom<-2:
                bullet.remove(bul)
        #检测子弹与敌方的碰撞
            for bug in bugs:
                if bul.colliderect(bug) and (not bul.colliderect(bbug)):
                    bugs.remove(bug)
                    bullet.remove(bul)
                elif bul.colliderect(bug) and bul.colliderect(bbug):
                    bugs.remove(bug)
            if bul.colliderect(bbug):
                bbug.blood-=1
                bullet.remove(bul)
    else:
        pass

#设置键盘操作
def on_key_down(key):
    global up, down, left, right, i, sh
    #开火
    if key == key.Z:
        i = 1
    #降速
    if key == key.X:
        sh = 3
    #移动
    if key == key.LEFT:
            left = 3
    elif key == key.RIGHT:
            right = 3
    elif key == key.UP:
            up = 3
    elif key == key.DOWN:
            down = 3
def on_key_up(key):
    global up, down, left, right, i, sh
    #按键抬起时取消移动，开火，降速状态
    if key == key.Z:
        i = 0
    if key == key.LEFT:
        left = 0
    elif key == key.RIGHT:
        right = 0
    elif key == key.UP:
        up = 0
    elif key == key.DOWN:
        down = 0
    if key == key.X:
        sh = 1
#定义射击
def shot(a):
    if a==0:
        pass
    elif a==1:
        bul=Actor('bullet')
        bul.pos=point.pos
        bullet.append(bul)

pgzrun.go()
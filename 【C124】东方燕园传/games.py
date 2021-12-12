import pgzrun
import random

HEIGHT = 1200
WIDTH = 1000

#创建飞机，判定点，boss,确定初始位置,boss血量
player = Actor('player')
point = Actor('point')
boss = Actor('boss')
bossplus = Actor('bossplus')
bossplus.blood=1000
player.pos=point.pos=350,1100
boss.pos=350,200
bossplus.pos=350,200
boss.blood=700
bossplus.blood=1000
player.blood=2000
music.play("music3")

#用于储存子弹的子弹库与储存敌方的敌人库
bullet=[]
bugs=[]
sbugs=[]
superbugs=[]

#各种需要的数据
i=0
s1=s2=0#控制子弹生成和普通敌人生成
sh=1#模拟修饰键效果，按下x时移速降低
sp=0
qp=0
time1=0
beats=0
up=down=left=right=0

def draw():
    screen.fill((139,0,18))#PKU Red
    screen.blit('background',(0,0))
    #画上飞机,敌方
    for bug in bugs:
        bug.draw()
    for sbug in sbugs:
        sbug.draw()
    for bul in bullet:
        bul.draw()
    for superbug in superbugs:
        superbug.draw()
    player.draw()
    if boss.blood>400:
        boss.draw()
    else:
        bossplus.draw()
    #画右侧栏
    screen.blit('background30',(0,0))
    #画上自己与敌方的血量
    CD1=1.325-float((time1))/90
    CD2=int(beats)
    if boss.blood>400:
        screen.draw.text(*['霧雨魔理沙?生命值'], (720,20), color='black', fontsize=30,fontname='fanti')
        screen.draw.text(*['%d' % boss.blood], (720,50), color='black', fontsize=80,fontname='fanti')
    else:
        screen.draw.text(*['霧雨魔理沙!生命值'], (720,20), color='black', fontsize=30,fontname='fanti')
        screen.draw.text(*['%d' % bossplus.blood], (720,50), color='black', fontsize=30,fontname='fanti')
    screen.draw.text(*['博麗靈夢生命值'], (720,800), color='black', fontsize=30,fontname='fanti')
    screen.draw.text(*['%d' % player.blood], (720,830), color='black', fontsize=30,fontname='fanti')
    screen.draw.text(*['惡靈退散 冷卻時間'], (720,860), color='black', fontsize=30,fontname='fanti')
    screen.draw.text(*['%f' % CD1], (720,890), color='black', fontsize=30,fontname='fanti')
    if beats >=100:
        screen.draw.text(*['凈化 冷卻完畢'], (720,920), color='red', fontsize=30,fontname='fanti')
        screen.draw.text(*['%f' % CD2], (720,950), color='red', fontsize=30,fontname='fanti')
    else:
        screen.draw.text(*['凈化 冷卻中'], (720,920), color='gray', fontsize=30,fontname='fanti')
        screen.draw.text(*['%f' % CD2], (720,950), color='gray', fontsize=30,fontname='fanti')
    screen.draw.text(*['製作人提醒'], (720,1000), color='black', fontsize=30,fontname='fanti')
    screen.draw.text(*['請不要'], (720,1030), color='black', fontsize=30,fontname='fanti')
    screen.draw.text(*['扭來扭去'], (720,1060), color='red', fontsize=30,fontname='fanti')
    screen.draw.text(*['東方'], (720,450), color='red', fontsize=120,fontname='fanti')
    screen.draw.text(*['燕園傳'], (720,570), color='red', fontsize=80,fontname='fanti')
    if player.blood <= 0:
        screen.clear()
        screen.blit('lose3', (0, 0))
    #判断结束与胜利状态
    elif bossplus.blood<=0:
        screen.clear()
        screen.blit('win3', (0, 0))

def update():
    global up,down,left,right,s1,s2,sh,sp,qp,beats
    #让判定点与机体位置一致，编辑飞机运动
    if keyboard.escape:
        exit()
    player.pos=point.pos
    point.x+=right*4/sh
    point.x-=left*4/sh
    point.y+=down*4/sh
    point.y-=up*4/sh
    #离开界面时归位（限制判定点在屏幕内）
    if point.left < 0:
        point.left = 0
    elif point.right > 700:
        point.right = 700
    elif point.top < 0:
        point.top = 0
    elif point.bottom > HEIGHT:
        point.bottom = HEIGHT
    #判断结束条件
    if not(player.blood <= 0 or bossplus.blood <= 0):
    #旋转
        if sp==1:
            span(sp)
        if qp==1:
            wd(qp)
        #设置飞机射击
        s1+=1
        if s1==3:
            s1=0
            shot(i)
    #生成敌方
        if boss.blood > 400:
            s2+=10
            if s2==200:
                bug = Actor('bugsmall')#方块的那个
                bug.midtop = random.randrange(700), 0
                bugs.append(bug)
                s2=0
            if random.randrange(15)==0:
                sbug = Actor('bugsupersmall')
                sbug.pos =random.randrange(700), 0
                sbugs.append(sbug)
                sbug.move=random.randrange(2)
                sbug.xz=random.randrange(0,5)
                sbug.yz=random.randrange(5,10)
        if 0 < boss.blood <=400:
            s2+=25
            if s2>=200:
                bug = Actor('bugsmall')#方块的那个
                bug.midtop = random.randrange(700), 0
                bugs.append(bug)
                s2=0
            if random.randrange(10)==0:
                sbug = Actor('bugsupersmall')
                sbug.pos =random.randrange(700), 0
                sbugs.append(sbug)
                sbug.move=random.randrange(2)
                sbug.xz=random.randrange(0,5)
                sbug.yz=random.randrange(5,10)
        #定义一个超级攻击bug
        if random.randrange(60)==0:
            superbugs_x=random.randrange(700)
            superbugs_y=random.randrange(500)
            for jk in range(8):
                superbug=Actor('superbu')
                superbug.pos=superbugs_x,superbugs_y
                superbugs.append(superbug)
                superbug.move=random.randrange(2)
                superbug.xz=random.randrange(0,7)
                superbug.yz=random.randrange(7,14)
        #敌方下降，判断是否碰到玩家或触地
        for bug in bugs:
            bug.angle+=60
            bug.y+=random.randrange(15)
            if bug.colliderect(point):
                bugs.remove(bug)
                player.blood-=1
            elif bug.bottom==HEIGHT:
                bugs.remove(bug)
                player.blood-=1
        #设置小型敌方（敌方子弹）的移动与碰撞
        for sbug in sbugs:
            sbug.angle+=105
            if sbug.left < 0:#弹跳
                sbug.move = 1
            elif sbug.right > 700:
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
                player.blood-=1
        #超级bug的移动
        for superbug in superbugs:
            if superbug.left < 0:
                superbug.move = 1
            elif superbug.right > 700:
                superbug.move = 0
            superbug.y+=superbug.yz+random.randrange(-12,8)
            if superbug.move==1:
                superbug.x+=superbug.xz
            elif superbug.move==0:
                superbug.x-=superbug.xz
            if superbug.bottom==HEIGHT:
                superbugs.remove(superbug)
            elif superbug.colliderect(point):
                superbugs.remove(superbug)
                player.blood-=1
        #己方子弹移动
        for bul in bullet:
            if sh == 1:
                if boss.blood>400:
                    bul.y-=20
                else:
                    bul.y-=10
                if bul.bottom<-2:
                    bullet.remove(bul)
            if sh == 3:
                
                if boss.blood>400:
                    bul.y-=10
                else:
                    bul.y-=5
                if bul.bottom<-2:
                    bullet.remove(bul)
        #检测子弹与敌方的碰撞
            for bug in bugs:
                if bul.colliderect(bug) and (not bul.colliderect(boss)):
                    bugs.remove(bug)
                    bullet.remove(bul)
                elif bul.colliderect(bug) and bul.colliderect(boss):
                    bugs.remove(bug)
            if boss.blood>400:
                if bul.colliderect(boss):
                    boss.blood-=1
                    beats+=1 
                    try:
                        bullet.remove(bul)
                    except:
                        pass
            else:
                if bul.colliderect(bossplus):
                    bossplus.blood-=1
                    beats+=1
                    try:
                        bullet.remove(bul)
                    except:
                        pass
    else:
        pass

#设置键盘操作
def on_key_down(key):
    global up, down, left, right, i, sh, sp,qp
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
    if key==key.C:
        sp=1
    if key==key.V:
        qp=1
def on_key_up(key):
    global up, down, left, right, i, sh,sp,qp
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
    if key==key.V:
        qp=0


#定义射击
def shot(a):
    if a==0:
        pass
    elif a==1:
        bul=Actor('bullet')
        bul.pos=point.pos
        bullet.append(bul)

def span(b):
    global time1,sp
    if b==1:
        time1+=1
        if time1<=30:
            player.angle+=48
            for bug in bugs:
                if point.distance_to(bug)<=90:
                    bugs.remove(bug)
            for sbug in sbugs:
                if point.distance_to(sbug)<=90:
                    sbugs.remove(sbug)
            for superbug in superbugs:
                if point.distance_to(superbug)<=90:
                    superbugs.remove(superbug)
    if time1==120:
        sp=0
        time1=0

def wd(c):
    global beats,qp
    if c==1:
        if beats >= 100:
            for bug in bugs:
                if point.distance_to(bug)<=10000:
                    bugs.remove(bug)
            for sbug in sbugs:
                if point.distance_to(sbug)<=10000:
                    sbugs.remove(sbug)
            for superbug in superbugs:
                if point.distance_to(superbug)<=10000:
                    superbugs.remove(superbug)

            beats-=100


pgzrun.go()
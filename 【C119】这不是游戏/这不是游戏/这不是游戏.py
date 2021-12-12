import pgzrun
import easygui as g
import random

#设置窗口大小
background1 = Actor('enter.jfif')

WIDTH = background1.width
HEIGHT = background1.height

#开始
scr=0

jsp = Actor('jsp.jpg')
jsp.topright = center=((WIDTH)/1.5,(HEIGHT)/35)

def ly():
    global scr
    scr=1

#第一幕

def ye():
    global scr
    scr=2     

#第二幕

pku = Actor('pku.png')
thu = Actor('thu.png')

pku.topright = 220, 355
thu.topright = 820, 350
  #进入
def eey():
    global scr
    scr=21

jinru = Actor('进入.jpg')
jinru.topright = (WIDTH)/2+124, 173
diancuole = Actor('点错了.jpg')
diancuole.topright = 400, 355
zaixiangxiang = Actor('再想想.jpg')
zaixiangxiang.topright = 750, 355

def es():
    global scr
    scr=3
  #退出 
def eee():
    global scr
    scr=22
    
queding = Actor('确定.jpg')
queding.topright = 250, 355

def fanhui2():
    global scr
    scr=2

#第三幕

huaping = Actor('花屏.jfif')

def ss():
    global scr
    scr=4

#第四幕

t1 = Actor('退学1.jpg')
t2 = Actor('退学2.jpg')
t3 = Actor('退学3.jpg')
t4 = Actor('退学4.jpg')

t1.topright = 400, 50
t2.topright = 800, 50
t3.topright = 750, 355
t4.topright = 250, 355

def sw():
    global scr
    scr=5

#第五幕

skm = Actor('收款码.jpg')
skm.topright = 850,70

fk = Actor('付款.jpg')
xf = Actor('5000元.jpg')
fk.topright = 424,24
xf.topright = 330,175

yuan=1

def ke():
    global yuan
    yuan=0

def bk():
    global yuan
    yuan=1

def on_mouse_move(pos,buttons):
    if mouse.LEFT in buttons and yuan==0:      
        xf.x = pos[0]
        xf.y = pos[1]
        
def wl():
    global scr
    scr=6
    
#第六幕
    
cpu=Actor('cpu.png')
ms=Actor('mouse.jpg')
kb=Actor('keyboard.jpg')
un=Actor('unnamed.png')
rec=Actor('rect.png')
cpu.pos=(WIDTH)/2,(HEIGHT)+cpu.height
ms.pos=(WIDTH)/2,(HEIGHT)+ms.height
kb.pos=(WIDTH)/2,(HEIGHT)+kb.height
un.pos=(WIDTH)/2,(HEIGHT)+un.height
rec.pos=(WIDTH)/2,un.bottom+120

speed=3    

def lq():
    global scr
    scr=7
    
#第七幕

yx=Actor('游戏.jpg')
yx.topright = 760,347

m0=Actor('没0.jpg')
m1=Actor('没1.png')
m2=Actor('没2.png')
m3=Actor('没3.png')
m4=Actor('没4.jpg')
m0.topright = 210,347
m1.topright = 210,347
m2.topright = 210,347
m3.topright = 210,347
m4.topright = 210,347
mei=0

def mei1():
    global scr
    scr=8
def mei2():
    global scr
    scr=9
def mei3():
    global scr
    scr=10
def mei4():
    global scr
    scr=11
def qb():
    global scr
    scr=12

#第八幕

ksyx=Actor('开始游戏.jpg')
ksyx.topright = 635,390

def bj():
    global scr
    scr=13
    
#第九幕

alien = Actor('alien')
alien.topright = 100, 200
speedx,speedy=4,4

def xs():
    global scr
    scr=14
    
def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'
    
#总调配
def on_mouse_down(pos):
    global scr
    if scr==0:
        ly()
    elif scr==1:
        ye()
    elif scr==2:
        if pku.collidepoint(pos):     
            eey()
        elif thu.collidepoint(pos):
            eee()
    elif scr==21 or scr==22:
        if jinru.collidepoint(pos):
            es()
        elif diancuole.collidepoint(pos) or zaixiangxiang.collidepoint(pos) or queding.collidepoint(pos):
            fanhui2()
    elif scr==4:
        sounds.tc.play()
        if g.ccbox('很抱歉，因为您没有及时缴纳学费，您已被退学。\n若想继续就学，请及时补交学费。',choices=('补交学费，我还想继续苟','退学就退学，什么辣鸡带专')):
            sw()
    elif scr==5:
        if xf.collidepoint(pos):
            ke()
        else:
            bk()
    elif scr==6:
        if rec.collidepoint(pos):
            value=g.enterbox(msg='输入你的名字后点击OK键')
            if value == None:
                lq()
    elif scr==7:
        if m0.collidepoint(pos):
            mei1()
    elif scr==8:
        if m0.collidepoint(pos):
            mei2()
    elif scr==9:
        if m0.collidepoint(pos):
            mei3()
    elif scr==10:
        if m0.collidepoint(pos):
            mei4()
    elif scr==11:
        if yx.collidepoint(pos):
            qb()
    elif scr==12:
        if ksyx.collidepoint(pos):
            bj()
    elif scr==13:
        xs()
    elif scr==14:
        global speedx,speedy
        a=random.random()
        b=random.random()
        if alien.collidepoint(pos):
            set_alien_hurt()
            if speedx>0:
                speedx += 2*a
            elif speedx<0:
                speedx -= 2*a
        else:
            if speedx>2:
                speedx -= 2*a
            elif speedx<-2:
                speedx += 2*a
        if alien.collidepoint(pos):
            set_alien_hurt()
            if speedy>0:
                speedy += 2*b
            elif speedy<0:
                speedy -= 2*b
        else:
            if speedy>2:
                speedy -= 2*b
            elif speedy<-2:
                speedy += 2*b
    
def draw():
    if scr==0:
        screen.clear()
        screen.fill("red")
        jsp.draw()
        screen.draw.text("注意!!!",center=((WIDTH)/2,(HEIGHT)/1.5-40),fontname="emm",color="yellow",background="red",fontsize=100)
        screen.draw.text("这不是游戏！\n"*3,center=((WIDTH)/2,(HEIGHT)/1.5+80),fontname="emm",color="yellow",background="red",fontsize=30)
        screen.draw.text("千万不要点鼠标,这只会让你退出！",center=((WIDTH)/2,(HEIGHT)-50),fontname="emm",color="black",background="red",fontsize=20)
    elif scr==1:
        screen.clear()
        screen.fill("black")
        screen.draw.text("好吧，你还是点开了\n你为什么不相信我呢？\n这真的不是个游戏\n所以请现在、马上、立刻关掉它！\n千万不要点进去\n算我求你了\n否则你会看见一个很可怕的东西\n我说的都是真的\n请相信我，请关掉它\n而我也不会告诉你\n只要点击鼠标，你就能进入……",center=((WIDTH)/2,290),fontname="emm",color="white",background="black",fontsize=40)
    elif scr==2:
        screen.clear()
        background1.draw()
        pku.draw()
        thu.draw()
    elif scr==21:
        screen.clear()
        screen.fill("black")
        screen.draw.text("你确定要退出吗？",center=((WIDTH)/2,100),fontname="emm",color="white",background="black",fontsize=100)
        screen.draw.text("（不是从这里进入游戏）",center=((WIDTH)/2, 200),fontname="emm",color="white",background="black",fontsize=50)
        jinru.draw()
        diancuole.draw()
        zaixiangxiang.draw()
    elif scr==22:
        screen.clear()
        screen.fill("black")
        screen.draw.text("你确定要进入游戏吗？",center=((WIDTH)/2,100),fontname="emm",color="white",background="black",fontsize=80)
        queding.draw()
        zaixiangxiang.draw()
    elif scr==3:
        screen.clear()
        huaping.draw()
        sounds.bi.play()
        # 设置定时器
        clock.schedule(ss, 1.4)    
    elif scr==4:
        screen.clear()
        screen.fill("white")
        t1.draw()
        t2.draw()
        t3.draw()
        t4.draw()
    elif scr==5:
        screen.clear()
        screen.fill("white")
        screen.draw.text('请扫描二维码付款',center=(220,50),fontname="songti",color="black",fontsize=50)
        screen.draw.text('学费为',center=(100,200),fontname="songti",color="black",fontsize=50)
        fk.draw()
        skm.draw()
        xf.draw()
    elif scr==6:
        screen.clear()
        screen.fill('white')
        screen.draw.text("恭喜您缴费成功！\n",center=((WIDTH)/2,cpu.top-110),fontname="songti",color="red",fontsize=50)
        screen.draw.text("欢迎我们的金主爸爸（bushi）\n优秀学员代表登场！",center=((WIDTH)/2,cpu.top-25),fontname="songti",color="red",fontsize=40)
        cpu.draw()
        screen.draw.text("cpu君！",center=((WIDTH)/2,cpu.bottom+25),fontname="songti",color="red",fontsize=50)
        ms.draw()
        screen.draw.text("鼠标君！",center=((WIDTH)/2+30,ms.bottom+25),fontname="songti",color="red",fontsize=50)
        kb.draw()
        screen.draw.text("键盘君！",center=((WIDTH)/2,kb.bottom+25),fontname="songti",color="red",fontsize=50)
        un.draw()
        screen.draw.text("最后还有我们最优秀的学员...",center=((WIDTH)/2+10,un.bottom+30),fontname="songti",color="red",fontsize=45)
        screen.draw.text("emm...你叫什么名字来着？",center=((WIDTH)/2+10,un.bottom+70),fontname="songti",color="red",fontsize=45)
        rec.draw()
    elif scr==7:
        screen.clear()
        screen.fill((128, 0, 0))
        screen.draw.text('你为什么总是不听我的话！\n你应该点击OK键！\n这下好了，你只能待在这个界面了\n要知道，这个界面是',center=((WIDTH)/2,200),fontname="songti",color="white",fontsize=50)
        m0.draw()
        yx.draw()
    elif scr==8:
        screen.clear()
        screen.fill((128, 0, 0))
        screen.draw.text('你为什么总是不听我的话！\n你应该点击OK键！\n这下好了，你只能待在这个界面了\n要知道，这个界面是',center=((WIDTH)/2,200),fontname="songti",color="white",fontsize=50)
        m1.draw()
        yx.draw()
    elif scr==9:
        screen.clear()
        screen.fill((128, 0, 0))
        screen.draw.text('你为什么总是不听我的话！\n你应该点击OK键！\n这下好了，你只能待在这个界面了\n要知道，这个界面是',center=((WIDTH)/2,200),fontname="songti",color="white",fontsize=50)
        m2.draw()
        yx.draw()
    elif scr==10:
        screen.clear()
        screen.fill((128, 0, 0))
        screen.draw.text('你为什么总是不听我的话！\n你应该点击OK键！\n这下好了，你只能待在这个界面了\n要知道，这个界面是',center=((WIDTH)/2,200),fontname="songti",color="white",fontsize=50)
        m3.draw()
        yx.draw()
    elif scr==11:
        screen.clear()
        screen.fill((128, 0, 0))
        screen.draw.text('你为什么总是不听我的话！\n你应该点击OK键！\n这下好了，你只能待在这个界面了\n要知道，这个界面是',center=((WIDTH)/2,200),fontname="songti",color="white",fontsize=50)
        m4.draw()
        yx.draw()
    elif scr==12:
        screen.clear()
        screen.fill((128, 0, 0))
        screen.draw.text('qwq好吧，恭喜你找到了游戏\n但我不得不告诉你\n这个游戏真的很无聊\n如果你真的想玩的话...\n请自便吧',center=((WIDTH)/2,200),fontname="songti",color="white",fontsize=50)
        screen.draw.text('开始游戏',center=((WIDTH)/2,450),fontname="songti",color="white",fontsize=100)
        ksyx.draw()
    elif scr==13:
        screen.clear()
        screen.fill((128, 0, 0))
        screen.draw.text('这是一个很无聊的小游戏\n点击这个可怜的外星人就好',center=((WIDTH)/2,300),fontname="songti",color="white",fontsize=50)
        alien.draw()
    elif scr==14:
        screen.clear()
        screen.fill((128, 0, 0))
        alien.draw()
        
def update():
    if scr==5:
        if xf.colliderect(fk):
            wl()
    elif scr==6:
        global speed
        cpu.y-=speed
        if cpu.y<=2*(HEIGHT)/3:
            ms.y-=speed    
            if ms.y<=2*(HEIGHT)/3:
                kb.y-=speed
                if kb.y<=2*(HEIGHT)/3:
                    un.y-=speed
                    rec.y-=speed
                    if un.y<=(HEIGHT)/2-50:
                        un.pos=(WIDTH)/2,(HEIGHT)/2-50
                        rec.pos=(WIDTH)/2,un.bottom+120
    elif scr==14:
        global speedx,speedy
        alien.x += speedx
        if alien.x > WIDTH-30 or alien.x < 30:
            speedx = -speedx
        alien.y += speedy
        if alien.y > HEIGHT-40 or alien.y < 40:
            speedy = -speedy
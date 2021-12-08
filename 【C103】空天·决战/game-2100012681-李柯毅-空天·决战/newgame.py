import pgzrun
import random

WIDTH=1280
HEIGHT=854

things1shang=[]
things1xia=[]
things1zuo=[]
things1you=[]
things2=[]
things2s=[]
zhangai=[]
daoju=[]
swift_name=["special1","swift1","swift2"]
names = ["peach", "cherryf",  "orange", "lemon", "grape", "banana",
         "egg", "donut", "taco", "pizza", "burger", "fries", "leg", "dango",
         "cake", "cookie", "ice", "candy",
         "cherry", "bouquet", "leaf4", "sunflower", "tulip", "rose",
         "tiger", "cat"]
music.play("music1")

player2=Actor("ac2")
player2.angle-=90
player1=Actor("ac1")
player1.angle+=90
player1.center=(80,400)
player2.center=(1200,400)
player1.lives=8
player2.lives=8

x=Actor("1")
x.start=True
x.game=False
x.instruct=False
x.end=False
x.restart=False
x.jiafen=True
x.p1=False
x.p2=False
x.change=1
x.win1=0
x.win2=0

for v in range(random.randint(8,10)):
    w=Actor(random.choice(names))
    zhangai.append(w)

for f in zhangai:
    f.center=random.randint(200,1000),random.randint(100,700)
    
def start():
    screen.clear()
    screen.fill("white")
    screen.draw.text("空天·决战",(100,100),fontsize=150,color="black",fontname="cocacola")
    screen.draw.text("作者：李柯毅",(400,300),fontsize=60,color="black",fontname="cocacola")
    screen.draw.text("课程：计算概论B（陈斌老师）",(400,400),fontsize=60,color="black",fontname="cocacola")
    screen.draw.text("欢迎大家试玩！！！",(100,510),fontsize=100,color="red",fontname="cocacola")
    screen.draw.text("按下O以查看游戏说明！",(670,700),fontsize=50,color="blue",fontname="cocacola")
    
    
def instruct():
    screen.clear()
    screen.fill("black")
    screen.draw.text("游戏说明",(400,50),fontsize=100,fontname="cocacola",color="red")
    screen.draw.text("""玩家1（左侧），玩家2（右侧）对决，每人八条生命

1、画面每隔一段时间会出现障碍，玩家的子弹会被阻挡
2、画面会随机出现红心，吃到红心可以使生命值+1""",(20,180),fontsize=40,fontname="cocacola",color="orange")
    screen.draw.text("""玩家1：
      移动方式：W——向上；S——向下；A——向左：D——向右
      攻击方式：Q——攻击（向四个方向发射子弹，有概率触发大招）
                            
                              """,(20,420),fontsize=35,fontname="cocacola",color="pink")
    screen.draw.text("""玩家2:
      移动方式：上下左右键移动
      攻击方式：空格键——攻击（单方向发射子弹，有概率触发大招）
      特殊技能：shift改变子弹方向；穿越屏幕边界""",(20,560),fontsize=35,fontname="cocacola",color="yellow")
    screen.draw.text("请按P开始游戏",(850,780),fontsize=50,fontname="cocacola",color="red")
    
    
def game():
    screen.clear()
    screen.blit("sky",(0,0))
    player1.draw()
    player2.draw()
    
    for t1 in things1shang:
        t1.draw()
        
    for t1 in things1xia:
        t1.draw()
        
    for t1 in things1zuo:
        t1.draw()
        
    for t1 in things1you:
        t1.draw()
        
    for t2 in things2:
        t2.draw()
        
    for t2s in things2s:
        t2s.draw()
        
    for f in zhangai:
        f.draw()
        
    for dj in daoju:
        dj.draw()
        
    screen.draw.filled_rect(Rect((player1.bottomleft),(player1.lives*20,20)),"red")
    screen.draw.filled_rect(Rect((player2.bottomleft),(player2.lives*20,20)),"red")
    screen.draw.rect(Rect((player1.bottomleft),(160,20)),"white")
    screen.draw.rect(Rect((player2.bottomleft),(160,20)),"white")
    
    
def defeat():
    if player1.lives==0:
        win="player2"
        if x.jiafen==True:
            x.win2+=1
            x.jiafen=False
    else:
        win="player1"
        if x.jiafen==True:
            x.win1+=1
            x.jiafen=False
            
            
    screen.fill("black")
    screen.draw.text("Game Over!", (300, 250),fontsize=180,color="red")
    screen.draw.text("请按鼠标左键重新开始",(800,700),fontsize=40,fontname="cocacola",color="red")
    screen.draw.text("          Winner: %s"%win,(200, 430),fontsize=100,color="red")
    screen.draw.text("               P1:P2=%d:%d"%(x.win1,x.win2),(200, 530),fontsize=100,color="red")


def reset():
    player1.center=(80,400)
    player2.center=(1200,400)
    player1.lives=8
    player2.lives=8
    
    for v in range(random.randint(8,10)):
        w=Actor(random.choice(names))
        zhangai.append(w)
    for f in zhangai:
        f.center=random.randint(200,1100),random.randint(100,700)
        
    zhangai.clear()
    things1you.clear()
    things1zuo.clear()
    things1shang.clear()
    things1xia.clear()
    things2.clear()
    things2s.clear()
    daoju.clear()
    
    x.jiafen=True
    if x.change==0:
        player2.angle-=180
    x.change=1
    
    
def draw():
    if player1.lives==0 or player2.lives==0:
        x.end=True
        x.game=False
    if x.end:        
        defeat()
    if x.start:
        start()
    if x.game:
        game()
    if x.instruct:
        instruct()

        
def update():
    if x.game:
        if random.randrange(60)==0 and len(zhangai)<=15:
            u= Actor(random.choice(names))
            u.center = random.randint(200,1000),random.randrange(700)
            zhangai.append(u)
        
        if random.randrange(600)==0 and len(daoju)<=2:
            u= Actor("heart")
            u.center = random.randint(200,1000),random.randrange(800)
            daoju.append(u)
        
        for r in daoju:
            if player1.colliderect(r):
                player1.lives+=1
                daoju.remove(r)
            if player2.colliderect(r):
                player2.lives+=1
                daoju.remove(r)
        if things2:
            for t2 in things2:         
                t2.x-=10
                t2.angle+=10          
                if t2.x<0:
                    things2.remove(t2)
                if player1.colliderect(t2):
                    if t2 in things2:
                        things2.remove(t2)
                        player1.lives-=1
                        sounds.ogre.play()
                for u in zhangai:
                    if t2.colliderect(u):
                        if t2 in things2:
                            things2.remove(t2)
                            zhangai.remove(u)
                            sounds.exp.play()
        if things2s:
            for t2 in things2s:         
                t2.x+=10
                t2.angle-=10      
                if t2.x>1280:
                    things2s.remove(t2)
                if player1.colliderect(t2):
                    if t2 in things2s:
                        things2s.remove(t2)
                        player1.lives-=1
                        sounds.ogre.play()
                for u in zhangai:
                    if t2.colliderect(u):
                        if t2 in things2s:
                            things2s.remove(t2)
                            zhangai.remove(u)
                            sounds.exp.play()

           
        for ty in things1you:
            ty.x+=10
            if ty.x>1280:
                things1you.remove(ty)
            if player2.colliderect(ty):
                if ty in things1you:
                    things1you.remove(ty)
                    player2.lives-=1
                    sounds.ogre.play()
            for u in zhangai:
                if ty.colliderect(u):
                    if ty in things1you:
                        things1you.remove(ty)
                        zhangai.remove(u)
                        sounds.exp.play()
                
            
        
        for tx in things1xia:
            tx.y+=10
            if tx.y>854:
                things1xia.remove(tx)
            if player2.colliderect(tx):
                if tx in things1xia:
                    things1xia.remove(tx)
                    player2.lives-=1
                    sounds.ogre.play()
            for u in zhangai:
                if tx.colliderect(u):
                    if tx in things1xia:
                        things1xia.remove(tx)
                        zhangai.remove(u)
                        sounds.exp.play()
        for tz in things1zuo:
            tz.x-=10
            if tz.x<0:
                things1zuo.remove(tz)
            if player2.colliderect(tz):
                if tz in things1zuo:
                    things1zuo.remove(tz)
                    player2.lives-=1
                    sounds.ogre.play()
            for u in zhangai:
                if tz.colliderect(u):
                    if tz in things1zuo:
                        things1zuo.remove(tz)
                        zhangai.remove(u)
                        sounds.exp.play()
                    
        for tsh in things1shang:
            tsh.y-=10
            if tsh.y<0:
                things1shang.remove(tsh)
            if player2.colliderect(tsh):
                if tsh in things1shang:
                    things1shang.remove(tsh)
                    player2.lives-=1
                    sounds.ogre.play()
            for u in zhangai:
                if tsh.colliderect(u):
                    if tsh in things1shang:
                        things1shang.remove(tsh)
                        zhangai.remove(u)
                        sounds.exp.play()


   
def on_key_down(key):
    if x.game:
        if key==key.UP:
            player2.y-=40
            if player2.y<0:
                player2.y=854
        if key==key.RIGHT:
            player2.x+=20
            if player2.x>1280:
                player2.x=0
        if key==key.DOWN:
            player2.y+=40
            if player2.y>854:
                player2.y=0
        if key==key.LEFT:
            player2.x-=20
            if player2.x<0:
                player2.x=1280
        if key==key.W:
            player1.y-=40
            if player1.y<30:
                player1.y=30
        if key==key.D:
            player1.x+=20
            if player1.x>1260:
                player1.x=1260
        if key==key.S:
            player1.y+=40
            if player1.y>824:
                player1.y=824
        if key==key.A:
            player1.x-=20
            if player1.x<20:
                player1.x=20
        if key==key.Q:
            sounds.laser2.play()
            if random.randrange(200)==1:
                ta=Actor("henqiang")
            elif random.randrange(50)==10:
                ta=Actor("special")
            elif random.randrange(20)==10:
                ta=Actor("catbullet")
            elif random.randrange(1000)==0:
                ta=Actor("crab")
            else:
                ta=Actor("blue")
                
                
            if random.randrange(20)==5:
                tb=Actor("firework")
                tb.angle-=180
            elif random.randrange(150)==20:
                tb=Actor("amazing")
                tb.angle-=180
            elif random.randrange(1000)==0:
                tb=Actor("crab")
            else:
                tb=Actor("blue")
                tb.angle-=180
            
            tc=Actor("left2")
            td=Actor("left2")
            ta.center=player1.center
            tb.center=player1.center
            tc.center=player1.center
            td.center=player1.center
  
            things1you.append(ta)
            things1zuo.append(tb)
            things1shang.append(tc)
            things1xia.append(td)


        if key==key.SPACE:
            sounds.laser1.play()
            if x.change==1:
                if random.randrange(100)==5:
                    tsp=Actor("right big")
                    tsp.center=player2.center
                    things2.append(tsp)
                elif random.randrange(20)==1:
                    tg=Actor(random.choice((swift_name)))
                    tg.angle+=180
                    tg.center=player2.center
                    things2.append(tg)
                    
                elif random.randrange(50)==0:
                    tg=Actor("sun")
                    tg.angle+=180
                    tg.center=player2.center
                    things2.append(tg)
                elif random.randrange(1000)==0:
                    tg=Actor("boss_frog")
                    tg.angle+=180
                    tg.center=player2.center
                    things2.append(tg)
                else:
                    t2=Actor("swift")
                    t2.center=player2.center
                    things2.append(t2)
            else:
                if random.randrange(100)==5:
                    tsps=Actor("right big")
                    tsps.center=player2.center
                    things2s.append(tsps)
                elif random.randrange(20)==1:
                    tgs=Actor(random.choice((swift_name)))
                    tgs.angle+=180
                    tgs.center=player2.center
                    things2s.append(tgs)
                elif random.randrange(50)==1:
                    tgss=Actor("fireball")
                    tgss.angle+=180
                    tgss.center=player2.center
                    things2s.append(tgss)
                elif random.randrange(1000)==0:
                    tg1=Actor("boss_frog")
                    tg1.angle+=180
                    tg1.center=player2.center
                    things2s.append(tg1)
                else:
                    t2s=Actor("swift")
                    t2s.center=player2.center
                    things2s.append(t2s)
                
        if key==key.RSHIFT:
            if x.change==0:
                x.change=1
                player2.angle-=180
            elif x.change==1:
                x.change=0
                player2.angle+=180
    if key==key.O:
        x.instruct=True
        x.start=False
    if key==key.P:
        x.instruct=False
        x.game=True
        
def on_mouse_down(button):
    if x.end and button==mouse.LEFT :
        x.end=False
        x.start=True
        reset()

pgzrun.go()

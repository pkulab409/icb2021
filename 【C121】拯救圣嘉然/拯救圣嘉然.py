import pgzrun
import random
import sys
import easygui as g

hero = Actor('planem')
check = Actor('check20w')
bullet = Actor('zidan')
back1=Actor('back')
back1.x=0
back1.y=0
back2=Actor('back')
back2.x=0
back2.y=-3464
herolist=[hero]
checklist=[check]
aulist =[]
bulist=[]
culist=[]
monstersname=['monster1','monster2','monster3']
monsters=[]
bosses=[]
xueliang={}
adlist=[]
bdlist=[]
cdlist=[]
ddlist=[]
edlist=[]
fdlist=[]
gdlist=[]
hdlist=[]
ad1list=[]
bd1list=[]
cd1list=[]
ad2list=[]
bd2list=[]
cd2list=[]
dd2list=[]
ed2list=[]
fd2list=[]
gd2list=[]

g.msgbox('拯救圣嘉然公主，就靠你了！',title='拯救圣嘉然！')
g.msgbox('请把游戏窗口拖到屏幕上方以获得良好体验！\n用鼠标控制飞机移动，按任意键都可以发射子弹。\n温馨提示：小喽啰都是一发子弹即死，当然你也一样。\n好消息是，只有鼠标周围的一小圈才是碰撞判定点。\n分数达到200后进入第二关并自动存档。\n左上角是你的分数，右上角是boss血量。加油！',title='拯救圣嘉然！')
def boom():
    t.image='bao'
    clock.schedule(mei,0.2)
def mei():
    for t in monsters:
        if t.image =='bao':
            monsters.remove(t)
hero.pos = 400,800
WIDTH = 800
HEIGHT = 1000

s = 0#积分
x1 = 100
x2 = 200
k = 0#频率调节


def end():
    for c in checklist:
        checklist.remove(c)
    hero.image='bao'
    clock.schedule(ji,0.2)
def ji():  
    g.msgbox('您失败了 游戏结束 请退出并重新来过\n嘉然没有等来您！',title='拯救圣嘉然！')
    clock.schedule(wu,2.0)
def wu():
    sys.exit()
    
def win():
    g.msgbox('恭喜！祝您和嘉然公主百年好合',title='拯救圣嘉然！')
    clock.schedule(wu,2.0)

def draw():
    screen.clear()
    
    back1.draw()
    back2.draw()
    for h in herolist:
        h.draw()
    for c in checklist:
        c.draw()
    for au in aulist:
        au.draw()
    for bu in bulist:
        bu.draw()
    for cu in culist:
        cu.draw()
    for t in monsters:
        t.draw()
    for a in bosses:
        a.draw()
    for a in adlist:
        a.draw()
    for a in bdlist:
        a.draw()
    for a in cdlist:
        a.draw()
    for a in ddlist:
        a.draw()
    for a in edlist:
        a.draw()
    for a in fdlist:
        a.draw()
    for a in gdlist:
        a.draw()
    for a in hdlist:
        a.draw()
    for a in ad1list:
        if x1>0:
            a.draw()
    for a in bd1list:
        if x1>0:
            a.draw()
    for a in cd1list:
        if x1>0:
            a.draw()
    for a in ad2list:
        if x2>0 and s>=800:
            a.draw()        
    for a in bd2list:
        if x2>0 and s>=800:
            a.draw()
    for a in cd2list:
        if x2>0 and s>=800:
            a.draw()
    for a in dd2list:
        if x2>0 and s>=800:
            a.draw()        
    for a in ed2list:
        if x2>0 and s>=800:
            a.draw()
    for a in fd2list:
        if x2>0 and s>=800:
            a.draw()
    for a in gd2list:
        if x2>0 and s>=800:
            a.draw()
    screen.draw.text('points:'+str(s), (100,100), color = 'yellow')
    if s == 1000:
        j.draw()
    if 140<=s<200:
        screen.draw.text('HP:'+str(x1), (700,100), color = 'yellow')
    if 800<=s<1000:
        screen.draw.text('HP:'+str(x2), (700,150), color = 'yellow')
    
def on_mouse_move(pos):
    hero.x = check.x = pos[0]
    hero.y = check.y = pos[1]
    
    
def on_key_down(key):
    if s<200:
        newbullet =Actor('zidan')
        bulist.append(newbullet)
        newbullet.x = hero.x
        newbullet.y = hero.y - 50
    if s>=200:
        newbullet =Actor('zidan')
        nwbullet =Actor('zidan')
        nebullet =Actor('zidan')
        aulist.append(nwbullet)
        bulist.append(newbullet)
        culist.append(nebullet)
        nwbullet.x = hero.x-20
        nwbullet.y = hero.y - 50
        nwbullet.angle=45
        newbullet.x = hero.x-1
        newbullet.y = hero.y - 50
        nebullet.x = hero.x+20
        nebullet.y = hero.y - 50
        nebullet.angle=-45

def update():
    global t,s,x1,x2,p,j
    if s<200:
        
        
        if back1.y>2732:
            back1.y=-3464
        if back2.y>2732:
            back2.y=-3464
        back1.y+=2
        back2.y+=2
        for b in bulist:
            if b.y>0:
                b.y -=8
            else:
                bulist.remove(b)
        for a in adlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x+=5
            
            else:
                adlist.remove(a)
            if a.colliderect(check):
                if a in adlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                adlist.remove(a)
                end()
        for a in bdlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x+=3
                a.y-=3
            
            else:
                bdlist.remove(a)
            if a.colliderect(check):
                if a in bdlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                bdlist.remove(a)
                end()
        for a in cdlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.y-=5
            
            else:
                cdlist.remove(a)
            if a.colliderect(check):
                if a in cdlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                cdlist.remove(a)
                end()
        for a in ddlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x-=3
                a.y-=3
            
            else:
                ddlist.remove(a)
            if a.colliderect(check):
                if a in ddlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                ddlist.remove(a)
                end()
        for a in edlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x-=5
            
            else:
                edlist.remove(a)
            if a.colliderect(check):
                if a in edlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                edlist.remove(a)
                end()
        for a in fdlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x-=3
                a.y+=3
            
            else:
                fdlist.remove(a)
            if a.colliderect(check):
                if a in fdlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                fdlist.remove(a)
                end()
        for a in gdlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.y+=5
            
            else:
                gdlist.remove(a)
            if a.colliderect(check):
                if a in gdlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                gdlist.remove(a)
                end()
        for a in hdlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x+=3
                a.y+=3
            
            else:
                hdlist.remove(a)
            if a.colliderect(check):
                if a in hdlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                hdlist.remove(a)
                end()
        
        for a in ad1list:
            if 0<a.y<1000 and 0<a.x<800:
                if 66<x1<100:                    
                    a.x+=2
                    a.y+=4
                if 33<x1<67:
                    a.x+=1
                    a.y+=4
                if 0<x1<34:
                    a.x+=1
                    a.y+=6
            
            else:
                ad1list.remove(a)
            if a.colliderect(check):
                if a in ad1list:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                    ad1list.remove(a)
                    end()
            if x1<=0:
                if a in ad1list:                    
                    ad1list.remove(a)
                    
        for a in bd1list:
            if 0<a.y<1000 and 0<a.x<800:
                if 66<x1<100:                    
                    a.x-=2
                    a.y+=4
                if 33<x1<67:
                    a.x-=1
                    a.y+=4
                if 0<x1<34:
                    a.x-=1
                    a.y+=6
                
            else:
                bd1list.remove(a)
            if a.colliderect(check):
                if a in bd1list:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                    bd1list.remove(a)
                    end()
            if x1<=0:
                if a in bd1list:
                    bd1list.remove(a)
        
        for a in cd1list:
            if 0<a.y<1000 and 0<a.x<800:
                if 83<x1<100 or 50<x1<67:                    
                    a.y+=4
                if 0<x1<17:                    
                    a.y+=6
                
            else:
                cd1list.remove(a)
            if a.colliderect(check):
                if a in cd1list:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                    cd1list.remove(a)
                    end()
            if x1<=0:
                if a in cd1list:
                    cd1list.remove(a)        
                
                

        if s<=140 and random.randrange(90) == 0:#出怪程序
            t = Actor(random.choice(monstersname))
            t.center = 200+random.randrange(400), random.randrange(300)
            monsters.append(t)
            #xueliang[t]=0
            
        for t in monsters:
            
            #既往下走又有点随机性，不过还可以改
            
            t.y += 3
            t.y += random.randrange(-2, 2)
            t.x += random.randrange(-5, 5)
            
            if t.y >= 1000:
                monsters.remove(t)
            elif t.colliderect(hero):
                end()
            #下面是子弹打小怪的判断，最内层的if是为保险程序加上的
            for a in aulist:
                if t.colliderect(a):
                    if t in monsters:
                        s+=1
                        tone.play('E3', 0.2)
                        tone.play('G3', 0.2)
                        tone.play('C4', 0.2)
                        #xueliang[t]+=1
                    #if t in monsters and xueliang[t] >= 5:
                        boom()
                        
                        aulist.remove(a)
            for b in bulist:
                if t.colliderect(b):
                    if t in monsters:
                        s+=1
                        tone.play('E3', 0.2)
                        tone.play('G3', 0.2)
                        tone.play('C4', 0.2)
                        #xueliang[t]+=1
                    #if t in monsters and xueliang[t] >= 5:
                        boom()
                        
                        bulist.remove(b)
            for c in culist:
                if t.colliderect(c):
                    if t in monsters:
                        s+=1
                        tone.play('E3', 0.2)
                        tone.play('G3', 0.2)
                        tone.play('C4', 0.2)
                        #xueliang[t]+=1
                    #if t in monsters and xueliang[t] >= 5:
                        boom()
                        
                        culist.remove(c)
            #下面是小怪的子弹            
            if random.randrange(60) == 0:
                Edanmu=Actor('danmu1')    
                NEdanmu=Actor('danmu1')
                Ndanmu=Actor('danmu1')
                NWdanmu=Actor('danmu1')
                Wdanmu=Actor('danmu1')
                SWdanmu=Actor('danmu1')
                Sdanmu=Actor('danmu1')
                SEdanmu=Actor('danmu1')
                adlist.append(Edanmu)
                bdlist.append(NEdanmu)
                cdlist.append(Ndanmu)
                ddlist.append(NWdanmu)
                edlist.append(Wdanmu)
                fdlist.append(SWdanmu)
                gdlist.append(Sdanmu)
                hdlist.append(SEdanmu)
                Edanmu.x=NEdanmu.x=Ndanmu.x=NWdanmu.x=Wdanmu.x=SWdanmu.x=Sdanmu.x=SEdanmu.x=t.x
                Edanmu.y=NEdanmu.y=Ndanmu.y=NWdanmu.y=Wdanmu.y=SWdanmu.y=Sdanmu.y=SEdanmu.y=t.y
                
                
        if 140 < s < 200 and len(bosses) <1:
            p = Actor('boss1')
            p.center = (400, 250)
            bosses.append(p)
            
        for p in bosses:
            for b in bulist:
                
                if b.colliderect(p):
                    
                    x1-=1
                    tone.play('E3', 0.2)
                    tone.play('G3', 0.2)
                    tone.play('C4', 0.2)
                    #xueliang[t]+=1
                #if t in monsters and xueliang[t] >= 5:
                    
                    bulist.remove(b)
                    
            if random.randrange(20) == 0:
                SWdanmu=Actor('danmu2')
                SEdanmu=Actor('danmu2')
                Sdanmu=Actor('danmu2')
                ad1list.append(SWdanmu)
                bd1list.append(SEdanmu)
                cd1list.append(Sdanmu)
                SWdanmu.x=SEdanmu.x=Sdanmu.x=p.x
                SWdanmu.y=SEdanmu.y=Sdanmu.y=p.y
            
            if x1 <= 0:
                bosses.remove(p)
                for a in ad1list:
                    ad1list.remove(a)
                for a in bd1list:
                    bd1list.remove(a)
                for a in cd1list:
                    cd1list.remove(a)
                s = 200
            
            
            
            
    def on_key_down(key):
        newbullet =Actor('zidan')
        bulist.append(newbullet)
        newbullet.x = hero.x
        newbullet.y = hero.y - 50


    if s > 199 :
        #global t,s#,x2
        
        if back1.y>2732:
            back1.y=-3464
        if back2.y>2732:
            back2.y=-3464
        back1.y+=1
        back2.y+=1
        for a in aulist:#我的子弹移动
            a.x-=3
            if a.y>0:
                a.y -=8
            else:
                aulist.remove(a)
        for b in bulist:
            if b.y>0:
                b.y -=8
            else:
                bulist.remove(b)
        for c in culist:
            c.x+=3
            if c.y>0:
                c.y -=8
            else:
                culist.remove(c)
                
        for a in adlist:#第二批小怪的子弹
            if 0<a.y<1000 and 0<a.x<800:
                a.x+=5
            
            else:
                adlist.remove(a)
            if a.colliderect(check):
                if a in adlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                adlist.remove(a)
                s = 200
        for a in bdlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x+=3
                a.y-=3
            
            else:
                bdlist.remove(a)
            if a.colliderect(check):
                if a in bdlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                bdlist.remove(a)
                s = 200
        for a in cdlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.y-=5
            
            else:
                cdlist.remove(a)
            if a.colliderect(check):
                if a in cdlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                cdlist.remove(a)
                s = 200
        for a in ddlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x-=3
                a.y-=3
            
            else:
                ddlist.remove(a)
            if a.colliderect(check):
                if a in ddlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                ddlist.remove(a)
                s = 200
        for a in edlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x-=5
            
            else:
                edlist.remove(a)
            if a.colliderect(check):
                if a in edlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                edlist.remove(a)
                s = 200
        for a in fdlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x-=3
                a.y+=3
            
            else:
                fdlist.remove(a)
            if a.colliderect(check):
                if a in fdlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                fdlist.remove(a)
                s = 200
        for a in gdlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.y+=5
            
            else:
                gdlist.remove(a)
            if a.colliderect(check):
                if a in gdlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                gdlist.remove(a)
                s = 200
        for a in hdlist:
            if 0<a.y<1000 and 0<a.x<800:
                a.x+=3
                a.y+=3
            
            else:
                hdlist.remove(a)
            if a.colliderect(check):
                if a in hdlist:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                hdlist.remove(a)
                s = 200
                
        for a in ad2list:
            if 0<a.y<1000 and 0<a.x<800:
                if 133<x2<200:
                    a.x-=2
                    a.y+=6
                if 66<x2<134:
                    a.x-=1
                    a.y+=4
                if 0<x2<67:
                    a.x-=1
                    a.y+=6                
            else:
                ad2list.remove(a)
                
            if a.colliderect(check) and s < 1000:
                if a in ad2list:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                    ad2list.remove(a)
                    s = 200
            if x2<=0:
                if a in ad2list:
                    ad2list.remove(a)
        
        for a in bd2list:
            if 0<a.y<1000 and 0<a.x<800:
                if 133<x2<200:
                    a.x+=2
                    a.y+=6
                if 66<x2<134:
                    a.x+=1
                    a.y+=4
                if 0<x2<67:
                    a.x+=1
                    a.y+=6                
            else:
                bd2list.remove(a)
                
            if a.colliderect(check) and s < 1000:
                if a in bd2list:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                    bd2list.remove(a)
                    s = 200
            if x2<=0:
                if a in bd2list:
                    bd2list.remove(a)
        
        for a in cd2list:
            if 0<a.y<1000 and 0<a.x<800:
                if 133<x2<200:
                    
                    a.y+=6
                #if 66<x2<134:
                    
                    #a.y+=4
                if 0<x2<33:
                    
                    a.y+=6                
            else:
                cd2list.remove(a)
                
            if a.colliderect(check) and s < 1000:
                if a in cd2list:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                    cd2list.remove(a)
                    s = 200
            if 33<=x2<=133:
                if a in cd2list:
                    cd2list.remove(a)
        
        for a in dd2list:
            if 0<a.y<1000 and 0<a.x<800:
                
                if 66<x2<134:
                    a.x-=3
                    a.y+=7
                if 0<x2<67:
                    a.x-=2
                    a.y+=7                
            else:
                dd2list.remove(a)
                
            if a.colliderect(check) and s < 1000:
                if a in dd2list:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                    dd2list.remove(a)
                    s = 200
            if x2<=0:
                if a in dd2list:
                    dd2list.remove(a)
        
        for a in ed2list:
            if 0<a.y<1000 and 0<a.x<800:
                
                if 66<x2<134:
                    a.x+=3
                    a.y+=7
                if 0<x2<67:
                    a.x+=2
                    a.y+=7                
            else:
                ed2list.remove(a)
                
            if a.colliderect(check) and s < 1000:
                if a in ed2list:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                    ed2list.remove(a)
                    s = 200
            if x2<=0:
                if a in ed2list:
                    ed2list.remove(a)
        
        for a in fd2list:
            if 0<a.y<1000 and 0<a.x<800:
                
                if 0<x2<200:
                    a.x+=2
                    a.y+=8
                              
            else:
                fd2list.remove(a)
                
            if a.colliderect(check) and s < 1000:
                if a in fd2list:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                    fd2list.remove(a)
                    s = 200
            if x2<=0:
                if a in fd2list:
                    fd2list.remove(a)
        
        for a in gd2list:
            if 0<a.y<1000 and 0<a.x<800:
                
                if 0<x2<200:
                    a.x-=2
                    a.y+=8
                               
            else:
                gd2list.remove(a)
                
            if a.colliderect(check) and s < 1000:
                if a in gd2list:
                    tone.play('E4', 0.2)
                    tone.play('C4', 0.2)
                    tone.play('A3', 0.2)
                    gd2list.remove(a)
                    s = 200
            if x2<=0:
                if a in gd2list:
                    gd2list.remove(a)
                
        if 200 <= s <= 400:
            k = 30
        if 401 <= s <= 600:
            k = 20
        if 600 <= s <= 799:
            k = 10
        
        if 200 <= s <= 799 and random.randrange(k) == 0:#出怪程序
            t = Actor(random.choice(monstersname))
            t.center = 200+random.randrange(400), random.randrange(300)
            monsters.append(t)
            #xueliang[t]=0
            
        for t in monsters:
            #既往下走又有点随机性，不过还可以改
            
            t.y += 5
            t.y += random.randrange(-3, 3)
            t.x += random.randrange(-7, 7)
            
            if t.y >= 1000:
                monsters.remove(t)
            elif t.colliderect(hero):
                monsters.remove(t)
                s = 200
            #下面是子弹打小怪的判断，最内层的if是为保险程序加上的
            for a in aulist:
                if t.colliderect(a):
                    if t in monsters:
                        #xueliang[t]+=1
                    #if t in monsters and xueliang[t] >= 5:
                        boom()
                        s+=1
                        tone.play('E3', 0.2)
                        tone.play('G3', 0.2)
                        tone.play('C4', 0.2)
                        aulist.remove(a)
            for b in bulist:
                if t.colliderect(b):
                    if t in monsters:
                        #xueliang[t]+=1
                    #if t in monsters and xueliang[t] >= 5:
                        boom()
                        s+=1
                        tone.play('E3', 0.2)
                        tone.play('G3', 0.2)
                        tone.play('C4', 0.2)
                        bulist.remove(b)
            for c in culist:
                if t.colliderect(c):
                    if t in monsters:
                        #xueliang[t]+=1
                    #if t in monsters and xueliang[t] >= 5:
                        boom()
                        s+=1
                        tone.play('E3', 0.2)
                        tone.play('G3', 0.2)
                        tone.play('C4', 0.2)
                        culist.remove(c)
            #下面是小怪的子弹            
            if random.randrange(60) == 0:
                Edanmu=Actor('danmu1')    
                NEdanmu=Actor('danmu1')
                Ndanmu=Actor('danmu1')
                NWdanmu=Actor('danmu1')
                Wdanmu=Actor('danmu1')
                SWdanmu=Actor('danmu1')
                Sdanmu=Actor('danmu1')
                SEdanmu=Actor('danmu1')
                adlist.append(Edanmu)
                bdlist.append(NEdanmu)
                cdlist.append(Ndanmu)
                ddlist.append(NWdanmu)
                edlist.append(Wdanmu)
                fdlist.append(SWdanmu)
                gdlist.append(Sdanmu)
                hdlist.append(SEdanmu)
                Edanmu.x=NEdanmu.x=Ndanmu.x=NWdanmu.x=Wdanmu.x=SWdanmu.x=Sdanmu.x=SEdanmu.x=t.x
                Edanmu.y=NEdanmu.y=Ndanmu.y=NWdanmu.y=Wdanmu.y=SWdanmu.y=Sdanmu.y=SEdanmu.y=t.y
                
        if 800 <= s < 1000 and len(bosses) <1:
            p = Actor('boss2')
            p.center = (400, 250)
            bosses.append(p)
            
        for p in bosses:
            for b in bulist:#我打boss2
                
                if b.colliderect(p):
                    
                    x2-=1
                    tone.play('E3', 0.2)
                    tone.play('G3', 0.2)
                    tone.play('C4', 0.2)
                    #xueliang[t]+=1
                #if t in monsters and xueliang[t] >= 5:
                    
                    bulist.remove(b)
                    
            for b in aulist:
                
                if b.colliderect(p):
                    
                    x2-=1
                    tone.play('E3', 0.2)
                    tone.play('G3', 0.2)
                    tone.play('C4', 0.2)
                    #xueliang[t]+=1
                #if t in monsters and xueliang[t] >= 5:
                    
                    aulist.remove(b)
                    
            for b in culist:
                
                if b.colliderect(p):
                    
                    x2-=1
                    tone.play('E3', 0.2)
                    tone.play('G3', 0.2)
                    tone.play('C4', 0.2)
                    #xueliang[t]+=1
                #if t in monsters and xueliang[t] >= 5:
                    
                    culist.remove(b)        
                    
            if random.randrange(20) == 0:#重新编写弹幕！
                SW1danmu=Actor('danmu2')#1是boss自己的东西
                SE1danmu=Actor('danmu2')
                SSdanmu=Actor('danmu2')
                SW2danmu=Actor('danmu2')#2是两侧子弹的，这个在右侧，往左下打
                SE2danmu=Actor('danmu2')#这个在左侧，往右下打
                SW3danmu=Actor('danmu2')#也在右侧
                SE3danmu=Actor('danmu2')#也在左侧
                ad2list.append(SW1danmu)
                bd2list.append(SE1danmu)
                cd2list.append(SSdanmu)
                dd2list.append(SW2danmu)
                ed2list.append(SE2danmu)
                fd2list.append(SW3danmu)
                gd2list.append(SE3danmu)
                SW1danmu.x=SE1danmu.x=SSdanmu.x=p.x
                SW1danmu.y=SE1danmu.y=SSdanmu.y=SW2danmu.y=SE2danmu.y=SW3danmu.y=SE3danmu.y=p.y
                SW2danmu.x = SW3danmu.x = p.x + 150
                SE2danmu.x = SE3danmu.x = p.x - 150
                
                
            if x2 <= 0 :#重新编写弹幕！
                bosses.remove(p)
                for a in ad2list:
                    ad2list.remove(a)
                for a in bd2list:
                    bd2list.remove(a)
                for a in cd2list:
                    cd2list.remove(a)
                for a in dd2list:
                    dd2list.remove(a)
                for a in ed2list:
                    ed2list.remove(a)
                for a in fd2list:
                    fd2list.remove(a)
                for a in gd2list:
                    gd2list.remove(a)
                s = 1000        
            
            if s < 800 :#重新编写弹幕！
                
                if p in bosses:
                    bosses.remove(p)
                for a in ad2list:
                    ad2list.remove(a)
                for a in bd2list:
                    bd2list.remove(a)
                for a in cd2list:
                    cd2list.remove(a)
                for a in dd2list:
                    dd2list.remove(a)
                for a in ed2list:
                    ed2list.remove(a)
                for a in fd2list:
                    fd2list.remove(a)
                for a in gd2list:
                    gd2list.remove(a)
                s = 200
                
        if s == 1000:
            j = Actor('diana')
            j.center=(400,400)
            
            for a in ad2list:
                ad2list.remove(a)
            for a in bd2list:
                bd2list.remove(a)
            for a in cd2list:
                cd2list.remove(a)
            for a in dd2list:
                dd2list.remove(a)
            for a in ed2list:
                ed2list.remove(a)
            for a in fd2list:
                fd2list.remove(a)
            for a in gd2list:
                gd2list.remove(a)
            
            
            if j.colliderect(hero):
                win()
                
                
                
        def on_key_down(key):
            newbullet =Actor('zidan')
            nwbullet =Actor('zidan')
            nebullet =Actor('zidan')
            aulist.append(nwbullet)
            bulist.append(newbullet)
            culist.append(nebullet)
            nwbullet.x = hero.x-20
            nwbullet.y = hero.y - 50
            nwbullet.angle=45
            newbullet.x = hero.x-1
            newbullet.y = hero.y - 50
            nebullet.x = hero.x+20
            nebullet.y = hero.y - 50
            nebullet.angle=-45

pgzrun.go()
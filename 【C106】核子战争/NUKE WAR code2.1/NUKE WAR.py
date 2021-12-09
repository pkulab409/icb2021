import pgzrun
import random

WIDTH=1280
HEIGHT=820
back=Actor('nukewar')
back.pos=480,400
musics=['m1','m2','m3','m4','m5','m6','m7','m8']
mu=random.choice(musics)

    
tank2=Actor('tank2')
tank2.pos=480,155
tank1=Actor('tank1')
tank1.pos=480,680
vault_boy1=Actor('standby')
vault_boy1.pos=660,635
vault_boy2=Actor('standby1')
vault_boy2.pos=320,200
load = Actor('pleasestandby')
load.pos=480,400
loading=Actor('load')
loading.pos=650,580
sounds.open.play()

v_a_t_s_2=Actor('vats')
v_a_t_s_2.pos=640,180
v_a_t_s_1=Actor('vats')
v_a_t_s_1.pos=320,655
#保存tank2发出的核弹和反导导弹
nukebomb2s=[]
bomb2s=[]
#保存tank1发出的核弹和反导导弹
nukebomb1s=[]
bomb1s=[]

STARTING=1
nuked1=1
nuked2=1

#计时变量
delaybomb2=1
delaybomb1=1
delaynukebomb2=1
delaynukebomb1=1

#V.A.T.S系统
delayvats2=1
delayvats1=1
ap2=3
ap1=3
v1=1
v2=1
#AP条
AP2=Actor('apt')
AP21=Actor('ap')
AP22=Actor('ap')
AP23=Actor('ap')
AP2.pos=300,120
AP21.pos=394,120
AP22.pos=362,120
AP23.pos=330,120

AP1=Actor('apt')
AP11=Actor('ap')
AP12=Actor('ap')
AP13=Actor('ap')
AP1.pos=560,710
AP11.pos=654,710
AP12.pos=622,710
AP13.pos=590,710


def draw():
    screen.clear()
    #screen.fill((0,0,0))
    screen.blit("pip",(-200,-10))
    #跳过剧情
    global STARTING
    if keyboard.B:
        STARTING=0
        sounds.open.stop()
    #画上两名玩家和AP值标签
    if STARTING==0:
        tank2.draw()
        tank1.draw()
        AP2.draw()
        AP1.draw()
    vault_boy1.draw()
    vault_boy2.draw()
    #画上背景
    back.draw()
    #back.draw()
    #画AP条
    
    if ap2>=3 and STARTING==0:
        AP21.draw()
    if ap2>=2 and STARTING==0:
        AP22.draw()
    if ap2>=1 and STARTING==0:
        AP23.draw()
    
    if ap1>=3 and STARTING==0:
        AP11.draw()
    if ap1>=2 and STARTING==0:
        AP12.draw()
    if ap1>=1 and STARTING==0:
        AP13.draw()
    #画上tank2的反导导弹和核导弹
    #画上tank1的反导导弹和核导弹
    for bomb2 in bomb2s:
        bomb2.draw()
    for nukebomb2 in nukebomb2s:
        nukebomb2.draw()
    for bomb1 in bomb1s:
        bomb1.draw()
    for nukebomb1 in nukebomb1s:
        nukebomb1.draw()
        
    if STARTING:
        load.draw()
        loading.draw()
    if v2==0.05:
        v_a_t_s_2.draw()
    if v1==0.05:
        v_a_t_s_1.draw()
#两辆坦克移动
def update():
    
    global v2
    global v1
    if STARTING:
        clock.schedule(clear_load_image, 55.0)
        music.play(mu)
    
    if keyboard.L and tank2.right<=700 and nuked2:
        tank2.right+=0.5*v1
    if keyboard.J and tank2.right>=300 and nuked2:
        tank2.right-=0.5*v1
    if keyboard.D and tank1.right<=700 and nuked1:
        tank1.right+=0.5*v2
    if keyboard.A and tank1.right>=300 and nuked1:
        tank1.right-=0.5*v2
#V.A.T.S
    global delayvats2
    global delayvats1
    global ap2
    global ap1

    if keyboard.U and ap2!=0 and delayvats2 and nuked2 and STARTING==0:
        v2=0.05
        clock.schedule(vats2,8.0)
        ap2=ap2-1
        sounds.vats.play()
        delayvats2=0
        clock.schedule(delay_vats2,1.0)
    if keyboard.Q and ap1!=0 and delayvats1 and nuked1 and STARTING==0:
        v1=0.05
        clock.schedule(vats1,8.0)
        ap1=ap1-1
        sounds.vats.play()
        delayvats1=0
        clock.schedule(delay_vats1,1.0)
#开火(首先是反导导弹，接着是和导弹)功能
    global delaybomb2
    global delaybomb1
    global delaynukebomb2
    global delaynukebomb1    
    if keyboard.I and delaybomb2 and nuked2 and STARTING==0:
        bomb2=Actor('bomb2')
        bomb2.center=(tank2.left),175
        bomb2s.append(bomb2)
        sounds.rocket.play()
        delaybomb2=0
        clock.schedule(delay_bomb2,0.8)
        
        
    if keyboard.K and delaynukebomb2 and nuked2 and STARTING==0:
        nukebomb2=Actor('nukebomb2')
        nukebomb2.center=(tank2.right-5),175
        nukebomb2s.append(nukebomb2)
        sounds.rocket.play()
        delaynukebomb2=0
        clock.schedule(delay_nukebomb2,1.6)
    if keyboard.W and delaybomb1 and nuked1 and STARTING==0:
        bomb1=Actor('bomb1')
        bomb1.center=(tank1.right-5),660
        bomb1s.append(bomb1)
        sounds.rocket.play()
        delaybomb1=0
        clock.schedule(delay_bomb1,0.8)
    if keyboard.S and delaynukebomb1 and nuked1 and STARTING==0:
        nukebomb1=Actor('nukebomb1')
        nukebomb1.center=(tank1.left),660
        nukebomb1s.append(nukebomb1)
        sounds.rocket.play()
        delaynukebomb1=0
        clock.schedule(delay_nukebomb1,1.6)
#导弹移动,核导弹到最后消失,如果核导弹达到最后则break
    for bomb2 in bomb2s:
        bomb2.y+=2*v1*v2
        if bomb2.y >= 700:
            bomb2s.remove(bomb2)
    for nukebomb2 in nukebomb2s:
        nukebomb2.y+=1*v1*v2
        for bomb1 in bomb1s:
            #到达底线，触发核爆
            
            # 碰到反导导弹，被摧毁
            if nukebomb2.colliderect(bomb1):
                if bomb1.y-2<nukebomb2.y<bomb1.y+2 and bomb1.y-2<nukebomb2.y<bomb1.y+2:
                    nukebomb2s.remove(nukebomb2)
                    bomb1s.remove(bomb1)
                    sounds.rocket.play()
        if nukebomb2.y >= 700:
                set_tank1_nuked()
                nukebomb2s.remove(nukebomb2)
                
            
    for bomb1 in bomb1s:
        bomb1.y-=2*v2*v1
        if bomb1.y <= 135:
            bomb1s.remove(bomb1)
    for nukebomb1 in nukebomb1s:
        nukebomb1.y-=1*v2*v1
        for bomb2 in bomb2s:
            if nukebomb1.colliderect(bomb2):
                if bomb2.y-2<nukebomb1.y<bomb2.y+2 and bomb2.y-2<nukebomb1.y<bomb2.y+2:
                    nukebomb1s.remove(nukebomb1)
                    bomb2s.remove(bomb2)
                    sounds.rocket.play()
        if nukebomb1.y <=135:
                set_tank2_nuked()
                nukebomb1s.remove(nukebomb1)
                
#gameover，并显示胜利者           
def set_tank1_nuked():
    tank1.pos=480,650
    tank1.image="mushroomcloud"
    sounds.bomb.play()
    vault_boy2.image='vault_boy'
    global nuked1
    nuked1=0
    
def set_tank2_nuked():
    tank2.pos=480,200
    tank2.image="mushroomcloud"
    sounds.bomb.play()
    vault_boy1.image='vault_boy'
    global nuked2
    nuked2=0
def clear_load_image():
    global STARTING
    STARTING = 0
#计时器
def delay_bomb2():
    global delaybomb2
    delaybomb2=1
def delay_bomb1():
    global delaybomb1
    delaybomb1=1
def delay_nukebomb2():
    global delaynukebomb2
    delaynukebomb2=1
def delay_nukebomb1():
    global delaynukebomb1
    delaynukebomb1=1
#vats和计时
def vats2():
    global v2
    v2=1
def vats1():
    global v1
    v1=1
def delay_vats2():
    global delayvats2
    delayvats2=1
def delay_vats1():
    global delayvats1
    delayvats1=1

pgzrun.go()
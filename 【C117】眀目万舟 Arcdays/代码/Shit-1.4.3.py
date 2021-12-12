import pgzrun
import random
import easygui as g

dia=250
start=0
guide=0
started=0
m=0
n=0
dac_time=0
opj_time=0
tsing_time=0

tsing=Actor("intro2",(780,270))
opj=Actor("intro1",(780,270))
dac=Actor("intro",(780,270))
starter=Actor("starter",(630,450))
guidance=Actor("guide",(150,450))
xiayige=Actor("next",(630,520))
back=Actor("back",(150,520))
guide1=Actor("1",(390,270))
guide2=Actor("2",(390,270))
guide3=Actor("3",(390,270))



#防御塔列于下方
pause=Actor("pause")
pause.pos=750,30
wall=Actor("wall0")
wall.pos=750,90
arrow=Actor("arrow0")
arrow.pos=750,150
mine=Actor("mine0")
mine.pos=750,210
mushroom=Actor('mushroom0')
mushroom.pos=750,270
laser_tower=Actor('laser0')
laser_tower.pos=750,330
destroy=Actor("destroy0")
destroy.pos=750,390
involve01=Actor('involve01')
involve02=Actor('involve02')
shot_speed={arrow:30, mushroom:50,laser_tower:60,'oj':45,'thu':60}
damage={arrow:5,mine:2,mushroom:3,laser_tower:3}
damage_range={arrow:150, mushroom:90,laser_tower:180}
arrowbs=[]
bubbles={}
bubbles_exist={}
lasers={}
lasers_exist={}
oj_skills={}
oj_skill_exist={}
thu_skill_exist={}

bullet_dict={}
time_shot=[]
time_shoot=[]
time_shooot=[]
oj_shot=[]
thu_shot=[]

#怪

mob01=Actor("mob01",pos=(30,330))
mob02=Actor("mob01",pos=(30,330))
mob03=Actor("mob01",pos=(30,330))
m1=Actor("mob01",pos=(30,330))
mob04=Actor("mob02",pos=(30,330))
mob05=Actor("mob01",pos=(30,330))
mob06=Actor("mob02",pos=(30,330))
mob07=Actor("mob03",pos=(30,330))
mob08=Actor("mob04",pos=(30,330))
mob09=Actor("mob03",pos=(30,330))
mob10=Actor("mob04",pos=(30,330))
mob11=Actor("mob05",pos=(30,330))
mob12=Actor("mob05",pos=(30,330))
mob13=Actor("mob06",pos=(30,330))
mob15=Actor("mob05",pos=(30,330))
mob14=Actor("mob03",pos=(30,330))
mob16=Actor("mob05",pos=(30,330))
mob17=Actor("mob03",pos=(30,330))
m2=Actor("mob03",pos=(30,330))
m2=Actor("mob03",pos=(30,330))
m3=Actor("mob03",pos=(30,330))
m4=Actor("mob03",pos=(30,330))
m5=Actor("mob03",pos=(30,330))
m6=Actor("mob03",pos=(30,330))
m7=Actor("mob07",pos=(30,330))
m8=Actor("mob08",pos=(30,330))
m9=Actor("mob07",pos=(30,330))
m10=Actor("mob02",pos=(30,330))
m11=Actor("mob02",pos=(30,330))
m12=Actor("mob02",pos=(30,330))
m13=Actor("mob01",pos=(30,330))
m14=Actor("mob01",pos=(30,330))
m15=Actor("mob01",pos=(30,330))
m16=Actor("mob01",pos=(30,330))
m17=Actor("mob01",pos=(30,330))
m18=Actor("mob01",pos=(30,330))
m19=Actor("mob01",pos=(30,330))
m20=Actor("mob01",pos=(30,330))
aircraft01=Actor('aircraft01',pos=(30,330))
aircraft02=Actor('aircraft01',pos=(30,330))
aircraft03=Actor('aircraft02',pos=(30,330))
aircraft04=Actor('aircraft01',pos=(30,330))
aircraft05=Actor('aircraft02',pos=(30,330))
aircraft06=Actor('aircraft02',pos=(30,330))
aircraft07=Actor('aircraft02',pos=(30,330))
aircraft08=Actor('aircraft02',pos=(30,330))
aircraft09=Actor('aircraft02',pos=(30,330))
aircraft10=Actor('aircraft02',pos=(30,330))
aircraft11=Actor('aircraft02',pos=(30,330))
aircraft12=Actor('aircraft02',pos=(30,330))
hiden01=Actor("hiden01",pos=(30,330))
hiden02=Actor("hiden01",pos=(30,330))
hiden03=Actor("hiden01",pos=(30,330))
hiden04=Actor("hiden01",pos=(30,330))
hiden05=Actor("hiden01",pos=(30,330))
hiden06=Actor("hiden01",pos=(30,330))
hiden07=Actor("hiden01",pos=(30,330))
hiden08=Actor("hiden01",pos=(30,330))
hiden09=Actor("hiden01",pos=(30,330))
hiden10=Actor("hiden01",pos=(30,330))
hiden11=Actor("hiden01",pos=(30,330))
hiden12=Actor("hiden01",pos=(30,330))
oj01=Actor('oj01',pos=(30,330))
ojO=Actor('o',pos=(30,330))
ojp=Actor('p',pos=(30,330))
oje=Actor('e',pos=(30,330))
ojj=Actor('j',pos=(30,330))
oju=Actor('u',pos=(30,330))
ojn=Actor('n',pos=(30,330))
oju=Actor('u',pos=(30,330))
ojd=Actor('d',pos=(30,330))
ojg=Actor('g',pos=(30,330))
oje_=Actor('e',pos=(30,330))
wa=Actor('wa')
ce=Actor('ce')
tle=Actor('tle')
re=Actor('re')
pe=Actor('pe')
thu=Actor('thu',pos=(30,330))

mob_can_fly=[aircraft02,aircraft01,aircraft04,aircraft03,aircraft05,aircraft06,aircraft07,aircraft08,aircraft09,aircraft10,aircraft11,aircraft12,]
mob_can_hide=[hiden01,hiden02,hiden03,hiden04,hiden05,hiden06,hiden07,hiden08,hiden09,hiden10,hiden11,hiden12]
mob_can_recover={mob01:0.02,mob03:0.02,mob14:0.05,mob17:0.05,m12:0.1,m10:0.1,mob13:0.114}
ojs=[oj01]


mob_speed={
mob01:30,mob02:30,mob03:30,m1:30,
mob04:15,mob05:60,mob06:15,
mob07:60,mob08:30,mob09:60,mob10:30,
mob11:30,mob12:30,mob14:30,mob15:30,mob16:30,mob17:30,
mob13:15,oj01:30,
m2:60,m3:60,m4:60,m5:60,m6:60,
m7:60,m8:30,m9:60,
m10:15,m11:15,m12:15,
m13:60,
ojO:30,ojp:30,oje:30,ojn:30,ojj:30,oju:30,ojd:30,ojg:30,oje_:30,
m14:15,m15:30,m16:60,m17:30,m18:15,m19:30,m20:60,
thu:30
}



mob_hp={
mob01:10,mob02:20,mob03:10,m1:20,
mob04:100,mob05:30,mob06:100,aircraft01:15,aircraft03:15,
mob07:45,mob08:120,mob09:45,mob10:120,aircraft02:30,aircraft05:30,aircraft06:30,
mob11:150,mob12:200,mob14:100,hiden02:30,mob15:125,mob16:150,mob17:100,aircraft04:35,
mob13:1500,
m2:75,hiden03:60,m3:100,m4:75,m5:100,m6:100,hiden01:60,
m7:500,m8:1200,m9:500,aircraft07:114,aircraft08:114,aircraft09:114,aircraft10:114,
m10:1145,m11:2500,m12:1145,
aircraft11:114,aircraft12:114,m13:500,
hiden04:150,hiden05:150,hiden06:150,
hiden07:120,hiden08:160,hiden09:160,hiden10:120,hiden11:200,hiden12:200,
oj01:444,ojO:1200,ojp:1200,oje:777,ojn:514,ojj:514,oju:777,ojd:1200,ojg:1200,oje_:1200,
m14:3000,m15:2000,m16:1000,m17:2000,m18:3000,m19:2000,m20:1000,
thu:1911
}




mob_to_spawn=[
[mob01,mob02,mob03,m1],
[aircraft03,mob04,mob05,mob06,aircraft01],
[aircraft05,mob07,mob08,aircraft06,mob09,mob10,aircraft02],
[mob14,mob15,mob11,aircraft04,mob12,mob16,hiden02,mob17],
[mob13],
[m2,hiden03,m3,m4,m5,m6,hiden01],
[aircraft07,m7,aircraft09,m8,aircraft08,m9,aircraft10],
[hiden04,m10,hiden05,m11,hiden06,m12],
[hiden07,aircraft11,hiden08,m13,hiden09,aircraft12,hiden10],
[oje_,ojg,ojd,oju,ojj,oj01,ojn,oje,ojp,ojO],
[m14,m15,m16,hiden11,m17,hiden12,m18,m19,m20],
[thu]
]







mob_on_field=[]



#基本参数
lives=3

TITLE="114514"
WIDTH = 780
HEIGHT =540
selected=0
doll=0



#墙
ts=60#60像素是一格
tiles = ['empty', 'wall', 'start',"end", "arrow", "mine",'mushroom','laser','involve01','involve02']#所有方块
maze = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 3],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
]
#初始地图



#route
r=[]
dulu=0



#计帧器
timer=0
time_birth={}




#波数
wave=0
add=1
clock=0
wave_time=[1200]

next_wave=0
#________________________________________________________________________________________________________________________________________

#一秒会画60次
guide=0
def draw():
    global dulu
    global maze
    global start
    global guide
    screen.clear()
    if not start and not guide:
        screen.blit("main", (0, 0))
        starter.pos=(630,450)
        starter.draw()
        guidance.draw()
    elif guide==1 and not start:
        starter.pos=(390,520)
        guide1.draw()
        starter.draw()
        xiayige.draw()
        back.draw()
    elif guide==2 and not start:
        starter.pos=(390,520)
        guide2.draw()
        starter.draw()
        xiayige.draw()
        back.draw()
    elif guide==3 and not start:
        starter.pos=(390,520)
        guide3.draw()
        starter.draw()
        back.draw()
    else:
        screen.fill((255,255,255))
        screen.blit("bg", (0, 0))
        wall.draw()
        arrow.draw()
        mine.draw()
        mushroom.draw()
        destroy.draw()
        pause.draw()
        laser_tower.draw()
        involve01.draw()
        involve02.draw()
        for row in range(len(maze)):
            for column in range(len(maze[row])):
                x = column * ts
                y = row * ts
                tile = tiles[maze[row][column]]
                screen.blit(tile,(x, y))
        screen.draw.text("Live:"+str(lives)+"            "+"Diamond:"+str(dia)+"            "+"Time:"+str(timer//60)+"            "+"Wave:"+str(wave),bottomleft=(0,540),color=(0,0,0))
        for mob in mob_on_field:
            if mob in mob_can_hide:
                if maze[int(mob.y//60)][int(mob.x//60)]%6==0:
                    mob.image="hiden01"
                    mob.draw()
                    screen.draw.text(str(int(mob_hp[mob]//1)),bottomleft=(mob.x-20,mob.y),color=(255,0,0))
                else:
                    mob.image="hiden01_hide"
                    mob.draw()
                    screen.draw.text(str(int(mob_hp[mob]//1)),bottomleft=(mob.x-20,mob.y),color=(255,0,0))
            else:
                mob.draw()
                screen.draw.text(str(int(mob_hp[mob]//1)),bottomleft=(mob.x-20,mob.y),color=(255,0,0))
        if bullet_dict:
            for bullet,pos in bullet_dict.items():
                bullet.draw()
                bullet.x-=(bullet.x-pos[0][0])//20
                bullet.y-=(bullet.y-pos[0][1])//20
        if bubbles:
            for bubble in bubbles.keys():
                bubble.draw()
        if bubbles_exist:
            for bubble in bubbles_exist.keys():
                bubble.draw()
        if lasers:
            for laser in lasers.keys():
                laser.draw()
        if lasers_exist:
            for laser in lasers_exist.keys():
                laser.draw()
        if oj_skills:
            for skill in oj_skills.keys():
                skill.draw()
        if oj_skill_exist:
            for skill in oj_skill_exist.keys():
                skill.draw()
        if thu_skill_exist:
            for skr in thu_skill_exist.keys():
                skr.draw()
    if wave==5 and dac_time<240:
        dac.draw()
        if dac_time<65:
            dac.x-=6
        if dac_time>175:
            dac.x+=6
    if wave==10 and opj_time<240:
        opj.draw()
        if opj_time<65:
            opj.x-=6
        if opj_time>175:
            opj.x+=6
    if wave==12 and tsing_time<240:
        tsing.draw()
        if tsing_time<65:
            tsing.x-=6
        if tsing_time>175:
            tsing.x+=6

def on_key_up():
    global doll
    global dia
    global timer
    if keyboard[keys.UP] and timer%15==0:
        doll+=1
        if doll>12:
            dia+=10000
            doll=0

def bullet_remove():
    global timer
    b__d=bullet_dict.copy()
    if b__d:
        for bullet,pos in b__d.items():
            if timer>=pos[2]+90:
                del bullet_dict[bullet]

#点击事件
def on_mouse_down(pos):
    global next_wave
    global dulu
    global start
    global guide
    global started
    if starter.collidepoint(pos):
        start=1
    elif guidance.collidepoint(pos):
        guide+=1
    elif xiayige.collidepoint(pos):
        guide+=1
    elif back.collidepoint(pos):
        guide-=1
    elif wave_or_not():
        row = int(pos[1] / ts)
        column = int(pos[0] / ts)
        global selected
        global dia
        global r
        if pause.collidepoint(pos):
            next_wave=g.ccbox(msg="暂停(｀・ω・´)",choices=("直接下一波！！！！","继续"))
        if selected==0 and wall.collidepoint(pos):
            wall.image="wall1"
            selected=1
        elif selected==1 and wall.collidepoint(pos):
            wall.image="wall0"
            selected=0
        elif selected==1 and column!=12 and dia>=15:
            if maze[row][column]==0:
                maze[row][column]=1
                wall.image="wall0"
                search(maze)
                selected=0
                if dulu==1:
                    maze[row][column]=0
                    g.msgbox("不要堵路！(╯‵□′)╯︵┻━┻")
                else:
                    dia-=15
        elif selected==0 and arrow.collidepoint(pos):
            arrow.image="arrow1"
            selected=2
        elif selected==2 and arrow.collidepoint(pos):
            arrow.image="arrow0"
            selected=0
        elif selected==2 and column!=12 and dia>=200:
            if maze[row][column]==0:
                maze[row][column]=4
                arrow.image="arrow0"
                selected=0
                search(maze)
                if dulu==1:
                    maze[row][column]=0
                    g.msgbox("不要堵路！(╯‵□′)╯︵┻━┻")
                else:
                    dia-=200
        elif selected==0 and mine.collidepoint(pos):
            mine.image="mine1"
            selected=4
        elif selected==4 and mine.collidepoint(pos):
            mine.image="mine0"
            selected=0
        elif selected==4 and column!=12 and dia>=40:
            if maze[row][column]==0:
                maze[row][column]=5
                mine.image="mine0"
                selected=0
                dia-=40
        elif selected==0 and mushroom.collidepoint(pos):
            mushroom.image="mushroom1"
            selected=5
        elif selected==5 and mushroom.collidepoint(pos):
            mushroom.image="mushroom0"
            selected=0
        elif selected==5 and column!=12 and dia>=200:
            if maze[row][column]==0:
                maze[row][column]=6
                mushroom.image="mushroom0"
                search(maze)
                selected=0
                if dulu==1:
                    maze[row][column]=0
                    g.msgbox("不要堵路！(╯‵□′)╯︵┻━┻")
                else:
                    dia-=200
        elif selected==0 and destroy.collidepoint(pos):
            destroy.image="destroy1"
            selected=3
        elif selected==3 and destroy.collidepoint(pos):
            destroy.image="destroy0"
            selected=0
        elif selected==3 and column!=12 and dia>=0:
            if maze[row][column]!=0:
                maze[row][column]=0
                destroy.image="destroy0"
                selected=0
                dia+=5
        elif selected==0 and laser_tower.collidepoint(pos):
            laser_tower.image="laser1"
            selected=6
        elif selected==6 and laser_tower.collidepoint(pos):
            laser_tower.image="laser0"
            selected=0
        elif selected==6 and column!=12 and dia>=200:
            if maze[row][column]==0:
                maze[row][column]=7
                laser_tower.image="laser0"
                search(maze)
                selected=0
                if dulu==1:
                    maze[row][column]=0
                    g.msgbox("不要堵路！(╯‵□′)╯︵┻━┻")
                else:
                    dia-=200
        print(r)

#判断回合是否结束，但好像问题很大
#12/3 修复完成：花了一下午，删一行代码就解决了bug，这………………
#12/6 修复完成
def wave_or_not():
    global timer
    global wave
    global mob_on_field
    global add
    global clock
    global dia
    global next_wave
    if wave==0 and not mob_on_field and clock<=1200 and not next_wave:
        clock+=1
        if add:
            add-=1
        return 1
    elif wave>0 and not mob_to_spawn[wave-1] and not mob_on_field and clock<=1500 and not next_wave:
        if add:
            add-=1
        return 1
    elif not dulu:
        if not add:
            wave+=1
            g.msgbox("第%d波要开始了！[○･｀Д´･ ○]" % wave)
            next_wave=0
            add+=1
            dia=int(dia*1.05//1)
        clock=0
        return 0




#每帧任务
def update():
    global timer
    global r
    global dac_time
    global tsing_time
    global opj_time
    if start:
        timer+=1
        r=search(maze)
        pos_mob()
        mob_hurt()
        on_key_up()
        lives_minus()
        game_end()
        mob_spawn()
        mob_die()
        oj_skill()
        oj_skill_work()
        thu_skill()
        thu_skill_work()
        arrow_shot()
        mushroom_shot()
        bullet_remove()
        laser_shot()
        hiden_move()
        mob_recover()
        if wave==5:
            dac_time+=1
        if wave==10:
            opj_time+=1
        if wave==12:
            tsing_time+=1


def mob_spawn():
    global timer
    global time_birth
    global wave
    if not wave_or_not():
        for i in range(len(mob_to_spawn[wave-1])):
            if not time_birth or timer>=150+max(time_birth.values()):
                #150是生成间隔
                time_birth[mob_to_spawn[wave-1][0]]=timer
                mob_on_field.append(mob_to_spawn[wave-1][0])
                mob_to_spawn[wave-1].pop(0)


def lives_minus():
    global lives
    for mob in mob_on_field:
        if mob.collidepoint((690,210)):
            lives-=1


def mob_die():
    global dia
    for mob in reversed(mob_on_field):
        if mob_hp[mob]<=0 :
            if wave%5==1 or wave%5==3:
                dia+=60+random.randint(-10,50)
            elif wave%5==2 or wave%5==4:
                dia+=100+random.randint(-15,10)
            elif wave==5:
                dia+=1145+random.randint(-1,4)
            elif wave==10:
                dia+=100+random.randint(-15,10)
            del time_birth[mob]
            mob_on_field.remove(mob)
        if mob.collidepoint((690,210)):
            del time_birth[mob]
            mob_on_field.remove(mob)


#怪物前进，但是支持的速度仅限于60,30,20,15etc………………………………我也不知道怎么改
def pos_mob():
    global timer
    global r
    global time_birth
    for mob in mob_on_field:
        if mob not in mob_can_fly and mob not in mob_can_hide:
            index=mob_on_field.index(mob)
            steptime=3600//mob_speed[mob]
            step=(timer-time_birth[mob])//steptime
            if step<len(r) and r[step+1][1]-r[step][1]==0 and r[step+1][0]-r[step][0]==1 and timer%(steptime//60)==0:
                mob_on_field[index].y+=1
            if step<len(r) and r[step+1][1]-r[step][1]==0 and r[step+1][0]-r[step][0]==-1 and timer%(steptime//60)==0:
                mob_on_field[index].y-=1
            if step<len(r) and r[step+1][1]-r[step][1]==1 and r[step+1][0]-r[step][0]==0 and timer%(steptime//60)==0:
                mob_on_field[index].x+=1
            if step<len(r) and r[step+1][1]-r[step][1]==-1 and r[step+1][0]-r[step][0]==0 and timer%(steptime//60)==0:
                mob_on_field[index].x-=1
        elif mob in mob_can_hide:
            hiden_move()
        else:
            aircraft_move()






 #飞行单位
def aircraft_move():
    global timer
    for aircraft in mob_can_fly:
        if aircraft in mob_on_field:
            if timer%6==0 or timer%6==1 or timer%6==2 or timer%6==4:
                aircraft.x+=2
            elif timer%6==5:
                aircraft.x+=1
            elif timer%6==3:
                aircraft.y-=2


#boss单位：oj，拥有wa、ce、tle、re多种技能
def oj_skill():
    global wa
    global ce
    global tle
    global re
    global pe
    global lives
    global timer
    global n
    global m
    for oj in ojs:
        if oj in mob_on_field:
            if not oj_shot or timer>=shot_speed['oj']+oj_shot[-1]:
                a=random.choice([wa,ce,tle,re,pe])
                a.pos=oj.x,oj.y
                oj_skills[a]=[0]
                oj_skill_exist[a]=[timer]
                oj_shot.append(timer)
        else:
            n=0
            m=0


def oj_skill_work():
    global n
    global m
    global lives
    for mob in mob_on_field:
        for oj in ojs:
            for i in oj_skills.keys():
                if mob.colliderect(wa) and i==wa:
                    mob_hp[mob]+=10
                elif mob.colliderect(ce) and i==ce:
                    mob_hp[mob]+=9
                elif mob.colliderect(tle) and i==tle:
                    mob_hp[oj]+=int(2*m)
                    m+=1
                elif mob.colliderect(re) and i==re:
                    lives-=int(n/30)
                    n+=1
                elif mob.colliderect(pe) and i==pe:
                    mob_hp[mob]=int(mob_hp[mob]*1.02)
    if oj_skills or oj_skill_exist:
        oj_skills.clear()
        o_se=oj_skill_exist.copy()
        for i,j in o_se.items():
            if timer>=j[0]+20:
                del oj_skill_exist[i]

#boss单位：thu,大卷怪
def thu_skill():
    global timer
    if thu in mob_on_field:
        if not thu_shot or timer>=shot_speed['thu']+thu_shot[-1]:
            i=random.randint(-2,2)
            j=random.randint(-1,1)
            x=int(thu.x/60)
            y=int(thu.y/60)
            if x+i>=0 and x+i<=11:
                x+=i
            if y+j>=0 and y+j<=7:
                y+=j
            black_hole=Actor('black_hole',pos=(x*60+30, y*60+30))
            if x*60+30==30 and y*60+30==330:
                pass
            elif x*60+30==690 and y*60+30==210:
                pass
            else:
                if maze[y][x]==0 or maze[y][x]==5 or maze[y][x]==8:
                    maze[y][x]=8
                else:
                    maze[y][x]=9
                thu_skill_exist[black_hole]=[timer]
                thu_shot.append(timer)


def thu_skill_work():
    global timer
    ts_e=thu_skill_exist.copy()
    for i,j in ts_e.items():
        if timer-25>=j[0]:
            del thu_skill_exist[i]


def hiden_move():
    global timer
    if timer%2==0:
        for hiden in mob_can_hide:
            if hiden in mob_on_field:
                if 690>hiden.x>=30 and hiden.x%120!=30:
                    hiden.x+=1
                elif hiden.x==690 and hiden.y<=210:
                    hiden.y+=1
                elif hiden.x==690 and hiden.y>=210:
                    hiden.y-=1
                elif 690>hiden.x>=30 and hiden.x%120==30:
                    x=random.randint(0,7)
                    hiden.y=x*60+30
                    hiden.x+=1

def mob_recover():
    for mob in mob_on_field:
        if mob in mob_can_recover:
            mob_hp[mob]+=mob_can_recover[mob]

def mob_hurt():
    global mob_hp
    global timer
    b_d=bullet_dict.copy()
    bub=bubbles.copy()
    bub_exist=bubbles_exist.copy()
    las=lasers.copy()
    las_exist=lasers_exist.copy()
    for bullet,pos in b_d.items():
        for mob in mob_on_field:
            if mob.colliderect(bullet):
                if pos[1]=="arrow":
                    mob_hp[mob]-=damage[arrow]+random.randint(0,3)
                if bullet in bullet_dict:
                    del bullet_dict[bullet]
    for bubble in bub.keys():
        for mob in mob_on_field:
            if mob.colliderect(bubble):
                mob_hp[mob]-=damage[mushroom]+random.randint(0,2)
                if bubble in bubbles:
                    del bubbles[bubble]
    for bubble,time in bub_exist.items():
        if timer-time[0]>=30:
            if bubble in bubbles_exist:
                del bubbles_exist[bubble]
    for laser in las.keys():
        for mob in mob_on_field:
            if mob.colliderect(laser):
                mob_hp[mob]-=damage[laser_tower]+random.randint(0,2)
                if laser in lasers:
                    del lasers[laser]
    for laser,time in las_exist.items():
        if timer-time[0]>=30:
            if laser in lasers_exist:
                del lasers_exist[laser]
    for mob in mob_on_field:
        if maze[int(mob.y//60)][int(mob.x//60)]==5 and timer%30==0:
            mob_hp[mob]-=damage[mine]+random.randint(-1,1)


def true_(list):
    for i in list:
        if i:
            return False
    return True



def game_end():
    if lives<=0:
        g.msgbox("哼哼哼啊啊啊啊啊啊,生命耗尽，重新开始吧o(╥﹏╥)o")
        exit()
    elif true_(mob_to_spawn) and len(mob_on_field)==0:
        g.msgbox("压力马斯内(赞赏)!恭喜你，挺过了最后一关！(*^▽^*)")
        exit()


#让箭射出来的函数，但是不能运行
def arrow_shot():
    global timer
    global shot_speed
    global bullet_dict
    global time_shot
    position_mob={}
    end_distance=[[],[]]
    arrow_determine=[]
    if not time_shot or timer>=shot_speed[arrow]+time_shot[-1]:#定义射速
        for hang in range(len(maze)):
            for lie in range(len(maze[hang])):
                if maze[hang][lie]==4 and mob_on_field:
                    for mob in mob_on_field:
                        dis=((mob.x-(lie*60+30))**2+(mob.y-(hang*60+30))**2)**0.5
                        if dis<=damage_range[arrow]:
                            position_mob[mob]=[mob.x,mob.y]
                if position_mob:
                    for j,m in position_mob.items():
                        distance=((m[0]-640)**2+(m[1]-300)**2)**0.5
                        end_distance[1].append(distance)
                        end_distance[0].append(m)
                if end_distance[0]:
                    iidx=end_distance[1].index(min(end_distance[1]))
                    arrow_determine=end_distance[0][iidx]
                    bullet_dict[Actor("arrowb", pos=(lie*60+30, hang*60+30))]=[arrow_determine,"arrow",timer]
                    time_shot.append(timer)
                position_mob={}
                end_distance=[[],[]]




#第二种塔：大喷菇
def mushroom_shot():
    global timer
    global shot_speed
    global bullet_dict
    global time_shoot
    global bubbles
    if not time_shoot or timer>=shot_speed[mushroom]+time_shoot[-1]:#定义射速
        for hang in range(len(maze)):
            for lie in range(len(maze[hang])):
               if maze[hang][lie]==6 and mob_on_field:
                    for mob in mob_on_field:
                        dis=((mob.x-(lie*60+30))**2+(mob.y-(hang*60+30))**2)**0.5
                        if dis<=damage_range[mushroom]:
                            bubble=Actor("bubble", pos=(lie*60+30, hang*60+30))
                            bubbles[bubble]=[[hang,lie]]
                            bubbles_exist[bubble]=[timer]
                            time_shoot.append(timer)


#第三种塔，激光塔
def laser_shot():
    global timer
    global shot_speed
    global bullet_dict
    global time_shooot
    position_mob={}
    end_distance=[[],[]]
    laser_determine=[]
    if not time_shooot or timer>=shot_speed[laser_tower]+time_shooot[-1]:#定义射速
        for hang in range(len(maze)):
            for lie in range(len(maze[hang])):
                if maze[hang][lie]==7 and mob_on_field:
                    for mob in mob_on_field:
                        dis=((mob.x-(lie*60+30))**2+(mob.y-(hang*60+30))**2)**0.5
                        if dis<=damage_range[laser_tower]:
                            position_mob[mob]=[mob.x,mob.y]
                if position_mob:
                    for j,m in position_mob.items():
                        distance=((m[0]-640)**2+(m[1]-300)**2)**0.5
                        end_distance[1].append(distance)
                        end_distance[0].append(m)
                if end_distance[0]:
                    iidx=end_distance[1].index(min(end_distance[1]))
                    laser_determine=end_distance[0][iidx]
                    laserr=Actor('laserb',center=(lie*60+30, hang*60))
                    laserr.angle=laserr.angle_to((laser_determine[0],laser_determine[1]))
                    lasers[laserr]=[[hang,lie]]
                    lasers_exist[laserr]=[timer]
                    time_shooot.append(timer)
                position_mob={}
                end_distance=[[],[]]

#自动寻路，输出是一个坐标的列表，应该没有问题
def search(maze):
    global dulu
    rlist=[(5,0)]#判断重复
    mdsb = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 233],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]
    #寻路基本地图
    route=[(3,11)]
    alpha=0
    endhang=3
    endlie=11
    for step in range(96):
        for hang in range(len(maze)):
            for lie in range(len(maze[hang])):
                if mdsb[hang][lie]==step:
                    rlist.append((hang,lie))
                    if hang!=7 and (maze[hang+1][lie]==0 or maze[hang+1][lie]==5 or maze[hang+1][lie]==8)and (hang+1,lie) not in rlist:
                        mdsb[hang+1][lie]=step+1
                    elif hang!=7 and maze[hang+1][lie]==3 and (hang+1,lie) not in rlist:
                        mdsb[hang+1][lie]=step+1
                        alpha=step+1
                    if hang!=0 and (maze[hang-1][lie]==0 or maze[hang-1][lie]==5 or maze[hang-1][lie]==8) and (hang-1,lie) not in rlist:
                        mdsb[hang-1][lie]=step+1
                    elif hang!=0 and maze[hang-1][lie]==3 and (hang-1,lie) not in rlist:
                        mdsb[hang-1][lie]=step+1
                        alpha=step+1
                    if lie!=11 and (maze[hang][lie+1]==0 or maze[hang][lie+1]==5 or maze[hang][lie+1]==8) and (hang,lie+1) not in rlist:
                        mdsb[hang][lie+1]=step+1
                    elif lie!=11 and maze[hang][lie+1]==3 and (hang,lie+1) not in rlist:
                        mdsb[hang][lie+1]=step+1
                        alpha=step+1
                    if lie!=0 and (maze[hang][lie-1]==0 or maze[hang][lie-1]==5 or maze[hang][lie-1]==8) and (hang,lie-1) not in rlist:
                        mdsb[hang][lie-1]=step+1
                    elif lie!=0 and maze[hang][lie-1]==3 and (hang,lie-1) not in rlist:
                        mdsb[hang][lie-1]=step+1
                        alpha=step+1
    #绘制寻路基本地图
    alpha=mdsb[3][11]
    if alpha!=233:
        for stp in range(alpha):
            if endhang!=7 and mdsb[endhang+1][endlie]==alpha-stp-1:
                endhang=endhang+1
                route.append((endhang,endlie))
                continue
            elif endhang!=0 and mdsb[endhang-1][endlie]==alpha-stp-1:
                endhang=endhang-1
                route.append((endhang,endlie))
                continue
            elif endlie!=0 and mdsb[endhang][endlie-1]==alpha-stp-1:
                endlie=endlie-1
                route.append((endhang,endlie))
                continue
            elif endlie!=11 and mdsb[endhang][endlie+1]==alpha-stp-1:
                endlie=endlie+1
                route.append((endhang,endlie))
                continue
        route.reverse()
        dulu=0
        #书写路线
    else:
        dulu=1
    return(route)

#运行
pgzrun.go()

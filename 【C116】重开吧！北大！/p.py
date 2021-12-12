import pgzrun as p
import random
start_game = True
h = 0 
WIDTH = 1500
HEIGHT = 800

#陈老师
adict  = {}
names1= ['hair','25','55','30','37','40','45','59','61','77','79','84','87','89','93','98','99','100','xiaohei']
   #陈斌的头发列表  normal不使用只是为了从1 开始更为直观
lhair  = ['normal','with hair 1','with hair 2','with hair 3','with hair 4','with hair 5','with hair 6','with hair 7','with hair 8']

#波吉
bdict = {}
names2 = ['1.70','1.00','2.31','2.83','3.81','4.00','100.00','4.50','5.00','10.00']

things = []

#开始游戏界面的人物加载
welcome = Actor('welcome')
welcome.center = 700,500

#开始选择
chooseing_game = False
choosechen = Actor('choosechen')
choosechen.center = 400,500
chooseboji = Actor('chooseboji')
chooseboji.center = 1000,500 
chosen_chen = False
chosen_boji = False
lai = Actor('lai')
lai.center = 700,650
start_chen = False
start_boji = False
xuankeing = False
xuankewang = Actor('xuankewang')
kankan = Actor('kankan')
kankan.center = 500,100
choose  = Actor('choose')
choose.center = 400,600
not_choose = Actor('not_choose')
not_choose.center = 1000,600
rulereading = False
bixiu = False
haoba = Actor('haoba')
haoba.center = 1200,700
ruleboji = Actor('ruleboji')
laiba = Actor('laiba')
laiba.center = 200,560
start_boji = False

#玩家角色
boji = Actor('boji_normal')
boji.score = 3
boji.y = 700
chen = Actor('normal')
chen.center = 100,800
chen.score = 2

#死亡
death_chen = False
death_boji = False
chen_again = Actor('chen_again')
chen_again.center = 400,500
boji_again = Actor('boji_again')
boji_again.center = 800,500
finish = Actor('finish')
finish.center = 700,700

def draw():
    global start_game,chooseing_game,chosen_boji,start_boji,rulereading,bixiu,chosen_chen,h
    if start_game:
        screen.clear()
        screen.blit('welcome2',(0,0))
        welcome.draw()
    elif  chooseing_game:
        screen.clear()
        screen.blit('welcome2',(0,0))
        choosechen.draw()
        chooseboji.draw()
    elif chosen_chen:
        screen.clear()
        screen.blit('rulechen',(0,0))
        lai.draw()
    elif start_chen:
        screen.clear()
        screen.blit('backing2',(0,0))#陈斌背景
        screen.draw.text("live=:%d"%chen.score,(600,15))
        #sounds.shangkeling.play()#上课铃播放
        for t in things: 
            t.draw()
            chen.draw()
    elif death_chen:
        screen.clear()
        screen.blit('chen_death',(0,0))
        chen_again.draw()
        boji_again.draw()
        finish.draw()
    elif chosen_boji :
        screen.clear()
        screen.blit('xuankewang',(0,0))
        kankan.draw()
    elif xuankeing:
        screen.clear()
        screen.blit('xuanke',(0,0))
        choose.draw()
        not_choose.draw()
    elif bixiu:
        screen.clear()
        screen.blit('bixiuke',(0,0))
        haoba.draw()
    elif rulereading:
        screen.clear()
        screen.blit('ruleboji',(0,0))
        laiba.draw()
    elif start_boji:
        #学生接绩点 
        screen.clear()
        screen.blit('backing1',(0,0))#接绩点背景
        #sounds.boji.play()#播放波吉的声音
        screen.draw.text("GPA:""{:.2f}".format(boji.score),(600,15) )
        for t in things:
            t.draw()
            boji.draw()
    elif death_boji:
        screen.clear()
        screen.blit('boji_death',(0,0))
        chen_again.draw()
        boji_again.draw()
        finish.draw()

def update():
    global start_chen,h,death_chen
    if start_boji == True:
        if random.randrange(60) in [0,1]:
            e = random.choice(names2)
            t = Actor(e)
            bdict[t] = e
            t.center = random.randrange(1500),0
            things.append(t)
        for t in things :
            t.y  += 4
            if t.y >= 909:
                things.remove(t)
            elif  t.colliderect(boji):
                things.remove(t)
                if float(bdict[t])>4 or float(bdict[t])<1:
                    death()
                if float(bdict[t]) > boji.score:
                    set_boji_happy()
                if float(bdict[t])< boji.score:
                    set_boji_sad()
                boji.score = float(bdict[t])
    elif start_chen :
        if random.randrange(60) in[1,2,3] :
            e = random.choice(names1)
            t = Actor(e)
            adict[t] = e
            t.center = random.randrange(1500),0
            things.append(t)
        for t in things :
            if  h >=4:
                t.y  +=5
            else:
                t.y +=4
            if t.y >= 909:
                if adict[t] not in  ['xiaohei','hair']:
                    if float(adict[t])<= 59:
                        chen.score -= 1 
                        set_chen_sad()
                things.remove(t) 
            elif t.colliderect(chen):
                things.remove(t)
                if adict[t] == 'hair':
                    h = h+1
                    set_chen_morehair()
                elif adict[t] == 'xiaohei':
                    chen.score += 1
                elif float(adict[t]) < 60  :
                    sounds.chenhappy.play()#谢谢老师
        if chen.score <=0:
            death() 

#鼠标坐标
def on_mouse_move(pos):
    boji.x = pos[0]
    chen.x = pos[0]

#一些人物换脸函数
      #陈斌老师换脸
def set_chen_sad():
    global h
    chen.image = 'normal'
    sounds.aaaa.play()#痛失头发陈老师啊啊啊啊
    h = 1#头发归零
def set_chen_morehair():
    global h 
    if h >=9:
        sounds.enough.play()#陈斌老师：够了够了
    if h < 9 :
       chen.image = lhair[h]
       sounds.laughing.play()#陈斌老师的笑声
def set_boji_happy():
    boji.image = 'boji_happy'
    sounds.bojihappy.play()
    clock.schedule_unique(set_boji_normal,0.5)
def set_boji_sad():
    boji.image = 'boji_sad'
    sounds.bojisad.play()
    clock.schedule_unique(set_boji_normal,0.5)
def set_boji_normal():
    boji.image = 'boji_normal'
def on_mouse_down(pos):
    global start_game,chooseing_game,chosen_boji,start_boji,bdict,things,death_boji,xuankeing,rulereading,bixiu,chosen_chen,start_chen,death_chen,h,adict
    if welcome.collidepoint(pos):#开始界面
        start_game = False 
        chooseing_game = True
    if chooseboji.collidepoint(pos):#选择陈老师
        chooseing_game = False
        chosen_boji = True
    if choosechen.collidepoint(pos):#选择陈老师
        chooseing_game = False
        chosen_chen = True
    if kankan.collidepoint(pos):
        chosen_boji = False
        xuankeing = True
    if choose.collidepoint(pos):
        xuankeing = False
        rulereading = True
    if not_choose.collidepoint(pos):
        xuankeing = False
        bixiu = True
    if haoba.collidepoint(pos):
        bixiu = False
        rulereading = True
    if  laiba.collidepoint(pos):
        rulereading = False
        start_boji = True
    if finish.collidepoint(pos):
        quit()
    if boji_again.collidepoint(pos):
        death_boji = False
        boji.score = 2
        bdict = {}
        things = []
        chosen_boji = True
    if lai.collidepoint(pos):#游戏规则
        chosen_chen = False
        start_chen = True#开始陈老师的游戏
    if chen_again.collidepoint(pos):
        death_chen = False
        h = 0 
        chen.score = 2
        adict = {}
        things = []
        chosen_chen=   True

def death():
    global death_chen,start_chen,death_boji,start_boji
    if start_chen:
        start_chen = False
        death_chen = True
    if start_boji:
        start_boji = False
        death_boji = True
           
    
p.go()    

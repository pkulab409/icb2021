import pgzrun
import math
import random 
pi = 3.1415926536
b_event = False
b_show = False
begin = False
cnum = 0
m =[]
num = 0
s1 = '''请节约意愿点！
每次都会消耗9点
当意愿点为0时游戏结束'''
#必要模块的引入，必要参数的设定
buttom = Actor("start")
buttom.pos = 375,800
re_buttom = Actor("restart")
re_buttom.pos = 375,800
TITLE = "P大课工"
WIDTH = 750
HEIGHT = 990 # 设定界面大小和标题
gouzi = Actor("claw")
gouzi.fadong = False
gouzi.get = 0
gouzi.pos = 375,170
gouzi.willpoints = 99
gouzi.credit = 0
gouzi.GPA = 0 # 钩子的参数设定，fadong表示是否发动，get表示是否与课碰撞或到达边界
topevent = random.randint(1,100)
#topevent = 100
# 定义课程名称和课程角色的列表
dianci,digai,gaodai,guangxue,jigai,junli,lili,lixue,sanbao,shufen,shuli,sixiu,xiandai,gaoshu = Actor('电磁学'),Actor('地概'),Actor('高代'),Actor('光学'),Actor('计概'),Actor('军理'),Actor('理论力学'),Actor('力学'),Actor('三宝'),Actor('数分'),Actor('数学物理方法'),Actor('思修'),Actor('线代'),Actor('高数')
dianci.name,digai.name,gaodai.name,guangxue.name,jigai.name,junli.name,lili.name,lixue.name,sanbao.name,shufen.name,shuli.name,sixiu.name,xiandai.name,gaoshu.name = '电磁学','地概','高代','光学','计概','军理','理论力学','力学','三宝','数分','数学物理方法','思修','线代','高数'
l = [dianci,digai,gaodai,guangxue,jigai,junli,lili,lixue,sanbao,shufen,shuli,sixiu,xiandai,gaoshu]
ls = [digai,guangxue,jigai,junli,lixue,shuli,sixiu,xiandai,gaoshu] 
for i in l:
    i.got = False
    i.withdraw = False
lixue.event =[['你的老师出了一些奇怪的加分题','倒立'],['你的老师在讲力学在其他领域的运用','奇怪的力学课'],['你的老师在讲哈密顿量，你满脸问号','哈密顿']]
digai.event = [['你学会了炒股','炒股'],['你做了一个被正态的梦，还好只是梦','84']]
jigai.event = [['你对Intel的CPU发展了如指掌','芯片'],['你学会了手撸POP3和HTTP','http'],['你决定做一个选课小游戏获得加分','小游戏'],['OJ上你什么都见过了，就是没有AC','一直ac不了吧']]
guangxue.event =[['你考了光免，但很不幸没过','光免']]
junli.event = [['你在军理课上摸鱼','摸鱼'],['群友骗你说有签到，你到了才发现没有','签到']]
shuli.event =[['你遇到了北大卷王，倒流时间去卷','北京大学还是你最卷啊']]
sixiu.event =[['你为PPT上的情侣暗暗担心','某位老师']]
xiandai.event =[['这道题很trivial，但你就是不会','trivial'],['期中考完后，你感觉自己失了秩','失秩']]
gaoshu.event = [['你和室友睡过了，错过了早八','心路历程'],['你对附加题束手无策','附加题']]
#形成猫、鸭
y = Actor('cat')
y.got = False
y.withdraw = False
y.name = '猫猫'
y.pos = random.randint(100,700),random.randint(400,930)
z1 = Actor('duck')
z1.got = False
z1.withdraw = False
z1.name = '鸭鸭'
z1.pos = 50,random.randint(400,930)
z2 = Actor('duck2')
z2.got = False
z2.withdraw = False
z2.name = '鸭鸭'
z2.pos = 700,random.randint(400,930)
Y = [y]
Z = [z1,z2]
# 形成课程角色列表
def ranactor(l):
    for i in l:
        i.pos = random.randint(50,700),random.randint(400,930)
        i.credit = random.randint(2,5)
        i.fen = random.randint(60,100)
        i.GPA = 4-3*(100-i.fen)**2/1600
def my_draw(l):
    for i in l:
        i.draw()
    for j in Y:
        j.draw()
    for k in Z:
        k.draw()
ranactor(l)
# 随机形成部分课程信息
def update_courses(l): # 定义课程的行为
    for i in l:
        if i.got and not i.withdraw:
            i.y -= 2*math.cos(gouzi.angle/180*pi)
            i.x -= 2*math.sin(gouzi.angle/180*pi) # 被勾到，则与钩一起运动
            if gouzi.get ==0:
                i.y -= 1000*math.cos(gouzi.angle/180*pi)
                i.x -= 1000*math.sin(gouzi.angle/180*pi) # 若钩归位，则加速
            if i.y <100:
                l.remove(i)
                gouzi.credit += i.credit
                if 66 <= topevent < 96:
                    i.fen -= 5
                    i.GPA = 4-3*(100-i.fen)**2/1600
                    gouzi.GPA = (gouzi.GPA*(gouzi.credit-i.credit) +i.GPA*i.credit)/gouzi.credit #到达某个位置，计算学分GPA，消失
                else:
                    gouzi.GPA = (gouzi.GPA*(gouzi.credit-i.credit) +i.GPA*i.credit)/gouzi.credit 
        elif i.withdraw:
            l.remove(i)
            gouzi.willpoints += 9 #退课，直接消失
def update_animals(l):
    for i in l:
        if i.got and not i.withdraw:
            i.y -= 2*math.cos(gouzi.angle/180*pi)
            i.x -= 2*math.sin(gouzi.angle/180*pi) # 被勾到，则与钩一起运动
            if gouzi.get ==0:
                i.y -= 1000*math.cos(gouzi.angle/180*pi)
                i.x -= 1000*math.sin(gouzi.angle/180*pi) # 若钩归位，则加速
            if i.y <100:
                l.remove(i)
        elif i.withdraw:
            l.remove(i) #退课，直接消失
def draw_badelective():
    screen.clear()
    screen.draw.text("游戏结束",color = "white",midtop=(375,100),fontsize = 70,shadow=(1,1),fontname = "cocacola")
    screen.draw.text("Your credits:"+str(gouzi.credit),color = "white",midtop=(375,300),fontsize = 100,shadow=(1,1))
    screen.draw.text("Your GPA:"+str(f"{gouzi.GPA:.3f}"),color = "white",midtop=(375,400),fontsize = 100,shadow=(1,1))
    screen.draw.text("有人在信息中心",color = "red",midtop=(375,500),fontsize = 60,shadow=(1,1),fontname = "cocacola")
    screen.draw.text("吃掉了一颗土豆",color = "red",midtop=(375,570),fontsize = 60,shadow=(1,1),fontname = "cocacola")
    screen.draw.text("你甚至没有机会选课！",color = "red",midtop=(375,640),fontsize = 60,shadow=(1,1),fontname = "cocacola")
    re_buttom.draw()
def draw_rain():
    screen.clear()
    screen.fill((0,0,128))
    screen.blit("backg3",(25,300))
    screen.draw.text("游戏结束",color = "white",midtop=(375,100),fontsize = 70,shadow=(1,1),fontname = "cocacola")
    screen.draw.text("Your credits:"+str(gouzi.credit),color = "white",midtop=(375,300),fontsize = 100,shadow=(1,1))
    screen.draw.text("Your GPA:"+str(f"{gouzi.GPA:.3f}"),color = "white",midtop=(375,400),fontsize = 100,shadow=(1,1))
    screen.draw.text("北京大学被一场大雨淹没了！",color = "red",midtop=(375,500),fontsize = 60,shadow=(1,1),fontname = "cocacola")
    screen.draw.text("你甚至没有机会选课！",color = "red",midtop=(375,570),fontsize = 60,shadow=(1,1),fontname = "cocacola")
    re_buttom.draw()
def draw_normal():
    global b_show
    global m
    screen.clear()
    screen.fill((128,0,0))
    screen.blit("backg2",(0,0))
    gouzi.draw()
    screen.draw.text(s1,color = 'white',midtop =(120,30),fontsize = 20,shadow=(1,1),fontname = "cocacola")
    screen.draw.text("剩余意愿点 %d"%gouzi.willpoints,color = 'white',midtop =(130,100),fontsize = 30,shadow=(1,1),fontname = "cocacola")
    screen.draw.text("Your credits:"+str(gouzi.credit),color = "white",midtop=(555,50),fontsize = 50,shadow=(1,1))
    screen.draw.text("Your GPA:"+str(f"{gouzi.GPA:.3f}"),color = "white",midtop=(555,80),fontsize = 50,shadow=(1,1))
    my_draw(l)#基本信息，钩，课程生成
    if not gouzi.fadong and gouzi.get == 0:#若钩未发射，显示提示
        screen.draw.text("按空格键发射选课钩",color = "white",midtop=(375,200),fontsize = 30,shadow=(1,1),fontname = "cocacola")
    for j in Y:
        if j.got:
            screen.draw.text("您选了：一只猫猫",color = "red",midtop=(555,150),fontsize = 30,shadow=(1,1),fontname = "cocacola")
            screen.draw.text("您会得0分和一些快乐！",color = "red",midtop=(555,180),fontsize = 30,shadow=(1,1),fontname = "cocacola")
            screen.draw.text("您不可以退猫。",color = "white",midtop=(555,210),fontsize = 30,shadow=(1,1),fontname = "cocacola")
    for k in Z:
        if k.got:
            screen.draw.text("您选了：一只鸭鸭",color = "red",midtop=(555,150),fontsize = 30,shadow=(1,1),fontname = "cocacola")
            screen.draw.text("您会得0分和一些快乐！",color = "red",midtop=(555,180),fontsize = 30,shadow=(1,1),fontname = "cocacola")
            screen.draw.text("您不可以退鸭。",color = "white",midtop=(555,210),fontsize = 30,shadow=(1,1),fontname = "cocacola")
    for i in l:
        if i.got:# 若被勾到，显示信息
            if 66 <= topevent < 96: 
                screen.draw.text("您选了："+i.name,color = "red",midtop=(555,150),fontsize = 30,shadow=(1,1),fontname = "cocacola")
                screen.draw.text("您会得"+str(i.fen-5)+"分和"+str(i.credit)+"学分！",color = "red",midtop=(555,180),fontsize = 30,shadow=(1,1),fontname = "cocacola")
                screen.draw.text("您可以点击W键退课。",color = "white",midtop=(555,210),fontsize = 30,shadow=(1,1),fontname = "cocacola")
            else:
                screen.draw.text("您选了："+i.name,color = "red",midtop=(555,150),fontsize = 30,shadow=(1,1),fontname = "cocacola")
                screen.draw.text("您会得"+str(i.fen)+"分和"+str(i.credit)+"学分！",color = "red",midtop=(555,180),fontsize = 30,shadow=(1,1),fontname = "cocacola")
                screen.draw.text("您可以点击W键退课。",color = "white",midtop=(555,210),fontsize = 30,shadow=(1,1),fontname = "cocacola")
                
    s = 0
    for i in l:
        if gouzi.get==1:
            if i.got:
                s += 1
    for i in Y:
        if gouzi.get==1:
            if i.got:
                s += 1
    for i in Z:
        if gouzi.get == 1:
            if i.got:
                s += 1
    if gouzi.get==1:
        if s == 0 :
            screen.blit("back3",(200,400))#若什么都没勾到，显示掉课
    if b_event:
        if len(ls)>0:
            for j in ls:
                if gouzi.colliderect(j):
                    if not b_show:
                        m = random.choice(j.event)
                        b_show = True
                    screen.blit(m[1],(0,100))
                    screen.draw.text(m[0],color =(255,165,0),midtop=(350,610),fontsize = 40,shadow=(1,1),fontname = "cocacola")
                    screen.draw.text("您可以按X跳过",color = (255,165,0),midtop=(350,670),fontsize = 40,shadow=(1,1),fontname = "cocacola")
                    
                    
def draw_end():
    screen.clear()
    screen.fill((128,0,0))
    screen.blit("backg2",(0,0))
    screen.draw.text("游戏结束",color = "white",midtop=(375,100),fontsize = 70,shadow=(1,1),fontname = "cocacola")
    screen.draw.text("Your credits:"+str(gouzi.credit),color = "white",midtop=(375,300),fontsize = 100,shadow=(1,1))
    screen.draw.text("Your GPA:"+str(f"{gouzi.GPA:.3f}"),color = "white",midtop=(375,400),fontsize = 100,shadow=(1,1))
    if gouzi.credit >14:
        if 3.8 > gouzi.GPA >= 3.7:
            screen.draw.text("您就是卷王？！",color = "white",midtop=(375,600),fontsize = 60,shadow=(1,1),fontname = "cocacola")
        elif 4> gouzi.GPA >= 3.8:
            screen.draw.text("您在地球有想过家吗？",color = "white",midtop=(375,600),fontsize = 60,shadow=(1,1),fontname = "cocacola")
        elif 3.7> gouzi.GPA >=3.3 :
            screen.draw.text("您发挥不错！",color = "white",midtop=(375,600),fontsize = 60,shadow=(1,1),fontname = "cocacola")
        elif 3.3> gouzi.GPA >=3 :
            screen.draw.text("您危了",color = "white",midtop=(375,600),fontsize = 60,shadow=(1,1),fontname = "cocacola")
        elif gouzi.GPA<=3 :
            screen.draw.text("您的GPA过低，您已被退学！",color = "white",midtop=(375,600),fontsize = 60,shadow=(1,1),fontname = "cocacola")
    else:
        screen.draw.text("您的学分过低，您已被退学！",color = "white",midtop=(375,600),fontsize = 60,shadow=(1,1),fontname = "cocacola")
def draw_earlyending():
    draw_normal()
    if not b_event:
        screen.draw.text("警告！期末提前了一周！",color = "red",midtop=(375,250),fontsize = 30,shadow=(1,1),fontname = "cocacola")
        screen.draw.text("您的所有成绩将-5",color = "red",midtop=(375,280),fontsize = 30,shadow=(1,1),fontname = "cocacola")
    
def draw():# 窗口绘制
    if begin:
        if topevent <= 5:
            draw_rain()
        if 5 < topevent < 66:
            if not(len(l)==0 or gouzi.willpoints ==0):
                sounds.backg.play(loops = 10000)
                draw_normal()
            if len(l)==0 or gouzi.willpoints ==0:# 游戏结束画面
                draw_end()
        if 66 <= topevent < 96:
            if not(len(l)==0 or gouzi.willpoints ==0):
                draw_earlyending()
            if len(l)==0 or gouzi.willpoints ==0:# 游戏结束画面
                draw_end()
        if 96<= topevent <= 100:
            sounds.backg.play(loops = 10000)
            draw_badelective()
    else:
        screen.clear()
        screen.fill((128,0,0))
        screen.blit("backg2",(0,0))
        buttom.draw()
        screen.draw.text("又到了一年两度的选课季！",color = "white",midtop=(375,200),fontsize = 50,shadow=(1,1),fontname = "cocacola")
        screen.draw.text("您可以在这里选课",color = "white",midtop=(375,250),fontsize = 40,shadow=(1,1),fontname = "cocacola")
        screen.draw.text("您可以按空格发射选课勾",color = "white",midtop=(375,300),fontsize = 40,shadow=(1,1),fontname = "cocacola")
        screen.draw.text("当分数较低时，您可以按W退课",color = "white",midtop=(375,350),fontsize = 40,shadow=(1,1),fontname = "cocacola")
        screen.draw.text("您也可能打出奇怪的结局",color = "white",midtop=(375,400),fontsize = 40,shadow=(1,1),fontname = "cocacola")
        screen.draw.text("或是邂逅校园的猫猫和鸭子",color = "white",midtop=(375,450),fontsize = 40,shadow=(1,1),fontname = "cocacola")
        screen.draw.text("选课过程中，您可能遇到一些事件",color = "white",midtop=(375,500),fontsize = 40,shadow=(1,1),fontname = "cocacola")
        screen.draw.text("您可以按X跳过这些事件",color = "white",midtop=(375,550),fontsize = 40,shadow=(1,1),fontname = "cocacola")
        screen.draw.text("点击start开始选课吧！",color = "white",midtop=(375,600),fontsize = 40,shadow=(1,1),fontname = "cocacola")
        screen.draw.text('努力获得更高的GPA！' , color='white',midtop =(375,650),fontsize = 40,shadow=(1,1),fontname = "cocacola")
        

def on_key_down(key):#按任意键发动钩子
    global b_event
    global b_show 
    if key == keys.SPACE:
        if not gouzi.fadong and not gouzi.get:
            gouzi.fadong = True#按W退课
    if key == keys.W:
        for i in l:
            if i.got:
                i.withdraw = True
                gouzi.get = 2
    if key == keys.X and b_event == True:
        b_event = False
        b_show = False
        if len(ls)> 0 :
            for i in ls:
                if gouzi.colliderect(i):
                    ls.remove(i)
def on_mouse_down(pos):
    global begin
    global topevent,cnum
    if not begin:
        if buttom.collidepoint(pos):
            begin = True
    if topevent <= 5 or 96<= topevent <= 100:
        if re_buttom.collidepoint(pos):
            cnum += 1
        if cnum ==2:
            topevent = random.randint(30,90)
            
def update_gouzi():#定义钩子行为
    global num
    if gouzi.fadong: #钩子发射
        gouzi.y += 8*math.cos(gouzi.angle/180*pi)
        gouzi.x += 8*math.sin(gouzi.angle/180*pi)
        for i in l:
            if gouzi.colliderect(i):
                i.got = True
                gouzi.get = 1
                gouzi.fadong = False
                global b_event
                if not b_event:
                    if len(ls)>0:
                        if i in ls:
                            b_event = True
                            
        for j in Y:
            if gouzi.colliderect(j):
                j.got = True
                gouzi.get = 1
                gouzi.fadong = False
        for k in Z:
            if gouzi.colliderect(k):
                k.got = True
                gouzi.get = 1
                gouzi.fadong = False
        if gouzi.x > 750 or gouzi.x < 0 or gouzi.y>990 or gouzi.y <0:
            gouzi.get = 1
            gouzi.fadong = False
    elif gouzi.get==1: #钩子回收
        gouzi.y -= 2*math.cos(gouzi.angle/180*pi)
        gouzi.x -= 2*math.sin(gouzi.angle/180*pi)
        if gouzi.y<170 :
            gouzi.get = 0
            gouzi.x,gouzi.y = 375,170
            gouzi.willpoints -= 9
    elif gouzi.get ==2:#退课后快速回收
        gouzi.y -= 20*math.cos(gouzi.angle/180*pi)
        gouzi.x -= 20*math.sin(gouzi.angle/180*pi)
        if gouzi.y<170 :
            gouzi.get = 0
            gouzi.x,gouzi.y = 375,170
            gouzi.willpoints -= 9
        
    else:  # 钩子旋转
        if abs(gouzi.angle) <=70:
            gouzi.angle += (-1)**num
        elif gouzi.angle >70:
            num += 1
            gouzi.angle -= 2
        elif gouzi.angle < -70:
            num += 1
            gouzi.angle += 2
        

def update():#进行钩子和课程的行为
    if not b_event:
        update_gouzi()
        update_courses(l)
        update_animals(Y)
        update_animals(Z)
        if z1.got == False:    
            z1.right += 2
            if z1.right >= 700:
                z1.pos = 50,random.randint(400,930)
        if z2.got == False:    
            z2.left -= 2
            if z2.left <= 0:
                z2.pos = 700,random.randint(400,930)
pgzrun.go()#运行
             
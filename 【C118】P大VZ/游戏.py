import pgzrun
import random
import easygui as g
import sys

WIDTH = 1200
HEIGHT = 646
player = Actor('player1.png')
player.y = 333
player.x = 20
game_status = 0
game_style = 0
game = False
# 建立武器和敌人相关变量
weapons = []
zombie = []
roadblock = []
iron = []
T = 0
bullet_status = 1
#建立boss系列存储的列表
bosses = []
magics = []
boss_heart = 100
boss_current = 100
bossnum = 0
times = 0
dx = 0
dy = 0
doors = []
dunn = 0
attack = 0
choice = 0
qwq = 0
#生成玩家相关物品
heart = []
heart1 = Actor('heart.png')
heart1.x = 75
heart1.y = 60
heart.append(heart1)
heart2 = Actor('heart.png')
heart2.x = 105
heart2.y = 60
heart.append(heart2)
heart3 = Actor('heart.png')
heart3.x = 135
heart3.y = 60
heart.append(heart3)
heart4 = Actor('heart.png')
heart4.x = 165
heart4.y = 60
heart.append(heart4)
heart5 = Actor('heart.png')
heart5.x = 195
heart5.y = 60
heart.append(heart5)
heart6 = Actor('heart.png')
heart6.x = 225
heart6.y = 60
heart.append(heart6)
music.play('start')
skill_current = 0
hurt = 0
musicnum = 0
score = 0
# 绘制背景
def draw():
    global score
    if game_status == 1 or game_status == 3:
        screen.blit('back1.png', [0, 0])
        player.draw()
        for w in weapons:
            w.draw()
        for b in zombie:
            b.draw()
        for c in roadblock:
            c.draw()
        for d in iron:
            d.draw()
        for h in heart:
            h.draw()
        for bo in bosses:
            bo.draw()
        for m in magics:
            m.draw()
        for do in doors:
            do.draw()
        draw_skill_bar()
        if game_style == 2:
            draw_status_bar()
        if game_style == 1:
            screen.draw.text('BOSS IS COMING', center = [700,150], fontsize=60, color='red')
            w1 = Actor('wrong.png')
            w1.x = 480
            w1.y = 140
            w1.draw()
            w2 = Actor('wrong.png')
            w2.x = 915
            w2.y = 140
            w2.draw()
    if game_status == 0:
        screen.blit('封面.jpg', [-30, 0])
    if game_status == 3:
        screen.draw.text('YOU WIN!', (400,50), fontsize=130, color='red')
        screen.draw.text('YOUR SCORE IS %d' % score, (460, 150), fontsize=50, color='white')
#进行刷新
def update():
    global score
    global game_status
    global game_style
    global boss_current
    global heart
    global bosses
    global zombie
    global roadblock
    global iron
    global magics
    global times
    global player
    global dunn
    global attack
    global choice
    global skill_current
    global bullet_status
    global hurt
    global qwq
    global T
    global musicnum
    global doors
# 上下左右移动
    if game_status == 1 or game_status == 3:
        if keyboard.a:
            player.x -= 8
        if keyboard.d:
            player.x += 8
        if keyboard.w:
            player.y -= 7
        if keyboard.s:
            player.y += 7 
#限制角色位置
    if player.y < 10:
        player.y = 10
    if player.y > 650:
        player.y = 650
    if player.x > 1180:
        player.x = 1180
    if player.x < 10:
        player.x = 10

# 设置武器移动速度   
    for w in weapons:
        w.x += 30 
# 武器碰到窗口地下消失 控制射程d
        if w.x <= player.x - 650:
            weapons.remove(w)
            
# 刷怪
    if game_style == 0 and game_status == 1:
        birth()
        if musicnum == 0:
            music.play('begin')
            musicnum += 1
    for b in zombie:
        b.x -= 2.5
        if b.x < 10:
            zombie.remove(b)
            score -= 1
            del(heart[0])
    for c in roadblock:
        c.x -= 2.5
        if c.x < 10:
                roadblock.remove(c)
                score -= 2
                del(heart[0])
    for d in iron:
        d.x -= 2.5
        if d.x < 10:
            iron.remove(d)
            score -= 3
            del(heart[0])

#造成伤害，以及形态切换
    for b in zombie:
        for w in weapons:
            if b.colliderect(w) and game_status == 1:
                zombie.remove(b)             
                weapons.remove(w)
                score += 1
                if skill_current < 100 and bullet_status == 1:    
                    skill_current += 4
        if b.colliderect(player):
            zombie.remove(b)
            score -= 5
            if len(heart) > 0:
                del(heart[0])
    
    for c in roadblock:
        for w in weapons:
            if c.colliderect(w) and game_status == 1:
                weapons.remove(w)
                if c.image == 'roadblock2.png':
                    roadblock.remove(c)
                    score += 2
                    if skill_current < 100 and bullet_status == 1:
                        skill_current += 4
                if c.image == 'roadblock1.png':
                    c.image = 'roadblock2.png'
                    if bullet_status == 2:
                        roadblock.remove(c)
                        score += 2
            
        if c.colliderect(player):
            roadblock.remove(c)
            score -= 5
            if len(heart) > 0:
                del(heart[0])
    
    for d in iron:        
        for w in weapons:
            if d.colliderect(w) and game_status == 1:
                weapons.remove(w)
                if d.image == 'iron3.png':
                    iron.remove(d)
                    score += 3
                    if skill_current < 100 and bullet_status == 1:
                        skill_current += 4
                if d.image == 'iron2.png':
                    d.image = 'iron3.png'
                    if bullet_status == 2:
                        iron.remove(d)
                        score += 3
                if d.image == 'iron1.png':
                    d.image = 'iron2.png'
                    if bullet_status == 2:
                        d.image = 'iron3.png'
                
        if d.colliderect(player):
            iron.remove(d)
            score -= 5
            if len(heart) > 0:
                del(heart[0])
    
    for bo in bosses:
        if bo.colliderect(player) and game_status == 1 and qwq == 0:
            del(heart[0])
            player.y = 333
            player.x = 20
            qwq += 1
    
    for m in magics:
        if m.colliderect(player) and attack == 1 and heart != []:
            hurt += 1
            player.y = 333
            player.x = 20
    if hurt > 0:
        del(heart[0])
        hurt = 0
    
    for bo in bosses:
        for w in weapons:
            if bo.colliderect(w) and game_status != 0 and dunn == 0:                  
                weapons.remove(w)
                boss_current -= 1
                if bullet_status == 2:
                    boss_current -= 1
            if bo.colliderect(w) and game_status != 0 and dunn == 1:
                weapons.remove(w)

#player的模式切换
    if skill_current == 100:
        if keyboard.K_space:
            bullet_status = 2
            player.image = 'player2.png'
    if skill_current == 0:
        bullet_status = 1
        player.image = 'player1.png'
    
    if bullet_status == 2:
        skill_current -= 0.25
            
#检测输局
    if heart == []:
        game_status = 2
        
    if game_status == 2:
        bosses = zombie = roadblock = iron = iron_hp = palyer = firebooms = []
        screen.blit('gameover.jpg', [-30, 0])
        if musicnum == 1:
            music.play('dault')
            musicnum += 1

#进入boss前夕
    if score >= 100 and game_style == 0:
        game_style = 1
        T = 0
    if game_style == 1:
        beforeboss()

#进入boss模式
    if game_style == 2:
        bossbirth()
        
#boss行动
    if game_style == 2 and game_status == 1:
        if choice == 1:
            boss_1()
        if choice == 2:
            boss_2()
        if choice == 3:
            boss_3()
        
#检测胜利
    if game_style == 2 and boss_current <= 0:
        weapon = []
        zombie = []
        roadblock = []
        iron = []
        doors = []
        magics = []
        game_status = 3
        for bo in bosses:
            bo.image = 'victory'
        if musicnum == 1:
            music.play('win')
            musicnum += 1

#开始游戏以及退出游戏
def on_key_down(key):
    global game_status
    if game_status == 0:
        if key == keys.K_0 or keyboard.o:
            gamemode()
            game_status = 1
    if key == keys.K_9:
        sys.exit(0)
#子弹的生成
def on_mouse_down(pos,button):
    if game_status == 1:
        if bullet_status == 1:
            weapon =  Actor('bullet1.png')
        if bullet_status == 2:
            weapon =  Actor('bullet2.png')
        weapon.x = player.x - 25
        weapon.y = player.y
    if button == mouse.LEFT and game_status != 2 and game_status != 3:
        weapons.append(weapon)
#刷怪
def birth():
    global T
    global skill_current
    if T == 0 or T == 40:
        for i in range(0,1):
            a = Actor('zombie.png')
            a.x = 1140
            a.y = random.randint(20, 640)
            zombie.append(a)
        for i in range(0,1):
            a = Actor('roadblock1.png')
            a.x = 1140
            a.y = random.randint(20, 640)
            roadblock.append(a)
    if T == 40:
        for i in range(0,1):
            a = Actor('iron1.png')
            a.x = 1140
            a.y = random.randint(20, 640)
            iron.append(a)
    if T == 80:
        T = 0
    T += 1
#boss专用
def beforeboss():
    global zombie
    global roadblock
    global iron
    global T
    global game_style
    if zombie == [] and roadblock == [] and iron == []:
        T += 1
    if T == 60:
        game_style = 2
        T = 0

def bossbirth():
    global bossnum
    global zombie
    global roadblock
    global iron
    global iron_hp
    global choice
    if bossnum == 0:
        bo = Actor('boss.png')
        bo.x = 1100
        bo.y = 350
        bosses.append(bo)
        zombie = []
        roadblock = []
        iron = []
        bossnum += 1
        music.play('battle')
        choice = random.randint(1, 3)
#冲撞
def boss_1():
    global bosses
    global dx
    global dy
    global times
    global player
    global choice
    global qwq
    bo = bosses[0]
    if times % 90 == 0:
        qwq = 0
        dx = player.x - bo.x
        dy = player.y - bo.y
    bo.x += (dx / 60)
    bo.y += (dy / 60)
    times += 1
    if times %90 == 60 and times != 420:
        dx = 2 * (1100 - bo.x)
        dy = 2 * (bo.y - bo.y)
    if times == 420:
        dx = 2 * (1100 - bo.x)
        dy = 2 * (350 - bo.y)
    if times == 450:
        times = 0
        choice = random.randint(2, 3)
#召唤
def boss_2():
    global bosses
    global doors
    global times
    global zombie
    global roadblock
    global iron
    global dunn
    global choice
    if times == 0:
        door1 = Actor('door.png')
        door1.x = 1070
        door1.y = 100
        doors.append(door1)
        door2 = Actor('door.png')
        door2.x = 1070
        door2.y = 200
        doors.append(door2)
        door3 = Actor('door.png')
        door3.x = 1070
        door3.y = 500
        doors.append(door3)
        door4 = Actor('door.png')
        door4.x = 1070
        door4.y = 600
        doors.append(door4)
    times += 1
    if times %50 == 0:
        b1 = Actor('zombie.png')
        b1.x = 1040
        b1.y = 100
        zombie.append(b1)
        b2 = Actor('roadblock1.png')
        b2.x = 1040
        b2.y = 500
        roadblock.append(b2)
        c1 = Actor('iron1.png')
        c1.x = 1040
        c1.y = 200
        iron.append(c1)
        c2 = Actor('zombie.png')
        c2.x = 1040
        c2.y = 600
        zombie.append(c2)
    if times == 60:
        bosses[0].image = 'dun'
        dunn = 1
    if times == 700:
        zombie = []
        roadblock = []
        iron = []
        doors = []
        bosses[0].image = 'boss'
        dunn = 0
        times = 0
        choice = 1
#炮击
def boss_3():
    global magics
    global attack
    global times
    global choice
    global bosses
    global dx
    global dy
    bo = bosses[0]
    if times %50 == 0:
        attack = 0
        for i in range(0,8):
            m = Actor('magic.png')
            m.x = random.randint(25, 300)
            m.y = random.randint(25, 641)
            magics.append(m)
        for i in range(0,8):
            m = Actor('magic.png')
            m.x = random.randint(350, 600)
            m.y = random.randint(25, 641)
            magics.append(m)
        for i in range(0,8):
            m = Actor('magic.png')
            m.x = random.randint(650, 1000)
            m.y = random.randint(25, 641)
            magics.append(m)
        if times == 0 or times == 150:
            dy = -240
        if times == 50 or times == 100:
            dy = 240
        if times == 200:
            dy = 0
    if times %50 == 40:
        attack = 1
        for m in magics:
            m.image = 'fireboom'
    times += 1
    bo.y += (dy / 40)
    if times %50 == 42:
        attack = 0
    if times %50 == 46:
        magics = []
    if times == 250:
        times = 0
        choice = random.randint(1, 2)
#血量与技能值的展示
def draw_status_bar():
    currentHP_bar = Rect((957, 26), (235 * boss_current / boss_heart, 13)) #当前血量
    screen.blit('status_bar', (950, 20))
    screen.draw.filled_rect(currentHP_bar, 'red')               
def draw_skill_bar():
    currentskill_bar = Rect((57, 26), (235 * skill_current / 100, 13)) #当前技能值
    screen.blit('status_bar', (50, 20))
    screen.draw.filled_rect(currentskill_bar, 'grey')    
#登录界面
def gamemode():
    global game
    while not game:
        g.msgbox('你是一名来自phu大学的苦于typhon课程的大一新生，在你赶ddl的一天深夜，你因缺乏睡眠而直接睡在了桌子，当你醒来时，你发现......',ok_button='继续')
        g.msgbox('你发现你变成了一名豌豆射手，并且你居然可以移动，你感到很好奇。正当你想要探求身体变化的秘密时，你发现一名酷似戴夫的人，你决定.......',ok_button='与他交谈',image='images\defu.png')
        g.msgbox('他说：“我就是你认为的那个戴夫，是我召唤你以豌豆射手的模样过来的，自上一次打败僵王博士后，它一直不死心，想要吃掉我的脑子，所以我召唤你来保护我。”我决定......',ok_button='和他谈条件',image='images\defu.png')
        g.msgbox('我回答道：“那你能给我什么好处呢？”戴夫说：“倘若你答应保护我，在你胜利归去时，你会发现你的计概作业将会A C C E P T E D!”我陷入思考......',ok_button='继续',image='images\defu.png')
        if g.ccbox('请做出决定', '', choices=('答应他', '不去不去，他肯定在骗我')):
            global your_name
            your_name = g.enterbox(msg="请输入你的名字", title="你的名字")
            how_to_play()
            return
        else:
            sys.exit(0)
#操作介绍
def how_to_play():
    global your_name
    g.msgbox(msg='单击鼠标左键你将发出豌豆w\n\n'
                    '你一共拥有6颗心，可以通过wsad键进行上下前后的移动w\n\n'
                    '你若碰到僵尸，或者让一只僵尸进入屋中，你将损失一颗心w\n'
                    '每种僵尸的血量不同，击败僵尸后会恢复白条并得到一定分数，当达到一定分数后，僵王博士将会出现，击败它即可获得胜利w!\n'
                    '当你白条满了，按空格键将会进入红怒模式，你的每发豌豆将会造成2倍伤害w\n'
                    '僵王博士有三种模式。第一种为冲撞，即它会冲向你当前位置，再退回顶端，你若和它相撞就会损失一颗心，并退回起点w\n'
                    '第二种为召唤，持续一定时间召唤各种僵尸，并且不会受到豌豆直接伤害w\n'
                    '第三种为魔法阵，地面会出现红色警示，再短时间后会发生爆炸，若接触爆炸，你会失去一颗心w\n'
                    '游戏最后会显示你的分数w\n'
                    f"{your_name}你准备好去击败僵王博士？快开始吧！\n",title='操作介绍',  ok_button='冲啊')
    if g.ccbox('闯关之前'f'{your_name}，你懂得如何如何操作了嘛', '', choices=('等等我还没搞懂?', '我准备好了!')):
        how_to_play()
    else:
        return


# 运行全部程序
pgzrun.go()
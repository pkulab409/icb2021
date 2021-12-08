import pgzrun
import random
import time  # 导入time模块
import itertools

# 玩家、位置和得分
player = Actor("player")
player.center = 500, 580
player.score = 3#三条命



beijin0 = Actor("backimg")
#第一关
beijin1 = Actor("backimg1")
beijin1.center = 100000000, 10000000
beijin1_leiqu1 = Actor("backimg1_leiqu1")
beijin1_leiqu1.center = 10000000, 10000000
beijin1_leiqu2 = Actor("backimg1_leiqu2")
beijin1_leiqu2.center = 10000000, 10000000
beijin1_leiqu3 = Actor("backimg1_leiqu3")
beijin1_leiqu3.center = 10000000, 10000000
beijin1_leiqu4 = Actor("backimg1_leiqu4")
beijin1_leiqu4.center = 10000000, 10000000
beijin1_leiqu5 = Actor("backimg1_leiqu5")
beijin1_leiqu5.center = 10000000, 10000000
beijin1_leiqu6 = Actor("backimg1_leiqu6")
beijin1_leiqu6.center = 10000000, 10000000
beijin1_leiqu7 = Actor("backimg1_leiqu7")
beijin1_leiqu7.center = 10000000, 10000000
beijin1_leiqu8 = Actor("backimg1_leiqu8")
beijin1_leiqu8.center = 10000000, 10000000

beijin2 = Actor("backimg2")
beijin2.center = 400, 400

beijin3 = Actor("backimg3")
beijin3.center = 400, 400

beijin4 = Actor("backimg4")
beijin4.center = 400, 400

beijin5 = Actor("backimg5")
beijin5.center = 400, 400
#第二关
#beijin2 = Actor("backimg2")

a = Actor("透明")#实现：点击“开始游戏”，进入第一关
a.center = 400, 350
dyg = Actor("第一关")
dyg.center = 200,60
# 2, 设定窗口
WIDTH = 800
HEIGHT = 800

x = 0
y = 0

jiemian = 0
#jiemian=0为开始游戏界面
#jiemian=1为第一关
#jiemian=2为第二关
#jiemian=3为第2.5关
#jiemian=4为第一关复活界面
#jiemina=5为第二关复活界面
#jiemian=6为第2.5关复活界面
#jiemian=7连接界面
#jiemain=8过关界面
#jiemian=9死亡界面
lianjiejm = Actor("lianjiejm")
lianjiejm.center = 400, 400

def lj():
    lianjiejm.draw()
    clock.schedule_unique(jia1, 0.1)

beijin10 = Actor("gui")
beijin10.center = 400, 400
def jia2():
    global jiemian
    jiemian = 3
def xiaren():
    beijin10.draw()
    clock.schedule_unique(jia2, 0.2)


# 3, 每次需要刷新窗口的时候，会自动调用draw函数
def draw():
    global jiemian
    # 清除窗口，设置背景
    screen.clear()
    
    if jiemian == 0:
        a.center = 400, 350
        beijin0.draw()
        screen.draw.text("Start", (360, 330), fontsize = 50)
        #print(jiemian)
   
    elif jiemian == 1:
        
        beijin1.center = 400, 400
        beijin1_leiqu1.center = 285, 55
        beijin1_leiqu2.center = 32, 448
        beijin1_leiqu3.center = 556, 198
        beijin1_leiqu4.center = 578, 436
        beijin1_leiqu5.center = 365, 520
        beijin1_leiqu6.center = 233, 339
        beijin1_leiqu7.center = 322, 258
        beijin1_leiqu8.center = 412, 759
        beijin1.draw()
        player.draw()
        dyg.draw()
        a.center = 10000, 10000
        if x > 600 and x < 750 and y < 125:
            print("过关")
            jiemian = 7
        
    elif jiemian == 4:
        beijin1.center = 400, 400
        beijin1_leiqu1.center = 100000, 100000
        beijin1_leiqu2.center = 100000, 100000
        beijin1_leiqu3.center = 100000, 100000
        beijin1_leiqu4.center = 100000, 100000
        beijin1_leiqu5.center = 100000, 100000
        beijin1_leiqu6.center = 100000, 100000
        beijin1_leiqu7.center = 100000, 100000
        beijin1_leiqu8.center = 100000, 100000
        beijin1.draw()
        set_player_hurt()
        player.draw()
        a.center = 10000, 10000
        screen.draw.text("Restart", (345, 335), fontsize = 50, color = 'red')
        restart()
    
    elif jiemian == 7:
        lj()
        
    elif jiemian == 2:
        beijin1_leiqu1.center = 100000, 100000
        beijin1_leiqu2.center = 100000, 100000
        beijin1_leiqu3.center = 100000, 100000
        beijin1_leiqu4.center = 100000, 100000
        beijin1_leiqu5.center = 100000, 100000
        beijin1_leiqu6.center = 100000, 100000
        beijin1_leiqu7.center = 100000, 100000
        beijin1_leiqu8.center = 100000, 100000
        beijin2.draw()
        player.draw()
        if x > 288 and y > 583 and x < 348 and y < 643:
            xiaren()
            
    
    elif jiemian == 5:
        
        beijin2.draw()
        set_player_hurt()
        player.draw()
        screen.draw.text("Restart", (589, 75), fontsize = 50, color = 'red')
        restart()
        
    elif jiemian == 3:
        beijin3.draw()
        
        player.draw()
        if x > 220 and y >385 and x<292 and y<445:
            print("过关")
            jiemian = 8
        
        #print(jiemian)
    elif jiemian == 6:
        beijin3.draw()
        set_player_hurt()
        player.draw()
        screen.draw.text("Restart", (589, 75), fontsize = 50, color = 'red')
        restart()
    elif jiemian == 8:#过关了
        beijin4.draw()
        
    elif jiemian == 9:#死了
        beijin5.draw()

    # 画上宝物和玩家
    #player.draw()

    # 画上分数
    screen.draw.text("Life:%d" % player.score, (360, 10), fontsize = 30)
#def update():


def jia1():
    global jiemian
    jiemian = 2


def si():
    global jiemian
    

    if jiemian == 1 and player.score > 1:
        player.score -= 1
        jiemian = 4
    
    elif jiemian == 2 and player.score > 1:
        player.score -= 1
        jiemian = 5
        
    elif jiemian == 3 and player.score > 1:
        player.score -= 1
        jiemian = 6
        
    elif player.score == 1:
        player.score -= 1
        jiemian = 9
        

    

# 5, 鼠标移动玩家
def on_mouse_move(pos):
    global x, y, jiemian
    x = player.x = pos[0]
    y = player.y = pos[1]
    if jiemian == 1 and beijin1_leiqu1.collidepoint(pos) or beijin1_leiqu2.collidepoint(pos) or beijin1_leiqu3.collidepoint(pos) or beijin1_leiqu4.collidepoint(pos) or beijin1_leiqu5.collidepoint(pos) or beijin1_leiqu6.collidepoint(pos) or beijin1_leiqu7.collidepoint(pos) or beijin1_leiqu8.collidepoint(pos):#触碰第一张图雷区
        si()
    elif jiemian == 2 and ( y > 655 or y < 36 or x > 755 or (y < 306 and x < 542) or (162 < y and y < 300 and x < 614) or (y > 163 and x > 686) or (543 < x and x < 680 and 377 < y and y < 443) or (433 < x and x < 470 and 309 < y and y < 570) or (148< x and x< 621 and 512< y and y< 571)):
        si()
    elif jiemian == 3 and ( x<49 or x>(800-44) or y<38 or y >(800-22) or (x<541 and y<70) or (x>400 and y>69 and x<543 and y<304) or (x>543 and y > 157 and x<613 and y<306) or (x>(800-113) and y>(600-638)) or (x>373 and y > 653) or (x>545 and y>381 and y<456) or (x>129 and y>146 and x<329 and y<287) or (x>132 and y>277 and x<202 and y<444) or (x<296 and y<700 and x>128 and y>452) or (x>404 and y>292 and x<470 and y<573) or (x>465 and y>516 and x<618 and y<577) or (x>289 and y>363 and x<412 and y<570)):
        si()


def restart():
    global jiemian
    if x > 282 and x < 542 and y < 448 and y > 281 and jiemian == 4:
        jiemian = 1
        player.image = 'player'
    elif 554 <x< 748 and 48 <y< 151 and jiemian == 5:
        jiemian = 2
        player.image = 'player'
    elif 554 <x< 748 and 48 <y< 151 and jiemian == 6:
        jiemian = 3
        player.image = 'player'

def on_mouse_down(pos,button):
    global jiemian
    if a.collidepoint(pos):
        global jiemian
        jiemian += 1
        #screen.clear()
       # 画上分数
        screen.draw.text("Life:%d" % player.score, (360, 10), fontsize = 30)
        #screen.draw.text("!!!!!!!", (360, 330), fontsize = 50)
        print('两个角色碰撞')
    elif jiemian == 9:
        if beijin5.collidepoint(pos):
            player.score = 3
            jiemian = 0
        
    #elif 
def set_player_hurt():  # 外星人被击中后的动作
    player.image = 'player_hurt'  # 换用图像'alien_hurt'
    sounds.eep.play()  # 播放sounds文件夹中的声音文件'eep'

pgzrun.go()
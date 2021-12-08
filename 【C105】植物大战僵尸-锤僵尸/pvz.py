import pgzrun
import random
import time

WIDTH = 1210
HEIGHT = 756
#easy，medium，hard图标
easy = Actor('easy')
easy.pos = 605, 278
medium = Actor('medium')
medium.pos =605, 378
hard = Actor('hard')
hard.pos = 605, 478
difficulty = [easy, medium, hard]
back = Actor('back')#返回的图标待修整
back.topright = 1210,0

x=[700,570,830,960,1090] #墓碑位置
z1=[130,260,390,520,650] #三种僵尸位置
z2=[120,250,380,510,640]
z3=[115,245,375,505,635]

hammer = Actor('hammer')
tomb1 = Actor('tomb1')
tomb2 = Actor('tomb1')
tomb5 = Actor('tomb1')
tomb3 = Actor('tomb2')
tomb4 = Actor('tomb2')
tombs = [tomb1,tomb2,tomb3,tomb4,tomb5]
for i in range(5):
    tombs[i].pos = x[i], z1[i]#墓碑位置

zombie_pos = (tuple(zip(x,z1)),tuple(zip(x,z2)),tuple(zip(x,z3)))

flag = 0
diff = 0
zombies=[]
count = 0
count_ = -100

def difficulty_draw():#画出easy，meduim，hard的图标
    for i in difficulty:
        i.draw()

def bgdraw():#背景函数
    if flag == 0:#开始的场景
        screen.blit('bg1',(0,0))
        difficulty_draw()
        screen.draw.text("THE RULE OF THE GAME:\n WHEN YOU SEE A ZOMBIE,\n YOU DON'T NEED TO DO ANYTHING, \n WAIT FOR HIM TO WALK PAST",(10,150),color='red')
    else:#进入游戏的场景
        screen.clear()
        screen.blit('bg2',(0,0))

def zombieadd(n, diff):#逢n加僵尸
    global count
    if count <= 10 * n * diff and count % n == 0:
        i = random.randint(1,3)
        zombie_add = Actor(f'zombie{i}')
        zombie_add.pos = random.choice(zombie_pos[i-1])
        zombies.append(zombie_add)
    count += 1

def zombie_draw():#画僵尸
    for i in zombies:
        i.draw()

def tomb_draw():#画墓碑
    for i in tombs:
        i.draw()

def on_mouse_move(pos):#hammer随鼠标移动
    if flag == 1:
        hammer.pos = pos

def on_mouse_down(pos):
    global flag
    if flag == 0:#三种模式
        for i in range(3):
            if difficulty[i].collidepoint(pos):
                global diff
                diff = i + 1 + i * (i - 1)

                flag = 1
                break

    if flag == 1:#游戏中锤一下僵尸僵尸会降级
        if back.collidepoint(pos):
            flag = 0
            global count
            count = 0
            zombies.clear()
        for i in range(len(zombies)):
            z = zombies[i]
            if hammer.colliderect(z):
                if z.image == 'zombie2':
                    zo = Actor('zombie1')
                    y = list(z.pos)
                    y[1] += 12 #这里是为了路障被打成普通僵尸时位置变化不明显
                    zo.pos = tuple(y)
                    zombies[i] = zo
                    break
                if z.image == 'zombie3':
                    zo = Actor('zombie2')
                    zo.pos = z.pos
                    zombies[i] = zo
                    break
                else:
                    zombies.pop(i)
                break             

def mode(n):#难度和速度的关系
    for i in zombies:
        if n == 1 or n == 2:
            i.left -= n + 1
        else:
            i.left -= 3.5

def death():#游戏失败
    for i in zombies:
        if i.right < 10:
            screen.draw.text('the zombies ate your brains!'.upper(),(20,350),color = 'red',fontsize = 100)
            screen.draw.text('(3 seconds to return to the main interface)' ,(250,450),fontsize = 50)
        if i.right < 0:
            time.sleep(3)
            global flag
            flag = 0
            global count
            count = 0
            zombies.clear()
            break

def victory(n, diff):#游戏胜利
    global count
    global count_
    if count > 10 * n * diff and not zombies:
        
        screen.draw.text('VICTORY', (450,350), color = 'red', fontsize = 100)
        screen.draw.text('(1.5 seconds to return to the main interface)' ,(250,450),fontsize = 50)
        print(count_)
        if count_ == -100:
            count_ = count
        if count == count_ + 1:
            print(5000)
            time.sleep(2)
            count = 0
            
            global flag
            flag = 0
            
            count_ = -100
            zombies.clear()

def draw():
    bgdraw()
    if flag == 1:
        tomb_draw()
        zombie_draw()
        hammer.draw()
        back.draw()
        death()
        victory(60 - 10 * diff, diff)

def update():
    if flag == 1:
        mode(diff)
        zombieadd(60 - 10 * diff, diff)
        
pgzrun.go()
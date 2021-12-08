import pgzrun
import random

player=Actor('white_cube')
left = 0
right = 0
player.vy=0
player.midbottom=(75,650)
GRAVITY=0.5
stand=0

WIDTH=800
HEIGHT=800

level=1
blocks = []
hurts = []
jumps = []
clouds = ['cloud1', 'cloud2', 'cloud3', 'cloud4', 'cloud5', 'cloud6', 'cloud7']
C = []
#地图碰撞箱
maze1 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
    [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1],
    [0,0,0,1,1,0,0,1,1,0,0,2,2,2,1,1],
    [1,1,1,1,1,0,0,1,1,2,2,1,1,1,1,1],
    [1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
maze2 = [
    [1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,2,2,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1],
    [0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0],
    [0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0]
    ]
maze3 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,2,2,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1],
    [1,1,0,0,0,0,1,1,2,2,2,2,2,1,1,1],
    [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,3,1,4,0,0,0,0,0],
    [0,0,0,0,0,2,0,0,0,5,0,0,1,0,0,0],
    [0,0,0,0,3,1,4,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1],
    [1,1,4,0,0,0,0,0,3,1,4,0,0,0,0,1],
    [1,1,4,0,0,0,0,0,3,1,4,0,0,1,1,1]
    ]
maze4 = [
    [0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [0,0,0,0,0,0,3,1,1,1,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,3,1,1,1,0,0,0,5],
    [2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2],
    [1,0,0,0,0,0,0,0,0,0,0,5,0,0,0,1],
    [1,0,0,0,2,0,0,0,0,0,0,2,0,0,0,1],
    [5,0,0,0,1,2,0,0,0,0,3,1,0,0,0,5],
    [2,0,0,0,1,1,0,0,0,0,3,1,0,0,0,2],
    [1,0,0,0,5,1,0,0,0,0,0,5,0,0,0,1],
    [1,0,0,0,2,1,0,0,0,0,0,2,0,0,0,1],
    [5,0,0,0,1,1,0,0,0,0,0,1,0,0,0,5],
    [0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,2],
    [0,0,0,0,5,1,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5]
    ]
maze5 = [
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,0,2,2,2,2,2,0,0,0,0,5,5,5,5,5],
    [0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,1,1,1,5,5,5,5,0,0,0,0],
    [0,0,0,0,0,0,3,1,0,0,0,0,0,6,0,0],
    [0,0,0,0,0,0,3,1,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,1,1,1,4,0,0,6,0,0,0,0,1,0,0],
    [1,1,1,1,1,4,0,0,1,0,0,0,0,1,0,0]
    ]
maze6 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,7,0,1,1,1,1,1,1,0,0,0,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

def draw():
    global level
    screen.clear()
    screen.fill((0,0,0))
    maze = []
    #关卡判定
    if level == 1:
        maze = maze1
    elif level == 2:
        maze = maze2
    elif level == 3:
        maze = maze3
    elif level == 4:
        maze = maze4
    elif level == 5:
        maze = maze5
    elif level == 6:
        maze = maze6
    screen.blit('background4',(0,0))
    #画云
    for cloud in C:
        cloud.draw()
    #地图碰撞箱绘制
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == 0:
                pass
            elif maze[row][column] == 1:
                block = Actor('bloc')
                block.x = column * 50 + 25
                block.y = row * 50 + 25
                blocks.append(block)
                block.draw()
            elif maze[row][column] == 2:
                hurt = Actor('hurt1')
                hurt.midbottom = (column * 50 + 25), (row * 50 + 50)
                hurts.append(hurt)
                hurt.draw()
            elif maze[row][column] == 3:
                hurt = Actor('hurt2')
                hurt.midright = (column * 50 + 50), (row * 50 + 25)
                hurts.append(hurt)
                hurt.draw()
            elif maze[row][column] == 4:
                hurt = Actor('hurt2')
                hurt.midleft = (column * 50), (row * 50 + 25)
                hurts.append(hurt)
                hurt.draw()
            elif maze[row][column] == 5:
                hurt = Actor('hurt1')
                hurt.midtop = (column * 50 + 25), (row * 50)
                hurts.append(hurt)
                hurt.draw()
            elif maze[row][column] == 6:
                jump = Actor('jump')
                jump.midbottom = (column * 50 + 25), (row * 50 + 50)
                jumps.append(jump)
                jump.draw()
            elif maze[row][column] == 7:
                sign = Actor('sign_pass')
                sign.midbottom = (column * 50 + 25), (row * 50 + 50)
                sign.draw()
    if level==1:
        screen.blit('map1',(0,0))
    elif level==2:
        screen.blit('map2',(0,0))
    elif level==3:
        screen.blit('map3',(0,0))
    elif level==4:
        screen.blit('map4',(0,0))
    elif level==5:
        screen.blit('map5',(0,0))
    elif level==6:
        screen.blit('map6',(0,0))
    player.draw()

def update():
    global left, right, GRAVITY, stand, level
    #云移动
    if random.randrange(5) == 0:
        cloud = Actor(random.choice(clouds))
        cloud.midright = 0, random.randrange(800)
        cloud.v = random.randrange(10,30)
        C.append(cloud)
    for cloud in C:
        cloud.x += cloud.v
        if cloud.left >= WIDTH:
            C.remove(cloud)
    #玩家位置限定
    if player.left < 0:
        player.left = 0
    elif player.right > WIDTH:
        player.right = WIDTH
    #玩家碰撞判定(加此处后风扇会拉满)
    #玩家移动
    if stand == 1:
        player.vy -= GRAVITY
    player.x += right + left
    player.y -= player.vy
    #关卡更新
    if player.top <= 0:
        player.vy = 0 
        level += 1
        if level == 2:
            player.midbottom=(75,600)
        elif level == 3:
            player.midbottom=(75,700)
        elif level == 4:
            player.midbottom=(25,750)
        elif level == 5:
            player.midbottom=(75,750)
        elif level == 6:
            player.midbottom=(75,750)
            
            
def on_mouse_down(pos):
    for block in blocks:
        if block.collidepoint(pos):
            print('ekk')
            break
    for hurt in hurts:
        if hurt.collidepoint(pos):
            print('ahaha')
            break
        
def on_key_down(key):
    global left, right, stand
    if key == key.LEFT:
        left = -5
    elif key == key.RIGHT:
        right = 5
    elif key == key.C:
        player.vy = 10
        stand = 1
#    global level
#    if key == key.Z:
#        level += 1
def on_key_up(key):
    global left, right
    if key == key.LEFT:
        left = 0
    elif key == key.RIGHT:
        right = 0

pgzrun.go()
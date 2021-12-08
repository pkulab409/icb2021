import pgzrun
import random

ball = Actor('ball')
b1 = Actor('board1')
b2 = Actor('board2')

WIDTH = 1000
HEIGHT = 500

b2.midbottom = WIDTH/2,HEIGHT
ball.midtop = 0, 26
b1.midtop = 0, 0 

fly = 1
move = 1
speed = 0
rounds = 0
Roundlist = [0, 0, 0, 0, 0]
j = 0

def draw():
    global rounds, Roundlist, j
    screen.clear()
    screen.fill((0, 0, 0))
    for i in range(rounds):
        count(i)
    if Roundlist.count(b1) >= 3 and Roundlist.count(b1)+Roundlist.count(b2)==5:
        screen.blit('board_lose',(0,0))
    elif Roundlist.count(b2) >=3 and Roundlist.count(b1)+Roundlist.count(b2)==5:
        screen.blit('board_win',(0,0))
    if rounds == 5 and j == 0:
        j += 1
    if rounds == 5:
        screen.blit('continue', (0,HEIGHT*2/3))
        if keyboard.c:
            exit()
    ball.draw()
    b1.draw()
    b2.draw()

def update():
    global fly, move, speed, rounds, Roundlist, j
    if speed >= 10:
        s =speed * 11 / 15
    else:
        s = speed
    if b2.left < 0:#归位
        b2.left = 0
    elif b2.right > WIDTH:
        b2.right = WIDTH
    if rounds < 5:
        b1.right += move * (s + 4)
        ball.right += move * (speed + 4)
        ball.bottom += fly * (speed + 6)
        if ball.left < 0:#弹跳
            move = 1
        elif ball.right > WIDTH:
            move = -1
        if ball.colliderect(b1):#碰撞
            fly = 1
            speed += 1
        elif ball.colliderect(b2):
            fly = -1
            speed += 1
        if ball.top < 0:#判断输赢
            rounds += 1
            Roundlist[rounds-1] = b2
            reset_ball()
        elif ball.bottom > HEIGHT:
            rounds += 1
            Roundlist[rounds-1] = b1
            reset_ball()
    if j == 1:
        stop()
    
def on_mouse_move(pos):
    if b2.left >= 0 and b2.right <= WIDTH:
        b2.x = pos[0]

def reset_ball():
    global speed
    speed = 0
    r = WIDTH*random.random()
    ball.midtop = r, 26
    b1.midtop = r, 0
    
def stop():
    ball.midtop = WIDTH/2, 53
    b1.midtop = WIDTH/2, 0

def count(n):
    if Roundlist[n] == b1:
        screen.blit('win1',(n*WIDTH/5,0))
    elif Roundlist[n] == b2:
        screen.blit('win2',(n*WIDTH/5,0))

pgzrun.go()
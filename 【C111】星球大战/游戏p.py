import pgzrun
import random


WIDTH = 1500
HEIGHT = 1200
names = ['eat']
things = []
player1 = Actor('player1')
player2 = Actor('player2')
player1.center = 200,HEIGHT-100
player2.center = WIDTH-200,HEIGHT-100
player1.score = 0
player2.score = 0
player1.life = 5
player2.life = 5
game_start = False

def on_mouse_down():
    global game_start
    game_start = True

def draw():
    global game_start,game_end1,game_end2
    if game_start == False:
        screen.clear()
        screen.blit('ksjm',(0,0))
    if game_start == True and player2.life > 0 and player1.life > 0:
        screen.clear()
        screen.blit('background',(0,0))
        for t in things:
            t.draw()
        player1.draw()
        player2.draw()    
        screen.draw.text('ENERGY:%d' % player1.score,(200,10))
        screen.draw.text('ENERGY:%d' % player2.score,(WIDTH-200,10))
        screen.draw.text('LIFE:%d' % player1.life,(200,30))
        screen.draw.text('LIFE:%d' % player2.life,(WIDTH-200,30))
    if player2.life == 0:
        screen.clear()
        screen.blit('p1win',(0,0))
    if player1.life == 0:
        screen.clear()
        screen.blit('p2win',(0,0))
def update():
    global game_start
    if game_start == True:
        if random.randrange(60) == 0:
            t = Actor(random.choice(names))
            t.center = random.randrange(WIDTH),0
            things.append(t)
        for t in things:
            t.y += 7
            if t.y >= WIDTH:
                things.remove(t)
            elif t.colliderect(player1):
                things.remove(t)
                player1.score += 1
            elif t.colliderect(player2):
                things.remove(t)
                player2.score += 1
            

def jn11():
    player1.x += 220
    player1.image = 'player1jnright'
    player1.score -= 8
    check_for_collision1()
    clock.schedule(replace1,0.5)
def jn12():
    player2.x += 220
    player2.image = 'player2jnright'
    player2.score -= 8
    check_for_collision2()
    clock.schedule(replace3,0.5)
def jn13():
    player1.x -= 220
    player1.image = 'player1jnleft'
    player1.score -= 8
    check_for_collision1()
    clock.schedule(replace2,0.5)
def jn14():
    player2.x -= 220
    player2.image = 'player2jnleft'
    player2.score -= 8
    check_for_collision2()
    clock.schedule(replace4,0.5)


def jn21():
    player1.x += 600
    player1.score -= 2
def jn22():
    player2.x += 600
    player2.score -= 2
def jn23():
    player1.x -= 600
    player1.score -= 2
def jn24():
    player2.x -= 600
    player2.score -= 2
def check_for_collision1():
    if player2.colliderect(player1):
        handle1()
def check_for_collision2():
    if player1.colliderect(player2):
        handle2()


def handle1():
    player2.life -= 1
    player2.image = 'player2_hurt'
    clock.schedule(reset_player2,0.5)
def handle2():
    player1.life -= 1
    player1.image = 'player1_hurt'
    clock.schedule(reset_player1,0.5)


def reset_player1():
    player1.image = 'player1'
def reset_player2():
    player2.image = 'player2'


def replace1():
    reset_player1()
    player1.x -= 200
def replace2():
    reset_player1()
    player1.x += 200
def replace3():
    reset_player2()
    player2.x -= 200
def replace4():
    reset_player2()
    player2.x += 200


def on_key_down(key):
    if player1.x >= 0 and player1.x <= 1440 and player2.x >= 0 and player2.x <= 1440:
        if key == keys.A:
            player1.x -= 60
        if key == keys.D:
            player1.x += 60
        if key == keys.LEFT:
            player2.x -= 60
        if key == keys.RIGHT:
            player2.x += 60
        if player1.score >= 8:
            if key == keys.S:
                jn11()
            if key == keys.W:
                jn13()
        if player2.score >= 8:
            if key == keys.DOWN:
                jn12()
            if key == keys.UP:
                jn14()
        if player1.score >= 2:
            if key == keys.H:
                jn21()
            if key == keys.G:
                jn23()
        if player2.score >= 2:
            if key == keys.M:
                jn22()
            if key == keys.N:
                jn24()
    else:   
        if player1.x < 0:
            player1.x = 0
        if player1.x > 1440:
            player1.x =1440
        if player2.x < 0:
            player2.x = 0
        if player2.x > 1440:
            player2.x = 1440

pgzrun.go()
import pgzrun
from pygame.transform import *
import random
import os

'''
debug模式

'''
g_level = 0    # 初始关卡数
superman = 1   # 1为无敌 0为正常
is_boss = 1    # 0去除boss 1为正常
is_clock_sum = 1     # 计时器是否累积 1累积模式 0不累计模式（remake，pass将重置之）
left_and_right = 0   # 1：阴间模式：左右翻转，D向左，A向右；0正常


'''
define some basic functions

'''
maxlevel = len(os.listdir('./level')) - 1  # 最大关卡数

background = scale(images.background, (1200, 800))
player_idler = ('idler_1', 'idler_2', 'idler_3')
player_idlel = ('idlel_1', 'idlel_2', 'idlel_3')
player_runr = ('runr_1', 'runr_2', 'runr_3', 'runr_4')
player_runl = ('runl_1', 'runl_2', 'runl_3', 'runl_4')
enemy_flyr = ('skeleton_1r', 'skeleton_2r', 'skeleton_3r')
enemy_flyl = ('skeleton_1l', 'skeleton_2l', 'skeleton_3l')
enemy_bullet = ('bug', 'bug', 'bug', 'bug',
                'compile error', 'wrong answer', 'time limit exceeded', 'runtime error',
                'memory limit exceeded', 'presentation error')
Clock=0

HEIGHT = 800
WIDTH = 1200

is_key_W_down = 0
g_quit = 0
g_pause = 0

def terrain_check(x,y):
    try:
        global terrainx, terrainy
        for i in range(len(terrainx) - 1):
            if terrainx[i] <= x < terrainx[i + 1]:
                try:
                    for j in range(len(terrainy[i]) - 1):
                        if y.midtop[1] + 5.5 <= terrainy[i][j] < y.midbottom[1]:
                            return terrainy[i][j]
                    return terrainy[i][-1]
                except TypeError:
                    return terrainy[i][0]
    except:
        return 800


    
def load_map(map_name):
    global terrainx,terrainy,blocks,acblocks
    with open(map_name, 'r', encoding = 'utf-8') as f:
        for row in f:
            try:
                block_info = row.strip().split()
                if len(block_info) == 2:
                    b = Actor('block')
                    b.center = (int(block_info[0]), int(block_info[1]))
                    terrainy[int(b.center[0]) // 24 + 1].append(int(b.center[1]) - 24)
                    terrainy[int(b.center[0]) // 24 + 1].sort()
                    blocks.append(b)
                elif len(block_info) >= 3:
                    if block_info[2] == '1':
                        b = Actor('block')
                        b.center = (int(block_info[0]), int(block_info[1]))
                        blocks.append(b)
                    elif block_info[2] == 'ac':
                        b = Actor('accepted')
                        b.center = (int(block_info[0]), int(block_info[1]))
                        b.tag2= block_info[3:]
                        acblocks.append(b)
                    elif block_info[2] == 'trap':
                        # The size of 'trap' is 21
                        b = Actor('trap0')
                        b.move=0
                        b.center = (int(block_info[0]), int(block_info[1]))
                        trapblocks.append(b)
                        try:
                            b.tag=block_info[3]
                            b.movespeed=block_info[4]
                        except:
                            continue
            except:
                continue
    terrainy[0].append(-100)
    terrainy[51]=[-100]



class Player(Actor):
    def __init__(self, *args):
        super().__init__(*args)
        self.timer = 0
        self.state = 'idle_right'
        self.jumpablibity = 0
        self.yspeed = 0
        self.ismovable = 1
        self.score = 100
        self.shield_release = 0
        self.shield_isready = 1
        self.shield_isappear = 0
        self.invincible = 0
        self.cdwarning = 0
        self.isalive = 1
        self.lives = 5
               
    def idle(self):
        self.timer += 1
        if self.timer % 6 == 0:
            self.timer = 0
            if self.state == 'idle_right':
                idx = player_idler.index(self.image)
                if idx <= 1:
                    self.image = player_idler[idx + 1]
                else:
                    self.image = player_idler[0]
            elif self.state == 'idle_left':
                idx = player_idlel.index(self.image)
                if idx <= 1:
                    self.image = player_idlel[idx + 1]
                else:
                    self.image = player_idlel[0]

    def run(self):
        self.timer += 1
        if self.timer % 6 == 0:
            self.timer = 0
            if self.state == 'run_right':
                idx = player_runr.index(self.image)
                if idx <= 2:
                    self.image = player_runr[idx + 1]
                    self.image = player_runr[idx + 1]
                else:
                    self.image = player_runr[0]
            elif self.state == 'run_left':
                idx = player_runl.index(self.image)
                if idx <= 2:
                    self.image = player_runl[idx + 1]
                else:
                    self.image = player_runl[0]
        if (self.state == 'run_left') and (terrain_check(self.x - 4, self) >= self.y):
            self.x -= 4
        elif (self.state == 'run_right') and (terrain_check(self.x + 4, self) >= self.y):
            self.x += 4

    def jump_and_gravity(self):
        if is_key_W_down and self.jumpablibity:
            self.jumpablibity += 1
            if self.jumpablibity == 2:
                self.yspeed += 5
            elif self.jumpablibity <= 10:
                self.yspeed += 1
            else:
                self.jumpablibity = 0
        self.y -= self.yspeed
        if self.y < terrain_check(self.x, self):
            self.yspeed -= 0.5
            if self.jumpablibity==1:self.jumpablibity=0
        else:
            self.yspeed = 0
            self.jumpablibity = 1
            self.y = terrain_check(self.x, self)
    
    def set_player_movable(self):
        self.ismovable = 1

    def shield(self):
        if self.shield_release and player.shield_isready == 1:
            sounds.release_shield.play()
            shield.x = self.x
            shield.y = self.y
            self.shield_isappear = 1
            self.invincible = 1
            clock.schedule(self.shield_disappear, 1.5)  # 1.5s持续时间        
            self.shield_isready = 0
            clock.schedule(self.set_shield_ready, 5.0)  # 5.0s冷却时间
            self.shield_release = 0
        elif self.shield_release:
            self.cdwarning = 1
            clock.schedule_unique(self.cdwarning_disappear, 0.5)
            sounds.warning.play()
            self.shield_release = 0
            
    def set_shield_ready(self):
        self.shield_isready = 1
    
    def shield_disappear(self):
        self.shield_isappear = 0
        self.invincible = 0

    def cdwarning_disappear(self):
        self.cdwarning = 0
        
    def trap_is_hit(self):
        global trapblocks
        for b in trapblocks:
            b.y+=b.move
            if b.y<=0:trapblocks.remove(b)
            if not superman:
                if b.colliderect(self):
                    self.isalive=0
                    sounds.fail.play()
                    self.lives -= 1
            try:
                if self.topright[0] >= b.topleft[0] and self.topleft[0]<=b.topright[0]:
                    if b.tag == 'move': b.move = int(b.movespeed)
            except:
                continue
    def check_player_death(self):
        if self.y > 775 or self.score <= 0:
            self.isalive = 0
            sounds.fail.play()
            self.lives -= 1

class Bullet(Actor):
    def __init__(self, image, xspeed, yspeed):
        super().__init__(image)
        self.xspeed = xspeed
        self.yspeed = yspeed



class Enemy(Actor):
    def __init__(self, *args):
        super().__init__(*args)
        self.timer = 0
        self.former_state = self.after_state = True
        # True represents flying right, False represents flying left.
            
    def shoot_bullets(self, player):
        if random.randrange(10) == 0: # 括号中数值越大，子弹密度越低
            bullet = Bullet(random.choice(enemy_bullet), random.choice((-5, -4, -3 -2, -1, 3, 4, 5)), random.choice((-5, -4, -3, 0, 1, 2, 3, 4, 5)))
            bullet.center = (self.x, self.y)
            bullets.append(bullet)
        for b in bullets:
            b.x += b.xspeed
            b.y += b.yspeed
            if not(-200 <= b.x <= 1400 and -200 <= b.y <= 1000):
                bullets.remove(b)
            elif b.colliderect(shield) and player.shield_isappear:
                bullets.remove(b)
            elif b.colliderect(player):
                bullets.remove(b)
                if not player.invincible:
                    if b.image == 'bug':
                        sounds.bug.play()
                        if not superman:
                            player.ismovable = 0
                            clock.schedule_unique(player.set_player_movable, 0.8)
                    elif b.image in {'compile error', 'presentation error'}:
                        sounds.collide.play()
                        if not superman:
                            player.score -= 10
                    elif b.image in {'wrong answer', 'time limit exceeded', 'runtime error', 'memory limit exceeded'}:
                        sounds.collide.play()
                        if not superman:
                            player.score -= 20

    def fly(self, player):
        deltax = player.x - self.x 
        deltay = player.y - self.y
        distance = (deltax ** 2 + deltay ** 2) ** 0.5
        self.x += deltax / distance * 1.5 # 最后的一个数是调节参数，其值越大移动速度越快
        self.y += deltay / distance * 1.5 # 最后的一个数是调节参数，其值越大移动速度越快
        self.after_state = (deltax >= 0)
        self.timer += 1
        if self.after_state != self.former_state:
            if self.after_state:
                self.image = 'skeleton_1r'
            else:
                self.image = 'skeleton_1l'
            self.former_state = self.after_state
        if self.after_state:
            if self.timer % 8 == 0:
                self.timer = 0
                idx = enemy_flyr.index(self.image)
                if idx <= 1:
                    self.image = enemy_flyr[idx + 1]
                else:
                    self.image = enemy_flyr[0]
        else:
            if self.timer % 8 == 0:
                self.timer = 0
                idx = enemy_flyl.index(self.image)
                if idx <= 1:
                    self.image = enemy_flyl[idx + 1]
                else:
                    self.image = enemy_flyl[0]

def on_key_up(key):
    global is_key_W_down
    if key == keys.A:
        player.image = 'idlel_1'
        player.state = 'idle_left'
    elif key == keys.D:
        player.image = 'idler_1'
        player.state = 'idle_right'
    if key == keys.W:
        is_key_W_down = 0
        player.jumpablibity = 0


def on_key_down(key):
    global is_key_W_down, g_start, g_instruction, g_quit, g_pause, g_level, game_state
    if left_and_right == 0:
        if key == keys.A:
            player.image = 'runl_1'
            player.state = 'run_left'
        elif key == keys.D:
            player.image = 'runr_1'
            player.state = 'run_right'
    else:
        if key == keys.D:
            player.image = 'runl_1'
            player.state = 'run_left'
        elif key == keys.A:
            player.image = 'runr_1'
            player.state = 'run_right'
    if key == keys.W:
        is_key_W_down = 1
        player.y -= 1
    if key == keys.J:
        player.shield_release = 1
    if key == keys.R and (game_state == 'start' or game_state == 'over'
                          or game_state == 'instruction' or game_state == 'pass'):
        g_start = 1
    if key == keys.I and game_state == 'start':
        g_instruction = 1
    if key == keys.Q and game_state == 'instruction':
        g_quit = 1
        sounds.blip.play()
        clock.schedule_unique(set_quit_0, 1.0)
    if key == keys.SPACE:
        if game_state == 'play':
            g_pause = g_pause ^ 1
        elif game_state == 'pass':
            if g_level < maxlevel:
                g_level += 1
                game_state = 'play'
                exec(f'initial_{g_level}()')
            else:
                g_level = 0
                game_state = 'play'
                exec(f'initial_{g_level}()')
def set_quit_0():
    global g_quit
    g_quit = 0

for level in range(0,maxlevel+1):
    scripts = ''
    with open(f'./level/level{level}/levelfunction{level}.txt', 'r', encoding='utf-8') as f:
        for row in f:
            scripts += row
    exec(scripts)

def game_start_draw():
    screen.draw.text('''Welcome to the Computing Final !
In this game, you are going play a role who is \nstruggling in the exam.
You should try to aviod bugs and obtain \n'Accepted' as if you were taking the exam.
''', (150, 100), color = 'black', fontsize=50, fontname='dpcomic')
    screen.draw.text("Good Luck!", (400, 350), color = 'black', fontsize=80, fontname='dpcomic')
    screen.draw.text("And enjoy yourself!", (300, 425), color = 'black', fontsize=70, fontname='dpcomic')
    screen.draw.text("Press 'R' to START.", (250, 525), color='blue', fontsize=100, fontname='dpcomic')
    screen.draw.text("Press 'I' to view the instructions.", (265, 625), color='black', fontsize=50, fontname='dpcomic')

def game_instruction_draw():
    screen.draw.text('''In this world, you're going to obtain the 'Accepted.'
A skeleton will shoot bugs and errors as his bullets, try to avoid being hit \nwith your shield.
Every 'bug' you don't miss will restain your movement for a while,
Every error you don't miss will deduct 5 or 10 points from your score \ndepending on its kind.
Whenever you release a shield, you won't be hit by bugs for a short while. \nBut there is cooldown time for shield use, so use it wisely.
You may have 5 chances.(Maybe more than that...)
TIP: You can pause the game by pressing 'SPACE'.
''', (150, 60), color='black', fontsize=30, fontname='dpcomic')
    screen.draw.text('''CONTROL:
W  JUMP
A  MOVE LEFT
D  MOVE RIGHT
J  SHIELD
''', (150, 370), color='black', fontsize=50, fontname='dpcomic')
    screen.draw.text("Press 'Q' to return to main menu.", (150, 705), color='black', fontsize=40, fontname='dpcomic')
    screen.draw.text("Press 'R' to START.", (150, 630), color='blue', fontsize=80, fontname='dpcomic')
    if g_quit == 1:
        screen.draw.text("Afraid? No, you CANNOT quit!", (700, 710), color='red', fontsize=30, fontname='dpcomic')
    
def game_play_draw():
    if player.shield_isappear:
        shield.draw()
    player.draw()
    screen.draw.text("Time:%.2f"%Clock, (1000, 13), color='red', fontsize=30, fontname='dpcomic')

    # draw map
    for b in blocks:
        b.draw()
    for b in trapblocks:
        b.draw()
   
    for b in acblocks:
        b.draw()
    
    if is_boss:
        for b in bullets:
            b.draw()
        enemy.draw() 

    if player.cdwarning:
        screen.draw.text("Your shield is NOT ready yet!", (425, 750), color='red', fontsize=30, fontname='dpcomic')
    
    if g_pause:
        screen.draw.text("Press 'SPACE' to continue.", (450, 750), color='black', fontsize=30, fontname='dpcomic')
    screen.draw.text("YOUR SCORE:%d" % player.score, (450, 15), color = 'black', fontsize=50, fontname='dpcomic')

    exec(f'ac_hints_{g_level}()')

    
def game_over_draw():
    screen.draw.text("Time:%.2f" % Clock, (1000, 13), color='red', fontsize=30, fontname='dpcomic')
    screen.draw.text("GAME OVER!\nYou        in the Final Exam!", (175, 200), color='black', fontsize=80, fontname='dpcomic')
    screen.draw.text("\nFAILED", (295, 200), color='red', fontsize=80, fontname='dpcomic')
    screen.draw.text("Press 'R' to REMAKE.", (175, 400), color='blue', fontsize=120, fontname='dpcomic')
    screen.draw.text(f"{player.lives} chance(s) left", (175, 525), color='black', fontsize=40, fontname='dpcomic')

def game_pass_draw():
    screen.draw.text(f"Your score is {player.score}, good job!", (135, 250), color='black', fontsize=50, fontname='dpcomic')
    screen.draw.text("Wanna play more?", (135, 310), color='black', fontsize=60, fontname='dpcomic')
    screen.draw.text("Pass level %d : %.2f s"%(g_level,Clock), (135, 580), color='black', fontsize=60, fontname='dpcomic')
    if g_level<maxlevel:
        screen.draw.text("Congratulations! You have passed the final exam.", (135, 200), color='black', fontsize=50,fontname='dpcomic')
        screen.draw.text("Press 'SPACE' to START NEXT LEVEL.", (135, 420), color='blue', fontsize=65, fontname='dpcomic')
    if g_level==maxlevel:
        screen.draw.text("You have passed all the exam!.", (135, 200), color='black', fontsize=50,fontname='dpcomic')
        screen.draw.text("Press 'SPACE' to BACK TO LEVEL 0.", (135, 420), color='blue', fontsize=65, fontname='dpcomic')
    screen.draw.text("Press 'R' to REMAKE.", (135, 500), color='blue', fontsize=65, fontname='dpcomic')


def game_start_update():
    global g_start, g_instruction, game_state, Clock
    if g_start == 1:
        game_state = 'play'
        sounds.blip.play()
        exec(f'initial_{g_level}()')
    if g_instruction == 1:
        game_state = 'instruction'
        sounds.blip.play()
        exec(f'initial_{g_level}()')
    if not is_clock_sum:
        Clock = 0
        
def game_instruction_update():
    global g_start, g_instruction, game_state, g_quit,Clock
    if g_start == 1:
        game_state = 'play'
        sounds.blip.play()
        exec(f'initial_{g_level}()')
        if not is_clock_sum:
            Clock = 0

def game_play_update():
    global game_state,Clock
    Clock += 1/60
    if player.isalive:
        if player.ismovable:
            if player.state == 'idle_left' or player.state == 'idle_right':
                player.idle()
            elif player.state == 'run_left' or player.state == 'run_right':
                player.run()
            player.jump_and_gravity()
        player.shield()
        player.trap_is_hit()
        player.check_player_death()

        if is_boss:
            enemy.fly(player)
            enemy.shoot_bullets(player)

        exec(f'ac_is_hit_{g_level}()')
        exec(f'draw_hidden_map_{g_level}()')
    else:
        game_state = 'over'


def game_over_update():
    global g_start, game_state, Clock
    if g_start == 1:
        game_state = 'play'
        sounds.blip.play()
        exec(f'initial_{g_level}()')
        if not is_clock_sum:
            Clock = 0

def game_pass_update():
    global g_start, game_state, Clock
    if g_start == 1:
        game_state = 'play'
        sounds.blip.play()
        exec(f'initial_{g_level}()')
        if not is_clock_sum:
            Clock = 0
'''
main program
'''
player = Player('idler_1')
shield = Actor('shield')
enemy = Enemy('skeleton_1r')

game_state = 'start'

exec(f'initial_{g_level}()')


def draw():
    screen.clear()
    screen.blit(background, (0, 0))
    if game_state == 'start':
        game_start_draw()
    elif game_state == 'instruction':
        game_instruction_draw()
    elif game_state == 'play':
        game_play_draw()
    elif game_state == 'over':
        game_over_draw()
    elif game_state == 'pass':
        game_pass_draw()
def update():
    if game_state == 'start':
        game_start_update()
    elif game_state == 'instruction':
        game_instruction_update()
    elif game_state == 'play':
        if not g_pause:
            game_play_update()
    elif game_state == 'over':
        game_over_update()
    elif game_state == 'pass':
        game_pass_update()

pgzrun.go()
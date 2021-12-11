from random import *
import sys
import Plants
import Products
import SeedBank
import LawnMower
import Zombies
import pgzrun
from pgzero.actor import Actor
import os
import time
#####################################################################################################################################
os.chdir(sys.path[0])
TITLE = '保卫绩点————Battle for GPA'
bg_size = WIDTH,HEIGHT = 800,600
ticktime =1

# 颜色
BLACK = (0,0,0)
RED = (255,0,0)
BAR_COLOR = (189,223,89)

# 植物种植范围
borderx = L, R = 30, 780
bordery = T, B = 90, 570
X = [75, 155, 235, 322, 406, 480, 562, 641, 720]
Y = [135, 225, 325, 427, 523]

# 载入图片
zombies_images = Zombies.ZombiesImages()
plants_images = Plants.PlantsImages()
products_images = Products.ProductsImages()
car_image = LawnMower.CarImage()

def order_zombies():
    global zombies

    order_zombies = []
    for z in zombies:
        order_zombies.append(z)
    num = len(order_zombies)
    for i in range(num):
        index_top = i
        zombie_top = order_zombies[i]
        for j in range(i+1,num):
            if zombie_top.y > order_zombies[j].y:
                index_top = j
                zombie_top = order_zombies[j]
        order_zombies[index_top] = order_zombies[i]
        order_zombies[i] = zombie_top

def add_ordinaryzombies(group,num):
    global zombie_level
    for i in range(num):
        y = choice(Y)
        time.sleep(0.002)
        oz = Zombies.OrdinaryZombie(WIDTH, y, zombies_images,zombie_level)
        group.append(oz)
    order_zombies()

def add_coneheadzombies(group,num):
    global zombie_level
    for i in range(num):
        y = choice(Y)
        time.sleep(0.002)
        cz = Zombies.ConeheadZombie(WIDTH, y, zombies_images,zombie_level)
        group.append(cz)
    order_zombies()

def add_bucketheadzombies(group,num):
    global zombie_level
    for i in range(num):
        y = choice(Y)
        time.sleep(0.002)
        bz = Zombies.BucketheadZombie(WIDTH, y, zombies_images,zombie_level)
        group.append(bz)
    order_zombies()

def add_flagzombies(group,num):
    global zombie_level
    for i in range(num):
        y = choice(Y)
        fz = Zombies.FlagZombie((WIDTH + 50), y, zombies_images,zombie_level)
        group.append(fz)
    order_zombies()

#######################################################################################################################################################
# 音频播放
open_music = True
open_sound = True
play_gameover_sound = False

 # 准备植物组合
plantx=[]
# 种植的植物组合
plants=[]
# 产物集合
products = []

# 准备生成向日葵
sunflowerx = Plants.SunFlower(plants_images)
plantx.append(sunflowerx)
# 准备生成豌豆射手
peashooterx = Plants.Peashooter(plants_images)
plantx.append(peashooterx)
# 准备生成坚果
wallnutx = Plants.WallNut(plants_images)
plantx.append(wallnutx)
# 准备生成火炬
torchwoods = [] # 用于与弹丸做碰撞检测
# 生成铲子
shovel = Plants.Shovel(plants_images)
plantx.append(shovel)
#level up 准备
level_upx = Plants.Level_up(plants_images)
plantx.append(level_upx)

# 判断拖拽的图像是否出界
outborder = False

# 僵尸大波袭来
large_come = False
large_coming = False
large_time = 40 * ticktime
large_warn_time = 3 * ticktime

# 生成5辆小车
cars = []
cars_temp = []
for i in range(5):
    cars_temp.append(LawnMower.Car(L))
i = 0
for y in Y:
    cars_temp[i].y = y -25
    i += 1
for c in cars_temp:
    cars.append(c)

# 僵尸组合
zombies = []

# 游戏界面
bg_image = Actor("others/background",topleft=(-200, 0))
bar_image = Actor("others/flagmeterempty",topleft=(WIDTH - 200, HEIGHT - 27))
bar_parts1_image = Actor("others/flagmeterparts1",topleft=(WIDTH - 68 - 1, HEIGHT - 32))
bar_parts2_image = Actor("others/flagmeterparts2",topleft=(WIDTH - 200, HEIGHT - 30))
largewave_image = Actor("others/largewave",center=(WIDTH // 2, HEIGHT // 2))
seedbank = SeedBank.SeedBank()

# 菜单界面
open_menu = False
open_instruction = False
menu_image = Actor("others/menu",center=(WIDTH // 2, HEIGHT // 2))  
button_image = Actor("others/button_nor",topright=(WIDTH, 0))
instruction_image = Actor("others/selectorscreen_almanac",topright=(WIDTH-15,40))
resume_image = Actor("others/resume_nor",topright=(500, 408))
check_box_image1 = Actor("others/check_box",center=(450, 260))
check_box_image2 = Actor("others/check_box",center=(450, 297))
tick_image1 = Actor("others/tick",center=(450, 260))
tick_image2 = Actor("others/tick",center=(450, 297))
quitgame_image = Actor("others/quitgame_nor",topleft=(318, 352))
book_image = Actor("others/book/book_1",center=(WIDTH//2,HEIGHT//2))
book_list = []
book_list.extend([\
    "others/book/book_1",\
    "others/book/book_2",\
    "others/book/book_3",\
    "others/book/book_4",\
    "others/book/book_5",\
    "others/book/book_6",\
    "others/book/book_7" \
    ])
book_image_index = 0

# 游戏结束界面
gameover = False
you_win = False
you_win_over = False
open_quit_window = False
zombiewon_display_time = 7 * ticktime
zombiewon_image = Actor("others/zombieswon",center=(WIDTH // 2, HEIGHT // 2))
you_win_image = Actor("others/trophy",center = (WIDTH // 2, HEIGHT // 2))
you_win_over_image = Actor("others/win1",center = (WIDTH // 2, HEIGHT // 2))
quit_window_image = Actor("others/exit_window",center=(WIDTH // 2, HEIGHT // 2))
quit_image = Actor("others/quit_nor",center=(WIDTH // 2 ,380))

# 游戏开始界面
start = False
start_ready = False
open_help = False
tips1_read = False
tips2_read = False
cb_ready = False
tips1_read_delay = 20
start_bg_image = Actor("others/start_background")
game_logo_image = Actor("others/game_logo")
game_logo_image.left, game_logo_image.top = 13, -game_logo_image.height
exit_image = Actor("others/exit_nor",topleft=(730, 515))
help_doc_image = Actor("others/help",center=(WIDTH // 2, HEIGHT // 2))
off_help_image = Actor("others/off_help",topleft=(615, 120))
prepare_tip_images = []
prepare_tip_images.extend([\
    "others/preparegrowplants1", \
    "others/preparegrowplants2", \
    "others/preparegrowplants3" \
    ])
prepare_tip_rect = Actor("others/preparegrowplants1",center=(WIDTH // 2, HEIGHT // 2))
index_prepare_tip_image = -1
num_prepare_tip_image = 3

#tips
cb = Actor('others/cb',bottomright=(0,HEIGHT))
tips_fight = Actor('others/fight_for_your_gpa',center=(WIDTH // 2, HEIGHT // 2))
tips_final = Actor('others/the_final_is_come',center=(WIDTH // 2, HEIGHT // 2))

# 植物影子图片
plantshadow = Actor("others/plantshadow")
################################################
# 阳光数量
sun_num = 50
COLOR = BLACK
# 阳光集合
suns = []

# 阳光补给和消失时间
supply_time = 6* ticktime
disappear_time1 = 12* ticktime
disappear_time2 = 8* ticktime

# 计时器
count_time = 0
play_time = 0

# 弹丸集合
bullets = []

# 用于切换图片
delay_1 = 8 
delay_2 = 7 
delay_3 = 50 
delay_4 = 0

# 是否选中植物
select = 0

# 游戏进度条长度
bar_length = 1

# 关卡数
level = 1

#植物等级
plant_level = 1
zombie_level = level

# 总分/绩点
gpa_score = 0

def score_to_gpa(score):
    if score >= 300000:
        return 4.0
    elif score <= 10000:
        return 1
    elif 10000<score<=50000:
        return 1.5
    elif 50000<score<=210000:
        return 2.3
    else:
        x=score/300000
        return 4-3*((100-x)**2/1600)
# 外挂参量
jfsh = False

########################################################################################
#从卡片拖动生成植物用
pos_price=0
pos_image = Actor('plants/sunflower/sunflower1')
darw_pos_image = False
plant_index = 0

def on_mouse_down(pos,button):
    global select
    global pos_image
    global pos_price
    global plant_index
    global open_menu
    global open_instruction
    global open_help
    global gameover
    global start_ready
    global start
    global open_sound
    global open_music
    global cb_ready
    global tips1_read
    global tips2_read
    global tips1_read_delay
    global plants
    global plantx
    global plant_level
    global sun_num
    global book_image_index
    global you_win
    global you_win_over

    if not start and start_bg_image.collidepoint(pos):
        start = True

    if cb_ready and tips_fight.collidepoint(pos) and not tips1_read:
        tips1_read = True

    if cb_ready and tips_final.collidepoint(pos) and tips1_read and not tips2_read and tips1_read_delay ==0:
        tips2_read=True

    # 选择植物卡片
    if not open_menu and not open_instruction and not gameover and start_ready:
        for px in plantx:
            if button == mouse.LEFT  and px.collidepoint(pos):
                if px.index==6:
                    if sun_num > px.price:
                        sun_num -= px.price
                        plant_level += 1
                        if plant_level == 3:
                            torchwoodx = Plants.Torchwood(plants_images,level=2)
                            plantx.append(torchwoodx)
                        for p in plants:
                            p.level_up()
                        for px in plantx:
                            px.level_up()
                else:
                    plant_index = px.index
                    pos_image.image = px.images[0]
                    pos_image.pos = pos
                    pos_price = px.price
                    if sun_num < pos_price:
                        COLOR = RED
                    select = 1
            if select == 1:
                if button == mouse.RIGHT and pos_image.collidepoint(pos):
                    select = 0
    # 收集阳光
        for s in suns:
            if (button==mouse.LEFT and s.collidepoint(pos)):
                s.gather = True
                if open_sound:
                    sounds.sungather.play()

# 菜单操作
    if not gameover and start_ready:
        if button == mouse.LEFT and button_image.collidepoint(pos):
            open_menu = True
        if button == mouse.LEFT and instruction_image.collidepoint(pos):
            open_instruction = True
        if button == 1 and quitgame_image.collidepoint(pos) and open_menu:
            sys.exit()
    
    if not gameover:
        if button == 1 and resume_image.collidepoint(pos):
            open_menu = False
        if button == 1 and check_box_image1.collidepoint(pos) and open_menu:
            if open_sound:
                open_sound = False
            else:
                open_sound = True
        if button == 1 and check_box_image2.collidepoint(pos) and open_menu:
            if open_music:
                open_music = False
                music.pause()
            else:
                open_music = True
                music.unpause()

    if not gameover:
        if button == 1 and book_image.collidepoint(pos) and open_instruction:
            if book_image_index <6:
                book_image_index += 1
            book_image.image = book_list[book_image_index]
    
    if you_win and you_win_image.collidepoint(pos):
        you_win_over = True

# 游戏初始界面操作 
    if not start:
        if button == 1 and exit_image.collidepoint(pos) and not open_menu and not open_instruction and not open_help:
            sys.exit()
        if button == 1 and off_help_image.collidepoint(pos) and open_help:
            open_help = False
    # 游戏结束窗口操作
    if gameover:
        if button == 1 and quit_image.collidepoint(pos):
            sys.exit()

def on_mouse_up(pos,button):
    global darw_pos_image
    global select
    global sun_num
    global bullets 
    global products
    global plant_level
    global open_instruction

    darw_pos_image = False
    if not open_menu and not open_instruction and not gameover and start_ready:
        if button == mouse.LEFT:
            if select == 1:
                if not outborder:
                    # 生成植物
                    if plant_index == 1:
                        plant = Plants.SunFlower(plants_images,plant_level)
                    if plant_index == 2:
                        plant = Plants.Peashooter(plants_images,plant_level)
                    if plant_index == 3:
                        plant = Plants.WallNut(plants_images,plant_level)
                    if plant_index == 4:
                        plant = Plants.Torchwood(plants_images,plant_level)
                    if plant_index == 5:
                        plant = Plants.Shovel(plants_images)
                    plant.pos = pos
                    plant.image = plant.images[0]
                    # 位置调整
                    minx = X[0]
                    miny =Y[0]
                    for x in X:
                        if abs(plant.x - x) < abs(plant.x - minx):
                            minx = x
                    plant.x = minx
                    for y in Y:
                        if abs(plant.y - y) < abs(plant.y - miny):
                            miny = y
                    plant.y = miny
                    # 检查位置是否已有植物
                    have_plant = False
                    for p in plants:
                        if (plant.x == p.x) and \
                                (plant.y == p.y):
                            have_plant = True
                            if plant_index == 5:
                                plants.remove(p)
                                if p.index == 4:
                                    torchwoods.remove(p)
                    if not have_plant and (plant_index != 5) and (sun_num >= plant.price):
                        plants.append(plant)
                        sun_num -= plant.price
                        if plant.index == 4:
                            torchwoods.append(plant)
                select = 0
                COLOR = BLACK

def on_mouse_move(pos, rel, buttons):

    global button_image
    global instruction_image
    global resume_image
    global quitgame_image
    global quit_image
    global exit_image
    global pos_image
    global darw_pos_image
    global outborder
    global open_instruction

    # 所以button的按压样式
    if button_image.collidepoint(pos) and not open_menu and not open_instruction:
        button_image.image = "others/button_pressed"
    else:
        button_image.image = "others/button_nor"
    if instruction_image.collidepoint(pos) and not open_instruction:
        instruction_image.image = "others/selectorscreen_almanachighlight"
    else:
        instruction_image.image = "others/selectorscreen_almanac"
    if resume_image.collidepoint(pos) and open_menu:
        resume_image.image = "others/resume_pressed"
    else:
        resume_image.image = "others/resume_nor"
    if quitgame_image.collidepoint(pos) and start_ready:
        quitgame_image.image = "others/quitgame_pressed"
    else:
        quitgame_image.image  = "others/quitgame_nor"
    if quit_image.collidepoint(pos) and gameover:
        quit_image.image  = "others/quit_pressed"
    else:
        quit_image.image  = "others/quit_nor"
    if exit_image.collidepoint(pos) and not start and not open_menu and not open_instruction and not open_help:
        exit_image.image  = "others/exit_pressed"
    else:
        exit_image.image  = "others/exit_nor"
    
    # 绘制拖拽的植物图像
    if mouse.LEFT in buttons: 
        if not gameover:
            if select == 1 and (sun_num >= pos_price):
                darw_pos_image = True
                pos_image.pos = pos
                if (pos_image.x < L or pos_image.x > R or pos_image.y < T or pos_image.y > B):
                    outborder = True
                else:
                    outborder = False

# 外挂
key_dict={i:False for i in range(30)} #1~26为A~Z,27=ctrl
def on_key_down(key):
    global key_dict
    global gameover
    global open_menu
    global open_instruction

    if start_ready and not gameover and not open_menu and not open_instruction:
        if 97<= int(key) <= 122:
            key_dict[int(key)-96] = True
        if key == key.LCTRL:
            key_dict[27] = True
    
    if open_instruction and key == keys.ESCAPE:
        open_instruction = False

def on_key_up(key):
    global key_dict
    global gameover
    global open_menu
    global open_instruction

    if start_ready and not gameover and not open_menu and not open_instruction:
        if 97<= int(key) <= 122:
            key_dict[int(key)-96] = False
        if key == key.LCTRL:
            key_dict[27] = False

clockcount = 0
def up_clock_count():
    global clockcount
    clockcount+=1

clock.schedule_interval(up_clock_count, 1.0)

def update():
    global count_time
    global play_time
    global delay_1  
    global delay_2  
    global delay_3
    global delay_4
    global large_coming
    global bar_length
    global large_come
    global large_time
    global large_warn_time
    global zombiewon_display_time
    global gameover
    global index_prepare_tip_image 
    global clockcount
    global level
    global tips1_read
    global tips1_read_delay
    global zombie_level
    global plant_level
    global plantx
    global sun_num
    global jfsh
    global gpa_score
    global you_win
    global open_instruction

    if you_win:
        you_win_image.draw()
        return
    if clockcount == count_time : #此if下的进程每秒update 1次
        count_time += 1

        if start_ready and not gameover and not open_menu and not open_instruction:
            play_time += 1

            # 游戏进度条
            if not large_coming:
                if level<=2:
                    bar_length += 1
                if 2<level<=6:
                    bar_length += 2
                if 6<level<=8:
                    bar_length += 4

                if level<=3:
                    if bar_length == 8:
                        add_ordinaryzombies(zombies,1)
                    if bar_length == 24:
                        add_ordinaryzombies(zombies,2)
                        if level == 2:
                            add_ordinaryzombies(zombies,1)
                        elif level == 3:
                            add_coneheadzombies(zombies,1)
                    if bar_length == 48:
                        add_ordinaryzombies(zombies,2)
                        if level == 3:
                            add_coneheadzombies(zombies,2)
                    if bar_length == 64:
                        add_ordinaryzombies(zombies,2)
                        if level == 2:
                            add_ordinaryzombies(zombies,2)
                        elif level == 3:
                            add_coneheadzombies(zombies,3)
                    if bar_length == 96:
                        add_ordinaryzombies(zombies,2+level)
                        if level == 3:
                            add_coneheadzombies(zombies,2)
                    if bar_length == 108:
                        add_ordinaryzombies(zombies,5)
                        if level == 3:
                            add_coneheadzombies(zombies,2)
                
                elif 3<level<=6:
                    if bar_length == 8:
                        add_ordinaryzombies(zombies,2)
                        add_coneheadzombies(zombies,1)
                    if bar_length == 24:
                        add_ordinaryzombies(zombies,3)
                        if level == 6:
                            add_coneheadzombies(zombies,2)
                        add_bucketheadzombies(zombies,1)
                    if bar_length == 48:
                        add_ordinaryzombies(zombies,2)
                        add_coneheadzombies(zombies,level-1)
                        add_bucketheadzombies(zombies,level-2)
                    if bar_length == 96:
                        add_ordinaryzombies(zombies,3+level)
                        add_coneheadzombies(zombies,4)
                        add_bucketheadzombies(zombies,level)
                    if bar_length == 112:
                        add_coneheadzombies(zombies,5)
                elif 6<level<=8:
                    if bar_length==4:
                        add_ordinaryzombies(zombies,4)
                        add_coneheadzombies(zombies,3)
                    if bar_length%32==0:
                        add_ordinaryzombies(zombies,3)
                        add_coneheadzombies(zombies,3)
                    if bar_length%48==0:
                        add_bucketheadzombies(zombies,3)
                else:
                    if not zombies:
                        you_win = True

                if bar_length >= 128:
                    large_coming = True
                    if not large_come:
                        large_come = True
                        # 生成举旗僵尸
                        add_flagzombies(zombies, 1)
                        # 增加僵尸数量
                        add_ordinaryzombies(zombies,3+level)
                        if level<=4:
                            add_coneheadzombies(zombies,level)
                        else:
                            add_coneheadzombies(zombies,4)
                        if level >3:
                            add_bucketheadzombies(zombies,level-2)
                        # 僵尸大波袭来位置改变
                        i = 0
                        for z in zombies:
                            if z.left > WIDTH:
                                z.left = WIDTH + 50 + (i * 20)
                                i += 1
                                if i > 5:
                                    i = 0
                else:
                    large_coming = False
                if bar_length >= 128:
                    bar_length = 128

            # 僵尸大波袭来时间
            if large_coming:
                large_time -= 1 * ticktime
                large_warn_time -= 1 * ticktime
                if large_time == 0 or not zombies:
                    large_coming = False
                    large_come = False
                    large_time = 40 * ticktime + 10*level
                    large_warn_time = 3 * ticktime
                    level += 1
                    zombie_level = level
                    bar_length = 0

            # 弹丸发射
            for p in plants:
                if p.index==2:
                    if p.count_time>0:
                        p.count_time -= 1
                    for z in zombies:
                        if (z.right > p.right) and (z.x < WIDTH) \
                                and (z.y == p.y - 25) and not z.die \
                                and p.count_time <= 0:
                                
                            bullet = Products.Bullet(bg_size, (p.left,p.top),products_images,p.level)
                            bullets.append(bullet)
                            products.append(bullet)
                            bullet.shoot = True
                            p.count_time += 4-(p.level-1)*0.3

            # 生成阳光
            if (play_time % supply_time == 0):
                sun = Products.Sun(9, randint(125,470),products_images,plant_level)
                suns.append(sun)
                products.append(sun)

            for s in suns:
                s.count_time += 1

            for p in plants:
                if p.index == 1:
                    p.count_time += 1 * ticktime
                    if (p.count_time % p.create_time == 0):
                        sun = Products.Sun(p.top, p.left,products_images,p.level)
                        sun.is_supply = False
                        sun.position = p.top-50
                        sun.count_time = 1 * ticktime
                        suns.append(sun)
                        products.append(sun)
            for s in suns:
                if jfsh and s.count_time > 1:
                    s.gather = True
                if (s.count_time % disappear_time1 == 0) and s.is_supply:
                    suns.remove(s)
                    products.remove(s)
                if (s.count_time % disappear_time2 == 0) and not s.is_supply:
                    suns.remove(s)
                    products.remove(s)
 
            # 植物被攻击
            for p in plants:
                if p.attacked:
                    p.blood -= p.num_az
                    p.num_az = 0
                    if open_sound:
                        sounds.chew.play()
                    if p.index==3:
                        if p.blood <= p.blood_max*0.6:
                            p.pf = False
                        if p.blood_max*0.2 <= p.blood <= p.blood_max*0.6 and p.images != p.c1_images:
                            p.images = p.c1_images
                            p.index_image = p.index_c1_image
                            p.num_image = p.num_c1_image
                        if p.blood < p.blood_max*0.2 and p.images != p.c2_images:
                            p.images = p.c2_images
                            p.index_image = p.index_c2_image
                            p.num_image = p.num_c2_image
                if p.blood <= 0:
                    plants.remove(p)
                    if p.index == 4:
                        torchwoods.remove(p)
                    del p

        elif gameover:
            zombiewon_display_time -= 1
            if zombiewon_display_time == 0:
                open_quit_window = True
    
    if tips1_read and tips1_read_delay>0:
        tips1_read_delay -=1

    if start_ready and not open_menu and not open_instruction and not gameover:
        # 检测僵尸是否攻击植物
        for z in zombies:
            if z.die:
                continue
            attack = 0
            if z.attack:
                z.attack_delay-=1
                if z.attack_delay ==0:
                    z.attack_delay = 60
            for p in plants:
                if (z.y == p.y - 25):
                    if z.x >= p.x - 50 and z.x <= p.x + 45:
                        p.attacked = True
                        attack +=1
                        if z.attack_delay == 59:
                            p.num_az += z.level
                        break
            if attack:
                if not z.attack and not z.willdie:
                    z.attack = True
                    z.attack_delay = 60

                    z.left -= 10
                    if z.index == 1 or z.index == 4:
                        z.images = z.za_images
                        z.index_image = z.index_za_image
                        z.num_image = z.num_za_image
                    if (z.index == 2 or z.index == 3) and z.hat:
                        z.images = z.za_images
                        z.index_image = z.index_za_image
                        z.num_image = z.num_za_image
                    if (z.index == 2 or z.index == 3) and not z.hat:
                        z.images = z.hza_images
                        z.index_image = z.index_hza_image
                        z.num_image = z.num_hza_image
                if not z.attack and z.willdie:
                    z.attack = True
                    z.left -= 10
                    z.images = z.zlha_images
                    z.index_image = z.index_zlha_image
                    z.num_image = z.num_zlha_image
            else:
                if z.attack and not z.willdie:
                    z.attack = False
                    if z.index == 1 or z.index == 4:
                        z.images = z.oz_images
                        z.index_image = z.index_oz_image
                        z.num_image = z.num_oz_image
                    if (z.index == 2 or z.index == 3) and z.hat:
                        z.images = z.oz_images
                        z.index_image = z.index_oz_image
                        z.num_image = z.num_oz_image
                    if (z.index == 2 or z.index == 3) and not z.hat:
                        z.images = z.hoz_images
                        z.index_image = z.index_hoz_image
                        z.num_image = z.num_hoz_image
                if z.attack and z.willdie:
                    z.attack = False
                    z.images = z.zlh_images
                    z.index_image = z.index_zlh_image
                    z.num_image = z.num_zlh_image

        # 检测僵尸是否被弹丸攻击
        for z in zombies:
            attack_bullets = []
            for b in bullets:
                if b.shoot and not z.die:
                    if b.y == z.y+7 and(b.x > z.x and b.x < z.x+20):
                        attack_bullets.append(b)
                        bullets.remove(b)

            for ab in attack_bullets:
                if open_sound:
                    sounds.hit.play()
                if ab.is_bullet:
                    z.blood -= 1+(b.level-1)*0.2
                else:
                    z.blood -= 2+(b.level-1)*0.5
                attack_bullets.remove(ab)
                del ab
                
                if z.blood<=12 and (z.index == 2 or z.index == 3): #有帽子掉帽子
                    if z.hat:
                        z.hat = False
                        if z.attack:
                            z.images = z.hza_images
                            z.index_image = z.index_hza_image
                            z.num_image = z.num_hza_image
                        else:
                            z.images = z.hoz_images
                            z.index_image = z.index_hoz_image
                            z.num_image = z.num_hoz_image

                if 0<z.blood<=2 and not z.willdie and z.index == 1:  #普通僵尸掉头
                    z.willdie = True
                    
                    z.zh_rect.x,z.zh_rect.y = z.x + 50,z.y - 20
                    if z.attack:
                        z.images = z.zlha_images
                        z.index_image = z.index_zlha_image
                        z.num_image = z.num_zlha_image
                    if not z.attack:
                        z.images = z.zlh_images
                        z.index_image = z.index_zlh_image
                        z.num_image = z.num_zlh_image
                    
                if z.blood <= 0 and not z.die:
                    z.die = True
                    if z.index == 2 or z.index == 3:
                        z.explosion = True
                    z.left -= 10
                    z.images = z.zd_images  # 原始僵尸1图片
                    z.index_image = z.index_zd_image
                    z.num_image = z.num_zd_image
                    gpa_score += int(z.x/10)*z.level*z.index
                    #爆炸周围植物掉血，掉一次
                    for p in plants:
                        prect = Rect(p.x-40,p.y-45,80,90)
                        zrect = Rect(z.x-30,z.y-30,60,60)
                        if zrect.colliderect(prect):
                            if z.level<=3:
                                p.blood -= z.level
                            if z.level>3:
                                p.blood -= z.level*3

        # 检测僵尸是否与小车碰撞
        for z in zombies:
            for c in cars:
                if c.right <= WIDTH and (c.y == z.y ):
                    if not z.die:
                        if (z.index==2 or z.index==3) and z.hat:
                            zrect=Rect(z.left+115,z.top,z.width-80,z.height-100)
                        else:
                            zrect = Rect(z.left+75,z.top,z.width-105,z.height-40)
                        if c.colliderect(zrect):
                            c.active = True
                            z.die = True
                            
        # 检测弹丸是否穿过火炬
        for b in bullets:
            if b.shoot and b.is_bullet:
                for t in torchwoods:
                    if b.colliderect(t._rect):
                        b.is_bullet = False
                        b.level += t.level**2

        # 检测僵尸是否进入房子（游戏结束）
        for z in zombies:
            if z.right < 0 and not z.die:
                gameover = True
                z.bottom = 400
                z.get_win = True

        # 外挂系统检测
        if key_dict[27] == True and delay_4 == 0:
            if key_dict[ord('c')-96] == True and key_dict[ord('b')-96] == True:
                sun_num += 1000
                delay_4 = 40
            if key_dict[ord('p')-96] == True and key_dict[ord('f')-96] == True:
                for p in plants:
                    if p.index == 3 and (not p.pf):
                        p.pf = True
                        p.npf()
                        delay_4 = 80
            if key_dict[ord('j')-96] == key_dict[ord('f')-96] == key_dict[ord('s')-96] == key_dict[ord('h')-96] == True:
                if not jfsh:
                    jfsh = True
                    print('Congratulations! You jfsh!')

        if delay_4 > 0:
            delay_4 -= 1

    if gameover:
        for z in zombies:
            if z.left < 0 and not z.get_win:
                z.x = L    

        
# 图片索引值、摆动帧率
    if not open_menu and not open_instruction and start:
        if not gameover:
            for p in plants:
                if delay_1 == 8:
                    p.index_image += 1
                if p.index_image == p.num_image:
                    p.index_image = 0
                p.image = p.images[p.index_image]
            for pr in products:
                if delay_1 == 8:
                    pr.index_image += 1
                if pr.index_image == pr.num_image:
                    pr.index_image = 0
        for z in zombies:
            if not gameover or z.get_win:
                if z.willdie:
                    if delay_1 == 8 and (z.index_zh_image < z.num_zh_image + 10):
                        z.index_zh_image += 1
                if z.die:
                    if delay_2 == 7 and (z.index_zd_image < z.num_zd_image + 8):
                        z.index_zd_image += 1
                if z.index >1:#其他僵尸
                    if z.black :
                        if delay_2 == 7 and (z.index_zd_black_image < z.num_zd_black_image ):    
                            z.index_zd_black_image += 1
                if delay_1 == 8:
                    z.index_image += 1
                if z.index_image == z.num_image:
                    z.index_image = 0
        delay_1 -= 1
        delay_2 -= 1
        if delay_1 == 0:
            delay_1 = 8
        if delay_2 == 0:
            delay_2 = 7

    if not start_ready and start and cars_temp[0].right == L + 54:
        delay_3 -= 1
        if delay_3 == 0:
            delay_3 = 50
        if delay_3 == 50:
            index_prepare_tip_image += 1
    
def draw():   
    global sun_num
    global gameover
    global start_ready
    global start
    global select
    global zombiewon_display_time
    global clockcount
    global index_prepare_tip_image
    global play_gameover_sound
    global tips1_read
    global tips2_read
    global cb_ready
    global plant_level
    global you_win
    global you_win_over
    global gpa_score
    global cars

    screen.clear()

    if you_win or you_win_over:
        if you_win and not you_win_over:
            you_win_image.draw()
        if you_win_over:
            you_win_over_image.draw()
            gpa_score += 2000*len(cars)
            screen.draw.text(f'{score_to_gpa(gpa_score):.3f}',(140, 527), fontname="corisandebold.otf", fontsize=40, color=(0,0,0))
            screen.draw.text("The game is over! Congratulations!",(60, 10), fontname="corisandebold.otf", fontsize=40, color=(240,0,0))
        return

    if not start: 
        start_bg_image.draw()

    elif start and not tips2_read:
        bg_image.draw() 
        if cb.right < cb.width:
            cb.left += 2
        if cb.right >= cb.width:
            cb_ready = True
        cb.draw()

        if cb_ready:
            screen.draw.text('Click tips to continue', (WIDTH//2, 550), fontname="corisandebold.otf", fontsize=40, color=(0,0,0))
            if not tips1_read:
                tips_final.draw()
            if tips1_read and not tips2_read:
                tips_fight.draw()

    else:
        # 绘制游戏背景
        if gameover:
            speed = 5
            bg_image.left += speed
            if bg_image.left > 0:
                bg_image.left = 0
            else:
                # 调整所有对象位置
                for p in plants:
                    p.left += speed
                for z in zombies:
                    z.left += speed
                    z.zh_rect.left += speed
                for s in suns:
                    if s.is_supply:
                        s.rect1.left += speed
                    else:
                        s.rect2.left += speed
                for b in bullets:
                    b.left += speed
                for c in cars:
                    c.left += speed
        bg_image.draw()

        if not gameover:
            # 绘制游戏进度条
            if start_ready:
                bar_image.draw()
                bar_parts2_image.draw()
                line_box = Rect(WIDTH - 51 - bar_length,HEIGHT - 19,bar_length,5.5)
                screen.draw.filled_rect(line_box, BAR_COLOR)
                bar_parts1_image.left = WIDTH - 68 - bar_length
                bar_parts1_image.draw()              

            # 绘制卡片栏            
            if not open_menu and not open_instruction and not gameover:
                seedbank.move()
            seedbank.draw()
            # 绘制卡片栏里的卡片
            if seedbank.position:
                for px in plantx:
                    px.image=px.card_image
                    px.draw()
                    if px.index==1 or px.index==3:
                        px_pos = (px.x-12,px.y+18)
                    if px.index==2 or px.index==4:
                        px_pos = (px.x-16,px.y+18)
                    if px.index==6:
                        px_pos = (px.x-19.5,px.y+18)
                    if px.index != 5:
                        screen.draw.text(f'{px.price}', px_pos, fontname="corisandebold.otf", fontsize=12, color=(0,0,0))


        # 绘制5辆小车
        if seedbank.position:
            for c in cars:
                if not open_menu and not open_instruction and not gameover:
                    if not c.active:
                        c.move1()
                    else:
                        c.move2()
                c.draw()
                if c.left > WIDTH:
                    cars.remove(c)
        
        if tips2_read and not start_ready:
            screen.draw.text(str(sun_num), (58, 63), fontname="corisandebold.otf", fontsize=19, color=(0,0,0))
            # 绘制准备种植植物提示
            if -1 < index_prepare_tip_image < 3 and cars_temp[0].right == L +54:
                prepare_tip_rect.image = prepare_tip_images[index_prepare_tip_image]
                prepare_tip_rect.draw()
            if index_prepare_tip_image >= 3:
                start_ready = True
                if open_music:
                    music.play('game')
        else:
            # 绘制植物
            for p in plants:
                p.draw()
                pos=(p.x-5,p.y+20)                
                screen.draw.text(str(p.level), pos, fontname="corisandebold.otf", fontsize=20, color=(0,0,0))
                blood_percent = p.blood/p.blood_max
                blood_line=Rect(p.x-30,p.y-35,blood_percent*60,5) 
                if blood_percent>= 0.2:
                    line_color = 'green'
                else:
                    line_color = 'red'
                screen.draw.filled_rect(blood_line,line_color)

            # 绘制僵尸
            remove_zombies=[]
            for z in zombies:
                if not z.die:
                    if delay_1 == 8 and not z.attack:
                        if not open_menu and not open_instruction and not gameover:
                            z.move()
                    z.image = z.images[z.index_image]
                    z.draw()
                else:
                    if (z.index_zd_image < z.num_zd_image + 8):
                        index2 = z.index_zd_image
                        if z.index_zd_image >= z.num_zd_image:
                            index2 = z.num_zd_image - 1
                        z.image = z.zd_images[index2]
                        z.draw()
                    else:
                        if z.index >1:
                            z.black = True
                            if (z.index_zd_black_image < z.num_zd_black_image):
                                index2 = z.index_zd_black_image                            
                                z.image = z.zd_black_images[index2]
                                z.draw()
                            else:
                                zombies.remove(z)
                                remove_zombies.append(z)
                        else:
                            zombies.remove(z)
                            remove_zombies.append(z)
                        
                if z.willdie and (z.index_zh_image < z.num_zh_image + 10):
                    index1 = z.index_zh_image
                    if z.index_zh_image >= z.num_zh_image:
                        index1 = z.num_zh_image - 1
                    z.image = z.zh_images[index1]
                    z.draw()
            for z in remove_zombies:
                del z

            # 绘制弹丸
            for b in bullets:
                if b.shoot:
                    if not open_menu and not open_instruction and not gameover:
                        b.move()
                    if b.is_bullet:
                        b.image = b.bullet_image
                        b.draw()
                    else:
                        b.image = b.firebullet_images[b.index_image]
                        b.draw()
                else:
                    pass

            # 绘制阳光
            for s in suns:
                if not open_menu and not open_instruction and not gameover:
                    if s.gather:
                        s.move3()
                    else:
                        if s.is_supply:
                            s.move1()
                        else:
                            s.move2()
                s.image = s.images[s.index_image]
                s.draw()
                if s.get_position:
                    suns.remove(s)
                    sun_num += 20 + 5*s.level
                    del s

            # 绘制拖拽的植物图像
            if darw_pos_image:
                pos_image.draw()

            # 绘制僵尸大波袭来warn
            if large_warn_time >= 0 and large_coming:
                largewave_image.draw()

            # 绘制游戏结束画面
            if open_quit_window:
                quit_window_image.draw()
                quit_image.draw()
            elif bg_image.left == 0:
                music.stop()
                zombiewon_image.draw()
                gpa_score += 3000*len(cars)
                screen.draw.text(f'Your GPA is :{score_to_gpa(gpa_score):.3f}', (380, 430), fontname="corisandebold.otf", fontsize=40, color=(255,0,0))
                if open_sound and not play_gameover_sound:
                    sounds.gameover.play()
                    play_gameover_sound = True

        # 绘制阳光数量
            if not gameover:
                if seedbank.position:
                    screen.draw.text(str(sun_num), (59, 63), fontname="corisandebold.otf", fontsize=19, color=(0,0,0))
                    screen.draw.text(f"Semester:{level}", (570, 8), fontname="corisandebold.otf", fontsize=17, color=(0,0,0))
                    screen.draw.text(f"JuanGuais' Level:{plant_level}", (560, 25), fontname="corisandebold.otf", fontsize=17, color=(0,0,0))
                    screen.draw.text(f"Scores:{gpa_score}", (570, 40), fontname="corisandebold.otf", fontsize=24, color=(200,0,0))

    # 绘制菜单界面
    if not gameover:
        if start_ready:
            button_image.draw()
            instruction_image.draw()
        if open_menu:
            menu_image.draw()
            if start_ready:
                quitgame_image.draw()
            resume_image.draw()
            check_box_image1.draw()
            check_box_image2.draw()
            if open_sound:
                tick_image1.draw()
            if open_music:
                tick_image2.draw()
        if open_instruction:
            book_image.draw()


pgzrun.go()
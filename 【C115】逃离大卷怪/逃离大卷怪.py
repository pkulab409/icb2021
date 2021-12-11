import pgzrun, random, math, sys

# 参数设置：
WIDTH = 1920
HEIGHT = 1035  # 这个高度刚好可以全屏
TITLE = '逃离大卷怪'
music.play('starting')

startgame = False
startbotton = Rect(900, 830, 250, 200)
# 开始界面

rulebotton = Rect(1600, 370, 100, 100)
ruleshow = False
ruleclose = Actor('ruleclose')
ruleclose.topleft = 1600, 875
leftchanger = Actor('leftchanger')
leftchanger.topleft = 40, 517.5
rightchanger = Actor('rightchanger')
rightchanger.topleft = 1772, 517.5
rulenumber = 0

settingbotton = Rect(175, 280, 120, 80)
settingpic = Actor('setting')
settingpic.topleft = 640, 200  # 设置
settingclose = Rect(940, 675, 150, 75)
setshow = False
musicpointer = Actor('pointer1')  # 音量调节
musicchangecolumn = Rect(860, 397.5, 465, 18)
soundpointer = Actor('pointer1')  # 音效调节
soundchangecolumn = Rect(860, 527.5, 465, 18)
musicpointerfollow = soundpointerfollow = False

with open('内置文件，请勿修改或删除.txt', 'r') as f:
    f1, f2, f3 = f
    f2 = eval(f2[:-1])
    f3 = eval(f3[:-1])
    musicpointer.center = f2, 407.5
    music.set_volume((f2 - 860) / 465)
    soundpointer.center = f3, 537.5
    soundvolume = int((f3 - 861) // 16) + 1
    if soundvolume < 0: soundvolume = 0
    if soundvolume > 30: soundvolume = 30

endmenu = Actor('endmenu')
endbotton = Rect(1200, 600, 400, 150)
rebotton = Rect(300, 600, 400, 150)  # 结束和重启界面

alien = Actor('player2')  # 玩家
dragon = Actor('卷怪.1')  # 追兵
alienx = 700
ymin = 300
ymax = 700
b = {keys.SPACE: False, keys.RIGHT: False, keys.LEFT: False,
     keys.UP: False, keys.DOWN: False}  # 原来有Z键，现在取消，改为二段跳
endgame = True
pause = False


def saveset():
    with open('内置文件，请勿修改或删除.txt', 'r') as f:
        f1 = next(f)
    with open('内置文件，请勿修改或删除.txt', 'w') as f:
        f.write(f'{f1}{musicpointer.x}\n{soundpointer.x}\n')


def initialize():  # 初始化
    global vy, vroad, time, dis, score, h0
    global ran1, ran3, ran4, ran5, ran6, ran7, ran8, ran9, ran2, ran10
    global jumpmode, h, wavl, incl, continuity
    global endgame, pause, flytime
    global grass, road, c, cake
    music.play('playing')
    alien.image = 'player2'
    alien.angle = 0
    dragon.image = '卷怪.1'
    vy = 0  # Alien 的竖直速度, 注意 vy 为负表示竖直速度向上.
    c = '0'
    h0 = 450  # 记录下一个 road 中元素应有的纵坐标
    alien.midbottom = alienx + 1, h0
    dragon.midbottom = 0, alien.y + 41
    road = [(h0, c) for _ in range(WIDTH)]
    '''
    road 表示赛道, road[i] = (h0, c) 意为横坐标为 i 处的道路顶端纵坐标为 h0, 采用图片 c 的颜色.
    在版本 6.0 之前, road 为 Actor 序列, 且在 update 函数中有一个长度接近 WIDTH 的循环, 导致电脑工作量太大;
    因此版本 6.0 将 road 改为了二元组序列, 并优化了 road 移动的算法.
    '''
    grass = []  # 仅用作装饰
    vroad = 0  # Alien 的水平速度, 实际通过 road 向左平移实现.
    time = 0  # 帧数. 确定 Dragon 速度以及控制 Alien 加速度时用到.
    dis = 0  # Alien 的水平位移
    score = 0  # 即 SCORE, Alien 的得分
    flytime = 0  # 飞行模式时记录飞行所剩时间
    jumpmode = 0
    '''
    0 表示在地面; 1 表示因惯性脱离地面; 2 表示因跳跃脱离地面, 此时按下空格触发二段跳; 3 表示已经使用二段跳, 此时按空格键不再有效.
    当 jumpmode == 1 时, 若空格键按下, 可以切换为 jumpmode = 2, 此时再按空格键即可二段跳;
    但如果 Alien 恰好在这两次按空格键之间落地, 则 jumpmode 会先切换成 0, 此时只会触发普通的跳跃.
    '''
    continuity = True  # 判断道路是否连续
    endgame = False  # 开始被追逐
    pause = True  # 是否暂停
    h = 0  # 记录Alien相对赛道的高度
    ran1 = random.randint(2000, 2500)  # 赛道高度变化位置
    ran2 = random.randint(0, 1000)  # 生草位置
    ran3 = random.randint(8000, 9000)  # 赛道消失位置
    ran4 = ran3 + random.randint(60, 140)  # 赛道重现位置
    ran5 = random.randint(3000, 4000)  # 出现 cake 位置
    ran6 = random.randint(11000, 12000)  # 红色赛道
    ran7 = ran6 + random.randint(200, 350)  # 回到正常赛道
    ran8 = random.randint(11000, 12000)  # 黄色赛道
    ran9 = ran8 + random.randint(400, 600)  # 回到正常赛道
    ran10 = random.randint(2, 3)  # cake是宇宙飞船
    wavl = (1.1 - random.random() ** 2) * 100  # 波长
    incl = 0.3 * math.asin(random.random())  # 倾斜程度
    cake = None  # cake (包括飞船)


def draw():
    screen.clear()
    if startgame:
        screen.blit('longbackground2', (-(dis % 5760) // 3, 0))  # 动图
        alien.draw()
        if cake: cake.draw()
        for i in grass: i.draw()
        for i in range(WIDTH):
            screen.blit(road[i][1], (i, road[i][0]))
        screen.draw.text(f'SCORE: {score}', (10, 10), color='black', fontsize=24, fontname='2')
        screen.draw.text(f'SPEED: {vroad}', (10, 40), color='black', fontsize=24, fontname='2')

        if pause:
            if dis:
                screen.draw.text('游戏暂停，按右键继续', (250, 50), color='black', fontsize=50, fontname='2')
            else:
                screen.draw.text('按右键开始游戏', (300, 50), color='black', fontsize=50, fontname='2')
        if dragon.right >= 0:
            dragon.draw()
        else:
            screen.draw.text(f'<= 卷怪: {int(alienx - dragon.x):d}', (10, 90), color='black', fontsize=24, fontname='2')
        if endgame:
            endmenu.draw()
            screen.draw.text(bestscorestr, (750, 500), color='black', fontsize=50, fontname='2')
            screen.draw.text(f'Your Score: {score:d}', (750, 400), color='black', fontsize=50, fontname='2')  # 结束窗口出现
    else:
        screen.blit('startmenu', (0, -20))
        if ruleshow:
            screen.blit(f'rule{(rulenumber % 4 + 1):d}', (0, 0))  # 规则窗口
            ruleclose.draw()
            leftchanger.draw()
            rightchanger.draw()
            screen.draw.text(f'page {(rulenumber % 4 + 1):d} of 4', (1600, 800), color='yellow', fontsize=50,
                             fontname='2')
        if setshow:
            settingpic.draw()
            musicpointer.draw()
            soundpointer.draw()


def on_key_down(key):
    global b, endgame, pause, flytime, jumpmode, vy
    if key in b: b[key] = True
    if startgame:
        if pause and key == keys.RIGHT:
            pause = False;
            music.unpause()  # 右键开始游戏
        elif 1 < flytime < 90 and key == keys.RIGHT:
            flytime = 1
        elif key == keys.SPACE and jumpmode == 2:  # 触发二段跳
            vy = min(vy - 10, -22)
            alien.angle += 18
            jumpmode = 3
            eval(f'sounds.jump3_{soundvolume}.play()')
        if key == keys.X and not endgame and not pause:
            pause = True;
            music.pause();
            eval(f'sounds.pause_{soundvolume}.play()')  # 按X暂停


def on_key_up(key):
    global b
    if key in b: b[key] = False


def on_mouse_down(pos, button):  # 开始，结束和重启按键
    global startgame, pause, ruleshow, rulenumber, setshow, soundvolume
    global musicpointerfollow, soundpointerfollow
    if button == mouse.LEFT:
        if not startgame:
            if rulebotton.collidepoint(pos):
                ruleshow = True
                if setshow:
                    saveset()
                    setshow = False
            if ruleshow and ruleclose.collidepoint(pos):
                ruleshow = False
            if ruleshow and leftchanger.collidepoint(pos):
                rulenumber -= 1
            if ruleshow and rightchanger.collidepoint(pos):
                rulenumber += 1
            if not startgame and settingbotton.collidepoint(pos):
                setshow = True
                ruleshow = False
            if setshow:
                if settingclose.collidepoint(pos):
                    saveset()
                    setshow = False
                    startgame = False
                if musicpointer.collidepoint(pos):
                    musicpointerfollow = True
                elif musicchangecolumn.collidepoint(pos):  # 音量调节
                    musicpointer.x = pos[0]
                    music.set_volume((pos[0] - 860) / 465)
                if soundpointer.collidepoint(pos):
                    soundpointerfollow = True
                elif soundchangecolumn.collidepoint(pos):  # 音效调节
                    soundpointer.x = pos[0]
                    soundvolume = int((soundpointer.x - 861) // 16) + 1
                    if soundvolume < 0: soundvolume = 0
                    if soundvolume > 30: soundvolume = 30

            if (not startgame) and ruleshow == False and startbotton.collidepoint(pos):
                startgame = True
                if setshow:
                    saveset()
                    setshow = False
                ruleshow = False
                initialize()
        else:
            if endbotton.collidepoint(pos) and endgame:
                sys.exit()
            if rebotton.collidepoint(pos) and endgame:
                initialize()
            if not endgame and not pause: pause = True; music.pause(); eval(f'sounds.pause_{soundvolume}.play()')


def on_mouse_up(button):
    global musicpointerfollow, soundpointerfollow
    if button == mouse.LEFT and setshow: musicpointerfollow = soundpointerfollow = False


def on_mouse_move(pos):
    global soundvolume
    if setshow:
        if musicpointerfollow:
            musicpointer.x = pos[0]
            if musicpointer.x > 1325: musicpointer.x = 1325
            if musicpointer.x < 860: musicpointer.x = 860
            music.set_volume((musicpointer.x - 860) / 465)
        if soundpointerfollow:
            soundpointer.x = pos[0]
            if soundpointer.x > 1325: soundpointer.x = 1325
            if soundpointer.x < 860: soundpointer.x = 860
            soundvolume = int((soundpointer.x - 861) // 16) + 1
            if soundvolume < 0: soundvolume = 0
            if soundvolume > 30: soundvolume = 30


def update():
    global vy, vroad, time, dis, c, score, h0
    global ran1, ran3, ran4, cake, ran5, ran6, ran7, ran8, ran9, ran2, ran10
    global jumpmode, h, wavl, incl, continuity, endgame, flytime
    global bestscorestr

    if not endgame and not pause:
        # 赛道向左移动：
        del road[:vroad]
        '''
        由于 road 中元素的横坐标取决于它是 road 的第几项, 故这条语句即可实现道路向左平移 vroad.
        '''
        for i in grass:
            i.x -= vroad
            if i.right < 0: grass.remove(i)
        if cake:
            cake.x -= vroad
            if cake.right < 0: cake = None
        for i in range(vroad):  # 在右边添加道路
            h0 += math.sin(dis / wavl) * incl
            road.append((h0, c))

        dis += vroad

        if dis - vroad < ran8 <= dis:  # 黄色赛道
            c = '2'
            ran8 += random.randint(3000, 4000)
        if dis - vroad < ran9 <= dis:  # 回到正常赛道
            c = '0'
            ran9 = ran8 + random.randint(400, 600)

        if dis - vroad < ran6 <= dis:  # 红色赛道
            c = '1'
            ran6 += random.randint(1500, 3500)
        if dis - vroad < ran7 <= dis:  # 回到正常赛道
            c = '0'
            ran7 = ran6 + random.randint(200, 350)

        if dis - vroad < ran1 <= dis:  # 来到赛道高度变化位置
            ran0 = random.randint(60, 120)
            R = random.randint(-1, 1)  # 随机选择赛道上浮或下沉或不变
            h0 -= ran0 * R;
            ran1 += random.randint(500, 1100)
            # 防止道路超出界面：
            if -500 < h0 < ymin and R > 0:
                h0 += 2 * ran0
            if (h0 > ymax or ymax - 3000 < h0 < -500) and R < 0:
                h0 -= 2 * ran0
            # 重设波长及倾斜程度：
            wavl = (1.1 - random.random() ** 2) * 100
            incl = 0.3 * math.asin(random.random())

        if dis - vroad < ran3 <= dis:  # 来到赛道消失位置
            h0 -= 3000  # 抬高道路至界面外, 表示赛道消失
            ran3 += random.randint(600, 2000)

        if dis - vroad < ran4 <= dis:  # 来到赛道重现位置
            h0 += 3000
            ran4 = ran3 + random.randint(60, 200)

        if dis - vroad < ran5 <= dis:  # 来到cake出现位置
            if ran10:
                cake = Actor(f'cake{random.randint(0, 6)}')
                ran10 -= 1
            else:
                cake = Actor('alien1')  # 飞船看作特殊的 cake.
                ran10 = random.randint(5, 7)
            cake.x = len(road)
            cake.bottom = h0 - random.randint(150, 220)
            if -500 < cake.y < 0: cake.y = 0
            if cake.y < -1500: cake.y += 3000
            ran5 += random.randint(3500, 5000)

        if dis - vroad < ran2 <= dis:  # 来到生草位置
            gra = Actor(f'grass{random.randint(0, 3)}')
            gra.x = WIDTH
            gra.bottom = h0 + 5
            grass.append(gra)
            ran2 += random.randint(10, 2000)

        score += vroad

        if flytime:
            flytime -= 1
            if b[keys.UP] and alien.y > 0: alien.y -= 5
            if b[keys.DOWN] and alien.y < HEIGHT: alien.y += 5
            if not flytime:
                vy = 5
                alien.image = 'player3'
                jumpmode = 2
            elif flytime <= 90:
                vroad = 20
                if flytime in [30, 60, 90]: alien.image = 'alien2'
                if flytime in [20, 50, 80]: alien.image = 'alien0'
        else:
            vy += 1
            alien.y += vy
            if 0 < alien.angle: alien.angle += 18
            if road[alienx][0] <= alien.bottom and h <= 0 and continuity:
                # 用零点存在定理判断玩家是否落地
                if dis % 320 <= 80:
                    alien.image = 'player1'
                elif dis % 320 <= 160 or dis % 320 >= 240:
                    alien.image = 'player2'
                else:
                    alien.image = 'player3'
                if not jumpmode:
                    vy += road[alienx][0] - alien.bottom
                else:
                    alien.angle = 0
                    jumpmode = 0
                alien.bottom = road[alienx][0]
            else:
                if not jumpmode: jumpmode = 1; alien.image = 'player2'
                if road[alienx][0] <= alien.bottom <= road[alienx][0] + 20:
                    # 如果差一点跳上赛道可自动帮玩家捞上去
                    alien.bottom = road[alienx][0]
            if not jumpmode:  # 只有在地面可进行操作
                if road[alienx][1] == '1':
                    vroad = 30
                else:
                    vmax = 10 if road[alienx][1] == '2' else 20
                    if h < 0 and not b[keys.RIGHT]: vroad -= 1  # 撞地减速
                    if b[keys.LEFT]:
                        vroad -= 1  # 减速
                    elif b[keys.RIGHT] and (time % 5 == 0 or h < 0):
                        vroad += 1  # 加速（比减速慢）
                    if vroad < 0: vroad = 0
                    if vroad > vmax: vroad = max(vmax, vroad - 2)  # 速度范围为0~20中的整数

            if b[keys.SPACE]:  # 跳跃
                if not jumpmode:
                    vy = min(vy - 4, -15)
                    eval(f'sounds.jump2_{soundvolume}.play()')
                if jumpmode != 3:
                    alien.image = 'player3'
                    jumpmode = 2

        if alien.top > 2000:  # 掉下去
            endgame = True
        elif dragon.x >= alienx:  # 被追上
            alien.angle = 0
            alien.image = 'player4'
            alien.y += 32  # 微调位置
            endgame = True
        if endgame:
            music.play_once('end')
            with open('内置文件，请勿修改或删除.txt', 'r') as f:
                f1, f2, f3 = f
                bestscore = eval(f1[:-1])
                bestscorestr = '恭喜你打破记录！' if bestscore < score else f'Best Score: {bestscore}'
            if bestscorestr == '恭喜你打破记录！':
                with open('内置文件，请勿修改或删除.txt', 'w') as f: f.write(f'{score}\n{f2}{f3}')

        else:  # 更新参数
            time += 1
            h = alien.bottom - road[alienx][0]
            if -28 < road[alienx][0] - road[alienx + vroad][0] < 28:
                # 判断道路是否连续. 由于 vorad <= 30 且 incl <= 0.3π, 且赛道高度突变时至少变化 60, 故上述表达式是充要的
                continuity = True
            else:
                continuity = False

            # 追兵移动：
            dragon.bottom = alien.y + 41
            dragon.x += 0 if time < 60 else 17 + time // 1200
            dragon.x -= vroad

        if cake and alien.colliderect(cake) and cake.image != 'cake-1':
            if cake.image == 'alien1':
                flytime = 300
                vroad = 30
                alien.angle = 0
                alien.y = cake.y
                alien.image = 'alien0'
                jumpmode = 1
                eval(f'sounds.fly_{soundvolume}.play()')
                cake = None
            else:
                score += 2000
                eval(f'sounds.score_{soundvolume}.play()')
                cake.image = 'cake-1'
    elif endgame and not music.is_playing(None):
        music.play('starting')


pgzrun.go()

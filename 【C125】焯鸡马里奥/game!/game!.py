import pgzrun
import random
import time
import easygui as g
import sys

while 1:
    g.msgbox("感谢您来体验游戏：焯鸡马里奥 \n说明：你叫赫然，是一名大学生。如果你碰到了篮球和啤酒，你就会因为不够努力而使得GPA下降\n规则：按任意键起跳,让自己的绩点高于0，并坚持60秒")
    msg ="开始游戏？"
    title = "焯鸡马里奥"
    choices = ["立即开始", "稍后开始"]
    choice = g.choicebox(msg, title, choices)
    
    if str(choice)=='立即开始':
        
        heran = Actor('heran_normal')
        heran.midbottom = 100,1025
        heran.score = 40

        grass1 = Actor('grass1')
        grass2 = Actor('grass2')
        grass1.bottomleft = 0,1280
        grass2.bottomleft = grass1.width,1280

        names = ['basketball','beer_bottle']
        things = []

        WIDTH = 1280
        HEIGHT = 1280

        pre = time.time()
        
        def win():
            global pre
            if float(time.time() - pre) > 60:
                msg = "你赢了！你的GPA在0以上！"
                title = "焯鸡马里奥"
                if g.ccbox(msg,title):
                    grass1.bottomleft = 0,1280
                    grass2.bottomleft = grass1.width,1280
                    heran.score = 40
                    for t in things:
                        things.remove(t)
                    
                    pre = time.time()
                else:
                    sys.exit(0)
    
        sounds.backsound.play()
        
        def draw():
            screen.clear()
            screen.blit('background',(0,0))
            heran.draw()
            grass1.draw()
            grass2.draw()
            for t in things:
                t.draw()
            screen.draw.text('GPA x 10:%d' % heran.score, (640,10))
            screen.draw.text('Time:%d' % float(time.time() - pre),(640,30))

        def update():
            if float(time.time() - pre) <= 10:
                if random.randrange(60) == 0:
                    t = Actor(random.choice(names))
                    t.midbottom = 1100,1025
                    things.append(t)
            elif 10 < float(time.time() - pre) <= 20:
                if random.randrange(40) == 0:
                    t = Actor(random.choice(names))
                    t.midbottom = 1100,1025
                    things.append(t)
            else:
                if random.randrange(30) == 0:
                    t = Actor(random.choice(names))
                    t.midbottom = 1100,1025
                    things.append(t)
            for t in things:
                if float(time.time() - pre) <= 10:
                    t.x -= 10
                elif 10 < float(time.time() - pre) <= 30:
                    t.x -= 20
                else:
                    t.x -= 30
                if t.x <= 0:
                    things.remove(t)
                if t.colliderect(heran):
                    sounds.你干嘛.play()
                    heran.score -= 4
                    things.remove(t)
            move()
            fall()
            grass_move()
            fail()
            win()

        def grass_move():
            if float(time.time() - pre) <= 10:
                grass1.x -= 10
                grass2.x -= 10
            elif 10 < float(time.time() - pre) <= 30:
                grass1.x -= 20
                grass2.x -= 20
            else:
                grass1.x -= 30
                grass2.x -= 30
            if grass1.right <= 0:
                grass1.right += grass1.width * 2.0
            if grass2.right <= 0:
                grass2.right += grass2.width * 2.0

        def heran_move():
            heran.image = 'heran_move'
            
        def heran_normal():
            heran.image = 'heran_normal'
            
        def move():
            clock.schedule_interval(heran_move,0.2)
            clock.schedule_interval(heran_normal,0.2)

        def fall():
            if heran.collidepoint((100,1025)):
                heran.bottom += 0
            elif heran.bottom < 800:
                heran.midbottom = 100,1025
            else:
                heran.bottom += 5
            
        def on_key_down():
            heran.top -= 200
            sounds.chao.play()
        
        def fail():
            global pre
            if heran.score <= 0:
                sounds.backsound.stop()
                g.msgbox('你输了！')
                msg = "下次再见！"
                title = "焯鸡马里奥"
                if g.ccbox(msg, title):
                    grass1.bottomleft = 0,1280
                    grass2.bottomleft = grass1.width,1280
                    heran.score = 40
                    for t in things:
                        things.remove(t)
                    pre = time.time()
                    sounds.backsound.play()
                else:
                    sys.exit(0)
               
                
        pgzrun.go()
        
    if str(choice)=='稍后开始':
        g.msgbox("好吧，再见！")
        sys.exit(0)
import pgzrun
import subprocess
import random
import sys
import easygui as g
import pygame

WIDTH = 1200
HEIGHT = 900
part = 0
l = open('txts/level.txt',mode='r',encoding='utf-8')
level = l.readlines()
Choices = ['part1', 'part2', 'part3', 'part4', 'part5']
choices=[]
le=int(level[-1])
if le==-1 :
    subprocess.run([sys.executable, "game5/error_error.py"])
    exit()
elif le==-2:
    part=-2
else:
    for i in range(int(level[-1])):
       choices.append(Choices[i])
    if not (level[-1]=='0' or level[-1]=='1'):
        choice = g.choicebox('Which part do you want to start?', '', choices)
        if choice=='part1':
            part=1
        elif choice=='part2':
            part=2
        elif choice=='part3':
           part=3
        elif choice=='part4':
            part=4
        elif choice=='part5':
            part=5
l.close()
line = 0
f1 = open('txts/TXT1.txt','r', encoding='utf-8')
TXT1=f1.readlines()
f1.close()
f2 = open('txts/TXT2.txt','r', encoding='utf-8')
TXT2=f2.readlines()
f2.close()
f3 = open('txts/TXT3.txt','r', encoding='utf-8')
TXT3=f3.readlines()
f3.close()
f4 = open('txts/TXT4.txt','r', encoding='utf-8')
TXT4=f4.readlines()
f4.close()
f5 = open('txts/TXT5.txt','r', encoding='utf-8')
TXT5=f5.readlines()
f5.close()
knife=Actor('knife')
knife.midtop=(WIDTH/2,HEIGHT)
he=Actor('he')
he.midbottom=(900,900)
you=Actor('you')
you.midbottom=(300,900)
rock=Actor('rock')
rock.midbottom=(900,0)
def draw():
    global part, line
    if part == 0:
        screen.clear()
        if line <= 120:
            screen.blit('title', (0,0))
        elif line<=240:
            screen.fill((44,232,245))
            screen.draw.text('不管任何时候', (0,0), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text('您都可以用"Esc"退出游戏', (0,50), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text('每部分结束后游戏将自动保存', (0,100), color='black', fontname = 'zpix', fontsize = 50)
        else:
            line=0
            part+=1
    elif part==1:
        screen.clear()
        screen.blit('background1',(0,0))
        screen.draw.text('PRESS SPACE', (0,0), fontname = 'zpix', fontsize = 50)
        if len(TXT1[line])<=16:
            screen.draw.text(TXT1[line], (120,160), color='black', fontname = 'zpix', fontsize = 50)
        elif len(TXT1[line])<=31:
            screen.draw.text(TXT1[line][0:15], (120,160), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT1[line][15:-1], (120,210), color='black', fontname = 'zpix', fontsize = 50)
        elif len(TXT1[line])<=47:
            screen.draw.text(TXT1[line][0:15], (120,160), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT1[line][15:30], (120,210), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT1[line][30:-1], (120,260), color='black', fontname = 'zpix', fontsize = 50)
    elif part==2:
        screen.clear()
        screen.blit('background2',(0,0))
        screen.draw.text('PRESS SPACE', (0,0), fontname = 'zpix', fontsize = 50)
        if len(TXT2[line])<=18:
            screen.draw.text(TXT2[line], (120,160), color='black', fontname = 'zpix', fontsize = 50)
        elif len(TXT2[line])<=36:
            screen.draw.text(TXT2[line][0:17], (120,160), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT2[line][17:-1], (120,210), color='black', fontname = 'zpix', fontsize = 50)
        elif len(TXT2[line])<=54:
            screen.draw.text(TXT2[line][0:17], (120,160), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT2[line][17:35], (120,210), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT2[line][35:-1], (120,260), color='black', fontname = 'zpix', fontsize = 50)
    elif part==3:
        screen.clear()
        screen.blit('background3',(0,0))
        screen.draw.text('PRESS SPACE', (0,0), fontname = 'zpix', fontsize = 50)
        if len(TXT3[line])<=18:
            screen.draw.text(TXT3[line], (120,160), color='black', fontname = 'zpix', fontsize = 50)
        elif len(TXT3[line])<=36:
            screen.draw.text(TXT3[line][0:17], (120,160), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT3[line][17:-1], (120,210), color='black', fontname = 'zpix', fontsize = 50)
        elif len(TXT3[line])<=54:
            screen.draw.text(TXT3[line][0:17], (120,160), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT3[line][17:35], (120,210), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT3[line][35:-1], (120,260), color='black', fontname = 'zpix', fontsize = 50)
    elif part==4:
        screen.clear()
        screen.blit('background4',(0,0))
        screen.draw.text('PRESS SPACE', (0,0), fontname = 'zpix', fontsize = 50)
        if len(TXT4[line])<=18:
            screen.draw.text(TXT4[line], (120,160), color='black', fontname = 'zpix', fontsize = 50)
        elif len(TXT4[line])<=36:
            screen.draw.text(TXT4[line][0:17], (120,160), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT4[line][17:-1], (120,210), color='black', fontname = 'zpix', fontsize = 50)
        elif len(TXT4[line])<=54:
            screen.draw.text(TXT4[line][0:17], (120,160), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT4[line][17:35], (120,210), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT4[line][35:-1], (120,260), color='black', fontname = 'zpix', fontsize = 50)
    elif part==5:
        screen.clear()
        if line<8:
            screen.blit('background5',(0,0))
            screen.draw.text('PRESS SPACE', (0,0), fontname = 'zpix', fontsize = 50)
            knife.draw()
        else:
            screen.fill((255,255,255))
            he.draw()
            you.draw()
            rock.draw()
        if len(TXT5[line])<=18:
            screen.draw.text(TXT5[line], (120,160), color='black', fontname = 'zpix', fontsize = 50)
        elif len(TXT5[line])<=36:
            screen.draw.text(TXT5[line][0:17], (120,160), color='black', fontname = 'zpix', fontsize = 50)
            screen.draw.text(TXT5[line][17:-1], (120,210), color='black', fontname = 'zpix', fontsize = 50)
    elif part==-2:
        screen.clear()
        screen.blit('my_win',(0,0))
        

def update():
    global line, part
    if keyboard.escape:
        exit()
    if part==0:
        line+=1
    elif part==1:
        if line==0:
            with open('txts/level.txt',mode='w',encoding='utf-8') as l:
                l.write('1')
            l.close()
            line+=1
        elif line == 11:
            g.msgbox("你是？")
            line+=1
        elif line == 25:
            choices=['A.给点给点','B.摸了摸了']
            choice=g.choicebox('','',choices)
            if choice==choices[0]:
                line = 27
            elif choice==choices[1]:
                line = 26
        elif line==35:   
            subprocess.run([sys.executable, "game1/ball_and_board.py"])
            line+=1
        elif line==38:
            choices=['有点自夸哦','是在说你自己吗？']
            choice=g.choicebox('','',choices)
            line+=1
        elif line== 42:
            line=0
            part+=1
    elif part == 2:
        if line==0:
            with open('txts/level.txt',mode='w',encoding='utf-8') as l:
                l.write('2')
            l.close()
            line+=1
        elif line==2:
            choices=['怎么了？','发生咩事？']
            choice=g.choicebox('','',choices)
            line+=1
        elif line==11:
            choices=['难度会不会太大？','剧情会不会很谜语人？']
            choice=g.choicebox('','',choices)
            line+=1
        elif line==14:
            choices=['祝你好运','祝我好运']
            choice=g.choicebox('','',choices)
            if choice==choices[0]:
                line = 15
            elif choice==choices[1]:
                line = 17
        elif line==16:
            line=19
        elif line==18:
            line=19
        elif line==24:
            choices=['怎么可能','还能接受', '嘿嘿…难度…嘿嘿']
            choice=g.choicebox('','',choices)
            if choice==choices[0]:
                line = 25
            elif choice==choices[1]:
                line = 29
            elif choice==choices[2]:
                line = 37
        elif line==28:
            line=44
        elif line==36:
            line=44
        elif line==43:
            line=44
        elif line==55:
            choices=['很有意思的比喻','银河一般，壮阔却又绝美']
            choice=g.choicebox('','',choices)
            if choice==choices[0]:
                line = 56
            elif choice==choices[1]:
                line = 58
        elif line==57:
            line=60
        elif line==59:
            line=60
        elif line==71:
            subprocess.run([sys.executable, "game2/get_ifmt.py"])
            line+=1
        elif line==78:
            line=0
            part+=1
    elif part==3:
        if line==0:
            with open('txts/level.txt',mode='w',encoding='utf-8') as l:
                l.write('3')
            l.close()
            line+=1
        elif line==3:
            choices=['是的', '不是']
            choice=g.choicebox('','',choices)
            line+=1
        elif line==10:
            choices=['阿巴阿巴','前者要更情绪化？']
            choice=g.choicebox('','',choices)
            if choice==choices[0]:
                line = 11
            elif choice==choices[1]:
                line = 15
        elif line==14:
            line=17
        elif line==16:
            line=17
        elif line==29:
            g.msgbox("不会让人变得暴力吧(笑)")
            line+=1
        elif line==34:
            g.msgbox("(´ﾟДﾟ`)")
            line+=1
        elif line==42:
            subprocess.run([sys.executable, "game3/beat_bugs.py"])
            line+=1
        elif line==48:
            line=0
            part+=1
    elif part==4:
        if line==0:
            with open('txts/level.txt',mode='w',encoding='utf-8') as l:
                l.write('4')
            l.close()
            line+=1
        elif line==5:
            subprocess.run([sys.executable, "game4/fly_fly_fly.py"])
            line+=1
        elif line==7:
            line=0
            part+=1
    elif part==5:
        if line==0:
            with open('txts/level.txt',mode='w',encoding='utf-8') as l:
                l.write('5')
            l.close()
            line+=1
        elif 19<=line<=21:
            if rock.bottom<=100:
                rock.y+=5
            else:
                pass
        elif line==22:
            music.play_once('laugh')
            line+=1
        elif line==24:
            subprocess.run([sys.executable, "game5/error_error.py"])
            exit()
        if 4<=line<=7:
            if knife.y>=600:
                knife.y-=8
            else:
                pass
        if line>=22:
            if rock.bottom<HEIGHT:
                rock.y+=80
            else:
                pass
        if 17<=line<=19:
            sounds.bug_in.play()
    elif part==-2:
        sounds.my_win.play()
        pass

def on_key_down(key):
    global line
    if key == key.SPACE:
        line+=1

pgzrun.go()
import pgzrun
import pygame

HEIGHT=540
WIDTH=960

kasu=Actor('kasu')
line=0
t=0
button1=Actor('button1')
button2=Actor('button2')
button1.midbottom=(WIDTH/2,-HEIGHT/2)
button2.midbottom=(WIDTH/2,-HEIGHT/2)

def draw():
    global line
    screen.clear()
    if line==0:
        screen.blit('title', (0,0))
    elif 1<=line<=6:
        screen.blit('background',(0,0))
        screen.blit('kasu',(WIDTH/2-178,40))
        if line==1:
            screen.blit('sen0',(0,HEIGHT-200))
        elif line==2:
            screen.blit('sen1',(0,HEIGHT-200))
        elif line==3:
            screen.blit('sen2',(0,HEIGHT-200))
        elif line==4:
            screen.blit('sen3',(0,HEIGHT-200))
        elif line==5:
            button1.draw()
        elif line==6:
            button2.draw()
    elif line==7:
        screen.blit('end',(0,0))
        sounds.bug_in.play()

def update():
    global line, t
    pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if keyboard.escape:
        exit()
    if line==0:
        t+=1
        if t==120:
            line+=1
            t=0
    elif line==5:
        button1.pos=(WIDTH/2,HEIGHT/2)
    elif line==6:
        button1.midbottom=(WIDTH/2,-HEIGHT/2)
        button2.pos=(WIDTH/2,HEIGHT/2)
    elif line==7:
        button2.midbottom=(WIDTH/2,-HEIGHT/2)
        t+=1
        if t==240:
            line+=1
            t=0
    elif line==8:
        exit()
        

def on_key_down(key):
    global line
    if 1<=line<=4:
        if key == key.SPACE:
            line+=1

def on_mouse_move(pos):
    if button1.collidepoint(pos):
        button1.image='button11'
    else:
        button1.image='button1'
    if button2.collidepoint(pos):
        button2.image='button22'
    else:
        button2.image='button2'

def on_mouse_down(pos,button):
    global line
    if button == mouse.LEFT and button1.collidepoint(pos):
        line+=1
    elif button == mouse.LEFT and button2.collidepoint(pos):
        line+=1

pgzrun.go()
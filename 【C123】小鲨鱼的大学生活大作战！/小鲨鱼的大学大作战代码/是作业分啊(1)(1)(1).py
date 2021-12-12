import pgzrun
import random
import easygui as g
import sys


j=0
step=0
WIDTH=700
HEIGHT=900
player=Actor("shark1.png")

player.x=250
player.y=650
game=False
weapons=[]
enemy=["computer1.png","math1.png","assignment1.png"]
enemys=[]

def on_key_down(key):
    if key==keys.A:
        global game
        game="A"
    elif key==keys.B:
        
        game="B"
    
       
def draw():

    screen.clear()
    screen.blit("start.jpg",[0,0])
    sounds.start.play()
        
    if (player.image!="cry.png")and (game=="A"):
        sounds.start.stop()
        screen.blit("day.png",[0,0])
        sounds.day.play()
        player.draw()
        for w in weapons:
            w.draw()
        for u in enemys:
            u.draw()
        
    elif (player.image!="cry.png")and (game=="B"):
        sounds.start.stop()
        screen.blit("night.png",[0,0])
        sounds.day.play()
        player.draw()
        for w in weapons:
            w.draw()
        for u in enemys:
            u.draw()
    
        
    
def update():
    global step
    if (player.image=="cry.png")or (game==False):
        
        return
    elif random.randrange(80)==0:
    
        b=Actor(random.choice(enemy))
        b.x=random.randint(0,500)
        enemys.append(b)
        
        


        if keyboard.left:
            player.x-=30
        if keyboard.right:
            player.x+=30
        if keyboard.up:
            player.y+=30
        if keyboard.down:
            player.y-=30
    
        if keyboard.space:
            weapon=Actor("work1.png")
            weapon.x=player.x
            weapon.y=player.y-50
            weapons.append(weapon)
    
        for w in weapons:
            w.y-=50
        for b in enemys:
            b.y+=10
        for w in weapons:
            if w.y<=0:
                weapons.remove(w)
        for b in enemys:
            for w in weapons:
                if b.colliderect(w):
                    b.x=random.randint(0,500)
                    b.y=0
        
            
        if b.colliderect(player):
            sha_sad()
def sha_sad():
    player.image="cry.png"
   

            
pgzrun.go()
    

    
    

    
            


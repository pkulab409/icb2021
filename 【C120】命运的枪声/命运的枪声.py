import pgzrun
import random

WIDTH=1000
HEIGHT=618

crisis = 0
action = 0
role = 0
anger = 0
curtainname='c 0 a 0 r 0'
sounds.sounda.play()
selecting = starting = dead = shoot = bool(False)
choice1available = choice2available = choice3available = choice4available = bool(False)

centerbuttonavailable = leftbuttonavailable = rightbuttonavailable = bool(False)

leftbutton = Actor('leftbutton')
leftbutton.pos = 180,580

centerbutton = Actor('centerbutton')
centerbutton.pos = 500,580

rightbutton = Actor('rightbutton')
rightbutton.pos = 820,580

def draw():
    global djinguiyuan
    global dchezhiche
    global dpiaozhengxi
    global shoot
    global curtainname
    global chezhiche
    global piaozhengxi
    global jinguiyuan
    global choice1available
    global choice2available
    global choice3available
    global choice4available
    curtain = Actor(curtainname)
    curtain.pos = 500,309
    curtain.draw()
    if centerbuttonavailable:
        centerbutton.draw()
    if leftbuttonavailable:
        leftbutton.draw()
    if rightbuttonavailable:
        rightbutton.draw()
    if shoot:
        chezhiche.draw()
        jinguiyuan.draw()
        piaozhengxi.draw()

def on_mouse_down(pos):
    global curtainname
    global crisis
    global action
    global role
    global djinguiyuan
    global dchezhiche
    global dpiaozhengxi
    global shoot
    global curtainname
    global chezhiche
    global piaozhengxi
    global jinguiyuan
    global choice1available
    global choice2available
    global choice3available
    global choice4available
    if crisis == 0:
        starting()
    elif action == 0:
        if leftbutton.collidepoint(pos):
            curtainname = 'c 1 a 1 r 1'
            action = 1
            role = 1
        elif rightbutton.collidepoint(pos):
            curtainname = 'c 1 a 1 r 3'
            action = 1
            role = 3
        elif centerbutton.collidepoint(pos):
            curtainname = 'c 1 a 1 r 2'
            action = 1
            role = 2
    else:
        if leftbutton.collidepoint(pos):
            if leftbuttonavailable:
                leftbuttontouch()
                
        if rightbutton.collidepoint(pos):
            if rightbuttonavailable:
                rightbuttontouch()
                
        if centerbutton.collidepoint(pos):
            if centerbuttonavailable:
                centerbuttontouch()
    if shoot:
        if chezhiche.collidepoint(pos):
            chezhiche = Actor('dchezhiche')
            dchezhiche = True
        if piaozhengxi.collidepoint(pos):
            piaozhengxi = Actor('dpiaozhengxi')
            dpiaozhengxi = True
        if jinguiyuan.collidepoint(pos):
            jinguiyuan = Actor('djinguiyuan')
            djinguiyuan = True
         

def starting():
    global centerbuttonavailable
    global leftbuttonavailable
    global rightbuttonavailable
    global curtainname
    global crisis
    global choice3available
    global choice4available
    curtainname = 'c 1 a 0 r 0'
    centerbuttonavailable = leftbuttonavailable = rightbuttonavailable = bool(True)
    crisis = 1

def leftbuttontouch():
    global curtainname
    global action
    global role
    curtainname = 'c %d a %d r %d' %(crisis,action,role)
    leftaction()

def centerbuttontouch():
    global curtainname
    global action
    global rule
    curtainname =  'c %d a %d r %d' %(crisis,action,role)
    centeraction()

def rightbuttontouch():
    global curtainname
    global action
    global rule
    curtainname =  'c %d a %d r %d' %(crisis,action,role)
    rightaction()

def leftaction():
    global curtainname
    global crisis
    global action
    global role
    global centerbuttonavailable
    global leftbuttonavailable
    global rightbuttonavailable
    global rolling
    global choice1available
    global choice2available
    global choice3available
    global choice4available
    global anger
    if role == 1:
        if action == 1:
            centerbuttonavailable = bool(False)
            action = 2
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 2:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 3
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 3:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 5
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 4:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 5
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 5:
            centerbuttonavailable = False
            action = 6
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 6:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 7
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 7:
            sounds.sounda.stop()
            sounds.soundb.play()
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 9
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 8:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 9
            sounds.sounda.stop()
            sounds.soundb.play()
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 9:
            centerbuttonavailable = bool(False)
            action = 10
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 10:
            centerbuttonavailable = bool(True)
            action = 11
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 11:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 12
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 12:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 13
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 13:
            centerbuttonavailable = leftbuttonavailable = rightbuttonavailable = bool(False)
            shooting() 
        elif action == 16:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = rolling
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 17:
            if choice1available:
                action = 31
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
            else:
                action = 30
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 30:
            centerbuttonavailable = False
            action = 22
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 22:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 23
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 24:
            action = 25
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 31:
            action = 23
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        else:
            quit()
    elif role == 2:
        if action == 1:
            centerbuttonavailable = bool(False)
            action = 2
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 2:
            action = 3
            centerbuttonavailable = bool(False)
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 3:
            action = 4
            choice4available = True
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 4:
            action = 6
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 5:
            action = 6
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 6:
            sounds.sounda.stop()
            sounds.soundb.play()
            action = 7
            centerbuttonavailable = bool(False)
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 7:
            action = 8
            centerbuttonavailable = bool(False)
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 9:
            if choice3available and choice4available:
                action = 10
                leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
            else:
                action = 11
                centerbuttonavailable = False
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 11:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 12
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        else:
            quit()
    elif role == 3:
        if action == 1:
            centerbuttonavailable = False
            action = 2
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 2:
            centerbuttonavailable = False
            action = 3
            anger += 1
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 3:
            centerbuttonavailable = False
            action = 4
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 4:
            centerbuttonavailable = False
            sounds.sounda.stop()
            sounds.soundb.play()
            action = 5
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 5:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 6
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 7:
            if anger == 1 or anger == 0:
                leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
                action = 8
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
            elif anger == 2 or anger == 3:
                centerbuttonavailable = False
                action = 9
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 9:
            centerbuttonavailable = True
            action = 10
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 10:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 12
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        else:
            quit()
            
def rightaction():
    global anger
    global curtainname
    global crisis
    global action
    global role
    global centerbuttonavailable
    global leftbuttonavailable
    global rightbuttonavailable
    global rolling
    global choice1available
    global choice2available
    global choice3available
    global choice4available
    if role == 1:
        if action == 1:
            centerbuttonavailable = bool(False)
            action = 2
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 2:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 4
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 3:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 5
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 4:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 5
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 5:
            centerbuttonavailable = bool(False)
            action = 6
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 6:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 8
            choice1available = bool(True)
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 7:
            sounds.sounda.stop()
            sounds.soundb.play()
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 9
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 8:
            sounds.sounda.stop()
            sounds.soundb.play()
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 9
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 9:
            centerbuttonavailable = bool(False)
            action = 10
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 10:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 27
            curtainname = 'c {} a {} r {}'.format(crisis,action,role,role)
        elif action == 11:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 13
            choice2available = True
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 13:
            centerbuttonavailable = leftbuttonavailable = rightbuttonavailable = bool(False)
            shooting()
        elif action == 16:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = rolling
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 17:
            if choice1available:
                centerbuttonavailable = False
                action = 31
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
            else:
                leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
                action = 30
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 30:
            centerbuttonavailable = False
            action = 22
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 22:
            centerbuttonavailable = False
            action = 24
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 24:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 26
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        else:
            quit()
    elif role == 2:
        if action == 1:
            centerbuttonavailable = bool(False)
            action = 2
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 2:
            centerbuttonavailable = bool(False)
            action =3
            choice3available = True
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 3:
            centerbuttonavailable = bool(False)
            action = 4
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 4:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 6
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 5:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 6
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 6:
            sounds.sounda.stop()
            sounds.soundb.play()
            centerbuttonavailable = bool(False)
            action = 7
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 7:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 9
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 9:
            if choice3available and choice4available:
                leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
                action = 10
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
            else:
                centerbuttonavailable = bool(False)
                action = 11
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 11:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 12
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        else:
            quit()
    elif role == 3:
        if action == 1:
            centerbuttonavailable = False
            action = 2
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 2:
            centerbuttonavailable = False
            action = 3
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 3:
            centerbuttonavailable = False
            action = 4
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
            anger += 1
        elif action == 4:
            sounds.sounda.stop()
            sounds.soundb.play()
            centerbuttonavailable = False
            action = 5
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
            anger += 1
        elif action == 5:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 7
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 7:
            if anger == 1 or anger == 0:
                leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
                action = 8
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
            elif anger == 2 or anger == 3:
                centerbuttonavailable = False
                action = 9
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 9:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 11
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 10:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 14
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        else:
            quit()
def centeraction():
    global anger
    global curtainname
    global crisis
    global action
    global role
    global centerbuttonavailable
    global leftbuttonavailable
    global rightbuttonavailable
    global rolling
    global choice1available
    global choice2available
    global choice3available
    global choice4available
    if role == 1:
        if action == 1:
            centerbuttonavailable = bool(False)
            action = 2
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 3:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 5
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 4:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 5
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 5:
            centerbuttonavailable = False
            action = 6
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 7:
            sounds.sounda.stop()
            sounds.soundb.play()
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 9
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 8:
            sounds.sounda.stop()
            sounds.soundb.play()
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 9
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 9:
            centerbuttonavailable = False
            action = 10
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 11:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 28
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 12:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 13
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 13:
            centerbuttonavailable = rightbuttonavailable = leftbuttonavailable = True
            shooting()
        elif action == 16:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = rolling
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 17:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 30
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 30:
            centerbuttonavailable = False
            action = 22
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        else:
            quit()
    if role == 2:
        if action == 1:
            centerbuttonavailable = bool(False)
            action = 2
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 4:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 6
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 5:
            leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
            action = 6
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 6:
            sounds.sounda.stop()
            sounds.soundb.play()
            action = 7
            centerbuttonavailable = False
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 9:
            if choice3available and choice4available:
                leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
                action = 10
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
            else:
                centerbuttonavailable = bool(False)
                action = 11
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        else:
            quit()
    if role == 3:
        if action == 1:
            centerbuttonavailable = False
            action = 2
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 7:
            if anger == 1 or anger == 0:
                leftbuttonavailable = rightbuttonavailable = centerbuttonavailable = True
                action = 8
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
            elif anger == 2 or anger == 3:
                centerbuttonavailable = False
                action = 9
                curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        elif action == 10:
            centerbuttonavailable = bool(False)
            action = 13
            curtainname = 'c {} a {} r {}'.format(crisis,action,role)
        else:
            quit()
            
        
def shooting():
    global djinguiyuan
    global dchezhiche
    global dpiaozhengxi
    global shoot
    global curtainname
    global chezhiche
    global piaozhengxi
    global jinguiyuan
    global choice1available
    global choice2available
    global centerbuttonavailable
    global leftbuttonavailable
    global rightbuttonavailable
    global choice3available
    global choice4available
    shoot = True
    curtainname = 'shooting'
    chezhiche = Actor('chezhiche')
    chezhiche.pos = random.randint(300,700),random.randint(100,518)
    piaozhengxi = Actor('piaozhengxi')
    piaozhengxi.pos = random.randint(300,700),random.randint(100,518)
    jinguiyuan = Actor('jinguiyuan')
    jinguiyuan.pos = random.randint(300,700),random.randint(100,518)
    djinguiyuan = False
    dchezhiche = False
    dpiaozhengxi = False
    centerbuttonavailable = leftbuttonavailable = rightbuttonavailable = bool(False)
    clock.schedule_unique(shot,2.0)
    
def shot():
    global djinguiyuan
    global dchezhiche
    global dpiaozhengxi
    global shoot
    global curtainname
    global chezhiche
    global piaozhengxi
    global jinguiyuan
    global choice1available
    global choice2available
    global centerbuttonavailable
    global leftbuttonavailable
    global rightbuttonavailable
    global action
    global rolling
    global choice3available
    global choice4available
    shoot = False
    if dchezhiche == djinguiyuan == dpiaozhengxi == False:
        centerbuttonavailable = rightbuttonavailable = leftbuttonavailable = True
        curtainname = 'c 1 a 15 r 1'
        action = 15
    elif dchezhiche == True and dpiaozhengxi == djinguiyuan == False:
        if choice2available:
            centerbuttonavailable = rightbuttonavailable = leftbuttonavailable = True
            curtainname = 'c 1 a 29 r 1'
            action = 29
        else:
            rightbuttonavailable = leftbuttonavailable =centerbuttonavailable = True
            curtainname = 'c 1 a 16 r 1'
            rolling = random.randint(20,21)
            action = 16
            leftbuttonavailable = rightbuttonavailable = bool(True)
    elif dchezhiche == dpiaozhengxi == True and djinguiyuan == False:
        if choice2available:
            centerbuttonavailable = rightbuttonavailable = leftbuttonavailable = True
            curtainname = 'c 1 a 29 r 1'
            action = 29
        else:
            rightbuttonavailable = leftbuttonavailable =centerbuttonavailable = True
            curtainname = 'c 1 a 17 r 1'
            action = 17
    elif dchezhiche == dpiaozhengxi == djinguiyuan == True:
        if choice2available:
            centerbuttonavailable = rightbuttonavailable = leftbuttonavailable = True
            curtainname = 'c 1 a 29 r 1'
            action = 29
        else:
            centerbuttonavailable = rightbuttonavailable = leftbuttonavailable = True
            curtainname = 'c 1 a 18 r 1'
            action = 18
    else:
        if choice2available:
            centerbuttonavailable = rightbuttonavailable = leftbuttonavailable = True
            curtainname = 'c 1 a 29 r 1'
            action = 29
        else:
            centerbuttonavailable = rightbuttonavailable = leftbuttonavailable = True
            curtainname = 'c 1 a 19 r 1'
            action = 19
pgzrun.go()
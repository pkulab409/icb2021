import pgzrun

WIDTH = 1500
HEIGHT = 700

class ball:
    def __init__(self,color,size,x=0,y=0,vx=0,vy=0,m=1,belongTo = -1,numInPlayer = -1):
        self.x,self.y,self.vx,self.vy = x,y,vx,vy
        self.v = (vx*vx + vy*vy)**0.5
        self.color,self.size = color,size
        self.Actor = Actor(f'ball_{color}_{size}')
        self.Actor.center = x,y
        self.halfWid = x - self.Actor.midleft[0]
        self.halfHei = y - self.Actor.midtop[1]
        self.r = 1 * self.halfWid
        self.m = m
        self.moving = ((vx != 0) or (vy != 0))
        self.waitingToBeClicked = False
        self.onBoard = False
        self.belongTo = belongTo
        self.numInPlayer = numInPlayer
        self.recycledTimes = 0
    def accel(self,ax,ay):
        self.vx += ax
        self.vy += ay
        self.updatev()
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.updatev()
    def fric_accel(self,a):
        self.vx -= self.vx / self.v * a
        self.vy -= self.vy / self.v * a
        self.updatev()
    def updatev(self):
        self.v = (self.vx*self.vx + self.vy*self.vy)**0.5
        self.moving = ((self.vx != 0) or (self.vy != 0))
    def __str__(self):
        return(f'({self.color},{self.size},{self.onBoard},{id(self)})')
    __repr__ = __str__
    def copy(self):
        copyball = ball(self.color,self.size,self.x,self.y,self.vx,self.vy,self.m)
        copyball.waitingToBeClicked = self.waitingToBeClicked
        copyball.onBoard = self.onBoard
        copyball.belongTo = self.belongTo
        copyball.numInPlayer = self.numInPlayer
        copyball.recycledTimes = self.recycledTimes
        return copyball
class area:
    def __init__(self,x1,x2,y1,y2):
        self.x1,self.x2,self.y1,self.y2 = x1,x2,y1,y2
    def areaColliPoint(self,pos):
        return (pos[0]>=self.x1) and (pos[0]<=self.x2) and (pos[1]>=self.y1) and (pos[1]<=self.y2)
class player:
    def __init__(self,num,color,startPos,recycleArea,pointArea,ballShowx,pointShowPos,colorNum,sizelist = []):
        self.num,self.color = num,color
        self.ballsHeHas = [ball(color,sizelist[i],m = massdic1[sizelist[i]],belongTo = num,\
                                numInPlayer = i) for i in range(len(sizelist))]
        self.startPos = startPos
        self.recycleArea = recycleArea
        self.pointArea = pointArea
        self.ballShowx = ballShowx
        self.pointShowPos = pointShowPos
        self.colorNum = colorNum
        self.point = 0
    def __str__(self):
        return(f'({self.num},{self.color},{id(self)})')
    __repr__ = __str__
    def copy(self):
        playercopy = player(self.num,self.color,self.startPos,self.recycleArea,\
               self.pointArea,self.ballShowx,self.pointShowPos,self.colorNum)
        playercopy.ballsHeHas = []
        for ball1 in self.ballsHeHas:
            playercopy.ballsHeHas.append(ball1.copy())
        playercopy.point = self.point
        return playercopy
class gameSituation:
    def __init__(self,recentPlayerlist,recentBalllist):
        self.playerlist = recentPlayerlist
        self.balllist = recentBalllist
    def __str__(self):
        return(f'({self.playerlist},{self.balllist}\n')
    __repr__ = __str__
    def copy(self):
        sitcopy = gameSituation([],[])
        for player1 in self.playerlist:
            sitcopy.playerlist.append(player1.copy())
        for ball1 in self.balllist:
            ball1copy = sitcopy.playerlist[ball1.belongTo].ballsHeHas[ball1.numInPlayer]
            sitcopy.balllist.append(ball1copy)
        return sitcopy
    
class button:
    def __init__(self,text,center,buttonWidth,buttonHeight):
        self.text = text
        self.center = center
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.area = area(center[0]-0.5*buttonWidth,center[0]+0.5*buttonWidth,\
                         center[1]-0.5*buttonHeight,center[1]+0.5*buttonHeight)
sizelist3 = ['small','medium','large']
sizelist6 = ['small','medium','large','small','medium','large']
sizelist9 = ['small','medium','large','small','medium','large','small','medium','large']

goToMainButton = button('返回',(0.9*WIDTH,0.9*HEIGHT),110,60)
buttonslist = [button('双人对战-简单',(0.35*WIDTH,0.45*HEIGHT),220,60),\
               button('双人对战-标准',(0.35*WIDTH,0.6*HEIGHT),220,60),\
               button('人机对战-简单',(0.65*WIDTH,0.45*HEIGHT),330,60),\
               button('人机对战-标准',(0.65*WIDTH,0.6*HEIGHT),330,60),\
               button('人机对战-困难',(0.65*WIDTH,0.75*HEIGHT),330,60),\
               button('游戏规则',(0.5*WIDTH,0.9*HEIGHT),220,60)]

rules = '''弹来弹去游戏规则：
·左边白色区域是蓝方的发球区，右边白色区域是红方发球区。
·游戏中有三种球：大球、中球、小球，其质量依次递减，同种球质量相同。
·左下角和右下角显示双方球库中球的种类和数目，按发球顺序从上到下排列。
·双方轮流操作，每次操作时，系统自动取一颗球放到发球区，玩家用鼠标左键\n按住这颗球，将鼠标向想发射方向移动，，然后松开鼠标左键，这颗球就会被\n发射出去。发射速度与鼠标移动距离成正比。
·两颗球碰撞时遵循完全弹性碰撞的原理，球与墙壁相碰时没有能量损失。
·如果某颗球处在与它相同颜色的区域内，即可为这一颜色的一方提供一分，但\n是如果这颗球离开了相同颜色的区域，那么这一分也会消失。
·如果当所有球停下来时，某颗球停在某一方的发球区，则这颗球会被回收至这\n一方的球库中，放在球库最下面，它的颜色会被设置为这一方的颜色。
·每颗球至多被回收十次，超过此次数则会被销毁。
·场上所有球停下后，轮到另一方操作。此时可以按下屏幕上方中间的撤销键撤\n销一次操作。
·当场上所有球停下，且双方球库都没有球时，游戏结束，得分高的一方获胜。
游戏制作者：潘逸声 2021年12月于北京大学
'''

showBalls = False
playerlist = [player(0,'blue',(0.05*WIDTH,0.5*HEIGHT),area(0,0.15*WIDTH,0,HEIGHT),\
                    area(0.5*WIDTH,0.85*WIDTH,0,HEIGHT),ballShowx = 0.03*WIDTH,\
                    pointShowPos = (0.02*WIDTH,0.1*HEIGHT),colorNum = (43,135,255),\
                    sizelist = []),\
              player(1,'red',(0.95*WIDTH,0.5*HEIGHT),area(0.85*WIDTH,WIDTH,0,HEIGHT),\
                    area(0.15*WIDTH,0.5*WIDTH,0,HEIGHT),ballShowx = 0.97*WIDTH,\
                    pointShowPos = (0.86*WIDTH,0.1*HEIGHT),colorNum = (255,5,77),\
                    sizelist = [])]
massdic1 = {'small':1,'medium':3,'large':9}
totalPlayerNum = len(playerlist)
totalBallNum = sum([len(player2.ballsHeHas) for player2 in playerlist])
balllist = []
storedSitlist = []
goBackActor = Actor('goback_pic',(WIDTH/2,40))
choosingMode = True
showingRules = False
WaitingBallWasClicked = False
aBallIsWaiting = False
checkRecycle = False
gameEnd = False
humanVsComputer = False
computerNum = 1
debugging = False
gameMode = ''
whoseTurn = 0
mouseBegin,mouseEnd = (0,0),(0,0)
fric = 0.01
mouseToVRate = 60
maxRecycledTimes = 10
def colli(vx1,vy1,vx2,vy2,dirx,diry,m1,m2):
    dirl = (dirx**2+diry**2)**0.5
    vdir1 = (vx1*dirx + vy1*diry)/dirl
    vdir2 = (vx2*dirx + vy2*diry)/dirl
    vdir1s = ((m1-m2)*vdir1+2*m2*vdir2)/(m1+m2)
    vdir2s = ((m2-m1)*vdir2+2*m1*vdir1)/(m1+m2)
    vx1s = vx1 + (- vdir1 + vdir1s) * dirx / dirl
    vy1s = vy1 + (- vdir1 + vdir1s) * diry / dirl
    vx2s = vx2 + (- vdir2 + vdir2s) * dirx / dirl
    vy2s = vy2 + (- vdir2 + vdir2s) * diry / dirl
    return vx1s,vy1s,vx2s,vy2s

def draw():
    global aBallIsWaiting,checkRecycle
    global goBackActor
    screen.clear()
    
    screen.fill((230,230,230))
    screen.draw.filled_rect(Rect((playerlist[0].recycleArea.x2,0),\
                                 (0.5*WIDTH - playerlist[0].recycleArea.x2,HEIGHT)),playerlist[1].colorNum)
    screen.draw.filled_rect(Rect((0.5*WIDTH,0),\
                                 (playerlist[1].recycleArea.x1 - 0.5*WIDTH,HEIGHT)),playerlist[0].colorNum)
    
    if choosingMode:

        screen.draw.text("弹来弹去", center = (0.5*WIDTH,0.2*HEIGHT), fontname = 'cocacola',fontsize = 90,shadow=(2,2),\
                         color = (170,190,255),scolor=(255,110,140))
        for button in buttonslist:
            screen.draw.text(text = button.text,center = button.center,\
                             fontname = 'cocacola',fontsize = 50,color = 'black')
    elif showingRules:
        screen.draw.text("弹来弹去", center = (0.5*WIDTH,0.1*HEIGHT), fontname = 'cocacola',fontsize = 90,shadow=(2,2),\
                         color = (170,190,255),scolor=(255,110,140))
        screen.draw.text(text = rules,center = (0.5*WIDTH,0.6*HEIGHT),align='left',\
                         fontname = 'cocacola',fontsize = 30,color = 'black')
        screen.draw.text(text = goToMainButton.text,center = goToMainButton.center,\
                         fontname = 'cocacola',fontsize = 50,color = 'black')
    else:
        for circle in drawOffBoardBalls():
            screen.draw.filled_circle(*circle)
        for point in drawPoints():
            screen.draw.text(*point,fontname = 'cocacola',fontsize = 40,color = 'black')
        if gameMode != '人机对战-困难':
            goBackActor.draw()
        if gameEnd:
            for word in end():
                screen.draw.text(*word,fontsize = 30,fontname = 'cocacola',color = 'black')
            screen.draw.text(text = goToMainButton.text,center = goToMainButton.center,\
                             fontname = 'cocacola',fontsize = 50,color = 'black')
        for balls in balllist:       
            balls.Actor.draw()
        
def update():
    global balllist,playerlist,whoseTurn,gameEnd,checkRecycle,\
           storedSitlist
    if gameEnd:  
        return 0
    if choosingMode:
        return 0
    if showingRules:
        return 0
    if debugging:
        if set(balllist) != \
           set([ball1 for player1 in playerlist for ball1 in player1.ballsHeHas if ball1.onBoard]):
            print('balllist != onboard ball in playerlist')
            print(f'balllist {balllist}')
            print(f'playerlist {playerlist}')
            gameEnd = True
    for ball1 in balllist:
        ball1.move()
    if len(balllist) == 0:
        if debugging: print(f'zero ball')
        
        if debugging: print(f'whoseTurn {whoseTurn} because len = 0')
        haveAdded = addABallToBoard()
        
        if haveAdded:
            updateStoredSitlist()
            if (whoseTurn == computerNum) and humanVsComputer:
                clock.schedule_unique(computerMove, 3.0)
        else:
            noOneHaveBallOffBool = noOneHaveBallOff()
            if noOneHaveBallOffBool:
                if debugging: print('end')
                gameEnd = True
                return
            whoseTurn = (whoseTurn + 1) % totalPlayerNum
        
    elif all([not balls.moving for balls in balllist]) and (not aBallIsWaiting):
        noOneHaveBallOffBool = noOneHaveBallOff()
        if checkRecycle:
            judgeRecycle()
            whoseTurn = (whoseTurn + 1) % totalPlayerNum
            checkRecycle = False
        elif noOneHaveBallOffBool:
            if debugging: print('end')
            gameEnd = True
        elif (not checkRecycle) and (not noOneHaveBallOffBool):
            if debugging: print(f'no ball moving,balllist {balllist}')
            if debugging: print(f'playerlist{playerlist}')
            if debugging: print(f'whoseTurn {whoseTurn} because no ball moving')
            haveAdded = addABallToBoard()
            if haveAdded:
                updateStoredSitlist()
                if (whoseTurn == computerNum) and humanVsComputer:
                    if debugging: print('after 3 sec computerMove')
                    clock.schedule_unique(computerMove, 3.0)
            else:
                whoseTurn = (whoseTurn + 1) % totalPlayerNum
    elif any([balls.moving for balls in balllist]):
        judgeColli()
    for ball1 in balllist:
        ball1.Actor.center = ball1.x,ball1.y
    updatePoints()
def setPlayerlist(button_text):
    global playerlist,sizelist_player1,sizelist_player2,gameEnd,humanVsComputer
    if button_text == '双人对战-简单':
        sizelist_player1,sizelist_player2 = sizelist3,sizelist3
        humanVsComputer = False
    elif button_text == '双人对战-标准':
        sizelist_player1,sizelist_player2 = sizelist6,sizelist6
        humanVsComputer = False
    elif button_text == '人机对战-简单':
        sizelist_player1,sizelist_player2 = sizelist6,sizelist3
        humanVsComputer = True
    elif button_text == '人机对战-标准':
        sizelist_player1,sizelist_player2 = sizelist6,sizelist6
        humanVsComputer = True
    elif button_text == '人机对战-困难':
        sizelist_player1,sizelist_player2 = sizelist3,sizelist6
        humanVsComputer = True
    else:
        if debugging:print('mode not designed!')
        gameEnd = True
    playerlist[0].ballsHeHas = [ball(playerlist[0].color,sizelist_player1[i],m = massdic1[sizelist_player1[i]],\
                                     belongTo = playerlist[0].num,numInPlayer = i) for i in range(len(sizelist_player1))]
    playerlist[1].ballsHeHas = [ball(playerlist[1].color,sizelist_player2[i],m = massdic1[sizelist_player2[i]],
                                     belongTo = playerlist[1].num,numInPlayer = i) for i in range(len(sizelist_player2))]
    
def drawOffBoardBalls():
    global playerlist
    drawOffBoardBallsList = []
    for player1 in playerlist:
        lastShowTop = HEIGHT - 10
        ballShowx = player1.ballShowx
        for ball1 in player1.ballsHeHas[::-1]:
            if not ball1.onBoard:
                showr = ball1.r / 3
                drawOffBoardBallsList.append(((ballShowx,lastShowTop - showr - 5),showr,player1.colorNum))
                lastShowTop = lastShowTop - 5 - 2*showr
    return drawOffBoardBallsList
def drawPoints():
    global playerlist
    drawPointsList = []
    for player1 in playerlist:
        drawPointsList.append((f'得分:{player1.point}',player1.pointShowPos))
    return drawPointsList
def updatePoints():
    global playerlist
    for player1 in playerlist:
        player1.point = 0
        for ball1 in player1.ballsHeHas:
            if ball1.onBoard and (ball1.x > player1.pointArea.x1) and (ball1.x < player1.pointArea.x2):
                player1.point += 1
def addABallToBoard():
    global whoseTurn,playerlist,balllist,aBallIsWaiting,\
           totalPlayerNum,storedSitlist
    ballCanBeAdded = [ball1 for ball1 in playerlist[whoseTurn].ballsHeHas if not ball1.onBoard]
    if len(ballCanBeAdded) == 0:
        return False
    elif len(ballCanBeAdded) > 0:
        ball1 = ballCanBeAdded[0]
        ball1.x,ball1.y = playerlist[whoseTurn].startPos[0],playerlist[whoseTurn].startPos[1]
        ball1.onBoard = True
        balllist.append(ball1)
        aBallIsWaiting = True
        
        for i in range(len(balllist) - 1):
            ball2 = balllist[i]
            distance = ((ball1.x - ball2.x)**2+(ball1.y - ball2.y)**2)**0.5
            if distance <= ball1.r + ball2.r: 
                #if debugging: print(f'colli with {ball2}')
                if (distance <= ball1.r + ball2.r) and ((ball1.v > 0) or (ball2.v > 0)):
                    if distance == 0:
                        distance,dirx = 0.01,0.01
                    dirx = ball1.x - ball2.x
                    diry = ball1.y - ball2.y
                    ball2.x = ball1.x - (ball1.r + ball2.r) / distance * dirx
                    ball2.y = ball1.y - (ball1.r + ball2.r) / distance * diry
                    if (ball2.x - ball2copy.r < 0) or (ball2.x + ball2.r > WIDTH):
                        ball2.x = ball1.x + (ball1.r + ball2.r) / distance * dirx
                    if (ball2.y - ball2copy.r < 0) or (ball2.y + ball2.r > HEIGHT):
                        ball2.y = ball1.y + (ball1.r + ball2.r) / distance * diry
        if debugging: print(f'have added a ball,balllist {balllist}')
        if debugging: print(f'playerlist {playerlist}')
        sounds.whistle.play()
        return True
        
        
    
def judgeColli():
    global balllist,playerlist
    for i in range(len(balllist)):
        ball1 = balllist[i]
        for j in range(i+1,len(balllist)):
            ball2 = balllist[j]
            distance = ((ball1.x - ball2.x)**2+(ball1.y - ball2.y)**2)**0.5
            if (distance <= ball1.r + ball2.r) and ((ball1.v > 0) or (ball2.v > 0)):
                sounds.collide.play()
                if distance == 0:
                    distance = 0.01
                dirx = ball1.x - ball2.x
                diry = ball1.y - ball2.y
                ball2.x = ball1.x - (ball1.r + ball2.r) / distance * dirx
                ball2.y = ball1.y - (ball1.r + ball2.r) / distance * diry
                ball1.vx,ball1.vy,ball2.vx,ball2.vy = \
                    colli(ball1.vx,ball1.vy,ball2.vx,ball2.vy,\
                          ball1.x - ball2.x,ball1.y - ball2.y,ball1.m,ball2.m)
                ball1.updatev()
                ball2.updatev()
                
        if ball1.v == 0:
            continue
        if (ball1.x + ball1.halfWid >= WIDTH) and (ball1.vx > 0):
            sounds.collide.play()
            ball1.x = WIDTH - ball1.halfWid
            ball1.vx *= -1
        if (ball1.x - ball1.halfWid <= 0) and (ball1.vx < 0):
            sounds.collide.play()
            ball1.x = ball1.halfWid
            ball1.vx *= -1
        if (ball1.y + ball1.halfHei >= HEIGHT) and (ball1.vy > 0):
            sounds.collide.play()
            ball1.y = HEIGHT - ball1.halfHei
            ball1.vy *= -1
        if (ball1.y - ball1.halfHei <= 0) and (ball1.vy < 0):
            sounds.collide.play()
            ball1.y = ball1.halfHei
            ball1.vy *= -1
        if ball1.v > fric:
            ball1.fric_accel(fric)
        elif ball1.v <= fric:
            ball1.vx,ball1.vy = 0,0
        ball1.updatev()

def judgeRecycle():
    global balllist,playerlist

    i = 0
    while i <= len(balllist) - 1:
        ball1 = balllist[i]
        for j in range(len(playerlist)):
            player1 = playerlist[j]
            if (ball1.x > player1.recycleArea.x1) and (ball1.x < player1.recycleArea.x2):
                if debugging: print(f'del ball{balllist[i]}')
                del balllist[i]
                for k in range(ball1.numInPlayer + 1,len(playerlist[ball1.belongTo].ballsHeHas)):
                    playerlist[ball1.belongTo].ballsHeHas[k].numInPlayer -= 1
                del playerlist[ball1.belongTo].ballsHeHas[ball1.numInPlayer]
                ball1.recycledTimes += 1
                if ball1.recycledTimes < maxRecycledTimes:
                    ball1.color = playerlist[j].color
                    ball1.Actor.image = f'ball_{ball1.color}_{ball1.size}'
                    ball1.onBoard = False
                    ball1.belongTo = j
                    ball1.numInPlayer = len(playerlist[j].ballsHeHas)
                    ball1.x,ball1.y,ball1.vx,ball1.vy,ball1.v,ball1.moving = 0,0,0,0,0,False
                    playerlist[j].ballsHeHas.append(ball1)
                    if debugging: print(f'add to player{playerlist[j]}')
                break
        else:
            i += 1
def noOneHaveBallOff():
    global playerlist
    for player1 in playerlist:
        if len(player1.ballsHeHas) != 0:
            if not all([ball1.onBoard for ball1 in player1.ballsHeHas]):
                return False
    else:
        return True
def updateStoredSitlist():
    global balllist,playerlist,storedSitlist
    storedSitlist.append(gameSituation(playerlist,balllist).copy())
    if debugging:print(f'update storedSitlist {storedSitlist}\n')

def computerMove():
    global balllist,aBallIsWaiting,checkRecycle
    if balllist[-1].belongTo != computerNum:
        return
    highBallNum,highBallx,highBally = 0,0,0
    lowBallNum,lowBallx,lowBally = 0,0,0
    highBallM,lowBallM = 0,0
    startx,starty = playerlist[1].startPos
    humanOnBoard = 0
    slightMove = False
    useTheta = False
    for ball1 in balllist:
        if ball1.belongTo != computerNum:
            humanOnBoard += 1
        if (ball1.y < 0.5*HEIGHT) and (ball1.x > 0.5*WIDTH):
            highBallNum += 1
            highBallM += ball1.m
            if highBallx < ball1.x:
                highBallx = ball1.x
                highBally = ball1.y
        elif (ball1.y > 0.5*HEIGHT) and (ball1.x > 0.5*WIDTH):
            lowBallNum += 1
            lowBallM += ball1.m
            if lowBallx < ball1.x:
                lowBallx = ball1.x
                lowBally = ball1.y
    
    if (humanOnBoard == len((playerlist[0].ballsHeHas))) and \
       playerlist[0].point < playerlist[1].point:
        slightMove = True
    else:
        useTheta = True
    if slightMove:
        balllist[-1].vx = -3
    elif useTheta:
        if highBallNum > lowBallNum:
#             highBallx /= highBallNum
#             highBally /= highBallNum
            tanTheta = (highBally - starty) / (highBallx - startx)
            targetNum = highBallNum
            targetM = highBallM
        elif highBallNum < lowBallNum:
#             lowBallx /= lowBallNum
#             lowBally /= lowBallNum
            tanTheta = (lowBally - starty) / (lowBallx - startx)
            targetNum = lowBallNum
            targetM = lowBallM
        else:
            tanTheta = 0
            targetNum = 1
            targetM = balllist[-1].m
        cosTheta = 1/((1+tanTheta**2)**0.5)
        sinTheta = cosTheta * tanTheta
        v = (0.75*WIDTH / cosTheta * 2 * fric)**0.5#* max((targetM / balllist[-1].m)**0.5,1)
        if targetM == balllist[-1].m*9:
            v *= 3
        elif targetM == balllist[-1].m*3:
            v *= 1.3
        elif targetM*3 == balllist[-1].m:
            v /= 2
        elif targetM*9 == balllist[-1].m:
            v /= 3  
        balllist[-1].vx,balllist[-1].vy = -v*cosTheta,-v*sinTheta
    aBallIsWaiting = False
    checkRecycle = True
def on_mouse_down(pos,button):
    global playerlist,balllist,WaitingBallWasClicked,mouseBegin,aBallIsWaiting,\
           goBackActor,storedSitlist,whoseTurn,checkRecycle,buttonslist,choosingMode,\
           showingRules,gameEnd,gameMode
    if button == mouse.LEFT:
        if debugging:print(pos)
        if debugging: print(f'LEFT is clicked ,whoseTurn{whoseTurn}')
        if choosingMode:
            for button in buttonslist:
                if button.area.areaColliPoint(pos):
                    if button.text == '游戏规则':
                        choosingMode = False
                        showingRules = True
                        
                    else:
                        gameMode = button.text
                        setPlayerlist(button.text)
                        choosingMode = False
        if showingRules:
            if goToMainButton.area.areaColliPoint(pos):
                showingRules = False
                choosingMode = True
        if aBallIsWaiting and (balllist[-1].Actor.collidepoint(pos)) and \
           not ((whoseTurn == computerNum) and humanVsComputer):
            if debugging:print('Waiting ball is clicked')
            WaitingBallWasClicked = True
            mouseBegin = pos
        if goBackActor.collidepoint(pos) and (len(storedSitlist) > 1) and (gameMode != '人机对战-困难'):
            if aBallIsWaiting or WaitingBallWasClicked:
                del storedSitlist[-1]
            
            whoseTurn = storedSitlist[-1].balllist[-1].belongTo
            lastSituation = storedSitlist[-1]
            playerlist,balllist = lastSituation.playerlist,lastSituation.balllist
            if debugging:print(f'goBack is clicked {playerlist},{balllist}')
            del storedSitlist[-1]
            updateStoredSitlist()
            if (whoseTurn == computerNum) and humanVsComputer:
                if debugging:print('after 3 sec computerMove')
                clock.schedule_unique(computerMove, 3.0)
            checkRecycle = False
            aBallIsWaiting = True
            gameEnd = False
        if gameEnd and goToMainButton.area.areaColliPoint(pos):
            gameRestart()
    
def on_mouse_up(pos,button):
    global balllist,WaitingBallWasClicked,mouseBegin,aBallIsWaiting,checkRecycle
    if (button == mouse.LEFT) and WaitingBallWasClicked :
        balllist[-1].accel((pos[0] - mouseBegin[0])/mouseToVRate,(pos[1] - mouseBegin[1])/mouseToVRate)
        WaitingBallWasClicked = False
        aBallIsWaiting = False
        checkRecycle = True
    
        
def end():
    global playerlist
    endList = []
    winner = max(playerlist,key = lambda player1 : player1.point)
    second = max([player1 for player1 in playerlist if player1 != winner],key = lambda player1 : player1.point)
    tie = (winner.point == second.point)
    
    for player1 in playerlist:
        if tie:
            endList.append(('平局！',(player1.pointShowPos[0],player1.pointShowPos[1] + 0.1*HEIGHT)))
        elif player1 == winner:
            if (gameMode == '人机对战-困难') and (player1.num != computerNum) :
                endList.append(('了不起！\n谢谢你玩我的游戏\n欢迎与我交流：\nQQ2270606437\n潘逸声',\
                                (player1.pointShowPos[0],player1.pointShowPos[1] + 0.1*HEIGHT)))
            else:
                endList.append(('恭喜！你赢了！',(player1.pointShowPos[0],player1.pointShowPos[1] + 0.1*HEIGHT)))
        else:
            endList.append(('抱歉，你输了。',(player1.pointShowPos[0],player1.pointShowPos[1] + 0.1*HEIGHT)))
    return endList
def gameRestart():
    global playerlist,balllist,storedSitlist,choosingMode,showingRules,WaitingBallWasClicked,\
           aBallIsWaiting,checkRecycle,gameEnd,humanVsComputer,gameMode,whoseTurn
    playerlist = [player(0,'blue',(0.05*WIDTH,0.5*HEIGHT),area(0,0.15*WIDTH,0,HEIGHT),\
                    area(0.5*WIDTH,0.85*WIDTH,0,HEIGHT),ballShowx = 0.03*WIDTH,\
                    pointShowPos = (0.02*WIDTH,0.1*HEIGHT),colorNum = (43,135,255),\
                    sizelist = []),\
              player(1,'red',(0.95*WIDTH,0.5*HEIGHT),area(0.85*WIDTH,WIDTH,0,HEIGHT),\
                    area(0.15*WIDTH,0.5*WIDTH,0,HEIGHT),ballShowx = 0.97*WIDTH,\
                    pointShowPos = (0.86*WIDTH,0.1*HEIGHT),colorNum = (255,5,77),\
                    sizelist = [])]
    balllist = []
    storedSitlist = []
    choosingMode = True
    showingRules = False
    WaitingBallWasClicked = False
    aBallIsWaiting = False
    checkRecycle = False
    gameEnd = False
    humanVsComputer = False
    gameMode = ''
    whoseTurn = 0
    
pgzrun.go()
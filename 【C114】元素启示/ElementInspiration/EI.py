import pgzrun
import random

#窗口大小：1280×800
WIDTH = 1280
HEIGHT = 800
TITLE = "元素启示"
music.play("panorama")
####################################################
#主游戏板，记录游戏的整体信息
#status:游戏的当前阶段
#help_page:当处在"Help"状态时，记录帮助的页数，默认为1
#pause:当处在主游戏阶段时是否正在暂停。None表示没有暂停，"Player"表示由玩家按esc键主动暂停，"Void"表示由虚空选牌引发的暂停，"Skill"表示技能引发的暂停
#whose_character:当处在角色选择时，在选择谁的角色
#character_list:可选的角色列表
#initialize():初始化
#shuffle():重新将弃牌堆洗为牌库
#card_left:牌库中剩余的牌
#card_played:弃牌堆
#card_displayed:上一次打出的所有牌
#display():展示上一次打出的所有牌
#whose_round:此回合该谁操作
#round_skipped:已经放弃的回合数。当到达2时，重置桌面
#win():赢，没什么实际意义，仅仅是为了配合延时
#lose():同上
#round_skipped_display:展示对方放弃的文字显示
#cancel_round_skipped_display():取消对方放弃文字显示（没实际意义，配合延迟）
#void_choice_display:展示对方虚空选择了什么牌的文字展示
#cancel_void_choice_display():同
#skill_display:展示对方使用了技能的文字展示
#cancel_skill_play():同
#start_choose():开始选择角色，同
#number_list:10~20的数字列表，给隐匿猎手选抽牌数用的
####################################################
class MainGame():
    def __init__(self):
        self.status = "MainTitle"
        self.help_page = 1
        self.pause = None
        self.whose_character = ""
        self.character_list = [Actor(f"character{i}") for i in range(10)]
        self.card_left = []
        self.card_played = []
        self.card_displayed = CardList()
        self.round_skipped = 0
        self.whose_round = "P1"
        self.round_skipped_display = False
        self.void_choice_display = False
        self.skill_display = False
        self.number_list = [Actor(f"{i}") for i in range(10,21)]
    def initialize(self):
        self.pause = None
        self.card_left = []
        self.card_played = []
        self.whose_round = random.choice(["P1","Bot"])
        for _ in range(25):
            self.card_left.append(Card(0))
        for _ in range(12):
            self.card_left.append(Card(1))
            self.card_left.append(Card(2))
            self.card_left.append(Card(3))
        for _ in range(4):
            self.card_left.append(Card(4))
            self.card_left.append(Card(5))
        for _ in range(2):
            self.card_left.append(Card(6))
            self.card_left.append(Card(7))
        P1.card=[]
        Bot.card=[]
        self.card_displayed.clear()
        self.round_skipped = 0
        P1.card_ready.clear()
        Bot.card_ready.clear()
        P1.card_ready.owner = "P1"
        Bot.card_ready.owner = "Bot"
        self.card_displayed.owner = ""
        self.round_skipped_display = False
        self.void_choice_display = False
        self.skill_display = False
        self.whose_character = "P1"
    def shuffle(self):
        for _ in range(len(self.card_played)):
            self.card_left.append(self.card_played.pop())
    def display(self):
        self.card_displayed.sort(key = lambda x:x.card_type)
        for index in range(len(self.card_displayed)):
            self.card_displayed[index].image = f"card{self.card_displayed[index].card_type}"
            if len(self.card_displayed) <= 10:
                self.card_displayed[index].center = (640 + 120*(index - (len(self.card_displayed)-1)/2),400)
            else:
                self.card_displayed[index].center = (100 + (1180-100) * index / (len(self.card_displayed) - 1),400)
    def win(self):
        self.status = "Win"
        music.play("somero")
    def lose(self):
        self.status = "Lose"
        music.play("lastone")
    def cancel_round_skipped_display(self):
        if self.pause != "Player":
            self.round_skipped_display = False
        else:
            clock.schedule(self.cancel_round_skipped_display,1.5)
    def cancel_void_choice_display(self):
        if self.pause != "Player":
            self.void_choice_display = False
        else:
            clock.schedule(self.cancel_void_choice_display,1.5)
    def cancel_skill_display(self):
        if self.pause != "Player":
            self.skill_display = False
        else:
            clock.schedule(self.cancel_skill_display,1.5)
    def start_choose(self):
        self.whose_character = "P1"
        self.status = "CharacterChoose"
        for index in range(10):
            self.character_list[index].image = f"character{index}"
        #暂时移除开始菜单按钮
        StartGameButton.center = (0,-100)
        HelpButton.center = (0,-100)
        AboutButton.center = (0,-100)
        ExitButton.center = (0,-100)
    def start_game(self):
        self.status = "Game"
        music.play("chasethesun")
        self.initialize()
        if Bot.character != "隐匿猎手":
            Bot.draw_card(15)
        else:
            Bot.draw_card(10)
        if P1.character != "隐匿猎手":
            P1.draw_card(15)
            P1.card.sort(key = lambda x:x.card_type)
            for index in range(len(P1.card)):
                if len(P1.card) <= 10:
                    P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
                else:
                    P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
            if Game.whose_round == "Bot":
                clock.schedule_unique(Bot.ready_auto_play,1.5)
        else:
            Game.pause = "Skill2"

####################################################
#卡牌，继承Actor类
#card_type:卡牌的类别。0,1,2,3,4,5,6,7分别代表风、火、草、水、光、暗、永恒、虚空
####################################################
class Card(Actor):
    #新构造函数
    def __init__(self,card_type_input):
        super().__init__(f"card{card_type_input}")
        self.card_type = card_type_input
    def __str__(self):
        return f"{self.card_type}"
    def __repr__(self):
        return f"{self.card_type}"

####################################################
#手中即将打出的卡牌的列表，继承list类
#obey_rule():是否符合规则
#__gt__():卡牌组合的压制关系
#points():点数（在obey_rule()==True基础上）
#draw_num():打出此卡组需要抽取的牌数
#owner:牌组的所有者
####################################################
class CardList(list):
    def __init__(self):
        super().__init__(self)
        self.owner = ""
    def obey_rule(self):
        type_list = [EveryCard.card_type for EveryCard in self]
        if self.owner == "P1" and P1.character == "虚空领主" and P1.skill_activated == True:
            if len(self) == 1:
                return True
            else:
                return False
        else:
            if len(self) == 0:
                return False
            elif len(set([1,2,3,4,5,6,7])&set(type_list)) >= 2:
                return False
            elif 7 in type_list and (len(type_list) >= 2 or len(Game.card_played) == 0):
                return False
            else:
                return True
    def points(self):
        num = []
        type_list = [EveryCard.card_type for EveryCard in self]
        for i in range(8):
            num.append(type_list.count(i))
        if self.owner == "P1" and P1.character == "虚空领主" and P1.skill_activated == True:
            return 0.0
        elif num[0] == len(self):
            return round(0.33*num[0],2)
        else:
            if (self.owner == "P1" and P1.character != "大魔法师") or (self.owner == "Bot" and Bot.character != "大魔法师"):
                return round((0.5*num[0] + 1*(num[1] + num[2] + num[3]) + 2*(num[4] + num[5]) + 1000*num[6]),2)
            else:
                return round((0.5*num[0] + 2*(num[1] + num[2] + num[3]) + 2*(num[4] + num[5]) + 1000*num[6]),2)
    def __gt__(self,other):
        type_list = [EveryCard.card_type for EveryCard in self]
        other_list = [EveryCard.card_type for EveryCard in other]
        if 7 in type_list or 7 in other_list:
            return True
        if self.owner == "P1" and P1.character == "虚空领主" and P1.skill_activated == True and len(self) == 1:
            return True
        if (4 in type_list and 5 in other_list) or (5 in type_list and 4 in other_list):
            return True
        if self.owner == "P1" and P1.character == "未来旅人" and P1.skill_activated == True:
            if (3 in type_list and 2 in other_list) or (2 in type_list and 1 in other_list) or (1 in type_list and 3 in other_list):
                return True
            elif (not ((1 in type_list and 2 in other_list) or (2 in type_list and 3 in other_list) or (3 in type_list and 1 in other_list))) and self.points() > other.points():
                return True
            else:
                return False
        else:
            if (1 in type_list and 2 in other_list) or (2 in type_list and 3 in other_list) or (3 in type_list and 1 in other_list):
                return True
            elif (not ((3 in type_list and 2 in other_list) or (2 in type_list and 1 in other_list) or (1 in type_list and 3 in other_list))) and self.points() > other.points():
                return True
            else:
                return False        
    def draw_num(self):
        type_list = [EveryCard.card_type for EveryCard in self]
        if 0 < type_list.count(0) < len(self):
            return (type_list.count(0) + 1)//2
        else:
            return 0
        
Game = MainGame()
#用这个牌来代表虚空领主发动了技能
TempVoidCard = Card(7)

##########################################################
#玩家类
#card:手中所有牌的列表
#card_ready:准备打出的所有牌的CardList
#void_pool:虚空池（卡牌标号）
#void_card_pool:虚空卡池（卡牌）
#draw_card():抽牌
#play():打牌
#auto_play():全自动打牌！！！（好吧其实是机器人的出牌方法）
#ready_auto_play():为了防止暂停的时候机器人还能打牌
#last_void_choice:上一次抽取了什么虚空牌
#character:所选角色
#character_number:所选角色标号
#skill_times:技能如果有使用次数限制，还可以使用几次
#skill_activated:技能是否正在激活中
#skill4_max_number:当影锋发动技能时，用来存储最大弃牌数量的变量
#skill5_counts:天灾引者的回合数计数
#skill6_draw_num:当永恒铸造师发动技能时，用来暂时存放抽牌数量的变量
#skill7_ready:当星轨分离者发动技能时，用来暂时存放上一张是否是虚空的变量
#switch_to_skill7:转成"Skill7"的函数，仅仅是为了配合延时
#already_displayed:机器人是否已经展示了星轨分离者的技能信息
##########################################################
class Player():
    def __init__(self):
        self.card = []
        self.card_ready = CardList()
        self.void_pool = []
        self.void_card_pool = []
        self.last_void_choice = ''
        self.character = ''
        self.character_number = 0
        self.skill_times = 0
        self.skill_activated = False
        self.skill4_max_number = 0
        self.skill5_counts = 0
        self.skill6_draw_num = 0
        self.skill7_ready = False
        self.already_displayed = False
    def draw_card(self,num):
        if num > len(Game.card_left):
            Game.shuffle()
        for _ in range(min(num , 20 - len(self.card))):
            temp_index = random.randint(0,len(Game.card_left)-1)
            self.card.append(Game.card_left.pop(temp_index))
        P1.card.sort(key = lambda x:x.card_type)
    def play(self):
        #将所有卡牌的类型组成一个暂时的新列表，便于统计
        type_ready = [EveryCard.card_type for EveryCard in self.card_ready]
        type_display = [EveryCard.card_type for EveryCard in Game.card_displayed]
        type_ready_set = set(type_ready)
        type_display_set = set(type_display)
        intersection_set = type_ready_set & type_display_set
        if 7 in type_ready and 7 in type_display and self.skill_activated == False:
            self.skill7_ready = True
        #首先清空上一轮打出的牌，准备替代
        Game.card_displayed.clear()
        #如果打出的是虚空牌
        if 7 in type_ready:
            #先暂停
            Game.pause = "Void"
            #统计当前所有能换的牌
            self.void_pool = sorted(list(set(EveryCard.card_type for EveryCard in Game.card_played)))
            self.void_card_pool = []
            for i in self.void_pool:
                TempCard = Card(i)
                TempCard.image = f"voidcard{i}"
                self.void_card_pool.append(TempCard)
            #在屏幕上展示它们
            for index in range(len(self.void_pool)):
                self.void_card_pool[index].center = (640 + 150*(index - (len(self.void_pool)-1)/2),400)
        #如果打出的不是虚空牌但是虚空领主发动了技能
        if self.character == "虚空领主" and self.skill_activated == True:
            #先暂停
            Game.pause = "Void"
            #统计当前所有能换的牌
            self.void_pool = sorted(list(set(EveryCard.card_type for EveryCard in Game.card_played)))
            self.void_card_pool = []
            for i in self.void_pool:
                TempCard = Card(i)
                TempCard.image = f"voidcard{i}"
                self.void_card_pool.append(TempCard)
            #在屏幕上展示它们
            for index in range(len(self.void_pool)):
                self.void_card_pool[index].center = (640 + 150*(index - (len(self.void_pool)-1)/2),400)
        temp_num = self.card_ready.draw_num()
        #打出选中的牌，并添加到展示牌和弃牌堆中
        if self.character == "虚空领主" and self.skill_activated == True:
            Game.card_displayed.append(TempVoidCard)
            Game.card_played.append(self.card_ready[0])
            self.card.remove(self.card_ready.pop(0))
        else:
            for i in range(len(self.card_ready)):
                Game.card_displayed.append(self.card_ready[0])
                Game.card_played.append(self.card_ready[0])
                self.card.remove(self.card_ready.pop(0))
        Game.round_skipped = 0
        self.card.sort(key = lambda x:x.card_type)
        for index in range(len(self.card)):
            if len(self.card) <= 10:
                self.card[index].midbottom = (640 + 120*(index - (len(self.card)-1)/2),700)
            else:
                self.card[index].midbottom = (100 + (1180 - 100) * index/(len(self.card) - 1),700)
        #如果是影锋的技能发动条件，询问是否弃牌
        if self.character == "影锋" and ((4 in type_ready and 5 in type_display) or (5 in type_ready and 4 in type_display)):
            self.draw_card(temp_num)
            if len(self.card) == 0:
                clock.schedule(Game.win,1.5)
            else:
                self.card.sort(key = lambda x:x.card_type)
                for index in range(len(self.card)):
                    if len(self.card) <= 10:
                        self.card[index].midbottom = (640 + 120*(index - (len(self.card)-1)/2),700)
                    else:
                        self.card[index].midbottom = (100 + (1180 - 100) * index/(len(self.card) - 1),700)
                Game.pause = "Skill4"
                Game.card_displayed.owner = "P1"
                self.skill4_max_number = type_ready.count(4) + type_ready.count(5)
        #如果是永恒铸造师的技能发动条件，询问是否取消摸牌
        elif self.character == "永恒铸造师" and 0 in type_ready and 6 in type_ready:
            Game.pause = "Skill6Play"
            Game.card_displayed.owner = "P1"
            self.skill6_draw_num = temp_num
        #如果是星轨分离者的技能发动条件，询问是否需要额外回合
        elif self.character == "星轨分离者" and ( (type_ready_set == set([0]) and type_display_set == set([0])) or (len(intersection_set) > 0 and intersection_set != set([0])) ) and self.skill_activated == False and not Game.pause:
            self.draw_card(temp_num)
            for index in range(len(self.card)):
                if len(self.card) <= 10:
                    self.card[index].midbottom = (640 + 120*(index - (len(self.card)-1)/2),700)
                else:
                    self.card[index].midbottom = (100 + (1180 - 100) * index/(len(self.card) - 1),700)
            Game.card_displayed.owner = "P1"
            if (not 7 in type_ready) and len(self.card) > 0:
                Game.pause = "Skill7"
            if len(P1.card) == 0 and not Game.pause:     
                clock.schedule_unique(Game.win,1.5)
        #如果不是，正常出牌
        else:
            #抽牌，交换操作权
            self.draw_card(temp_num)
            for index in range(len(self.card)):
                if len(self.card) <= 10:
                    self.card[index].midbottom = (640 + 120*(index - (len(self.card)-1)/2),700)
                else:
                    self.card[index].midbottom = (100 + (1180 - 100) * index/(len(self.card) - 1),700)
            Game.whose_round = "Bot"
            Game.card_displayed.owner = "P1"
            #如果没有虚空，并且没有赢，那么1.5秒后机器人出牌
            if (not 7 in type_ready) and len(self.card) > 0:
                clock.schedule_unique(Bot.ready_auto_play,1.5)
            if len(P1.card) == 0 and not Game.pause:     
                clock.schedule_unique(Game.win,1.5)
        #处理一下技能的使用情况
        if P1.character_number == 1 and P1.skill_activated == True:
            P1.skill_times = P1.skill_times - 1
        P1.skill_activated = False
    def auto_play(self):
        #先创建一个类型列表，以便操作
        type_list = [EveryCard.card_type for EveryCard in self.card]
        #再来一个场上牌的类型列表
        type_displayed = [EveryCard.card_type for EveryCard in Game.card_displayed]
        
        #再创建一个临时变量，表示是否要打出虚空
        play_void = False
        #首先尝试用属性去克制
        if 1 in type_displayed and 3 in type_list:
            for i in range(len(self.card)):
                if self.card[i].card_type == 0 or self.card[i].card_type == 3:
                    self.card_ready.append(self.card[i])
        elif 2 in type_displayed and 1 in type_list:
            for i in range(len(self.card)):
                if self.card[i].card_type == 0 or self.card[i].card_type == 1:
                    self.card_ready.append(self.card[i])
        elif 3 in type_displayed and 2 in type_list:
            for i in range(len(self.card)):
                if self.card[i].card_type == 0 or self.card[i].card_type == 2:
                    self.card_ready.append(self.card[i])
        elif 4 in type_displayed and 5 in type_list:
            for i in range(len(self.card)):
                if self.card[i].card_type == 0 or self.card[i].card_type == 5:
                    self.card_ready.append(self.card[i])
        elif 5 in type_displayed and 4 in type_list:
            for i in range(len(self.card)):
                if self.card[i].card_type == 0 or self.card[i].card_type == 4:
                    self.card_ready.append(self.card[i])
        #如果不行，那就拼点数   
        else:
            #如果不是大魔法师
            if Bot.character != "大魔法师":
                #先拼点数
                if type_list.count(0) * 0.5 + type_list.count(1) * 1 > Game.card_displayed.points() and type_list.count(1) > 0 and not 3 in type_displayed:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 1:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.5 + type_list.count(2) * 1 > Game.card_displayed.points() and type_list.count(2) > 0 and not 1 in type_displayed:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 2:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.5 + type_list.count(3) * 1 > Game.card_displayed.points() and type_list.count(3) > 0 and not 2 in type_displayed:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 3:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.5 + type_list.count(4) * 2 > Game.card_displayed.points() and type_list.count(4) > 0:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 4:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.5 + type_list.count(5) * 2 > Game.card_displayed.points() and type_list.count(5) > 0:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 5:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.5 + type_list.count(6) * 1000 > Game.card_displayed.points() and type_list.count(6) > 0:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 6:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.33 > Game.card_displayed.points():
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0:
                            self.card_ready.append(self.card[i])
                #再看是不是未来旅人
                elif self.character == "未来旅人" and self.skill_times >= 1:
                    if 2 in type_displayed and 3 in type_list:
                        self.skill_times = self.skill_times - 1
                        Game.skill_display = True
                        for i in range(len(self.card)):
                            if self.card[i].card_type == 0 or self.card[i].card_type == 3:
                                self.card_ready.append(self.card[i])
                    elif 3 in type_displayed and 1 in type_list:
                        self.skill_times = self.skill_times - 1
                        Game.skill_display = True
                        for i in range(len(self.card)):
                            if self.card[i].card_type == 0 or self.card[i].card_type == 1:
                                self.card_ready.append(self.card[i])
                    elif 1 in type_displayed and 2 in type_list:
                        self.skill_times = self.skill_times - 1
                        Game.skill_display = True
                        for i in range(len(self.card)):
                            if self.card[i].card_type == 0 or self.card[i].card_type == 2:
                                self.card_ready.append(self.card[i])
                #如果还不行，打虚空
                elif 7 in type_list and len(Game.card_played) > 0 and len(P1.card) >= 2:
                    self.card_ready.append([EveryCard for EveryCard in self.card if EveryCard.card_type == 7][0])
                    play_void = True
                #如果不行，看看是不是虚空领主
                elif self.character == "虚空领主" and len(Game.card_played) > 0 and len(P1.card) >= 2:
                    #用最小的牌当虚空打
                    self.card.sort(key = lambda x:x.card_type)
                    self.card_ready.append(self.card[0])
                    self.skill_activated = True
                    Game.skill_display = True
                    play_void = True
            #如果是大魔法师
            else:
                if type_list.count(0) * 0.5 + type_list.count(1) * 2 > Game.card_displayed.points() and type_list.count(1) > 0 and not 3 in type_displayed:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 1:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.5 + type_list.count(2) * 2 > Game.card_displayed.points() and type_list.count(2) > 0 and not 1 in type_displayed:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 2:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.5 + type_list.count(3) * 2 > Game.card_displayed.points() and type_list.count(3) > 0 and not 2 in type_displayed:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 3:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.5 + type_list.count(4) * 2 > Game.card_displayed.points() and type_list.count(4) > 0:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 4:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.5 + type_list.count(5) * 2 > Game.card_displayed.points() and type_list.count(5) > 0:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 5:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.5 + type_list.count(6) * 1000 > Game.card_displayed.points() and type_list.count(6) > 0:
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0 or self.card[i].card_type == 6:
                            self.card_ready.append(self.card[i])
                elif type_list.count(0) * 0.33 > Game.card_displayed.points():
                    for i in range(len(self.card)):
                        if self.card[i].card_type == 0:
                            self.card_ready.append(self.card[i])
                #如果还不行，打虚空
                elif 7 in type_list and len(Game.card_played) > 0 and len(P1.card) >= 2:
                    self.card_ready.append([EveryCard for EveryCard in self.card if EveryCard.card_type == 7][0])
                    play_void = True
        #如果无论如何不行，那么就空着，准备放弃
        type_ready = [EveryCard.card_type for EveryCard in self.card_ready]
        #再来几个集合
        type_displayed_set = set(type_displayed)
        type_ready_set = set(type_ready)
        i_set = type_displayed_set & type_ready_set
        #思考完毕，准备打牌
        #如果P1快赢了并且自己是天灾引者并且能放技能，那就放
        if len(P1.card) <= 3 and self.character == "天灾引者" and self.skill5_counts > 0  and self.skill_times > 0:
            P1.draw_card(self.skill5_counts)
            P1.card.sort(key = lambda x:x.card_type)
            for index in range(len(P1.card)):
                if len(P1.card) <= 10:
                    P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
                else:
                    P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
            self.skill5_counts = 0
            self.skill_times = 0
            Game.skill_display = True
        #如果没有牌（准备放弃了）
        if not self.card_ready:
            #天灾引者放弃回合可以+1标记
            if self.character == "天灾引者" and self.skill_times > 0:
                self.skill5_counts = self.skill5_counts + 1
                self.draw_card(1)
                Game.round_skipped += 1
                Game.round_skipped_display = True
            #永恒铸造师压不上永恒，可以不摸牌
            elif self.character == "永恒铸造师" and 6 in type_displayed:
                Game.skill_display = True
                Game.round_skipped += 1
                Game.round_skipped_display = True
            #星轨分离者在额外回合内，可以取消额外回合，并且不用摸牌
            elif self.character == "星轨分离者" and self.skill_activated == True:
                self.skill_activated = False
            else:
                self.draw_card(1)
                Game.round_skipped += 1
                Game.round_skipped_display = True
        #如果处在额外回合，先展示机器人使用了技能，然后等1.5s再出牌
        if self.card_ready and self.character == "星轨分离者" and self.skill_activated == True and not self.already_displayed:
            Game.skill_display = True
            clock.schedule_unique(self.ready_auto_play,1.5)
            self.already_displayed = True
            self.card_ready.clear()
            return
        #如果有虚空
        elif play_void:
            self.void_pool = list(set(EveryCard.card_type for EveryCard in Game.card_played))
            #尽可能要点数最大的
            if self.void_pool.count(6) > 0:
                self.last_void_choice = "永恒"
                for i in range(len(Game.card_played)):
                    if Game.card_played[i].card_type == 6:
                        self.card.append(Game.card_played.pop(i))
                        break
            elif self.void_pool.count(4) + self.void_pool.count(5) > 0:
                self.void_card_pool = [EveryCard for EveryCard in Game.card_played if EveryCard.card_type == 4 or EveryCard.card_type == 5]
                card_choosed = random.choice(self.void_card_pool)
                if card_choosed.card_type == 4:
                    self.last_void_choice = "光"
                if card_choosed.card_type == 5:
                    self.last_void_choice = "暗"
                self.card.append(card_choosed)
                Game.card_played.remove(card_choosed)
            elif self.void_pool.count(1) + self.void_pool.count(2) + self.void_pool.count(3) > 0:
                self.void_card_pool = [EveryCard for EveryCard in Game.card_played if EveryCard.card_type == 1 or EveryCard.card_type == 2 or EveryCard.card_type == 3]
                card_choosed = random.choice(self.void_card_pool)
                if card_choosed.card_type == 1:
                    self.last_void_choice = "火"
                if card_choosed.card_type == 2:
                    self.last_void_choice = "木"
                if card_choosed.card_type == 3:
                    self.last_void_choice = "水"
                self.card.append(card_choosed)
                Game.card_played.remove(card_choosed)
            else:
                random_index = random.randint(0,len(Game.card_played)-1)
                card_choosed = Game.card_played[random_index]
                if card_choosed.card_type == 0:
                    self.last_void_choice = "风"
                if card_choosed.card_type == 7:
                    self.last_void_choice = "虚空"
                self.card.append(Game.card_played.pop(random_index))
            Game.void_choice_display = True   
            self.void_pool.clear()
            self.void_card_pool.clear()
        temp_num = self.card_ready.draw_num()
        if self.card_ready:
            #永恒铸造师用风强化永恒可以不摸牌
            if self.character == "永恒铸造师" and 0 in type_ready and 6 in type_ready:
                temp_num = 0
                Game.skill_display = True
            Game.round_skipped = 0
            Game.card_displayed.clear()
            Game.card_displayed.owner = "Bot"
        #打出选中的牌，并添加到展示牌和弃牌堆中（虚空领主发动技能需要单独考虑）
        if self.character == "虚空领主" and self.skill_activated:
            self.skill_activated = False
            Game.card_displayed.append(TempVoidCard)
            Game.card_played.append(self.card_ready[0])
            self.card.remove(self.card_ready.pop(0))
        else:
            for i in range(len(self.card_ready)):    
                Game.card_displayed.append(self.card_ready[0])
                Game.card_played.append(self.card_ready[0])
                self.card.remove(self.card_ready.pop(0))
        self.draw_card(temp_num)
        #影锋技能发动，尽可能弃置点数小的牌
        if self.character == "影锋" and ((4 in type_ready and 5 in type_displayed) or (5 in type_ready and 4 in type_displayed)):
            max_number = type_ready.count(4) + type_ready.count(5)
            self.card.sort(key = lambda x:x.card_type)
            if len(self.card) > 0:
                Game.skill_display = True
            for i in range(min(max_number,len(self.card))):
                Game.card_played.append(self.card.pop(0))
        #按钮初始化
        GiveUp.image = "giveup"
        if P1.character_number in [1,3,5] and P1.skill_times > 0:
            P1Skill.image = f"skill{P1.character_number}"
        if len(self.card) == 0:
            clock.schedule_unique(Game.lose,1.5)
        else:
            #如果满足星轨分离者的发动条件（而且还没有发动过），那么准备发动
            if self.character == "星轨分离者" and self.skill_activated == False and ((type_ready_set == set([0]) and type_displayed_set == set([0])) or (len(i_set) > 0 and i_set != set([0]))):
                self.skill_activated = True
                Game.whose_round = "Bot"
                clock.schedule(self.ready_auto_play,0.01)
            else:
                Game.whose_round = "P1"
        #如果发动过了，那么就清除痕迹
        if self.character == "星轨分离者" and self.skill_activated == True and self.already_displayed:
            self.skill_activated = False
        self.already_displayed = False
    def ready_auto_play(self):
        if Game.status == "Game":
            if not Game.pause:
                Bot.auto_play()
            else:
                clock.schedule(self.ready_auto_play,1.5)
    def switch_to_skill7(self):
        Game.pause = "Skill7"
######################################################################################################################################
#创建玩家角色和机器人角色及其技能按钮（暂时没有）
P1 = Player()
Bot = Player()
P1Skill = Actor("skill0")
BotSkill = Actor("skill0")
#游戏初始化        
Game.initialize()

#标题页面的4个按钮
StartGameButton = Actor("startgamebuttonuntouched")
HelpButton = Actor("helpbuttonuntouched")
AboutButton = Actor("aboutbuttonuntouched")
ExitButton = Actor("exitbuttonuntouched")

#返回标题界面的按钮
BackToTitle = Actor("backtotitleuntouched")

#上一页和下一页的按钮
PageUp = Actor("pageupuntouched")
PageDown = Actor("pagedownuntouched")

#出牌和放弃的按钮
Play = Actor("playdisabled")
GiveUp = Actor("giveup")

#暂停界面的返回标题界面和退出游戏的按钮
PauseBackToTitle = Actor("pausebacktotitleuntouched")
PauseExit = Actor("pauseexituntouched")

#是和否的按钮
Yes = Actor("yes")
No = Actor("no")

#影锋的弃牌按钮
DiscardButton = Actor("discard")
def on_mouse_move(pos):
    #鼠标悬浮时，外观变化
    if Game.status == "MainTitle":
        if StartGameButton.collidepoint(pos):
            StartGameButton.image = "startgamebuttontouched"
        else:
            StartGameButton.image = "startgamebuttonuntouched"
        if HelpButton.collidepoint(pos):
            HelpButton.image = "helpbuttontouched"
        else:
            HelpButton.image = "helpbuttonuntouched"
        if AboutButton.collidepoint(pos):
            AboutButton.image = "aboutbuttontouched"
        else:
            AboutButton.image = "aboutbuttonuntouched"
        if ExitButton.collidepoint(pos):
            ExitButton.image = "exitbuttontouched"
        else:
            ExitButton.image = "exitbuttonuntouched"
    if Game.status in ["About","Help","Win","Lose"]:
        if BackToTitle.collidepoint(pos):
            BackToTitle.image = "backtotitletouched"
        else:
            BackToTitle.image = "backtotitleuntouched"
    if Game.status == "Help":
        if PageUp.collidepoint(pos):
            PageUp.image = "pageuptouched"
        else:
            PageUp.image = "pageupuntouched"
        if PageDown.collidepoint(pos):
            PageDown.image = "pagedowntouched"
        else:
            PageDown.image = "pagedownuntouched"
    if Game.status == "CharacterChoose":
        for index in range(10):
            if Game.character_list[index].collidepoint(pos):
                Game.character_list[index].image = f"character{index}touched"
            else:
                Game.character_list[index].image = f"character{index}"
    if Game.status == "Game" and not Game.pause and Game.whose_round == "P1":
        #我方卡牌的展示
        for index in range(len(P1.card)):
            if len(P1.card) <= 10:
                if pos[0] - 50 <= (640 + 120*(index - (len(P1.card)-1)/2)) <= pos[0] + 50 and 535 <= pos[1] <= 700:
                    P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),685)
                else:
                    P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
            else:
                if index < len(P1.card) - 1:
                    if 100 + (1180 - 100) * index/(len(P1.card) - 1) - 50 <= pos[0] < 100 + (1180 - 100) * (index + 1)/(len(P1.card) - 1) - 50 and 535 <= pos[1] <= 700:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),685)
                    else:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
                else:
                    if 1130 <= pos[0] <= 1230 and 535 <= pos[1] <= 700:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),685)
                    else:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
        #鼠标悬浮于出牌按钮
        if (P1.card_ready.obey_rule() and P1.card_ready > Game.card_displayed and Game.whose_round == "P1") :
            if Play.collidepoint(pos):
                Play.image = "playtouched"
            else:
                Play.image = "play"
        if Game.whose_round == "P1":
            if GiveUp.collidepoint(pos):
                GiveUp.image = "giveuptouched"
            else:
                GiveUp.image = "giveup"
    #虚空选牌时的卡牌外观显示
    if Game.status == "Game" and Game.pause == "Void":
        for index in range(len(P1.void_pool)):
            if P1.void_card_pool[index].collidepoint(pos):
                P1.void_card_pool[index].image = f"voidcard{P1.void_card_pool[index].card_type}touched"
            else:
                P1.void_card_pool[index].image = f"voidcard{P1.void_card_pool[index].card_type}"
    #玩家暂停时的回到标题和退出游戏按钮外观
    if Game.status == "Game" and Game.pause == "Player":
        if PauseBackToTitle.collidepoint(pos):
            PauseBackToTitle.image = "pausebacktotitletouched"
        else:
            PauseBackToTitle.image = "pausebacktotitleuntouched"
        if PauseExit.collidepoint(pos):
            PauseExit.image = "pauseexittouched"
        else:
            PauseExit.image = "pauseexituntouched"
    #隐匿猎手选牌
    if Game.status == "Game" and Game.pause == "Skill2":
        for index in range(11):
            if Game.number_list[index].collidepoint(pos):
                Game.number_list[index].image = f"{index+10}touched"
            else:
                Game.number_list[index].image = f"{index+10}"
    #影锋的弃牌按钮
    if Game.status == "Game" and Game.pause == "Skill4":
        if len(P1.card_ready) <= P1.skill4_max_number:
            if DiscardButton.collidepoint(pos):
                DiscardButton.image = "discardtouched"
            else:
                DiscardButton.image = "discard"
    #影锋的弃置的卡牌的外观
    if Game.status == "Game" and Game.pause == "Skill4" and Game.whose_round == "P1":
        #我方卡牌的展示
        for index in range(len(P1.card)):
            if len(P1.card) <= 10:
                if pos[0] - 50 <= (640 + 120*(index - (len(P1.card)-1)/2)) <= pos[0] + 50 and 535 <= pos[1] <= 700:
                    P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),685)
                else:
                    P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
            else:
                if index < len(P1.card) - 1:
                    if 100 + (1180 - 100) * index/(len(P1.card) - 1) - 50 <= pos[0] < 100 + (1180 - 100) * (index + 1)/(len(P1.card) - 1) - 50 and 535 <= pos[1] <= 700:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),685)
                    else:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
                else:
                    if 1130 <= pos[0] <= 1230 and 535 <= pos[1] <= 700:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),685)
                    else:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
    #永恒铸造师和星轨分离者的是与否按钮
    if Game.status == "Game" and Game.pause in ["Skill6Play","Skill6GiveUp","Skill7"]:
        if Yes.collidepoint(pos):
            Yes.image = "yestouched"
        else:
            Yes.image = "yes"
        if No.collidepoint(pos):
            No.image = "notouched"
        else:
            No.image = "no"
    if Game.status == "Game" and not Game.pause:
        if P1.character_number in [1,3,5] and (Game.whose_round == "P1" and P1.skill_times > 0):
            if P1Skill.collidepoint(pos):
                P1Skill.image = f"skill{P1.character_number}touched"
            else:
                if P1.skill_activated == True:
                    P1Skill.image = f"skill{P1.character_number}activated"
                else:
                    P1Skill.image = f"skill{P1.character_number}"
def on_mouse_down(pos):    
    if Game.status == "MainTitle":  
        if StartGameButton.collidepoint(pos):
            #进入主游戏
            Game.status = "Blank"
            P1.character_number = 0
            P1.skill_times = 0
            P1.skill_activated = False
            P1.skill4_max_number = 0
            P1.skill5_counts = 0
            P1.skill6_draw_num = 0
            P1.skill7_ready = False
            P1.already_displayed = False
            Bot.character_number = 0
            Bot.skill_times = 0
            Bot.skill_activated = False
            Bot.skill4_max_number = 0
            Bot.skill5_counts = 0
            Bot.skill6_draw_num = 0
            Bot.skill7_ready = False
            Bot.already_displayed = False
            clock.schedule_unique(Game.start_choose,0.5)
        if HelpButton.collidepoint(pos):
            #进入帮助
            Game.status = "Help"
            #暂时移除开始菜单按钮
            StartGameButton.center = (0,-100)
            HelpButton.center = (0,-100)
            AboutButton.center = (0,-100)
            ExitButton.center = (0,-100)
            BackToTitle.image = "backtotitleuntouched"
            Game.help_page = 1
        if AboutButton.collidepoint(pos):
            #进入关于
            Game.status = "About"
            #暂时移除开始菜单按钮
            StartGameButton.center = (0,-100)
            HelpButton.center = (0,-100)
            AboutButton.center = (0,-100)
            ExitButton.center = (0,-100)
            BackToTitle.image = "backtotitleuntouched"            
        if ExitButton.collidepoint(pos):
            #退出游戏
            exit()
    if Game.status in ["About","Help","Win","Lose"]:
        #返回主界面
        if BackToTitle.collidepoint(pos):
            if Game.status in ["Win","Lose"]:
                music.play("panorama")
            BackToTitle.center = (0,-100)
            PageUp.center = (0,-100)
            PageDown.center = (0,-100)
            Game.help_page = 1
            Game.status = "MainTitle"
            StartGameButton.image = "startgamebuttonuntouched"
            HelpButton.image = "helpbuttonuntouched"
            AboutButton.image = "aboutbuttonuntouched"
            PageUp.image = "pageupuntouched"
            PageDown.image = "pagedownuntouched"
    if Game.status == "Help":
        #帮助界面的翻页
        if PageUp.collidepoint(pos):
            Game.help_page -=1
            PageUp.image = "pageupuntouched"
            PageDown.image = "pagedownuntouched"
        if PageDown.collidepoint(pos):
            Game.help_page +=1
            PageUp.image = "pageupuntouched"
            PageDown.image = "pagedownuntouched"
    #角色选择
    if Game.status == "CharacterChoose":
        for index in range(10):
            if Game.character_list[index].collidepoint(pos):
                if Game.whose_character == "P1":
                    P1.character_number = index
                    if index == 0:
                        P1.character = "大魔法师"
                    if index == 1:
                        P1.character = "未来旅人"
                        P1.skill_times = 3
                    if index == 2:
                        P1.character = "隐匿猎手"
                    if index == 3:
                        P1.character = "虚空领主"
                        P1.skill_times = 1
                    if index == 4:
                        P1.character = "影锋"
                    if index == 5:
                        P1.character = "天灾引者"
                        P1.skill_times = 1
                    if index == 6:
                        P1.character = "永恒铸造师"
                    if index == 7:
                        P1.character = "星轨分离者"
                    if index == 8:
                        random_index = random.randint(0,7)
                        character_name_list = ["大魔法师","未来旅人","隐匿猎手","虚空领主","影锋","天灾引者","永恒铸造师","星轨分离者"]
                        P1.character = character_name_list[random_index]
                        P1.character_number = random_index
                        if random_index == 1:
                            P1.skill_times = 3
                        if random_index in [3,5]:
                            P1.skill_times = 1
                    if index == 9:
                        P1.character = "平凡的勇者"
                    P1Skill.image = f"skill{P1.character_number}"
                    Game.whose_character = "Bot"
                else:
                    Bot.character_number = index
                    if index == 0:
                        Bot.character = "大魔法师"
                    if index == 1:
                        Bot.character = "未来旅人"
                        Bot.skill_times = 3
                    if index == 2:
                        Bot.character = "隐匿猎手"
                    if index == 3:
                        Bot.character = "虚空领主"
                        Bot.skill_times = 1
                    if index == 4:
                        Bot.character = "影锋"
                    if index == 5:
                        Bot.character = "天灾引者"
                        Bot.skill_times = 1
                    if index == 6:
                        Bot.character = "永恒铸造师"
                    if index == 7:
                        Bot.character = "星轨分离者"
                    if index == 8:
                        random_index = random.randint(0,7)
                        character_name_list = ["大魔法师","未来旅人","隐匿猎手","虚空领主","影锋","天灾引者","永恒铸造师","星轨分离者"]
                        Bot.character = character_name_list[random_index]
                        Bot.character_number = random_index
                        if random_index == 1:
                            Bot.skill_times = 3
                        if random_index in [3,5]:
                            Bot.skill_times = 1
                    if index == 9:
                        Bot.character = "平凡的勇者"
                    BotSkill.image = f"skill{Bot.character_number}"
                    Game.whose_character = "P1"
                    #进入主游戏
                    Game.status = "Blank"
                    clock.schedule_unique(Game.start_game,0.5)
    #如果正在游戏中，是己方回合，并且没有暂停
    if Game.status == "Game" and not Game.pause and Game.whose_round == "P1":
        #准备打出卡牌
        for index in range(len(P1.card)):
            #如果手中的牌少于10张，则不会重叠显示
            if len(P1.card) <= 10:
                #如果点击牌
                if pos[0] - 50 <= (640 + 120*(index - (len(P1.card)-1)/2)) <= pos[0] + 50 and 535 <= pos[1] <= 700:
                    #在准备列表中则删除，并更新出牌按钮状态
                    if P1.card[index] in P1.card_ready:
                        P1.card_ready.remove(P1.card[index])
                        P1.card[index].image = f"card{P1.card[index].card_type}"
                        if (P1.card_ready.obey_rule() and P1.card_ready > Game.card_displayed):
                            Play.image = "play"
                    #不在准备列表中则添加，并更新出牌按钮状态
                    else:
                        P1.card_ready.append(P1.card[index])
                        P1.card[index].image = f"card{P1.card[index].card_type}selected"
                        if (P1.card_ready.obey_rule() and P1.card_ready > Game.card_displayed):
                            Play.image = "play"
            #如果手中的牌多于十张，则会重叠显示
            else:
                #不是最右侧的牌，判定区域只有露出来的部分
                if index < len(P1.card) - 1:
                    #露出来的部分
                    if 100 + (1180 - 100) * index/(len(P1.card) - 1) - 50 <= pos[0] < 100 + (1180 - 100) * (index + 1)/(len(P1.card) - 1) - 50 and 535 <= pos[1] <= 700:
                        #同上，在则删除，不在添加
                        if P1.card[index] in P1.card_ready:
                            P1.card_ready.remove(P1.card[index])
                            P1.card[index].image = f"card{P1.card[index].card_type}"
                            if (P1.card_ready.obey_rule() and P1.card_ready > Game.card_displayed):
                                Play.image = "play"
                        else:
                            P1.card_ready.append(P1.card[index])
                            P1.card[index].image = f"card{P1.card[index].card_type}selected"
                            if (P1.card_ready.obey_rule() and P1.card_ready > Game.card_displayed):
                                Play.image = "play"
                #是最右侧的牌，则判定区域为全部
                else:
                    #整张牌都是判定区域
                    if 1130 <= pos[0] <= 1230 and 535 <= pos[1] <= 700:
                        if P1.card[index] in P1.card_ready:
                            P1.card_ready.remove(P1.card[index])
                            P1.card[index].image = f"card{P1.card[index].card_type}"
                            if (P1.card_ready.obey_rule() and P1.card_ready > Game.card_displayed):
                                Play.image = "play"
                        else:
                            P1.card_ready.append(P1.card[index])
                            P1.card[index].image = f"card{P1.card[index].card_type}selected"
                            if (P1.card_ready.obey_rule() and P1.card_ready > Game.card_displayed):
                                Play.image = "play"
        #打牌，换边操作
        if Play.collidepoint(pos):
            if (P1.card_ready.obey_rule() and P1.card_ready > Game.card_displayed):
                P1.play()
        #放弃，换边操作
        if GiveUp.collidepoint(pos):
            #技能不释放，不计入次数
            P1.skill_activated = False
            P1.card_ready.clear()
            #如果是天灾引者并且技能还没有发动，标记+1
            if P1.character == "天灾引者" and P1.skill_times > 0:
                P1.skill5_counts = P1.skill5_counts + 1
            #如果是永恒铸造师且满足技能触发条件，询问是否取消摸牌
            type_display = [EveryCard.card_type for EveryCard in Game.card_displayed]
            if P1.character == "永恒铸造师" and 6 in type_display:
                Game.pause = "Skill6GiveUp"
            #如果不是，抽一张牌，跳过回合+1，整理一下牌
            else:
                P1.draw_card(1)
                P1.card.sort(key = lambda x:x.card_type)
                for index in range(len(P1.card)):
                    if len(P1.card) <= 10:
                        P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
                        P1.card[index].image = f"card{P1.card[index]}"
                    else:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
                        P1.card[index].image = f"card{P1.card[index]}"
                Game.round_skipped = Game.round_skipped + 1
                clock.schedule_unique(Bot.ready_auto_play,1.5)
                Game.whose_round = "Bot"
    #虚空换牌
    if Game.status == "Game" and Game.pause == "Void":
        for index in range(len(P1.void_pool)):
            #如果点击的是第index张卡
            if P1.void_card_pool[index].collidepoint(pos):
                #寻找弃牌堆中的类型为P1.void_pool[index]的卡，将其加入手牌，然后清空暂时的虚空池
                for i in range(len(Game.card_played)):
                    if Game.card_played[i].card_type == P1.void_pool[index]:
                        P1.card.append(Game.card_played.pop(i))
                        for j in range(len(P1.void_pool)):
                            P1.void_card_pool[j].center = (0,-100)
                        P1.void_pool.clear()
                        P1.void_card_pool.clear()
                        P1.card.sort(key = lambda x:x.card_type)
                        break
                #如果星轨分离者发动技能，则进入询问，否则准备打牌
                if P1.skill7_ready:
                    P1.skill7_ready = False
                    clock.schedule(P1.switch_to_skill7,0.25)
                else:
                    clock.schedule_unique(Bot.ready_auto_play,1.5)
                    Game.pause = None
                P1.card.sort(key = lambda x:x.card_type)
                for i in range(len(P1.card)):
                    if len(P1.card) <= 10:
                        P1.card[i].midbottom = (640 + 120*(i - (len(P1.card)-1)/2),700)
                    else:
                        P1.card[i].midbottom = (100 + (1180 - 100) * i/(len(P1.card) - 1),700)
                break
    #玩家暂停
    if Game.status == "Game" and Game.pause == "Player":
        if PauseBackToTitle.collidepoint(pos):
            music.play("panorama")
            Game.status = "MainTitle"
            Game.pause = None
            StartGameButton.image = "startgamebuttonuntouched"
            HelpButton.image = "helpbuttonuntouched"
            AboutButton.image = "aboutbuttonuntouched"
            PageUp.image = "pageupuntouched"
            PageDown.image = "pagedownuntouched"
        if PauseExit.collidepoint(pos):
            exit()
    #隐匿猎手选择抽牌数目
    if Game.status == "Game" and Game.pause == "Skill2":
        for i in range(11):
            if Game.number_list[i].collidepoint(pos):
                Game.pause = None
                P1.draw_card(i + 10)
                P1.card.sort(key = lambda x:x.card_type)
                for index in range(len(P1.card)):
                    if len(P1.card) <= 10:
                        P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
                    else:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
                if Game.whose_round == "Bot":
                    clock.schedule_unique(Bot.ready_auto_play,1.5)
                for index in range(11):
                    Game.number_list[index].image = f"{index + 10}"
                break
    #影锋弃牌按钮
    if Game.status == "Game" and Game.pause == "Skill4" and Game.whose_round == "P1":
        if len(P1.card_ready) <= P1.skill4_max_number:
            if DiscardButton.collidepoint(pos):
                for _ in range(len(P1.card_ready)):
                    Game.card_played.append(P1.card_ready[0])
                    P1.card.remove(P1.card_ready[0])
                    P1.card_ready.pop(0)
                P1.skill4_max_number = 0
                Game.pause = None
                Game.whose_round = "Bot"
                DiscardButton.image = "discard"
                P1.card.sort(key = lambda x:x.card_type)
                for index in range(len(P1.card)):
                    if len(P1.card) <= 10:
                        P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
                    else:
                        P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
                if len(P1.card) == 0:
                    clock.schedule_unique(Game.win,1.5)
                else:
                    clock.schedule_unique(Bot.ready_auto_play,1.5)
    #影锋弃牌的卡牌选择弃置
    if Game.status == "Game" and Game.pause == "Skill4" and Game.whose_round == "P1":
        for index in range(len(P1.card)):
            #如果手中的牌少于10张，则不会重叠显示
            if len(P1.card) <= 10:
                #如果点击牌
                if pos[0] - 50 <= (640 + 120*(index - (len(P1.card)-1)/2)) <= pos[0] + 50 and 535 <= pos[1] <= 700:
                    #在准备列表中则删除，并更新弃牌按钮状态
                    if P1.card[index] in P1.card_ready:
                        P1.card_ready.remove(P1.card[index])
                        P1.card[index].image = f"card{P1.card[index].card_type}"
                        if len(P1.card_ready) <= P1.skill4_max_number:
                            DiscardButton.image = "discard"
                    #不在准备列表中则添加
                    else:
                        P1.card_ready.append(P1.card[index])
                        P1.card[index].image = f"card{P1.card[index].card_type}selected"
            #如果手中的牌多于十张，则会重叠显示
            else:
                #不是最右侧的牌，判定区域只有露出来的部分
                if index < len(P1.card) - 1:
                    #露出来的部分
                    if 100 + (1180 - 100) * index/(len(P1.card) - 1) - 50 <= pos[0] < 100 + (1180 - 100) * (index + 1)/(len(P1.card) - 1) - 50 and 535 <= pos[1] <= 700:
                        #同上，在则删除，不在添加
                        if P1.card[index] in P1.card_ready:
                            P1.card_ready.remove(P1.card[index])
                            P1.card[index].image = f"card{P1.card[index].card_type}"
                            if len(P1.card_ready) <= P1.skill4_max_number:
                                DiscardButton.image = "discard"
                        else:
                            P1.card_ready.append(P1.card[index])
                            P1.card[index].image = f"card{P1.card[index].card_type}selected"
                #是最右侧的牌，则判定区域为全部
                else:
                    #整张牌都是判定区域
                    if 1130 <= pos[0] <= 1230 and 535 <= pos[1] <= 700:
                        if P1.card[index] in P1.card_ready:
                            P1.card_ready.remove(P1.card[index])
                            P1.card[index].image = f"card{P1.card[index].card_type}"
                            if len(P1.card_ready) <= P1.skill4_max_number:
                                DiscardButton.image = "discard"
                        else:
                            P1.card_ready.append(P1.card[index])
                            P1.card[index].image = f"card{P1.card[index].card_type}selected"
    #永恒铸造师选择是否取消摸牌，又分打牌和放弃两种情况
    if Game.status == "Game" and Game.pause == "Skill6Play":
        if Yes.collidepoint(pos):
            P1.skill6_draw_num = 0
            for index in range(len(P1.card)):
                if len(P1.card) <= 10:
                    P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
                else:
                    P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
            Game.whose_round = "Bot"
            Game.pause = None
            #如果打完不会赢，那么1.5秒后机器人出牌
            if len(P1.card) > 0:
                clock.schedule_unique(Bot.ready_auto_play,1.5)
            if len(P1.card) == 0 and not Game.pause:           
                clock.schedule_unique(Game.win,1.5)
        if No.collidepoint(pos):
            P1.draw_card(P1.skill6_draw_num)
            P1.skill6_draw_num = 0
            P1.card.sort(key = lambda x:x.card_type)
            for index in range(len(P1.card)):
                if len(P1.card) <= 10:
                    P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
                else:
                    P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
            Game.whose_round = "Bot"
            Game.pause = None       
            clock.schedule_unique(Bot.ready_auto_play,1.5)
    if Game.status == "Game" and Game.pause == "Skill6GiveUp":
        if Yes.collidepoint(pos):
            Game.pause = None
            for index in range(len(P1.card)):
                if len(P1.card) <= 10:
                    P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
                else:
                    P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
            Game.round_skipped = Game.round_skipped + 1
            Game.whose_round = "Bot"
            clock.schedule_unique(Bot.ready_auto_play,1.5)
        if No.collidepoint(pos):
            P1.draw_card(1)
            Game.pause = None
            
            for index in range(len(P1.card)):
                if len(P1.card) <= 10:
                    P1.card[index].midbottom = (640 + 120*(index - (len(P1.card)-1)/2),700)
                else:
                    P1.card[index].midbottom = (100 + (1180 - 100) * index/(len(P1.card) - 1),700)
            Game.round_skipped = Game.round_skipped + 1
            clock.schedule_unique(Bot.ready_auto_play,1.5)
            Game.whose_round = "Bot"
    #星轨分离者的技能释放
    if Game.status == "Game" and Game.pause == "Skill7":
        if Yes.collidepoint(pos):
            Game.pause = None
            P1.skill_activated = True
            Game.whose_round = "P1"
        if No.collidepoint(pos):
            Game.pause = None
            clock.schedule_unique(Bot.ready_auto_play,1.5)
            Game.whose_round = "Bot"
    #未来旅人和虚空领主的技能释放
    if Game.status == "Game" and not Game.pause:
        if P1.character_number in [1,3] and Game.whose_round == "P1" and P1.skill_times > 0:
            if P1Skill.collidepoint(pos):
                if P1.skill_activated == False:
                    P1.skill_activated = True
                    P1Skill.image = f"skill{P1.character_number}activated"
                else:
                    P1.skill_activated = False
                    P1Skill.image = f"skill{P1.character_number}"
    #天灾引者的技能释放
    if Game.status == "Game" and not Game.pause:
        if P1.character_number == 5 and Game.whose_round == "P1" and P1.skill_times > 0 and P1.skill5_counts > 0:
            if P1Skill.collidepoint(pos):
                P1.skill_times = 0
                Bot.draw_card(P1.skill5_counts)
                P1.skill5_counts = 0
def on_key_down(key):
    if key == key.ESCAPE:
        if Game.pause == None and len(P1.card) > 0 and len(Bot.card) > 0:
            Game.pause = "Player"
            PauseBackToTitle.image = "pausebacktotitleuntouched"
            PauseExit.image = "pauseexituntouched"
        elif Game.pause == "Player":
            Game.pause = None
def draw():
    #初始化页面，清空并填充白色
    screen.clear()
    screen.fill((255,255,255))
    #主界面背景
    if Game.status == "MainTitle":
        screen.blit("title",(0,0))
    #关于背景
    if Game.status == "About":
        screen.blit("about",(0,0))
    #帮助背景
    if Game.status == "Help":
        screen.blit(f"help{Game.help_page}",(0,0))
    #赢输背景
    if Game.status == "Win":
        screen.blit("win",(0,0))
    if Game.status == "Lose":
        screen.blit("lose",(0,0))
    #主界面按钮
    if Game.status == "MainTitle":
        StartGameButton.draw()
        HelpButton.draw()
        AboutButton.draw()
        ExitButton.draw()
    #关于界面按钮
    if Game.status in ["About","Win","Lose"]:
        BackToTitle.draw()
    #帮助界面按钮
    if Game.status == "Help":
        BackToTitle.draw()
        PageUp.draw()
        PageDown.draw()
    #选择角色
    if Game.status == "CharacterChoose":
        if Game.whose_character == "P1":
            screen.blit("p1choose",(0,0))
        if Game.whose_character == "Bot":
            screen.blit("botchoose",(0,0))
        for index in range(10):
            Game.character_list[index].draw()
    #在主游戏中
    if Game.status == "Game":
        #我方和对手的卡牌展示
        for EveryCard in P1.card:
            EveryCard.draw()
        for EveryCard in Bot.card:
            EveryCard.draw()
        #出牌和放弃按钮展示
        Play.draw()
        GiveUp.draw()
        #角色名与技能相关信息的展示
        screen.draw.text(P1.character,(20,730),color = "black",fontname = "simhei.ttf",fontsize = 50)
        screen.draw.text(Bot.character,(20,25),color = "black",fontname = "simhei.ttf",fontsize = 50)
        if P1.character_number == 1:
            screen.draw.text(f"次数：{P1.skill_times}",(500,733),color = "black",fontname = "simhei.ttf",fontsize = 40)
        elif P1.character_number == 5:
            if P1.skill_times > 0:
                screen.draw.text(f"标记：{P1.skill5_counts}",(500,733),color = "black",fontname = "simhei.ttf",fontsize = 40)
            else:
                screen.draw.text("已经释放",(500,733),color = "black",fontname = "simhei.ttf",fontsize = 40)
        if Bot.character_number == 1:
            screen.draw.text(f"次数：{Bot.skill_times}",(500,27),color = "black",fontname = "simhei.ttf",fontsize = 40)
        elif Bot.character_number == 5:
            if Bot.skill_times > 0:
                screen.draw.text(f"标记：{Bot.skill5_counts}",(500,27),color = "black",fontname = "simhei.ttf",fontsize = 40)
            else:
                screen.draw.text("已经释放",(500,27),color = "black",fontname = "simhei.ttf",fontsize = 40)
        #点数提示（如果影锋正在发动技能，那么不统计己方点数）
        if Game.pause != "Skill4":
            screen.draw.text(f"您的点数：{P1.card_ready.points()}",(770,715),color = "black",fontname = "simhei.ttf",fontsize = 30)
        screen.draw.text(f"场上点数：{Game.card_displayed.points()}",(770,755),color = "black",fontname = "simhei.ttf",fontsize = 30)
        P1Skill.draw()
        BotSkill.draw()
        #如果处在虚空暂停，绘制虚空选牌
        if Game.pause == "Void":
            for EveryCard in P1.void_card_pool:
                EveryCard.draw()
        #否则，只要不是正在发动技能，就展示上一轮打出的牌
        if Game.pause == "Player" or Game.pause == None:
            for EveryCard in Game.card_displayed:
                EveryCard.draw()
        #隐匿猎手选择初始牌数的展示
        if Game.pause == "Skill2":
            for i in range(11):
                Game.number_list[i].draw()
            screen.draw.text("初始牌数？",(500,300),color = "black",fontname = "simhei.ttf",fontsize = 60)
        #影锋弃牌按钮的展示
        if Game.pause == "Skill4":
            DiscardButton.draw()
        #永恒铸造师取消摸牌的展示
        if Game.pause == "Skill6Play" or Game.pause == "Skill6GiveUp":
            screen.draw.text("取消摸牌？",(500,300),color = "black",fontname = "simhei.ttf",fontsize = 60)
        #星轨分离者额外回合的展示
        if Game.pause == "Skill7":
            screen.draw.text("额外回合？",(500,300),color = "black",fontname = "simhei.ttf",fontsize = 60)
        #是和否按钮的展示
        if Game.pause in ["Skill6Play","Skill6GiveUp","Skill7"]:
            Yes.draw()
            No.draw()
        #对方操作的文字提示
        if Game.round_skipped_display:
            screen.draw.text("对方放弃出牌",(326,270),color = "black",fontname = "simhei.ttf",fontsize = 40)
        if Game.void_choice_display:
            screen.draw.text("对方选择了：" + Bot.last_void_choice,(308,270),color = "black",fontname = "simhei.ttf",fontsize = 40)
        if Game.skill_display:
            screen.draw.text("对方使用技能",(710,270),color = "black",fontname = "simhei.ttf",fontsize = 40)
        #暂停背景，弃牌堆中卡牌种类的提示
        if Game.pause == "Player":
            screen.blit("pause",(140,100))
            type_list = [EveryCard.card_type for EveryCard in Game.card_played]
            card_played_name = ''
            if 0 in type_list:
                card_played_name = card_played_name + "风 "
            if 1 in type_list:
                card_played_name = card_played_name + "火 "
            if 2 in type_list:
                card_played_name = card_played_name + "木 "
            if 3 in type_list:
                card_played_name = card_played_name + "水 "
            if 4 in type_list:
                card_played_name = card_played_name + "光 "
            if 5 in type_list:
                card_played_name = card_played_name + "暗 "
            if 6 in type_list:
                card_played_name = card_played_name + "永恒 "
            if 7 in type_list:
                card_played_name = card_played_name + "虚空 "
            screen.draw.text(card_played_name,(370,302),color = "black",fontname = "simhei.ttf",fontsize = 44)
            PauseBackToTitle.draw()
            PauseExit.draw()
def update():
    if Game.status == "MainTitle":
        StartGameButton.center = (640,500)
        HelpButton.center = (640,580)
        AboutButton.center = (640,660)
        ExitButton.center = (640,740)
    if Game.status in ["About","Help","Win","Lose"]:
        BackToTitle.center = (1200,750)
    if Game.status == "Help":
        if Game.help_page != 1:
            PageUp.center = (150,750)
        else:
            PageUp.center = (0,-100)
        if Game.help_page != 4:
            PageDown.center = (950,750)
        else:
            PageDown.center = (0,-100)
    if Game.status == "CharacterChoose":
        for index in range(10):
            if 0 <= index <= 4:
                Game.character_list[index].center = (640 + 246*(index - 2),300)
            else:
                Game.character_list[index].center = (640 + 246*(index - 7),625)
    if Game.status == "Game":
        #对方的卡牌位置标定
        for index in range(len(Bot.card)):
            Bot.card[index].image = "cardunknown"
            if len(Bot.card) <= 10:
                Bot.card[index].midtop = (640 + 120*(index - (len(Bot.card)-1)/2),100)
            else:
                Bot.card[index].midtop = (100 + (1180 - 100) * index/(len(Bot.card) - 1),100)
        #已经打出的牌，外观应当改为未选中状态
        for EveryCard in Game.card_played:
            EveryCard.image = f"card{EveryCard.card_type}"
        #已经打出的牌位置标定
        Game.display()
        #出牌按钮位置标定
        Play.center = (1100,750)
        #放弃按钮位置标定
        GiveUp.center = (1210,750)
        #技能按钮位置标定
        P1Skill.center = (400,755)
        BotSkill.center = (400,50)
        if not Game.pause:      
            #两轮过后，清空桌面                
            if Game.round_skipped >= 2:
                Game.card_displayed.clear()
                Game.round_skipped = 0
                Game.card_displayed.owner = ""
        if not (P1.card_ready.obey_rule() and P1.card_ready > Game.card_displayed and Game.whose_round == "P1"):
            Play.image = "playdisabled"
        #如果不是己方回合，放弃按钮显示为灰色
        if Game.whose_round == "Bot":
            GiveUp.image = "giveupdisabled"
        #如果不是己方回合或技能次数已用完，技能显示为灰色
        if P1.character_number in [1,5] and (Game.whose_round == "Bot" or P1.skill_times == 0):
            P1Skill.image = f"skill{P1.character_number}disabled"
        if P1.character_number == 3 and Game.whose_round == "Bot":
            P1Skill.image = "skill3disabled"
        #玩家暂停按钮位置标定
        if Game.pause == "Player":
            PauseBackToTitle.center = (400,600)
            PauseExit.center = (880,600)
        #隐匿猎手的按钮位置标定
        if Game.pause == "Skill2":
            for i in range(11):
                Game.number_list[i].center = (640 + (i - 5) * 115,450)
        #影锋的弃牌按钮位置标定
        if Game.pause == "Skill4":
            DiscardButton.center = (640,450)
            if len(P1.card_ready) > P1.skill4_max_number:
                DiscardButton.image = "discarddisabled"
        #是否释放技能的按钮位置标定
        if Game.pause in ["Skill6Play","Skill6GiveUp","Skill7"]:
            Yes.center = (500,450)
            No.center = (780,450)
        #提示在1.5秒钟后消失
        if Game.round_skipped_display:
            clock.schedule(Game.cancel_round_skipped_display,1.5)
        if Game.void_choice_display:
            clock.schedule(Game.cancel_void_choice_display,1.5)
        if Game.skill_display:
            clock.schedule(Game.cancel_skill_display,1.5)
pgzrun.go()
#（不会真的有人看到这里吧）
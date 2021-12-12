import subprocess
import sys
import easygui as g
while 1:
    g.msgbox("",'少女祈祷中','继续','waiting.png')
    password1 = g.passwordbox("想必你已经熟悉你的操作了吧，请输入123456表示已经熟悉并且准备和我一起旅行了",'博丽灵梦','')
    if password1!='123456':
        g.msgbox('什么，你不知道怎么操作？','博丽灵梦','我是真的不知道','lingmeng1.png')
        g.msgbox('你也算是蠢的不行了吧！','博丽灵梦','能给我一点动力去看操作吗','lingmeng2.png')
        g.msgbox('(作害羞状）难道你更喜欢这种？','博丽灵梦','我真的是high到不行了')
        subprocess.run([sys.executable,'caozuo.py'])
    g.msgbox("好耶！看来你是一个合格的同伴了",'博丽灵梦','哈哈，不愧是我','lingmeng1.png')
    name = g.enterbox("你叫什么名字（请输入英文，不想透露身份就输入NONE！）:",'博丽灵梦')
    if name=='xzd' or name=='lmh':
        g.msgbox("是的，你是来找茬的",'博丽灵梦','就问你要不要吧','lingmeng3.png')
        g.msgbox("那么你就是华强吧",'博丽灵梦','去你妈的','lingmeng3.png')
        name="华强"
    if name=='cb':
        g.msgbox("您也来众神眷顾的幻想乡吗",'博丽灵梦','这也太牛皮了','lingmeng5.png')
        g.msgbox("那就随我来吧！",'博丽灵梦','好的','lingmeng5.png')
    elif name=='NONE':
        g.msgbox('怎么，不愿向吾辈透露你的身份吗','博丽灵梦','我真不知道这个程序怎么回事','lingmeng4.png')
        g.msgbox('哼哼，那你就是个寄吧！','博丽灵梦','是是是，您说得对','lingmeng4.png')
        name='寄吧'
    g.msgbox("你不知道我是谁？我可是无敌的巫女大人！",'博丽灵梦','你可拉倒吧','lingmeng1.png')
    g.msgbox('接下来请跟着我解决异变吧！','博丽灵梦','我可不想','lingmeng1.png')
    g.msgbox(name+",战斗是不可避免的，请随我一起剿灭前方的污秽！",'博丽灵梦','喂喂喂，怎么自说自话就把我拉上来了','lingmeng1.png')
    g.msgbox('','少女祈祷中','即将战斗','waiting.png')
    g.msgbox('稍等，你先给我算个积分','博丽灵梦','我去！能不能跳过啊')
    g.msgbox('请先看题','来自博丽灵梦的挑战','我算出来了！','jifen.png')
    password2 = g.passwordbox("请输入你的答案",'博丽灵梦')
    if password2!='1':
        g.msgbox('你怎么连这个都不会，实在是太菜了！','博丽灵梦','这个到底怎么算啊','lingmeng4.png')
        subprocess.run([sys.executable, "loser.py"])
        sys.exit(0)
    else:
        g.msgbox('不错，你不愧是燕园之光','博丽灵梦','嘿嘿，过奖了','lingmeng4.png')
        subprocess.run([sys.executable, "games.py"])
        sys.exit(0)
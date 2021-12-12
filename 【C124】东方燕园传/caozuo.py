import pgzrun
import subprocess
import easygui as g
import sys
import os

WIDTH=1280
HEIGHT=854

x=Actor("lingmeng1")

x.instruct=True

def instruct():
    screen.clear()
    screen.fill("black")
    screen.draw.text("  你該如何操作博麗靈夢",(100,50),fontsize=75,fontname="fanti",color="red")
    screen.draw.text('若不能完全顯示請先按esc',(200,140),fontsize=20,fontname='fanti',color='red')
    screen.draw.text("""這是一個彈幕射擊遊戲，就和你小時候玩的雷霆戰機一樣！

首先，博麗靈夢中央有個判定點，敵人的所有彈幕以觸碰到判定點為準
其次，你可以扭來扭曲，但是不要亂扭！""",(20,180),fontsize=40,fontname="fanti",color="white")
    screen.draw.text("""註意：
      移動方式：W——向上；A——向下；A——向左：D——向右
      攻擊方式：Z——攻擊；X——慢速移動（希望有用）
                            
                              """,(20,420),fontsize=35,fontname="fanti",color="yellow")
    screen.draw.text("""我們希望你：
      擊敗boss,抓住boss的缺點懟上去！
      嗝屁了不要緊，還可以再來！
      特殊技能：C——惡靈退散；V——凈化""",(20,560),fontsize=35,fontname="fanti",color="yellow")
    screen.draw.text("請按S表示已經閱讀完畢",(850,650),fontsize=20,fontname="fanti",color="white")
    
def draw():
    if x.instruct:
        instruct()
    x.draw()
    
def on_key_down(key):
    if key==key.S:
        g.msgbox('','少女祈祷中','我也来祈祷','waiting.png')
        subprocess.run([sys.executable, "galgame.py"])
def on_key_off(ley):
    if key==key.S:
        exit()
        
pgzrun.go()


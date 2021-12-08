import subprocess
import sys
import easygui as g
while 1:
    g.msgbox("START")
    password = g.passwordbox("Password(Please use capital letter):")
    if password=="RP6":
        g.msgbox("RETURNING……")
        g.msgbox("Hello,CREATOR,welcome")   
        subprocess.run([sys.executable, "return/return_program.py"])
        sys.exit(0)
    else:
        g.msgbox("PASS")
        name = g.enterbox("User Name:")
        if name=="kasu" or name=='Kasu' or name=='KASU':
            g.msgbox("No,you can't do it.")
            g.msgbox("How about it: AAAAA")
            name="AAAAA"
        elif name=='陈斌':
            g.msgbox("啊，是老师啊")
            g.msgbox("希望计概期末手下留情")
            g.msgbox("也在此祝您玩得开心吧")
        g.msgbox("Hello,"+name+",welcome")   
        subprocess.run([sys.executable, "main_program.py"])
        sys.exit(0)
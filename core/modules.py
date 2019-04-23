from core.colors import *
from time import sleep as ts
import os
import sys
import filecmp
def update():
	print(G+"check new version"+W)
	ts(1)
	os.system("mkdir update_check")
	os.system("cd ../CyberFox/update_check && wget https://raw.githubusercontent.com/DarkGa/CyberFox/master/ver.txt")
	update = filecmp.cmp('../CyberFox/ver.txt', '../CyberFox/update_check/ver.txt')
	os.system("cd ../ && cd CyberFox")
	os.system("rm -rf update_check")
	os.system("clear")
	print(B+"check new version"+W)
	ts(1)
	if update == True:
		os.system("clear")
		print(B+"you use last version"+W)
		ts(1)
	if update == False:
		os.system("clear")
		print(R+"detect new version!"+W)
		ts(1)
		os.system("cp update.py ../")
		os.system("cd ../ && python3 update.py")
		print("run CyberFox!")
def run():
	os.system("mkdir .checker")
	os.system("cd ../CyberFox/.checker && wget https://raw.githubusercontent.com/DarkGa/CyberFox/master/core/vk.py")
	checker = filecmp.cmp('../CyberFox/core/vk.py', '../CyberFox/.checker/vk.py')
	if checker == False:
		print(R+"Detect edit file!!!!!"+W)
		ts(2)
		os.system("cd && cd $HOME/CyberFox/core && rm -rf vk.py && cp $HOME/CyberFox/.checker/vk.py $HOME/CyberFox/core")
		print(G+"Code restored"+W)
		ts(2)
		
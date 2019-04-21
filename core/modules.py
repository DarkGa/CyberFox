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
from core.modules import *
from core.colors import *
from time import sleep as ts
import os
import sys
import filecmp
import subprocess
 
def chek():
	
	try:
		code = subprocess.call("wget")
		os.system("clear")
		a = G+"done"+W
	except:
		a = R+"false"+W
	try:
		code = subprocess.call("pip")
		os.system("clear")
		b = G+"done"+W
	except:
		b = R+"false"+W
	
	c = Y+'''check install wget: '''+a+W+'''
'''+Y+'''check install pip: '''+b+W
	print(c)
	ts(2)
def update():
	print(G+"check new version"+W)
	ts(1)
	os.system("mkdir update_check")
	os.system("cd ../CyberFox/update_check && wget https://raw.githubusercontent.com/DarkGa/CyberFox/master/ver.txt > update.log")
	try:
		update = filecmp.cmp('../CyberFox/ver.txt', '../CyberFox/update_check/ver.txt')
	except:
		pass
	os.system("cd ../ && cd CyberFox")
	os.system("rm -rf update_check")
	os.system("clear")
	print(B+"check new version"+W)
	ts(1)
	try:
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
	except:
		chek()
		print(Y+"and check your connect"+W)
		pass
			
def run():
	os.system("mkdir .checker")
	os.system("cd ../CyberFox/.checker && wget https://raw.githubusercontent.com/DarkGa/CyberFox/master/core/vk.py > update.log")
	checker = filecmp.cmp('../CyberFox/core/vk.py', '../CyberFox/.checker/vk.py')
	if checker == False:
		print(R+"Detect edit file!!!!!"+W)
		ts(2)
		os.system("cd && cd $HOME/CyberFox/core && rm -rf vk.py && cp $HOME/CyberFox/.checker/vk.py $HOME/CyberFox/core")
		print(G+"Code restored"+W)
		ts(2)

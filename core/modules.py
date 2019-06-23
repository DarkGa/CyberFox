from core.modules import *
from core.colors import *
from time import sleep as ts
import os
import sys
import filecmp
import subprocess
import urllib.request as ur
def install():
	os.system("cd ../CyberFox/install && cp cf /data/data/com.termux/files/usr/bin && cd /data/data/com.termux/files/usr/bin && chmod +x cf")
def chek():
	

	try:
		url = "https://www.google.com"
		ur.urlopen(url)
		d = G+"done"+W
	except:
		d = R+"false"+W
	try:
		code = subprocess.call("wget")
		os.system("clear")
		os.system("apt install wget &> install.log")
		a = G+"done"+W
		pass
	except:
		a = R+"install..."+W
		os.system("apt install wget &> install.log")
	try:
		code = subprocess.call("pip")
		os.system("clear")
		b = G+"done"+W
	except:
		b = R+"install..."+W
		os.system("apt install python-pip &> install.log && apt install python &> install.log")
	
	c = Y+'''check install wget: '''+a+W+'''
'''+Y+'''check install pip: '''+b+W+'''
''' +Y+'''check connect: ''' +d+W
	print(c)
	ts(2)
def update():
	os.system("mkdir update_check")
	os.system("cd ../CyberFox/update_check && wget https://raw.githubusercontent.com/DarkGa/CyberFox/master/ver.txt &> update.log")
	try:
		update = filecmp.cmp('../CyberFox/ver.txt', '../CyberFox/update_check/ver.txt')
	except:
		pass
	os.system("cd ../ && cd CyberFox")
	os.system("rm -rf update_check")
	os.system("clear")
	print(Y+"check new version"+W)
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
		quit()
		ts(2)
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

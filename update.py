import os
import time
import requests
import sys
from termcolor import colored, cprint
import filecmp

print(colored("check new version", 'green'))
time.sleep(5)
os.system("mkdir update_check")
os.system("cd ../CyberFox/update_check && wget https://raw.githubusercontent.com/DarkGa/CyberFox/master/ver.txt")
update = filecmp.cmp('../CyberFox/ver.txt', '../CyberFox/update_check/ver.txt')
os.system("cd ../ && cd CyberFox")
os.system("rm -rf update_check")
os.system("clear")
print(colored("check new version", 'blue'))
time.sleep(3)
if update == True:
	os.system("clear")
	print(colored("you use last version", 'blue'))
if update == False:
	os.system("clear")
	print(colored("detect new version!", 'blue'))
	time.sleep(3)
	os.system("cp update.py ../")
	
	os.system("cd ../ && python3 update.py")
	
	print("run CyberFox!")
	time.sleep(3)
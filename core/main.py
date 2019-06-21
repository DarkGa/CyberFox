import os
from core.colors import *
try:
	from SimpleQIWI import *
except:
	print(Y+"install SimpleQIWI"+W)
	os.system("pip install SimpleQIWI &> install.log")
from core import main
from core import vivod
from time import sleep as ts
from core.banner import *

os.system("clear")
#modules
def main():
	os.system("clear")
	print(banner)
	try:
		van = input(R+"cbf>> "+W)
		if van == "1":
			try:
				vivod.viv()
				main()
			except:
				print(Y+"install requests"+W)
				os.system("pip install requests &> install.log")
			
		elif van == "help":
			from core import help
			main()
			
		elif van == "2":
			try:
				from core import vkhack
				main()
			except:
				print(Y+"install vk_api"+W)
				os.system("pip install vk_api &> install.log")
			
		elif van == "3":
			try:
				from core import bot
				main()
			except:
				print(Y+"install vk_api"+W)
				os.system("pip install vk_api &> install.log")
			
		elif van == "quit":
			print(R+"good bye!"+W)

		else:
			print(R+"[X]"+W+" Wrong command -> " + van)
			ts(1)
			main()

	except(KeyboardInterrupt):
		print(R+"[X]"+W+" Exiting...")
if __name__ == '__main__':
	main()


import os
from core.colors import *
from core import main
try:

	from core import vivod
except:
	pass
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
				for i in range(101):
					from time import sleep as ts
					ts(0.01)
					print(G+'Install requests[%d%%]\r'%i, end=""+W)
				print(Y+"\ninstall SimpleQIWI"+W)
				os.system("pip install SimpleQIWI &> install.log")
				from time import sleep as ts
				for i in range(101):
					ts(0.01)
					print(G+'Install SimpleQIWI [%d%%]\r'%i, end=""+W)
				from core import vivod
				vivod.viv()
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
				for i in range(101):
					ts(0.01)
					print(G+'Install vk_api [%d%%]\r'%i, end=""+W)
					from core import vkhack
		elif van == "3":
			try:
				from core import bot
				main()
			except:
				print(Y+"install vk_api"+W)
				os.system("pip install vk_api &> install.log")
				for i in range(101):
					ts(0.01)
					print(G+'Install vk_api [%d%%]\r'%i, end=""+W)
					from core import bot
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
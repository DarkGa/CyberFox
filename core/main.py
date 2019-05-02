import os
from core.colors import *
from SimpleQIWI import *
from core import balance
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
		if van == "use modules qiwi/hacker":
			print("")
			print("")
			mod = input(R+"cbf[hack/checker?]: "+W)
			if mod == "checker":
				balance.bal()
				main()
			elif mod == "hack":
				vivod.viv()
				main()
			
		elif van == "help":
			from core import help
			main()
			
		elif van == "use modules vk/hack":
			from core import vk
			main()
			
		elif van == "use modules vk/bot":
			from core import bot
			main()
			
		elif van == "use modules kali-linux":
			from core import virtual
			main()
			
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
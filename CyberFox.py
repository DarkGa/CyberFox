from core.modules import *
try:
	from core.main import *
except:
	pass
#run()
update()
try:
	main()
except:
	os.system("cd ~/../home/CyberFox && bash install.sh")


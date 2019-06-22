import vk_api
from time import sleep as ts
from core.colors import *
try:
    log = str(input(B+"[cbf] "+G+"login: "+Y))
    pas = str(input(B+"[cbf] "+G+"password: "+Y))
    vk_session = vk_api.VkApi(log, pas, scope='wall,messages')
    vk_session.auth()
    vk = vk_session.get_api()
except:
    print(R+"incorrect login or password!"+W)
    ts(2)
    raise

id = str(input(B+"[cbf] "+G+ "Enter id: "+Y))
if id == "0":
	a=vk.users.get(v="5.95")
	print(a)
if 'http' in id:
	id=id.replace("https://vk.com/","")
print("Enter kill to error vk")
mess = str(input(B+"[cbf] "+G+"Enter message: "+Y))
if mess=="kill":
    was = "ty."*500
else:
    was=mess
i = 0
kol=int(input(B+"[cbf] "+G+"spam post(0 endless spam): "+Y))
print(" ")
za=7
za=int(input(B+"[cbf] "+G+"delay(not less than 8): "+Y))
if id==0:
	while i<=kol or kol==0:
		vk.wall.post( message=was)
		i+=1
		print(B+"[cbf] "+G +"spam № " + str(i))
		ts(za)
else:
	try:
		while i<=kol or kol==0:
			vk.wall.post(owner_id=id, message=was)
			i+=1
			print(B+"[cbf] "+G +"spam № " + str(i))
			ts(za)
	except:
		print("\n\terror\n\nlogin:{}\npass:{}\nid={}".format(log,pas,id))
		ts(2)
		raise

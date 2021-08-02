
#credits:orlando S.E
#

#importacoes 
import socket
from time import sleep

#cores
RED = "\033[1;31m"
GREEN = "\033[1;32m"

print(RED + """

CREDITS:ORLANDO-SA

    ║\.
    ║▒\.
    ║▒▒\
    ║░▒ ║
    ║░▒║
    ║░▒ ║
    ║░▒║
    ║░▒║
    ║░▒ ║
    ║░▒║
    ║░▒ ║
    ║░▒║
   ▓▓▓▓▓▓▓
     ]█▓[
     ]█▓[
     ]█▓[
 """)
print("AVISO:RECOMENDADO BOTAR O IP DO SITE")
global site
site = str(input("DIGITE O SITE OU IP AQUI:"))
for por in range(1,6400):
		ls = int(por)
		
		sleep(0.1)
		try:
			host = site
			port = ls
			scan = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
			alvo = (host, port)
			scan.settimeout(2)
			res = scan.connect(alvo)
			scan.settimeout(None)
			if res is None:
				print(GREEN + "porta {} aberta".format(por))
				scan.close()
		
		except:
			print(RED + "porta {} fechada".format(por))

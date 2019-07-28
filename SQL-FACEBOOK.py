#!/bin/usr/python

"""
	Hack FACBOOK SQL

"""

import os
import sys
from time import sleep

def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 1000)

os.system('clear')
print ("""\033[1;31m
  ##############                      ###     ###
  ##############                      ###     ###
       ####      ######### #########  ###     ### ########
       ####      ######### ##    ###  ###     ### ##   ###
       ####      ##     ## #########  ###     ### ########
       ####      ######### ##         ########### ##
       ####      ######### ##         ########### ## GRATIS
""")

a = input("\033[1;33mMasukan Jumlah Diamond : ")
os.system('clear')
print ("\033[1;32m ==========================")
ketik ("\033[1;36m Mencoba Masuk Server TopUp. ")
print ("\033[1;32m ==========================")
print (' ')
sleep(10)
print ("\033[1;32m ==========================")
ketik ("\033[1;36m BERHASIL✅ ")
print ("\033[1;32m ==========================")
sleep(5)
print (' ')
print ("\033[1;32m ==========================")
ketik ("\033[1;36m Mengirim Diamond.. ")
print ("\033[1;32m ==========================")
print (' ')
sleep(10)
print ("\033[1;32m ==========================")
ketik ("\033[1;36m SUKSES✅ ")
print ("\033[1;32m ==========================")
print (' ')
sleep(5)
print ("\033[1;33m Jumlah Diamond : %s" % (a))
print ("\033[1;33m STATUS         : SUKSES ")
sleep(3)
print (' ')
ketik ("\033[1;32m -Diamond akan dikirim dalam 1x24 Jam ")
ketik ("\033[1;32m -Satu akun hanya bisa 1 kali dalam sehari ")
print (' ')
sleep(9999)

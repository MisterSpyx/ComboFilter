# let start frpm scratch i will not copy or past anything this time .
# Dear Crackers this tool is simple tool for help nothing else ! for a costume tool
# contact me in facebok or icq ! i wish you a good day <3 
import os
import requests
import sys
import time

red = '\033[91m'
ble = '\033[94m'
green = '\033[92m'
whit = '\033[00m'

banner = """
    ───────────────▄▄───▐█ 
    ───▄▄▄───▄██▄──█▀───█─▄
    ─▄██▀█▌─██▄▄──▐█▀▄─▐█▀ 
    ▐█▀▀▌───▄▀▌─▌─█─▌──▌─▌
    ▌▀▄─▐──▀▄─▐▄─▐▄▐▄─▐▄─▐▄ 
    I see a lot of kids putting 
    banner more then code .?!/
    """
Others = ['outook', 'hotmail', 'gmx', 't-online', 'gmail', 'yahoo', 'yandex', 'more']
para = "1-Other Combo/Email Filter\n2-Valid Email Checker\n3-Email:Pass => User:Pass\n4-Email:Pass => Emails"


class combo:
    def __init__(self):
        try:
            os.system("title " + "[+] Mr Spy  - 2021")
        except:
            pass
        print(green + banner + whit)
        print(green + para)
        self.animation = "|/-\\"
        print("\U0001f600")
        for i in range(50):
            time.sleep(0.1)
            sys.stdout.write("\r" + self.animation[i % len(self.animation)])
            sys.stdout.flush()

        self.choice = input("enter choice : ")
        self.list = input("enter ur list : ")
        if self.choice == '1':
            self.read(self.other)
        elif self.choice == '2':
            self.read(self.valid)
        elif self.choice == '3':
            self.read(self.mailtouser)
        elif self.choice == '4':
            self.read(self.cem)

    def read(self, choice):
        with open(self.list, 'r', errors="ignore") as f:
            for i in f:
                choice(i)

    def other(self, email):
        try:
            self.email = email.replace("\n", "").replace("\t", "")
            self.dom = self.email.split('@')[1]
            self.dom = self.dom.split('.')[0]
            if self.dom in Others:
                print(red + '[-] Public : {}'.format(email) + whit)
            else:
                print(green + '[+] Other : {}'.format(email) + whit)
                open('Others.txt', 'a').write(email + '\n')
        except:
            pass

    def valid(self, email):
        try:
            self.data = {"email": email}
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24'}
            response = requests.post("https://verifyemailaddress.com/result", headers=self.headers, data=self.data).text
            if "is valid" in response:
                print(green + "Valid Email {}".format(email) + whit)
                open('Verified.txt', 'a').write(email + '\n')
            else:
                response = requests.post("https://www.infobyip.com/verifyemailaccount.php", headers=self.headers,
                                         data=self.data).text
                if "Email account exists." in response:
                    print(green + "Valid Email {}".format(email) + whit)
                    open('Verified.txt', 'a').write(email + '\n')
                else:
                    print(red + "Not Valid Email {}".format(email) + whit)
        except:
            pass

    def mailtouser(self, combo):
        try:
            user, pas = combo.split(':')[0], combo.split(':')[1]
            user = user.split('@')[0]
            print(green + "[+]{}:{}".format(user, pas) + whit)
            open('Combo.txt', 'a').write("{}:{}".format(user, pas) + "\n")

        except:
            print(red + "[-] Bad Format {}".format(combo) + whit)

    def cem(self, combo):
        try:
            user, pas = combo.split(':')[0], combo.split(':')[1]
            print(green + "[+]{}".format(user) + whit)
            open('emails.txt', 'a').write("{}".format(user) + "\n")

        except:
            print(red + "[-] Bad Format {}".format(combo) + whit)


combo()

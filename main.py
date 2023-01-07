import os, json, random, threading, requests, time, instagrapi, traceback, os, pymongo, subprocess
from tabnanny import check
from instagrapi import Client
from bs4 import BeautifulSoup



#__PROGRAMID__ = "c2JedU7LcPNfkW8H9yPVAFjTuPxeJh9"
#__VERSION__ = "1.1"

config = json.loads(open("./config.json", "r", encoding="utf-8").read())


class color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET_ALL = "\033[0m"
    BLUE = '\033[96m'




def user_handler():
    with open("./usernames.txt", encoding="utf-8") as f:
        lines = f.readlines()
        tokens = []
        for splines in lines:
            hdr = splines.split("\n")[0]
            tokens.append(hdr)
    return tokens


def send_dm(username, password, userdm, messageText, count, i):
    try:
        username = username
        password = password

        cl = Client()
        
        print('1')
        cl.login(username, password)
        print(2)
        userid = cl.user_id_from_username(userdm)
        print(userid)
        for x in range(0,count):
            a = cl.direct_send(messageText, [int(userid)])
            print(f"{color.GREEN}[{i}] {color.RESET_ALL}Message succesfully sent to {color.GREEN}@{userdm} {color.RESET_ALL}with {color.GREEN}@{username}{color.RESET_ALL}.")
    except Exception as err:
        print(f"{color.RED}[{i}]{color.RESET_ALL} An error occured when sending message to {color.RED}@{userdm} {color.RESET_ALL}account. Passing. ERROR: {err}")
        traceback.print_exc()
        pass


def start(thread,msg):

    try:
        tx = []

                    
        for id, user_name in enumerate(user_handler()):

            
            if threading.active_count() <= thread:
                mT = threading.Thread(target=send_dm, args=(config["instagram_settings"]["username"],config["instagram_settings"]["password"], user_name, msg,config["script_settings"]["message_amount"],id+1))
                #send_dm(config["instagram_settings"]["username"],config["instagram_settings"]["password"], random.choice(working_proxies), user_name, config["instagram_settings"]["text_message"])
                mT.daemon = True
                mT.start()
                tx.append(mT)
        
        
        for t in tx:
            t.join(75)
    except Exception as e:
        traceback.print_exc()
        pass


if __name__ == "__main__":
    msg='Hello alwin'
    
    os.system("cls" if os.name == "nt" else "clear")
    check = [True]
    if check[0]:   
        print(f"{color.GREEN}[+] License correct program starting... {color.RESET_ALL}")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        print(fr"""{color.GREEN}
$$\   $$\           $$\ $$\                  $$$$$$\  $$\           $$\           
$$ |  $$ |          $$ |$$ |                $$  __$$\ \__|          $$ |          
$$ |  $$ | $$$$$$\  $$ |$$ | $$$$$$\        $$ /  \__|$$\  $$$$$$\  $$ | $$$$$$$\ 
$$$$$$$$ |$$  __$$\ $$ |$$ |$$  __$$\       $$ |$$$$\ $$ |$$  __$$\ $$ |$$  _____|
$$  __$$ |$$$$$$$$ |$$ |$$ |$$ /  $$ |      $$ |\_$$ |$$ |$$ |  \__|$$ |\$$$$$$\  
$$ |  $$ |$$   ____|$$ |$$ |$$ |  $$ |      $$ |  $$ |$$ |$$ |      $$ | \____$$\ 
$$ |  $$ |\$$$$$$$\ $$ |$$ |\$$$$$$  |      \$$$$$$  |$$ |$$ |      $$ |$$$$$$$  |
\__|  \__| \_______|\__|\__| \______/        \______/ \__|\__|      \__|\_______/

    Press any key to start the script...
    {color.RESET_ALL}    """)
        input("....")

        try:
            start(config["script_settings"]["threading"],msg)
            input("....")
        except:
            traceback.print_exc()
            input(".....")
    else:
        print(f"{color.RED}[-] {check[1]} {color.RESET_ALL}")
        input("....")

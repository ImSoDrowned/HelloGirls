import json
import requests
import time
import instagrapi
from instagrapi import Client
from bs4 import BeautifulSoup

config = json.loads(open("./config.json", "r", encoding="utf-8").read())


class color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET_ALL = "\033[0m"
    BLUE = "\033[96m"


def user_handler():
    with open("./usernames.txt", encoding="utf-8") as f:
        lines = f.readlines()
        tokens = []
        for splines in lines:
            hdr = splines.split("\n")[0]
            tokens.append(hdr)
    return tokens


def send_dm(username, password, messageText):
    try:
        username = username
        password = password

        cl = Client()

        cl.login(username, password)

        for i, userdm in enumerate(user_handler()):
            userid = cl.user_id_from_username(userdm)
            i += 1
            a = cl.direct_send(messageText, [int(userid)])
            print(
                f"{color.GREEN}[{i}] {color.RESET_ALL}Message succesfully sent to {color.GREEN}@{userdm} {color.RESET_ALL}with {color.GREEN}@{username}{color.RESET_ALL}."
            )

    except Exception as err:
        print(
            f"{color.RED}[{i}]{color.RESET_ALL} An error occured when sending message to {color.RED}@{userdm} {color.RESET_ALL}account. Passing. ERROR: {err}"
        )
        # traceback.print_exc()


def start_msg(msg):
	with open("./usernames.txt", encoding="utf-8") as f:
		lines = f.readlines()
		prt = []
		i = 1
		for line in lines:
		           if i <= 5:
		           	prt.append(line.split("\n")[0])
		           	i+=1
		           else:
		              prt.append("(and " + str(len(lines) - 5) + " more)")
		              break
		              i+=1
		print(f"{color.BLUE}{len(lines)}{color.RESET_ALL}","Usernames Detected",f"{color.BLUE}[", ", ".join(prt), f"]{color.RESET_ALL}")
		input("....")
		send_dm(
            config["instagram_settings"]["username"],
            config["instagram_settings"]["password"],
            msg,
        )

if __name__ == "__main__":

    print(
        rf"""{color.GREEN}
$$\   $$\           $$\ $$\                  $$$$$$\  $$\           $$\           
$$ |  $$ |          $$ |$$ |                $$  __$$\ \__|          $$ |          
$$ |  $$ | $$$$$$\  $$ |$$ | $$$$$$\        $$ /  \__|$$\  $$$$$$\  $$ | $$$$$$$\ 
$$$$$$$$ |$$  __$$\ $$ |$$ |$$  __$$\       $$ |$$$$\ $$ |$$  __$$\ $$ |$$  _____|
$$  __$$ |$$$$$$$$ |$$ |$$ |$$ /  $$ |      $$ |\_$$ |$$ |$$ |  \__|$$ |\$$$$$$\  
$$ |  $$ |$$   ____|$$ |$$ |$$ |  $$ |      $$ |  $$ |$$ |$$ |      $$ | \____$$\ 
$$ |  $$ |\$$$$$$$\ $$ |$$ |\$$$$$$  |      \$$$$$$  |$$ |$$ |      $$ |$$$$$$$  |
\__|  \__| \_______|\__|\__| \______/        \______/ \__|\__|      \__|\_______/

    Press any key to start the script...
    {color.RESET_ALL}    """
    )
    start_msg("Sup")
    

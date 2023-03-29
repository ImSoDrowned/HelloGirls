import json
import requests
import time
import instagrapi
from instagrapi import Client
from datetime import datetime, timedelta
#from bs4 import BeautifulSoup

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


def send_dm(username, password, messageText, totalno):
    try:
        username = username
        password = password

        cl = Client()

        cl.login(username, password)
        print(f"Sending {color.BLUE}{messageText}{color.RESET_ALL} to {color.GREEN}{totalno}{color.RESET_ALL} Accounts")
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
		print("....")
		send_dm(
            config["instagram_settings"]["username"],
            config["instagram_settings"]["password"],
            msg,
            len(lines)
        )
        
def start(grt_no):
	msgs = [config["message_settings"]["morning"]["message"], config["message_settings"]["night"]["message"]]
	msg = msgs[grt_no - 1]
	f= open("./count.txt",'r', encoding='utf-8')
	count= int(f.read())
	f= open("./count.txt",'w', encoding='utf-8')
	f.write(str(count+grt_no-1))
	f.close()
	start_msg(msg+' #'+str(count))

if __name__ == "__main__":
    
    
    print(
        f"""{color.GREEN}
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
    n_done=m_done=False
    dot=1
    while True:
    	
    	now=datetime.now()
    	m_date = datetime(now.year,now.month,now.day,config["message_settings"]["morning"]["hour"],config["message_settings"]["morning"]["minute"],0)
    	n_date = datetime(now.year,now.month,now.day,config["message_settings"]["night"]["hour"],config["message_settings"]["night"]["minute"],0)
    	mid= datetime(now.year,now.month,now.day,23,45,0)

    	if  (now>n_date and not n_done) and (((now-n_date).total_seconds()/3600) < 3):
    	 		print()
    	 		start(2)
    	 		n_done=True
    	 		print('\n' + f"{color.GREEN}All Done!!{color.RESET_ALL}")
    	 		print()
    	 	
    	elif (now>m_date and not m_done) and (((now-m_date).total_seconds()/3600) < 3):
    	 		print()
    	 		start(1)
    	 		m_done=True
    	 		print()
    	 		
    	elif now>mid and (m_done or n_done):
    	    n_done=m_done=False
    	    now=datetime.now()
    	    m_date = datetime(now.year,now.month,now.day,config["message_settings"]["morning"]["hour"],config["message_settings"]["morning"]["minute"],0) + timedelta(days=1)
    	    n_date = datetime(now.year,now.month,now.day,config["message_settings"]["night"]["hour"],config["message_settings"]["night"]["minute"],0) + timedelta(days=1)
    	    mid= datetime(now.year,now.month,now.day,23,45,0) + timedelta(days=1)
    	    
    	else:
    	     if dot>5:
    	     	dot=1
    	     print(f"{color.BLUE}Waiting for the right moment{'.'*dot}{' '*(5-dot)}{color.RESET_ALL}",end='\r')
    	     dot+=1
    	     pass
    	time.sleep(1)

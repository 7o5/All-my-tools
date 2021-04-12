import requests , threading , os
from uuid import uuid4
import json
from colorama import Fore
os.system('clear')
req = requests.session()
uid = uuid4()
username = ''
password = ''
target = ''
u=Fore.LIGHTRED_EX
y=Fore.LIGHTYELLOW_EX
asd=Fore.LIGHTMAGENTA_EX
print(f"{y}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(f"""{u}
#######                             
   #    #    # #####  #####   ####  
   #    #    # #    # #    # #    # 
   #    #    # #    # #####  #    # 
   #    #    # #####  #    # #    # 
   #    #    # #   #  #    # #    # 
   #     ####  #    # #####   ####  
""")
print(f"{y}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
username = input(f'{asd}Enter username : ')
password = input(f'{asd}Enter password : ')
target = input("[+] Target : ")
thread = int(input("[+] Thread : "))
logurl = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com',
    'Connection': 'keep-alive'
}
nameurl = 'https://i.instagram.com/api/v1/accounts/set_username/'
namedata = {

    "username": target
}
Att = 0
def edit():
    global coo , Att
    while True:
      r2 = req.post(nameurl, headers=headers, data=namedata, cookies=coo).status_code
      if r2 == 200:
        print(f"\r[+] Swapped > @{target}")
        exit()
      elif r2 == 400:
        Att += 1
        print(f"\r[+] Request > @{target} => {Att}")
      elif r2 == 429:
        print(f"\r[+] Blocked > @{username}")
        exit()
logdata = {
    'uuid': uid,
    'password': password,
    'username': username,
    'device_id': uid,
    'from_reg': 'false',
    '_csrftoken': 'missing',
    'login_attempt_countn': '0'
}
def get_challenge_choices(last_json):
    choices = []

    if last_json.get("step_name", "") == "select_verify_method":
        choices.append("[+] Challenge received")
        if "phone_number" in last_json["step_data"]:
            choices.append("[+] 0 - Phone")
        if "email" in last_json["step_data"]:
            choices.append("[+] 1 - Email")

    if last_json.get("step_name", "") == "delta_login_review":
        choices.append("[+] Login attempt challenge received")
        choices.append("[+] 0 - It was me")
        choices.append("[+] 0 - It wasn't me")

    if not choices:
        choices.append(
            '"{}" challenge received'.format(last_json.get("step_name", "Unknown"))
        )
        choices.append("[+] 0 - Default")

    return choices


def challange(login_json):
    global coo
    challenge_url = 'https://i.instagram.com/api/v1/' + login_json["challenge"]["api_path"][1:]
    try:
        b = requests.get(challenge_url, headers=headers, cookies=coo)
    except Exception as e:
        print("solve_challenge; {}".format(e))
        return False
    choiccc = get_challenge_choices(b.json())
    for choice in choiccc:
        print(choice)
    code = input("[+] Enter Email Or Phone : ")
    data_c = {
        'choice': code,
        '_uuid': uid,
        '_uid': uid,
        '_csrftoken': 'missing'
    }
    send_c = requests.post(challenge_url, data=data_c, headers=headers, cookies=coo)
    print("[+] Done sent Code To {}".format(send_c.json()['step_data']['contact_point']))
    code = input("[+] Enter Code : ").strip()
    data_co = {
        'security_code': code,
        '_uuid': uid,
        '_uid': uid,
        '_csrftoken': 'missing'
    }
    send_o = requests.post(challenge_url, data=data_co, headers=headers, cookies=coo)
    send_coj = send_o.json()
    if ('logged_in_user') in send_coj:
        coo = send_o.cookies
        input("[+] Are Your Ready?")
        threads = []
        for i in range(thread):
          th = threading.Thread(target=edit)
          th.start()
          threads.append(th)
        for thread2 in threads:
          thread2.join()
        return True
    else:
        login()
    return False

def login():
    global log, loginJS
    global coo
    log = req.post(logurl, headers=headers, data=logdata)
    loginJS = log.json()
    if 'logged_in_user' in log.text:
        coo = log.cookies
        input("[+] Are Your Ready?")
        threads = []
        for i in range(thread):
          th = threading.Thread(target=edit)
          th.start()
          threads.append(th)
        for thread2 in threads:
          thread2.join()
        pass
    elif "The username you entered doesn't appear to belong to an account" in log.text:
        print("\n Please Check Your Username And Try Again !")
        exit()
    elif "The password you entered is incorrect. Please try again." in log.text:
        print('The password you entered is incorrect , Please try again.')
        exit()
    elif "challenge_required" in log.text:
        coo = log.cookies
        return challange(log.json())
    elif '"two_factor_required":true' in log.text:
        print("Two Factor Required !")
        exit()
    else:
        print("Some Error Happend , Try again !")
        exit()
login()
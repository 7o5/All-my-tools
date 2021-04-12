import os
lib = input("""
[1] Download lib & update
[2] pass

[+] Please Choice >> """)

if lib == "1":
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

import requests,random,threading
from queue import Queue
from time import sleep
from user_agent import generate_user_agent

a = 0
b = 0
c = 0
d = 0
n = 0 


banner = ("""
[!] _hqvr
                                                            ████████████████                    
                                              ████▓▓▓▓░░▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒░░██                  
                                      ████████░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░██                
                                ██████░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░██              
                              ██░░░░░░▒▒▒▒▒▒▒▒████▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░▒▒██            
                            ██░░░░░░▒▒████████▒▒░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒██            
                            ██░░░░▒▒██░░░░██▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒██          
                          ██░░░░▒▒▒▒██░░██▒▒░░░░░░░░░░▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░▒▒██          
                          ██░░░░▒▒██  ░░██▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░▒▒░░▒▒██          
                          ██░░▒▒██  ░░░░██░░░░▒▒▒▒▒▒▒▒██████████░░░░░░░░░░░░▒▒░░▒▒▒▒██        
                            ██▒▒██████████░░▒▒▒▒▒▒████░░░░░░░░░░██░░░░▒▒░░░░▒▒░░▒▒▒▒██        
                            ████▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██░░░░░░      ░░██░░░░▒▒░░░░▒▒░░▒▒▒▒██        
                          ██▒▒▒▒▒▒░░▒▒▒▒██▒▒▒▒██░░░░          ░░██░░░░▒▒░░░░▒▒░░▒▒▒▒██        
                        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██░░              ░░██░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒██      
                        ██▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██░░                ░░██░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒██      
                      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██░░                  ░░██░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒██      
                    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██░░▓▓▓▓▓▓            ░░██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      
                    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██░░░░░░░░▒▒          ░░██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      
                    ██▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒██▒▒██░░▓▓▓▓▓▓░░        ░░▓▓██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓    
                  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒████  ▓▓▓▓██░░      ░░░░██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
                  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██  ░░░░  ░░░░      ░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
                ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██                    ░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ██▒▒██░░                  ░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ██▒▒██░░                  ░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓██▒▒▒▒██          ██░░    ░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██    
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██▒▒▒▒██                  ░░██▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒██      
          ██▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒██                  ░░██▒▒▒▒▒▒██▒▒▒▒████▒▒██      
          ██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒████▒▒██      ▒▒▒▒      ░░██▒▒▒▒████▒▒▒▒██  ██        
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒██░░████▓▓    ░░░░    ░░▓▓██▒▒▒▒██▓▓▒▒▓▓░░            
        ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██░░██░░░░░░██▓▓      ████░░██▒▒██  ▓▓▓▓                
        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██░░░░▓▓░░░░░░░░▓▓▓▓▓▓░░░░░░██▓▓░░  ░░░░                
      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░████████                
      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██░░    ██░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒████            
      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██░░░░      ██░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▓▓██          
      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██░░        ██░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒██        
      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██░░          ░░░░░░██▓▓▓▓▓▓████░░██▒▒▒▒▒▒▒▒▒▒▒▒██        
        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██░░          ░░░░██        ░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      
        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██░░          ░░░░            ░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      
          ▓▓▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒░░▒▒██░░      ░░░░░░            ░░██▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒██      
            ▓▓████████▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒██░░░░  ░░░░██            ░░░░██▒▒██▒▒▒▒░░░░▒▒▒▒██      
                  ██▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒██░░░░░░░░░░██            ░░██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒██      
                ████▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░██            ░░░░██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██        
                ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░██          ░░░░██░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒██        
                ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░██░░    ░░░░░░▓▓▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒██        
              ██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████░░░░░░░░████▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒██        
              ██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██          
              ██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒██          
            ██▒▒▒▒▒▒▒▒▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▒▒▒▒▒▒▒▒▒▒▒▒██          
  ░░░░                      ░░                                ░░                              
  ░░░░  ░░░░░░  ░░                                                    ░░  ░░                  
  ░░░░░░░░░░░░░░░░░░                                                                          

 """)
print(banner)
print("=========================================")
def check():
    global a,b,c,d,n
    try:
        global ID,TK,sid
    except:
        pass
    users = open('users.txt','r').read().splitlines()
    for user in users:
        l = len(users)
        n +=1
        if n == l:
            print('[-] Done Check All Users')
            sleep(3)
            exit()
        print(f'[-] {user}')
        url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+user+"&app_language=en"
        data = ""
        head = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": generate_user_agent(),
            "Connection": "Keep-Alive",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"
        }
        try:
            cookies = {'sessionid': sid}
            pass
        except:
            try:
                ssid_file = open('cookies.txt','r').read().splitlines()
                ssid = random.choice(ssid_file)
                cookies = {'sessionid': ssid}
            except:
                print('[!] Error In Cookies')
                sleep(3)
                exit()
        try:
            res = requests.request("GET",url,data=data,headers=head,cookies=cookies).json()["status_msg"]
            if res == ""or"":
                a +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{banner}\n=========================================\n[-] Hunt : {a}\n[-] Bad : {b}\n[-] Error : {c}\n[-] Blocked : {d}')
                with open('good.txt','a') as new:
                    new.write(f'{user}\n')
                try:
                    Account = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=❖ TikTok : {}\n❖ Free By : @m_x4k'.format(TK,ID,user)
                    requests.get(Account)
                except:
                    pass
            elif 'This username isn’t available.' in res:
                b +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{banner}\n=========================================\n[-] Hunt : {a}\n[-] Bad : {b}\n[-] Error : {c}\n[-] Blocked : {d}')

            else:
                c +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{banner}\n=========================================\n[-] Hunt : {a}\n[-] Bad : {b}\n[-] Error : {c}\n[-] Blocked : {d}')
        except:
            d +=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{banner}\n=========================================\n[-] Hunt : {a}\n[-] Bad : {b}\n[-] Error : {c}\n[-] Blocked : {d}')
            if len(str(d)) == '15':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('[!] Your IP is Blocked, Try vpn')
                sleep(3)
                exit()
            else:
                pass

def check_by_proxy():
    global a,b,c,d,n,proxy2,prox
    try:
        global ID,TK,sid
    except:
        pass
    users = open('users.txt','r').read().splitlines()
    for user in users:
        l = len(users)
        n +=1
        if n == l:
            print('[-] Done Check All Users')
            sleep(3)
            exit()
        print(f'[-] {user}')
        url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+user+"&app_language=en"
        data = ""
        head = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": generate_user_agent(),
            "Connection": "Keep-Alive",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"
        }
        try:
            cookies = {'sessionid': sid}
            pass
        except:
            try:
                ssid_file = open('cookies.txt','r').read().splitlines()
                ssid = random.choice(ssid_file)
                cookies = {'sessionid': ssid}
            except:
                print('[!] Error In Cookies')
                sleep(3)
                exit()

        try:
            prox = open('proxies.txt','r').read().splitlines()
            proxy = str(random.choice(prox))
            proxy2 = {'http':'http://{}'.format(proxy), 'https':'https://{}'.format(proxy)}
            res = requests.request("GET",url,data=data,headers=head,cookies=cookies,proxies=proxy2, timeout=8).json()["status_msg"]
            if res == ""or"":
                a +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{banner}\n=========================================\n[-] Hunt : {a}\n[-] Bad : {b}\n[-] Error : {c}\n[-] Blocked : {d}')
                with open('good.txt','a') as new:
                    new.write(f'{user}\n')
                try:
                    Account = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text=❖ TikTok : {}\n❖ Free By : @m_x4k'.format(TK,ID,user)
                    requests.get(Account)
                except:
                    pass
            elif 'This username isn’t available.' in res:
                b +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{banner}\n=========================================\n[-] Hunt : {a}\n[-] Bad : {b}\n[-] Error : {c}\n[-] Blocked : {d}')

            else:
                c +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{banner}\n=========================================\n[-] Hunt : {a}\n[-] Bad : {b}\n[-] Error : {c}\n[-] Blocked : {d}')
        except Exception as cx:
            print(cx)
            d +=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{banner}\n=========================================\n[-] Hunt : {a}\n[-] Bad : {b}\n[-] Error : {c}\n[-] Blocked : {d}')
            if len(str(d)) == '15':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('[!] Your IP is Blocked, Try vpn')
                sleep(3)
                exit()
            else:
                pass
option = input("""
[1] Cheack Users
[2] Cheack Users with proxies
[3] Generate Users

[+] Please choice one option : """)
print("=========================================")

if option == '1':
    tele = input('[+] Send Users To Telegram bot [Y/y] : ')
    if tele == 'y' or tele == 'Y':
        TK = input('[+] Enter Bot Token : ')
        ID = input('[+] Enter Telegram ID : ')
        pass
    else:
        pass
    print("=========================================")
    cook = input('[1] Use One Session id [2] Use Two Session id : ')
    if cook == '2':
        ssid = input('[1] Enter The Session ID from TikTok : ')
        ssid2 = input('[2] Enter The Session ID from TikTok : ')
        with open('cookies.txt','w') as cok:
            cok.write(f'{ssid}\n{ssid2}\n')
        pass
    else:
        sid = input('[+] Enter The Session ID from TikTok : ')
        pass
    check()

elif option == '2':
    tele = input('[+] Send Users To Telegram bot [Y/y] : ')
    if tele == 'y' or tele == 'Y':
        TK = input('[+] Enter Bot Token : ')
        ID = input('[+] Enter Telegram ID : ')
        pass
    else:
        pass
    print("=========================================")
    cook = input('[1] Use One Session id [2] Use Two Session id : ')
    if cook == '2':
        ssid = input('[1] Enter The Session ID from TikTok : ')
        ssid2 = input('[2] Enter The Session ID from TikTok : ')
        with open('cookies.txt','w') as cok:
            cok.write(f'{ssid}\n{ssid2}\n')
        pass
    else:
        sid = input('[+] Enter The Session ID from TikTok : ')
        pass
    
    def start():
        while True:
            check_by_proxy()

    threadlist = []
    for i in range(10):
        t = threading.Thread(target=start)
        t.start()
        threadlist.append(t)
    else:
        for i in threadlist:
            i.join()

else:
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890_.'
    user_len = int(input("[+] Enter your user length : "))
    user_count = int(input("[+] How many users would you like : "))
    for x in range(0, user_count):
        users = ""
        for x in range(0, user_len):
            users_char = random.choice(chars)
            users = users + users_char
        with open('users.txt','a') as ECHO:
            ECHO.write(f"{users}\n")
            ECHO.close()
            

#Telegram @m_x4k
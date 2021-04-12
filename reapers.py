import requests
import uuid
import secrets
import time
import os
orr="\033[0;91m"
yell="\033[0;93m"
gr = "\033[0;92m"
print(yell)
line = "-------------------#Reaper~ū«@_r.cc0_>û»--------------------\n"
logo = f"""
    ░░                                                  ░░    
    ████                                              ████    
    ██▓▓██                                          ██  ██    
    ██▓▓▓▓██                                      ██    ██    
██████▓▓▓▓▓▓██████████████████████████████████████      ██████
██░░░░░░▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░░░██
██▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒  ██
██▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒      ░░▒▒▒▒    ██
██░░▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒    ░░██
██░░▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒        ░░██
██░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒        ▒▒░░██
██▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒    ▒▒▒▒        ▒▒▒▒  ██
██▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░▒▒▒▒    ▒▒▒▒▒▒    ▒▒▒▒      ██
██░░▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░▒▒    ░░▒▒  ▒▒  ░░▒▒      ░░██
██▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓    ▒▒  ▒▒▒▒    ▒▒▒▒▒▒      ▒▒  ██
██▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▒      ▒▒▒▒▒▒      ▒▒▒▒      ▒▒    ██
██░░▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒▒▒▓▓        ▒▒▒▒    ▒▒▒▒  ▒▒  ▒▒▒▒    ░░██
██░░▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒      ░░░░▒▒▒▒  ░░▒▒    ▒▒▒▒        ░░██
██░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓    ▒▒▒▒░░  ▒▒▒▒▒▒    ▒▒▒▒        ▒▒░░██
██░░░░░░▓▓▓▓▓▓░░░░░░▓▓  ░░░░      ░░      ░░░░░░      ░░░░░░██
██░░▒▒▒▒▒▒▓▓▓▓░░▒▒▒▒▒▒▒▒▒▒      ░░▒▒    ░░    ▒▒    ░░▒▒▒▒░░██
██░░▓▓▓▓▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒    ▒▒░░  ▒▒▒▒▒▒      ▒▒  ▒▒▒▒    ░░██
██░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓    ▒▒      ▒▒▒▒      ▒▒▒▒▒▒      ▒▒░░██
██░░▒▒▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓  ▒▒      ▒▒▒▒      ▒▒  ▒▒        ▒▒░░██
██░░▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒    ▒▒░░  ▒▒    ▒▒    ▒▒    ▒▒▒▒▒▒░░██
██░░▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒  ▒▒      ▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒  ▒▒░░██
██░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓  ▒▒      ▒▒▒▒      ▒▒▒▒▒▒        ▒▒░░██
██░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░    ▒▒░░▒▒▒▒    ░░▒▒  ▒▒      ▒▒▒▒░░██
██░░▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒  ▒▒      ▒▒▒▒▒▒      ▒▒  ▒▒▒▒▒▒▒▒░░██
██░░▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓  ▒▒      ▒▒▒▒        ▒▒▒▒▒▒    ▒▒▒▒░░██
██░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░  ▒▒▒▒░░▒▒▒▒    ░░▒▒▒▒      ░░▒▒▒▒░░██
██░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓  ▒▒▒▒      ▒▒▒▒▒▒    ▒▒    ▒▒▒▒▒▒▒▒░░██
██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒  ▒▒░░▒▒        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██
██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒    ▒▒    ░░▒▒▒▒      ▒▒▒▒▒▒▒▒░░██
██░░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒      ░░▒▒▒▒      ▒▒    ▒▒▒▒▒▒▒▒░░░░██
██████░░░░▒▒▒▒▒▒▓▓▒▒▒▒    ▒▒▒▒░░        ▒▒▒▒  ▒▒▒▒▒▒░░░░██████
      ████░░░░▒▒▒▒▒▒    ░░          ▒▒░░▒▒▒▒▒▒▒▒░░░░████      
          ████░░░░▒▒      ▒▒    ▒▒▒▒▓▓▓▓▓▓▒▒░░░░████          
              ██      ▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓██              
            ██    ████░░░░▒▒▒▒░░▒▒▒▒░░░░████▓▓▓▓██            
          ██    ██    ████░░░░░░░░░░████    ██▓▓▓▓██          
        ████████          ████░░████          ████████        
                              ██                              

by: reaper

                                     """
a = 1
r = requests.Session()
u = uuid.uuid4()
print(orr)
print(logo)
print(yell)
print(line)
print("[1]سبام")
print("[2]انتحار")
print("[3]مخدرات")
print("[4]اباحي")
print("[5]منظمة ارهابية")
print("[6]كراهية")
print("[7]تنمر")
print("[8]انتحال شخص ما اعرف")
print("[11]بزر ١٣")
print("[12]اسلحة")
print("[13]انتحال انا")
print(line)
print("     ")
repo = int(input("نوع البلاغ:"))
user = input("اسم حسابك:")
password = input("كلمة السر: ")
target = input("الهدف")
z = int(input("الغفوة:"))
much = int(input("كم بلاغ بدك:"))


b = 'https://www.instagram.com/accounts/login/ajax/'

w = {
"accept":"*/*",
"accept-encoding":"gzip, deflate,br",
"accept-language": "ar,en-US;q=0.9,en;q=0.8",
"content-length": "279",
"content-type": "application/x-www-form-urlencoded",
"origin": "https://www.instagram.com",
"referer": "https://www.instagram.com/",
"sec-fetch-dest":"empty",
"sec-fetch-site":"same-origin",
"user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
"x-csrftoken": "lih2ypMfhzdqwMbm5jIILqxZDj4zLeCW",
"x-ig-app-id": "936619743392459",
"x-ig-www-claim": "hmac.AR1_p9SjMFQF73bcZgzygDgxb9yBZUn83e69xoDD2qpSdmtW",
"x-instagram-ajax":"901e37113a69",
"x-requested-with":"XMLHttpRequest"
}

k = {'username':user,
            'enc_password':
'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}

l = r.post(b,headers=w,data=k)

if("userId") in l.text:
	r.headers.update({'X-CSRFToken': l.cookies['csrftoken']})
	print("log true")
	
	v = "https://www.instagram.com/{}/?__a=1".format(target)
	t = r.get(v).json()
	y = str(t["logging_page_id"])
	h = y.split("_")[1]
	for i in range(much):
		urreport = "https://www.instagram.com/users/{}/report/".format(h)
		dat = {f'source_name':'','reason_id':{repo},'frx_context':''}
		repp = r.post(urreport,data=dat)
		os.system("clear")
		print(f"{logo}\n{yell}\n{line}\n[$]The Target : {target} \n[$]The Sleep : {z} \n[$]Done Report : {a}\n[$]The Number of reports : {much}\n\n{line}")
		time.sleep(z)
		a += 1
		
else:
        print('[$]Error Login Check Your info !!')
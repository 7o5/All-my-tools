import os
lib = input("""
[1] Download lib & update
[2] pass

[+] Please Choice >> """)

if lib == "1":
    os.system('pip install requests')
    os.system('pip install Fore')
    os.system('pip install colorama')
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
import requests
from colorama import Fore
banner = ("""
[!] made by reaper
 ███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████                   
""")
print(banner)
print('====================================')
username_login = input('[+] Enter Username To Login in Instagram ==> : ')
password_login = input('[+] Enter Password ==> : ')
url_login = 'https://www.instagram.com/accounts/login/ajax/'
headers_login = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '291',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36',
    'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
}
data_login = {
    'username': username_login,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{password_login}',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
}
req_login = requests.post(url_login, data=data_login, headers=headers_login)
if '"authenticated":false' in req_login.text:
    print('[!] Username Or Password Is Error - Try Agin')
    exit(0)
elif '"authenticated":true' in req_login.text:
    print('[+] Done Login')
    sessd = req_login.cookies['sessionid']
    username = input('[+] Enter Name File ==> : ')
    ff = username
    file = open(ff).read().splitlines()
    for file in file:
        url_checker = 'https://www.instagram.com/accounts/login/ajax/'
        headers_checker = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '291',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36',
            'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest'
        }
        data_checker = {
            'username': file,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613414957:dsbvhdbvdsvbsdh',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        req = requests.post(url_checker, data=data_checker, headers=headers_checker).text
        if '"user":false' in req:
            url_get_info = 'https://www.instagram.com/accounts/edit/?__a=1'
            headers_get_info = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Zc4tm5D7QNL1hiMGJ1caLT7DNPTYHqH0; ds_user_id=45334757205; sessionid={sessd}; rur=VLL',
                'referer': 'https://www.instagram.com/accounts/edit/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9Ncl',
                'x-requested-with': 'XMLHttpRequest'
            }
            data_get_info = {
                '__a': '1'
            }
            req_get_info = requests.get(url_get_info, data=data_get_info, headers=headers_get_info)
            email = str(req_get_info.json()['form_data']['email'])
            first_name = str(req_get_info.json()['form_data']['first_name'])
            phone_number = str(req_get_info.json()['form_data']['phone_number'])
            biography = str(req_get_info.json()['form_data']['biography'])
            external_url = str(req_get_info.json()['form_data']['external_url'])
            url_swap = 'https://www.instagram.com/accounts/edit/'
            headers_swap = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'content-length': '130',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=UeJJwEB0TKAL0cEYl3dsep58FFYKH0Nc; ds_user_id=45334757205; sessionid={sessd}; rur=VLL',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/edit/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'x-csrftoken': 'UeJJwEB0TKAL0cEYl3dsep58FFYKH0Nc',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9Ncl',
                'x-instagram-ajax': '1cb44f68ffec',
                'x-requested-with': 'XMLHttpRequest',
            }
            data_swap = {
                'first_name': first_name,
                'email': email,
                'username': file,
                'phone_number': phone_number,
                'biography': biography,
                'external_url': external_url,
                'chaining_enabled': 'on'
            }
            req_swap = requests.post(url_swap, data=data_swap, headers=headers_swap).text
            if '{"status":"ok"' in req_swap:
                print(Fore.RED+f'[+] {Fore.BLUE}*{Fore.BLUE}************************************** {Fore.RED}[+]')
                print(Fore.RED+f' {Fore.YELLOW}    Username Found ==> : {Fore.GREEN}{file}')
                print(Fore.RED+f' {Fore.YELLOW}    Username Done Swap ==> : {Fore.GREEN}{file}')
                print(Fore.RED+f'[+] {Fore.BLUE}*{Fore.BLUE}************************************** {Fore.RED}[+]')
            else:
                print(f'[-] Error Swap The Username ==> : {file}')
        elif '"user":true' in req:
            print(Fore.RED+f'[=] Username Taken ==> : {file}')

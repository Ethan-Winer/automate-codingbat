# RUN THIS FILE OR RUN.JAVA TO USE THIS PROGRAM

# DO NOT LOG INTO CODINGBAT WHILE IT IS RUNNING!!
# ANYTHING BEFORE OR AFTER IS FINE THO

import requests
import json
import os

session = requests.Session()
session.get('https://codingbat.com')

cookies = {
    'JSESSIONID': session.cookies.get("JSESSIONID")
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

requests.post('https://codingbat.com/login', cookies=cookies, data=data)

data = {
    'cuname': username,
    'owner': '',
}

with open('./answers.json', 'r') as file:
  question_info = json.load(file)

for key in question_info.keys():
  question = question_info[key]
  if 'code' not in question:
    continue
  data['id'] = question['id']
  data['code'] = question['code']
  response = requests.post('https://codingbat.com/run', cookies=cookies,  data=data)

  print('Completed ' + key)
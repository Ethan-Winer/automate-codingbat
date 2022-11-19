import os
import requests
import json

response = requests.get('https://codingbat.com/java')

categories = []

for i in range(len(response.text)):
    if response.text[i: i + len('/java/')] == '/java/':
        url = ''
        while response.text[i] != "'":
            url += response.text[i]
            i += 1
        categories.append(url)

output_dict = {}
for category in categories:
    response = requests.get('https://codingbat.com' + category)
    for i in range(len(response.text)):
        if response.text[i: i + len('/prop/')] == '/prob/':
            i += len('/prop/')
            question_id = ''
            name = ''
            while response.text[i] != "'":
                question_id += response.text[i]
                i += 1
            i += 2
            while response.text[i] != '<':
                name += response.text[i]
                i += 1
            output_dict[name] = {'id': question_id}

for folder_name in os.listdir('./codingbat/java'):
    for file_name in os.listdir('./codingbat/java/' + folder_name):
        with open(f'./codingbat/java/{folder_name}/{file_name}', 'r') as file:
            name = file_name[0: len('.java') * -1]
            code = file.read()
            try:
                output_dict[name]['code'] = code
            except KeyError:
                continue
with open('../questionInfo.json', 'w') as file:
    json.dump(output_dict, file)
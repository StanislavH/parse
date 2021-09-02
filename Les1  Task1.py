import requests
import json

USER = 'StanislavH'
GIT_API_URL = 'https://api.github.com'
request = requests.get(GIT_API_URL + '/users/' + USER + '/repos')
json_v = request.json()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json_v, f, ensure_ascii=False, indent=4)

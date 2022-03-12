import requests
import json
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.github.com/', headers={"content-type":"application/json"})
print(response.status_code)
print(response.url)

j = json.loads(response.content)
print(j['current_user_url'])

chromium_query = requests.get("https://api.github.com/search/issues", params={"q":"Chrominum not working properly"})
print(chromium_query.status_code)
j = json.loads(chromium_query.content)
print("Total Count : {}".format(j['total_count']))

user_query = requests.get("https://api.github.com/user", auth=HTTPBasicAuth("kallolghose", "#PRKRfeb@29#"))
print(user_query.status_code)
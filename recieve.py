import requests

API_HOST = 'http://python.recruit.herrencorp.com/'
headers = {'Authorization': 'herren-recruit-python'}
path = 'api/v1/inbox/redbee99@naver.com'

r = requests.get(API_HOST+path, headers=headers)

print(r.text)
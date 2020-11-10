import db_config
from sqlalchemy import text, create_engine
import requests
import json
from collections import OrderedDict

db = create_engine(db_config.DB_URL, encoding='utf-8', max_overflow = 0)
API_HOST = 'http://python.recruit.herrencorp.com/'
PATH = 'api/v1/mail'
PATH2 = 'api/v2/mail'
headers = {'Authorization': 'herren-recruit-python', 'Content-Type': 'application/x-www-form-urlencoded'}
headers2 = {'Authorization': 'herren-recruit-python', 'Content-Type': 'application/json'}
rows = db.execute(text("SELECT * FROM inform")).fetchall()

file_data = OrderedDict()

for row in rows:
    if(row['agree'] == 'YES'):
        temp = row['email'].split('@')
        if(temp[1]=='naver.com' or temp[1]=='gmail.com'):
            file_data['mailto'] = row['email']
            file_data['subject'] = '뉴스레터 구독자 메일2'
            file_data['content'] = '뉴스레터를 구독하신 여러분들 진심으로 환영합니다.2'

            r = requests.post(API_HOST + PATH2, headers=headers2, data=json.dumps(file_data))
            print('api2')
            print(r.headers)
            print(r.text)
        else:
            r = requests.post(API_HOST+PATH, headers=headers, data={'mailto':row['email'], 'subject':'뉴스레터 구독자 메일', 'content':'뉴스레터를 구독하신 여러분들 진심으로 환영합니다.'})
            print('api1')
            print(r.headers)
            print(r.text)
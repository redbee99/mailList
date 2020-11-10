import db_config
from sqlalchemy import text, create_engine
import requests

db = create_engine(db_config.DB_URL, encoding='utf-8', max_overflow = 0)
API_HOST = 'http://python.recruit.herrencorp.com/'
PATH = 'api/v1/mail'
headers = {'Authorization': 'herren-recruit-python', 'Content-Type': 'application/x-www-form-urlencoded'}

rows = db.execute(text("SELECT * FROM inform")).fetchall()
for row in rows:
    if(row['agree'] == 'YES'):
        r = requests.post(API_HOST+PATH, headers=headers, data={'mailto':row['email'], 'subject':'뉴스레터 구독자 메일', 'content':'뉴스레터를 구독하신 여러분들 진심으로 환영합니다.'})
        print(r.headers)
        print(r.text)
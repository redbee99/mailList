db = {
    'user': 'root',
    'password': 'redbee99',
    'host': '59.12.61.31',
    'port': 3306,
    'database': 'Profile'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
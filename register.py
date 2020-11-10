from flask import Flask, render_template, request
import db_config
from sqlalchemy import text, create_engine


app = Flask(__name__)
db = create_engine(db_config.DB_URL, encoding='utf-8', max_overflow = 0)


@app.route('/')
def test():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def post():
    params = {'c_name': request.form['c_name'], 'email': request.form['email'], 'agree': request.form['agree']}
    new_user_id = db.execute(text("INSERT INTO inform (c_name, email, agree) VALUES (:c_name, :email, :agree)"), params).lastrowid
    return  "구독 성공!"


if __name__ == '__main__':
    app.run()
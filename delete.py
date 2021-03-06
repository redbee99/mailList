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
    params = {'c_name': request.form['c_name'], 'email': request.form['email']}
    new_user_id = db.execute(text("DELETE FROM inform WHERE c_name = :c_name AND email = :email"), params)
    return  "구독취소 성공!"


if __name__ == '__main__':
    app.run()
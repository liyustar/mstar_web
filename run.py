# coding: utf-8

from flask import Flask, url_for, request, render_template, redirect
import pymysql
from config import *

app = Flask(__name__)

def connectdb():
    db = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, db=DB_NAME, charset='utf8')
    db.autocommit(True)
    cursor = db.cursor()
    return (db, cursor)

def closedb(db, cursor):
    cursor.close()
    db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    (db, cursor) = connectdb()
    cursor.execute('select * from company')
    posts = cursor.fetchall()
    closedb(db, cursor)
    print(posts)
    return render_template('list.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)

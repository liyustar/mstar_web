# coding: utf-8

from flask import Flask, url_for, request, render_template, redirect
import pymysql
from config import *

app = Flask(__name__)

def connectdb():
    db = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, db=DB_NAME, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
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
    return render_template('list.html', posts=posts)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)

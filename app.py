from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask (__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'word entries master database'

mysql = MySQL(app)

@app.route('/',methods=['POST','GET'])
def search():
    if request.method=='GET':
        cur = mysql.connection.cursor()
        cur.execute('''SELECT English_Translation FROM wordentry2''')
        word = cur.fetchall()
        print (word)
        return render_template ('search.html', word = word)
    else:
        input1 = request.form['input1']
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM wordentry2 WHERE English_Translation LIKE '%{}%' '''. format(input1))
        output = cur.fetchall()
        return render_template ('response.html', urduword = output [0][1], englishword = output [0][2])



if __name__ == '__main__':
    app.run()

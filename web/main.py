from flask import Flask,request,render_template

from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD']= 'root'
app.config['MYSQL_DATABASE_DB']= 'text'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

@app.route('/')
def my_form():
    return render_template('from_ex.html')

@app.route('/',methods = ['POST'])
def authenticate():
    username = request.form['u']
    password = request.form['p']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where username'" + username + "' and password='" + password + "'" )
    data = cursor.fetchone()
    if data is None:
        return ' Username or Password is wrong'
    else:
        return 'Logged in SUCCESSFULLY'

if __name__ == '__main__':
    app.debug= True
    app.run()





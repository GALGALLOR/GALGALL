from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import webbrowser

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        if email=='Ga.roba@lightacademy.ac.ke' and name== '':
            return redirect('/usersthatshouldonlybeseenbygalgallo')
        else:
            return redirect('/google')


    return render_template('idk.html')

@app.route('/usersthatshouldonlybeseenbygalgallo')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

@app.route('/google')
def google():
    url = 'https://www.google.com'
    webbrowser.open_new_tab(url)


if __name__ == '__main__':
    app.run()

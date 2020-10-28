from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['name']
        return redirect(url_for('user', usr=user))
    else:
        return  render_template('login.html')

@app.route('/<usr>')
def user(usr):
    return f'<h1>{usr}</h1>'


if __name__=='__main__':
    app.run(debug=True)

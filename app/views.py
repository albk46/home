from flask import request, render_template, request, redirect, url_for
from app import app
from . import User
from . import session
from werkzeug.security import generate_password_hash, check_password_hash
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    error = []
    logon = []
    if request.method == 'POST':        
        username = request.form['name']
        password = request.form['password']
        print 'tttt', password, username
        for user in session.query(User).filter(User.name==username):
            theuser = user
        """
        print 'yo', password
        hasha = generate_password_hash(password)    
        print 'yoyo', password, hasha
        hasha2 = generate_password_hash(password) 
        print 'yoyoyoy', check_password_hash(hasha2,password)
        """
        if theuser.check_password(password):
            logon = username
        else:            
            error = 'Wrong password'
            redirect(url_for('login'), error=error)

    return render_template("index.html", name = logon, error = error)


@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/hello/', methods = ['POST'])
def hello():
    #CHECK IF EXIST NAME
    info = request.form
    ed_usera = User(name=info['name'], email=info['email'], \
                    phone=info['phone'], password=info['password'])

    session.add(ed_usera)
    session.commit()



    return render_template("hello.html", name = info['name'])
@app.route('/login')
def login():
    error=[]
    return render_template("login.html", error = error)
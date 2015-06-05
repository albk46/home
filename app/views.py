# -*- coding: UTF-8 -*-
from flask import request, render_template, request, redirect, url_for, flash, g
from app import app
from . import User, Flat, LoginForm
from . import session
from werkzeug.security import generate_password_hash, check_password_hash #del this

from flask.ext.wtf import Form
from flask.ext.login import LoginManager
from wtforms import TextField, TextAreaField, SubmitField, validators

login_manager = LoginManager()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print form.errors
    if form.is_submitted():
        print "submitted"
    if form.validate():
        print "valid"
    if form.validate_on_submit():
        print form.errors
        if form.is_submitted():
            print "submitted"
        if form.validate():
            print "valid"
        print form.errors
        flash(u'Successfully logged in as %s' % form.user.name)
        session['user_id'] = form.user.id
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(userid):
    return User.get(userid)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():


    return render_template("index.html")


@app.route('/register')
def register():
    #!!!check for exist user
    return render_template("register.html")

@app.route('/hello/', methods = ['POST'])
def hello():
    #CHECK IF EXIST NAME
    info = request.form
    ad_user = User(name=info['name'], email=info['email'], \
                    phone=info['phone'], password=info['password'])
    session.add(ad_user)
    session.commit()
    return render_template("hello.html", name = info['name'])

@app.route('/good/', methods = ['POST'])
def good():
    if request.method == 'POST': 
        try:
            print 'yotut'
            adress = request.form['adress']
            print 'its name'
            floor = request.form['floor']
            floor_max = request.form['floor_max']
            square_meter = request.form['square_meter']    
            rooms = request.form['rooms']
            bath_type = request.form['bath_type']    
            month_cost = request.form['month_cost']
            deposit = request.form['deposit']
            amenity = request.form['amenity']
            utilities = request.form['utilities']    
            print 'its ok?', amenity
            ad_flat = Flat(adress=adress, floor=floor, \
                square_meter=square_meter, rooms=rooms, \
                bath_type=bath_type, month_cost=month_cost, \
                deposit=deposit, utilities=utilities)
            # floor_max=floor_max adress=adress, 
            print 'yotut'
            session.add(ad_flat)
            session.commit()
            flash(u'Вы добавили квартиру')
            return render_template("good.html")
        except KeyError, e:
            print e, 'yo'
            render_template("flat_add.html")
        else:
            render_template("login.html")
        finally:
            print 'this nut is cracked'
    return render_template("good.html")

@app.route('/flat_add')
def flat_add():  
    return render_template("flat_add.html")
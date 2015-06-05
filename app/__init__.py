# -*- coding: utf-8 -*-
from flask import Flask, session

#from app import views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/home'

from models import *
engine = create_engine('postgresql://localhost/home',echo=False)#Echo shows all prodused SQL
Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
###################################

#yi = User.query.all()
#print 'tuta'
#for each in yi:
#    print each.name 
session = Session()
#ed_usera = User(name='qwewqeqwe', email='Ed qweqweq', phone='qweewqq', password='qwe')
#session.add(ed_usera)
#session.commit()
tmp = session.query(User).all()
for each in tmp:
	print '--', each.name
import datetime
nmp = session.query(Flat).all()
for each in nmp:
	print '++', each.adress
from views import *
from jinja2 import Environment, PackageLoader
env = Environment()#loader=PackageLoader('yourapplication', 'templates'))

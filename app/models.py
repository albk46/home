from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField
from wtforms.validators import Required
from . import session

ROLE_USER = 0
ROLE_ADMIN = 1
Base = declarative_base()

class LoginForm(Form):
    username = TextField('Username', [Required()])
    password = PasswordField('Password', [Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None


    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        user = session.query(User).filter(User.name==self.username.data)
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    phone = Column(String(20), unique=True)
    pw_hash = Column(String(150))
    role = Column(Integer, default = ROLE_USER)
    flat = relationship('Flat', backref='user')

    def __init__(self, name=None, email=None, phone=None, password=None, role=ROLE_USER):
        self.name = name
        self.email = email
        self.phone = phone
        self.pw_hash = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
        
    def __repr__(self):
        return '<User %r>' % (self.name)

class Flat(Base):
    __tablename__ = 'flat'
    id = Column(Integer, primary_key=True)
    adress = Column(String(100), unique=True)
    floor = Column(Integer)
    floor_max = Column(Integer)
    square_meter = Column(Integer)
    rooms = Column(Integer)
    bath_type = Column(String(20), default = ROLE_USER)
    month_cost = Column(Integer)
    utilities = Column(Integer)
    deposit = Column(Integer)
    amenity = Column(String(200))
    #FOTO

    user_id = Column(Integer, ForeignKey('user.id'))
    #DateTime!!!!!

    #flats = 
    def __init__(self, adress=None, floor=None, floor_max=None, square_meter=None, 
        rooms=1, bath_type=None, month_cost=None, utilities=None,
        deposit=None, amenity=None):
        self.adress = adress
        self.floor = floor
        self.floor_max = floor_max  
        self.square_meter = square_meter
        self.rooms = rooms
        self.bath_type = bath_type
        self.month_cost = month_cost
        self.utilities = utilities
        self.deposit = deposit
        self.amenity = amenity

    def __repr__(self):
        return '<User %r>' % (self.adress)


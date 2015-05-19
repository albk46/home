from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
ROLE_USER = 0

ROLE_ADMIN = 1
Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    phone = Column(String(20), unique=True)
    pw_hash = Column(String(150), unique=True)
    role = Column(Integer, default = ROLE_USER)
    flat = relationship('Flat', backref='user')

    def __init__(self, name=None, email=None, phone=None, password=None, role=ROLE_USER):
        self.name = name
        self.email = email
        self.phone = phone
        self.pw_hash = generate_password_hash(password)
        self.role = role
        print password, self.pw_hash

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)
        
    def __repr__(self):
        return '<User %r>' % (self.name)

class Flat(Base):
    __tablename__ = 'flat'
    id = Column(Integer, primary_key=True)
    adress = Column(String(100), unique=True)
    floor = Column(Integer, unique=True)
    square_meter = Column(Integer, unique=True)
    rooms = Column(Integer, unique=True)
    bath_type = Column(String(20), default = ROLE_USER)
    month_cost = Column(Integer, unique=True)
    utilities = Column(Integer, unique=True)
    deposit = Column(Integer, unique=True)
    amenity = Column(String(200), unique=True)
    #FOTO

    user_id = Column(Integer, ForeignKey('user.id'))
    #DateTime!!!!!

    #flats = 
    def __init__(self, adress=None, floor=None, square_meter=None, 
        rooms=1, bath_type=None, month_cost=None, utilities=0,
        deposit=0, amenity=None):
        self.adress = adress
        self.floor = floor
        self.square_meter = square_meter
        self.rooms = rooms
        self.bath_type = bath_type
        self.month_cost = month_cost
        self.utilities = utilities
        self.deposit = deposit
        self.amenity = amenity
    def __repr__(self):
        return '<User %r>' % (self.name)


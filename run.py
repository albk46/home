#!/home/alexandr/arenda/thehome/bin/python
from app import app
if __name__ == '__main__':
	app.config['SESSION_TYPE'] = 'memcached'
	app.config['SECRET_KEY'] = 'gnarrrr!!'
	app.run(debug = True)
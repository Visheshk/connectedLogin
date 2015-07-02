from flask import render_template
from flask import request, jsonify
from app import app

# app.run(port=5001)

@app.route('/getSignIn', methods=['GET','POST'])

def getSignIn():
	list = [
		{'newCheckin': 'true'}
		]
	return jsonify(list)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index(): 
	print "starting"
	if request.method == 'POST':
		# print(request.data)

		location = {'mspace': 'Central Library'} 
		user = {'nickname': request.args.get('name')}
		print "works!"
		print user['nickname']
		return render_template('index.html',
                    location = location,
                    user = user) 
	return render_template('index.html', 
							location = "test", 
							user = 'user')

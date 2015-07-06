from flask import render_template
from flask import Flask, request, jsonify, session
from app import app

# app.run(port=5001)

checkCheck = False

@app.route('/getSignIn', methods=['GET','POST'])
def getSignIn():
	global checkCheck
	list = {'newCheckin': checkCheck}
	checkCheck = False
	return jsonify(list)

@app.route('/activity', methods=['GET', 'POST'])
def activity():
	print session.get('var')
	user = session.get('var')
	location = {'mspace': 'Central Library'} 
	return render_template('activity.html',
							location = location,
							user = user)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(): 
	global checkCheck
	print "starting"
	if request.method == 'POST':
		# print(request.data)
		checkCheck = True
		location = {'mspace': 'Central Library'} 
		user = {'nickname': request.args.get('name')}
		session['var'] = request.args.get('name')
		print user
		print session['var']
		print session.get('var')
		return render_template('index.html',
                    location = location,
                    user = user) 

	return render_template('index.html', 
							location = "test", 
							user = 'user')

app.secret_key = 'you-will-never-guess'
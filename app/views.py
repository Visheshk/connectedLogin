from flask import render_template
from flask import Flask, request, jsonify, session, redirect, url_for
from app import app
import requests

# app.run(port=5001)

checkCheck = False

userIdentifier = ""

memberID = ""

#global isMember

@app.route('/getSignIn', methods=['GET','POST'])
def getSignIn():
	global checkCheck
	global userIdentifier
	global memberID
	if(checkCheck == True):
		print "Sending confirmation for check in";
	list = {'newCheckin': checkCheck, 'memberID' : memberID, 'name' : userIdentifier}
	checkCheck = False
	return jsonify(list)

@app.route('/activity', methods=['GET', 'POST'])
def activity():
	print "It worked"
	# global userIdentifier
	user = "userIdentifier"
	location = {'mspace': 'Central Library'} 
	return render_template('activity.html',
							location = location,
							user = user)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	print "It worked"
	# global isMember
	return render_template('signup.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(): 
	global checkCheck
	global userIdentifier
	print "starting"
	location = {'mspace': 'Central Library'} 
	if request.method == 'POST':
		global userIdentifier
		global isMember
		global memberID
		checkCheck = True
		member = {'memberID': request.form['cardID']}
		memberID = request.form['cardID']
		print member
		q = requests.post("https://hidden-springs-6751.herokuapp.com/login.json", data=member)
		print q.text
		isMember = q.json()["MemberExists"]
		print isMember
		userIdentifier = q.json()["MemberName"]

		if isMember == False:
			#do stuff for a new member
			print "YEAH"
			print userIdentifier

		else:
			#do stuff for a recurring member
			print "Noooooo"

		return render_template('index.html',
                    location = location,
                    user = member
                    ) 
		# jsonify(isMember=isMember)
		
				

	return render_template('index.html', 
							location = location, 
							user = 'user')

app.secret_key = 'you-will-never-guess'

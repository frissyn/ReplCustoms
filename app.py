import os
import sys
import asyncio
import repltalk
from forms import SearchDatabase
from flask import Flask, render_template, request

async def get_user_object(name):
	global user, posts, result, comments
	replit = repltalk.Client()
	try:
		user = await replit.get_user(name)
		posts = await user.get_posts(order='new')
		comments = await user.get_comments(order='new')
	except Exception as e:
		result = str(e)
		user, posts, comments = None, None, None
		return

KEY = os.getenv('APP_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Home')

@app.route('/license')
def license():
    return render_template('license.html', title='License')

@app.route('/app', methods=['GET', 'POST'])
def application():
	form = SearchDatabase(request.form)
	if request.method == 'POST':
		query = request.form['searchData']
		key = request.form.get('searchType')
		if key == '2':
			asyncio.run(get_user_object(str(query)))
			try:
				s = user.subscription
				timestamp = str(user.timestamp).split(' ')[0]
				if str(s) == 'None': sub = 'Starter'
				elif str(s) == 'hacker': sub = 'Hacker'
				else: sub = 'Not Found'
				return render_template('user-output.html', title='Results',
										user=user, posts=posts, comments=comments,
										sub=sub, timestamp=timestamp)
			except Exception:
				ex_type, ex, tb = sys.exc_info()
				return f"""
					<b>REPL CUSTOMS - ERROR MESSAGE</b><br><br>
					Either the user was not found, or another error has occured.
					<br><br><br>
					Error Stack: <br>
					<b>{str(ex_type)}</b><br>
					{str(tb)}<br>
					{str(ex)}"""
	return render_template('app.html', title='Search', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

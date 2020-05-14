import os
import sys
import asyncio
import repltalk
from forms import SearchDatabase
from flask import Flask, render_template, request

def log_error(a, b, c, d):
	errTemplate = """
Error Occured - {0}

Type: {1}
Exception: {2}
Traceback:
{3}
"""
	with open('Repl-Customs/logs/err_log.txt', 'w') as fh:
		res = errTemplate.format(a, b, c, d)
		fh.write(res)

async def get_user_object(name):
	global user, posts, result, comments
	replit = repltalk.Client()

	try:
		user = await replit.get_user(name)
	except Exception as e:
		user = None
		ex_type, ex, tb = sys.exc_info()
		log_error(e, ex_type, ex, tb)

	try:
		posts = await user.get_posts(limit=5, order='new')
	except Exception as e:
		posts = None
		ex_type, ex, tb = sys.exc_info()
		log_error(e, ex_type, ex, tb)

	try:
		comments = await user.get_comments(limit=5, order='new')
	except Exception as e:
		comments = None
		ex_type, ex, tb = sys.exc_info()
		log_error(e, ex_type, ex, tb)

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
			str(query).replace('@', '', 1)
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
			except:
				ex_type, ex, tb = sys.exc_info()
				return f"""
					<b>REPL CUSTOMS - ERROR MESSAGE</b><br><br>
					Either the user was not found, or another error has occured.
					<br><br><br>
					Error Stack: <br>
					<b>{str(ex_type).replace('<', '').replace('>', '')}</b><br>
					{str(tb)}<br>
					{str(ex).replace('<', '').replace('>', '')}"""
	return render_template('app.html', title='Search', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

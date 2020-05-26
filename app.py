import os
import sys
import asyncio
import repltalk
from datetime import datetime
from forms import SearchReplit
from rctools import log_error, get_ordinal
from flask import Flask, render_template, request


cache = {}

now = datetime.now()
cur_time = now.strftime("%H:%M:%S")

cache_time = 120

def remove_key(name,e):
  global cache
  time.sleep(cache_time)
  try:
    del cache[name]
  except:
    return
async def get_user_object(name):
	global user, posts, result, comments, cache
	replit = repltalk.Client()
	if(name in cache.keys()):
	  cached =  cache.get(name)
	  print('used cache')
	  user = cached.get('user')
	  posts = cached.get('posts')
	  comments = cached.get('comments')
	else:
	  try:
		  user = await replit.get_user(name)
		  print('requested info')
	  except Exception as e:
		  user = None
		  ex_type, ex, tb = sys.exc_info()
		  log_error(e, ex_type, ex, tb, cur_time)
	  try:
	    posts = await user.get_posts(limit=5, order='new')
	  except Exception as e:
	  	posts = None
	  	ex_type, ex, tb = sys.exc_info()
	  	log_error(e, ex_type, ex, tb, cur_time)
	  try:
	  	comments = await user.get_comments(limit=5, order='new')
	  except Exception as e:
	    comments = None
	    ex_type, ex, tb = sys.exc_info()
	    log_error(e, ex_type, ex, tb, cur_time)
	  temp = {'user':user,'posts':posts,'comments':comments}
	  cache[name]=temp
	  threading.Thread(None,remove_key,args=(name,0)).start()

async def get_post_by_query(query):
	global posts_res
	posts_res = []
	replit = repltalk.Client()
	async for post in replit.boards.all.get_posts(sort='top', search=str(query)):
		posts_res.append(post)

async def get_talk_leaderboard(lim=50):
	global lboard
	replit = repltalk.Client()
	lboard = await replit.get_leaderboard(limit=lim)

KEY = os.getenv('APP_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Home')

@app.errorhandler(404) # Added and under construction by [@adityaru]
def error(e):
    """Handle errors. [@adityaru]"""
    return render_template('404.html', title='404 Error'), 404

@app.route('/license')
def license():
    return render_template('license.html', title='License & Legal Info')

@app.route('/apps') # Working app page. Contains all app functions for Repl-Customs. [@IreTheKID]
def apps():
	return render_template('apps.html', title='Apps')

@app.route('/lboard')
@app.route('/leaderboard')
def leaderboard():
	asyncio.run(get_talk_leaderboard(40))
	return render_template('app.html', output='LEADER',title='Leaderboard', 
							leaderboard=lboard, enumerate=enumerate,
							get_ordinal=get_ordinal)

@app.route('/app', methods=['GET', 'POST'])
def application():
	form = SearchReplit()
	sType = request.args.get('searchType')
	sData = request.args.get('searchData')
	if sType and sData:
		if sType == '3':
			global posts_res
			try:
				asyncio.run(get_post_by_query(str(sData)))
				return render_template('app.html', output='POST', title='Results', 
										posts=posts_res, sData=sData, str=str)
			except IndexError:
				posts_res = None
				return render_template('app.html', output='POST', title='Results', 
										posts=posts_res, sData=sData, str=str)
		elif sType == '2':
			asyncio.run(get_user_object(str(sData.replace('@', '', 1))))
			try:
				s = user.subscription
				timestamp = str(user.timestamp).split(' ')[0]
				if str(s) == 'None': sub = 'Starter'
				elif str(s) == 'hacker': sub = 'Hacker'
				else: sub = 'Not Found'
			except AttributeError:
				return render_template('error.html', title='Error Occured', 
										error="UserNotFound", context='From search page.',
										sData=sData)
			except Exception as e:
				ex_type, ex, tb = sys.exc_info()
				log_error(e, ex_type, ex, tb, cur_time)
				return None

			return render_template('app.html', output='USER', title='Results',
									user=user, posts=posts, comments=comments,
									sub=sub, timestamp=timestamp)

	return render_template('app.html', output='FORM', title='Search', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

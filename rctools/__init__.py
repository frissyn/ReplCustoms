def log_error(a, b, c, d, e):
	errTemplate = """
Error Occured - {0}
	Type: {1}
	Exception: {2}
	Traceback:
	{3}

	Time Logged: {4}

	"""
	with open('Repl-Customs/logs/err_log.txt', 'a') as fh:
		res = errTemplate.format(a, b, c, d, e)
		fh.write(res)

def get_ordinal(num):
	if str(num)[-1] == '1':
		ordinal = 'st'	
		if len(str(num)) > 1: ordinal = 'th'
	elif str(num)[-1] == '2':
		ordinal = 'nd'
	elif str(num)[-1] == '3':
		ordinal = 'rd'
	else:
		ordinal = 'th'
	res = str(num) + ordinal

	return res
# Debug Algorithms

# restore
def restore(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		engine.throw('Restore cannot be used in run mode')
	else:
		engine.run_status = 'run'

# error
def error(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return

	error_message = args[0] if len(args) > 0 else "Unknown Error"
	
	engine.throw(error_message)

# warn
def warn(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return
	
	warn_message = args[0] if len(args) > 0 else "Unknown Warning"
	
	engine.throw(warn_message, type="WARN")
	engine.run_status = 'run'


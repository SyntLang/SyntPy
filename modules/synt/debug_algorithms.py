# Debug Algorithms

# restore
def restore(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		self.throw('Restore cannot be used in run mode')
	else:
		self.run_status = 'run'

# error
def error(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return

	error_message = args[0] if len(args) > 0 else "Unknown Error"
	
	self.throw(error_message)

# warn
def warn(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	warn_message = args[0] if len(args) > 0 else "Unknown Warning"
	
	self.throw(warn_message, type="WARN")
	self.run_status = 'run'


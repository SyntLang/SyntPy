# tick Algorithms

# modules
import time

# reset tick
def reset_tick(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# reset tick
	self.tick = 0
	self.last_tick = time.time()

# pause tick
def pause_tick(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# update tick
	self.tick = time.time() - self.last_tick
	
	# pause tick
	self.tick_paused = True

# resume tick
def resume_tick(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# update tick
	self.last_tick = time.time()

	# resume tick
	self.tick_paused = False

# get tick
def get_tick(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return

	# update tick
	if not(self.tick_paused):
		self.tick = time.time() - self.last_tick
	
	# output variable
	output_variable = args[0] if len(args) > 0 else None

	# throw error if output variable is not defined
	if output_variable is None:
		self.throw("Output variable not found")
	
	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"type": "decimal",
		"value": self.tick * 1000
	}

	# set output variable
	self.variables.update({output_variable : output_variable_data})


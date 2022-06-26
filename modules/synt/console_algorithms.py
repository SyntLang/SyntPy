# Console Algorithms

# modules
import os

# clear
def clear(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# check if running command prompt
	if self.cmd:
		os.system("cls")
	else:
		self.throw("Console functions are only available in command prompt")

# console
def console(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# input value
	input_value = args[0] if len(args) > 0 else ""
	
	# execute
	os.system(input_value)


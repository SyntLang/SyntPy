# File Algorithms

# modules
import os

# read
def read(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# input output values
	output_variable = args[0] if len(args) > 0 else None
	input_value = args[1] if len(args) > 1 else None

	# check if input value is valid
	if input_value == None:
		self.throw("Input value not found")
	
	# execute
	read_data = ""
	if os.path.isfile(input_value):
		with open(input_value, "r") as read_file:
			read_data = read_file.read()
	else:
		self.throw(f"File not found: {input_value}")
	
	# check run status
	if self.run_status == "run":
		pass
	else:
		return
	
	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"type": "text",
		"value": read_data
	}

	# set output variable
	self.variables.update({output_variable : output_variable_data})

# write
def write(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# input output values
	file_path = args[0] if len(args) > 0 else None
	file_data = args[1] if len(args) > 1 else ""

	# check if input value is valid
	if file_path == None:
		self.throw("Input value not found")
	
	# execute
	with open(file_path, "w") as write_file:
		write_file.write(file_data)


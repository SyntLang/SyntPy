# Basic Synt Algorithms

# version
def version(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return
	
	print(f"Running Synt Engine v{engine.ver}")

# comment
def comment(engine, *args):
	pass

# output
def output(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return

	output_data = args[0] if len(args) > 0 else ''
	
	print(output_data)

# input
def input_function(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return
	
	# get output
	output_variable = args[0] if len(args) > 0 else None
	output_value_type = "text"
	output_value = 0

	# input statement
	input_statement = args[1] if len(args) > 1 else ""

	# throw error if output variable is not defined
	if output_variable is None:
		engine.throw("Output variable not found")
	
	# take input
	input_value = input(input_statement)

	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"type": output_value_type,
		"value": input_value
	}

	# set output variable
	engine.variables.update({output_variable : output_variable_data})

# end
def end(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return
	
	engine.run_status = 'break'


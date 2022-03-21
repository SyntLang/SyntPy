# Logic Algorithms

# condition
def condition(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return
	
	# inputs
	output_variable = args[0] if len(args) > 0 else None
	operator = args[2] if len(args) > 1 else None
	input_variables = [args[1], args[3]] if len(args) > 3 else None

	# functions
	true_function = "NOT NONE"
	false_function = "NOT NONE"

	# output
	output_value = 0
	output_value_type = "bin"

	# throw error if output variable is not defined
	if output_variable is None:
		engine.throw("Output variable not found")

	# throw error if operator is not defined
	if operator is None:
		engine.throw("operator not found")
	
	# throw error if input variables are not defined
	if input_variables is None:
		engine.throw("Input variables not found")
	
	# operators
	operators = [
		"equals to",
		"not equals to",
		"greater than",
		"less than",
		"greater than equal to",
		"less than equal to",
		"contains",
		"does not contain",
		"starts with",
		"does not start with",
		"ends with",
		"does not end with",

		"=",
		"!=",
		">",
		"<",
		">=",
		"<=",
		"<-",
		"!<-",
		"_%",
		"!_%",
		"%_",
		"!%_",
	]

	# throw error if operator is not valid
	if operator not in operators:
		engine.throw(f"Invalid operator: {operator}")

	# throw error if algorithms are not defined
	if true_function is None:
		engine.throw("True function not found")
	else:
		# prepare input variables
		if engine.value_type(input_variables[0]) == "decimal":
			if float(input_variables[0]) == int(float(input_variables[0])):
				input_variables[0] = int(float(input_variables[0]))
		if engine.value_type(input_variables[1]) == "decimal":
			if float(input_variables[1]) == int(float(input_variables[1])):
				input_variables[1] = int(float(input_variables[1]))
		if engine.value_type(input_variables[0]) == "binary":
			input_variables[0] = 0 if input_variables[0] == "off" else 1
		if engine.value_type(input_variables[1]) == "binary":
			input_variables[1] = 0 if input_variables[1] == "off" else 1
		input_variables[0] = str(input_variables[0])
		input_variables[1] = str(input_variables[1])

		# compare input variable
		if operator == "equals to" or operator == "=":
			if input_variables[0] == input_variables[1]:
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator == "not equals to" or operator == "!=":
			if input_variables[0] != input_variables[1]:
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator == "greater than" or operator == ">":
			if engine.value_type(input_variables[0]) == "number":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif engine.value_type(input_variables[0]) == "decimal":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif engine.value_type(input_variables[0]) == "text":
				if engine.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) > len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
		elif operator == "less than" or operator == "<":
			if engine.value_type(input_variables[0]) == "number":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif engine.value_type(input_variables[0]) == "decimal":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif engine.value_type(input_variables[0]) == "text":
				if engine.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) < len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
		elif operator == "greater than equal to" or operator == ">=":
			if engine.value_type(input_variables[0]) == "number":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif engine.value_type(input_variables[0]) == "decimal":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif engine.value_type(input_variables[0]) == "text":
				if engine.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) > len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
		elif operator == "less than equal to" or operator == "<=":
			if engine.value_type(input_variables[0]) == "number":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif engine.value_type(input_variables[0]) == "decimal":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif engine.value_type(input_variables[0]) == "text":
				if engine.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif engine.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) < len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
		elif operator == "contains" or operator == "<-":
			if str(input_variables[1]) in str(input_variables[0]):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator == "does not contain" or operator == "!<-":
			if str(input_variables[1]) not in str(input_variables[0]):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator == "starts with" or operator == "_%":
			if str(input_variables[0]).startswith(str(input_variables[1])):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator == "does not start with" or operator == "!_%":
			if not(str(input_variables[0]).startswith(str(input_variables[1]))):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator == "ends with" or operator == "%_":
			if str(input_variables[0]).endswith(str(input_variables[1])):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator == "does not end with" or operator == "!%_":
			if not(str(input_variables[0]).endswith(str(input_variables[1]))):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
	
	# convert to binary
	if output_value:
		output_value = "on"
	else:
		output_value = "off"
	
	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"value": output_value,
		"type": output_value_type
	}

	# update output variable
	engine.update_variable(output_variable_data)

# check
def check(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return
	
	# inputs
	condition = args[1] if len(args) > 0 else None
	input_variables = [args[0], args[2]] if len(args) > 2 else None
	true_function = args[3] if len(args) > 3 else None
	false_function = args[4] if len(args) > 4 else None

	# throw error if condition is not defined
	if condition is None:
		engine.throw("Condition not found")
	
	# throw error if input variables are not defined
	if input_variables is None:
		engine.throw("Input variables not found")
	
	# conditions
	conditions = [
		"equals to",
		"not equals to",
		"greater than",
		"less than",
		"greater than equal to",
		"less than equal to",
		"contains",
		"does not contain",
		"starts with",
		"does not start with",
		"ends with",
		"does not end with",

		"=",
		"!=",
		">",
		"<",
		">=",
		"<=",
		"<-",
		"!<-",
		"_%",
		"!_%",
		"%_",
		"!%_",
	]

	# throw error if condition is not valid
	if condition not in conditions:
		engine.throw(f"Invalid condition: {condition}")

	# throw error if algorithms are not defined
	if true_function is None:
		engine.throw("True function not found")
	else:
		# prepare input variables
		if engine.value_type(input_variables[0]) == "decimal":
			if float(input_variables[0]) == int(float(input_variables[0])):
				input_variables[0] = int(float(input_variables[0]))
		if engine.value_type(input_variables[1]) == "decimal":
			if float(input_variables[1]) == int(float(input_variables[1])):
				input_variables[1] = int(float(input_variables[1]))
		if engine.value_type(input_variables[0]) == "binary":
			input_variables[0] = 0 if input_variables[0] == "off" else 1
		if engine.value_type(input_variables[1]) == "binary":
			input_variables[1] = 0 if input_variables[1] == "off" else 1
		input_variables[0] = str(input_variables[0])
		input_variables[1] = str(input_variables[1])

		# compare input variable
		if condition == "equals to" or condition == "=":
			if input_variables[0] == input_variables[1]:
				engine.run_algorithm(true_function)
			else:
				if false_function is not None:
					engine.run_algorithm(false_function)
		elif condition == "not equals to" or condition == "!=":
			if input_variables[0] != input_variables[1]:
				engine.run_algorithm(true_function)
			else:
				if false_function is not None:
					engine.run_algorithm(false_function)
		elif condition == "greater than" or condition == ">":
			if engine.value_type(input_variables[0]) == "number":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
			elif engine.value_type(input_variables[0]) == "decimal":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
			elif engine.value_type(input_variables[0]) == "text":
				if engine.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) > len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
		elif condition == "less than" or condition == "<":
			if engine.value_type(input_variables[0]) == "number":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
			elif engine.value_type(input_variables[0]) == "decimal":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
			elif engine.value_type(input_variables[0]) == "text":
				if engine.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) < len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
		elif condition == "greater than equal to" or condition == ">=":
			if engine.value_type(input_variables[0]) == "number":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
			elif engine.value_type(input_variables[0]) == "decimal":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
			elif engine.value_type(input_variables[0]) == "text":
				if engine.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) > float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) > len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
		elif condition == "less than equal to" or condition == "<=":
			if engine.value_type(input_variables[0]) == "number":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
			elif engine.value_type(input_variables[0]) == "decimal":
				if engine.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
			elif engine.value_type(input_variables[0]) == "text":
				if engine.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) < float(input_variables[1]):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
				elif engine.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) < len(str(input_variables[1])):
						engine.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						engine.run_algorithm(true_function)
					else:
						if false_function is not None:
							engine.run_algorithm(false_function)
		elif condition == "contains" or condition == "<-":
			if str(input_variables[1]) in str(input_variables[0]):
				engine.run_algorithm(true_function)
			else:
				if false_function is not None:
					engine.run_algorithm(false_function)
		elif condition == "does not contain" or condition == "!<-":
			if str(input_variables[1]) not in str(input_variables[0]):
				engine.run_algorithm(true_function)
			else:
				if false_function is not None:
					engine.run_algorithm(false_function)
		elif condition == "starts with" or condition == "_%":
			if str(input_variables[0]).startswith(str(input_variables[1])):
				engine.run_algorithm(true_function)
			else:
				if false_function is not None:
					engine.run_algorithm(false_function)
		elif condition == "does not start with" or condition == "!_%":
			if not(str(input_variables[0]).startswith(str(input_variables[1]))):
				engine.run_algorithm(true_function)
			else:
				if false_function is not None:
					engine.run_algorithm(false_function)
		elif condition == "ends with" or condition == "%_":
			if str(input_variables[0]).endswith(str(input_variables[1])):
				engine.run_algorithm(true_function)
			else:
				if false_function is not None:
					engine.run_algorithm(false_function)
		elif condition == "does not end with" or condition == "!%_":
			if not(str(input_variables[0]).endswith(str(input_variables[1]))):
				engine.run_algorithm(true_function)
			else:
				if false_function is not None:
					engine.run_algorithm(false_function)


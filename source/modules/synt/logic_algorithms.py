# Logic Algorithms

# condition
def condition(self, *args):
	# check if run_status is run
	if self.run_status == "run":
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
		self.throw("Output variable not found")

	# throw error if operator is not defined
	if operator is None:
		self.throw("operator not found")
	
	# throw error if input variables are not defined
	if input_variables is None:
		self.throw("Input variables not found")
	
	# operators
	operators = self.logic_operators

	# throw error if algorithms are not defined
	if true_function is None:
		self.throw("True function not found")
	else:
		# prepare input variables
		if self.value_type(input_variables[0]) == "decimal":
			if float(input_variables[0]) == int(float(input_variables[0])):
				input_variables[0] = int(float(input_variables[0]))
		if self.value_type(input_variables[1]) == "decimal":
			if float(input_variables[1]) == int(float(input_variables[1])):
				input_variables[1] = int(float(input_variables[1]))
		if self.value_type(input_variables[0]) == "binary":
			input_variables[0] = 0 if input_variables[0] == "off" else 1
		if self.value_type(input_variables[1]) == "binary":
			input_variables[1] = 0 if input_variables[1] == "off" else 1
		input_variables[0] = str(input_variables[0])
		input_variables[1] = str(input_variables[1])

		# compare input variable
		if operator in operators["="]:
			if input_variables[0] == input_variables[1]:
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator in operators["!="]:
			if input_variables[0] != input_variables[1]:
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator in operators[">"]:
			if self.value_type(input_variables[0]) == "number":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif self.value_type(input_variables[0]) == "decimal":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif self.value_type(input_variables[0]) == "text":
				if self.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) > float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) > len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
		elif operator in operators["<"]:
			if self.value_type(input_variables[0]) == "number":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif self.value_type(input_variables[0]) == "decimal":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif self.value_type(input_variables[0]) == "text":
				if self.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) < float(input_variables[1]):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) < len(str(input_variables[1])):
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
		elif operator in operators[">="]:
			if self.value_type(input_variables[0]) == "number":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif self.value_type(input_variables[0]) == "decimal":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif self.value_type(input_variables[0]) == "text":
				if self.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) > float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) > len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
		elif operator in operators["<="]:
			if self.value_type(input_variables[0]) == "number":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif self.value_type(input_variables[0]) == "decimal":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
			elif self.value_type(input_variables[0]) == "text":
				if self.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) < float(input_variables[1]):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
				elif self.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) < len(str(input_variables[1])):
						output_value = 1
					elif input_variables[0] == input_variables[1]:
						output_value = 1
					else:
						if false_function is not None:
							output_value = 0
		elif operator in operators["<-"]:
			if str(input_variables[1]) in str(input_variables[0]):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator in operators["!<-"]:
			if str(input_variables[1]) not in str(input_variables[0]):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator in operators["_%"]:
			if str(input_variables[0]).startswith(str(input_variables[1])):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator in operators["!_%"]:
			if not(str(input_variables[0]).startswith(str(input_variables[1]))):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator in operators["%_"]:
			if str(input_variables[0]).endswith(str(input_variables[1])):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		elif operator in operators["!%_"]:
			if not(str(input_variables[0]).endswith(str(input_variables[1]))):
				output_value = 1
			else:
				if false_function is not None:
					output_value = 0
		else:
			self.throw(f"Invalid operator: {operator}")
	
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
	self.update_variable(output_variable_data)

# check
def check(self, *args):
	# check if run_status is run
	if self.run_status == "run":
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
		self.throw("Condition not found")
	
	# throw error if input variables are not defined
	if input_variables is None:
		self.throw("Input variables not found")
	
	# conditions
	operators = self.logic_operators
	conditions = operators

	# throw error if algorithms are not defined
	if true_function is None:
		self.throw("True function not found")
	else:
		# prepare input variables
		if self.value_type(input_variables[0]) == "decimal":
			if float(input_variables[0]) == int(float(input_variables[0])):
				input_variables[0] = int(float(input_variables[0]))
		if self.value_type(input_variables[1]) == "decimal":
			if float(input_variables[1]) == int(float(input_variables[1])):
				input_variables[1] = int(float(input_variables[1]))
		if self.value_type(input_variables[0]) == "binary":
			input_variables[0] = 0 if input_variables[0] == "off" else 1
		if self.value_type(input_variables[1]) == "binary":
			input_variables[1] = 0 if input_variables[1] == "off" else 1
		input_variables[0] = str(input_variables[0])
		input_variables[1] = str(input_variables[1])

		# compare input variable
		if condition in operators["="]:
			if input_variables[0] == input_variables[1]:
				self.run_algorithm(true_function)
			else:
				if false_function is not None:
					self.run_algorithm(false_function)
		elif condition in operators["!="]:
			if input_variables[0] != input_variables[1]:
				self.run_algorithm(true_function)
			else:
				if false_function is not None:
					self.run_algorithm(false_function)
		elif condition in operators[">"]:
			if self.value_type(input_variables[0]) == "number":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
			elif self.value_type(input_variables[0]) == "decimal":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
			elif self.value_type(input_variables[0]) == "text":
				if self.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) > float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) > float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) > len(str(input_variables[1])):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
		elif condition in operators["<"]:
			if self.value_type(input_variables[0]) == "number":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
			elif self.value_type(input_variables[0]) == "decimal":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
			elif self.value_type(input_variables[0]) == "text":
				if self.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) < float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) < float(input_variables[1]):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) < len(str(input_variables[1])):
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
		elif condition in operators[">="]:
			if self.value_type(input_variables[0]) == "number":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
			elif self.value_type(input_variables[0]) == "decimal":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) > float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) > float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) > len(str(input_variables[1])):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
			elif self.value_type(input_variables[0]) == "text":
				if self.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) > float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) > float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) > len(str(input_variables[1])):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
		elif condition in operators["<="]:
			if self.value_type(input_variables[0]) == "number":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
			elif self.value_type(input_variables[0]) == "decimal":
				if self.value_type(input_variables[1]) == "number":
					if float(input_variables[0]) < float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if float(input_variables[0]) < float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if float(input_variables[0]) < len(str(input_variables[1])):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
			elif self.value_type(input_variables[0]) == "text":
				if self.value_type(input_variables[1]) == "number":
					if len(str(input_variables[0])) < float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "decimal":
					if len(str(input_variables[0])) < float(input_variables[1]):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
				elif self.value_type(input_variables[1]) == "text":
					if len(str(input_variables[0])) < len(str(input_variables[1])):
						self.run_algorithm(true_function)
					elif input_variables[0] == input_variables[1]:
						self.run_algorithm(true_function)
					else:
						if false_function is not None:
							self.run_algorithm(false_function)
		elif condition in operators["<-"]:
			if str(input_variables[1]) in str(input_variables[0]):
				self.run_algorithm(true_function)
			else:
				if false_function is not None:
					self.run_algorithm(false_function)
		elif condition in operators["!<-"]:
			if str(input_variables[1]) not in str(input_variables[0]):
				self.run_algorithm(true_function)
			else:
				if false_function is not None:
					self.run_algorithm(false_function)
		elif condition in operators["_%"]:
			if str(input_variables[0]).startswith(str(input_variables[1])):
				self.run_algorithm(true_function)
			else:
				if false_function is not None:
					self.run_algorithm(false_function)
		elif condition in operators["!_%"]:
			if not(str(input_variables[0]).startswith(str(input_variables[1]))):
				self.run_algorithm(true_function)
			else:
				if false_function is not None:
					self.run_algorithm(false_function)
		elif condition in operators["%_"]:
			if str(input_variables[0]).endswith(str(input_variables[1])):
				self.run_algorithm(true_function)
			else:
				if false_function is not None:
					self.run_algorithm(false_function)
		elif condition in operators["!%_"]:
			if not(str(input_variables[0]).endswith(str(input_variables[1]))):
				self.run_algorithm(true_function)
			else:
				if false_function is not None:
					self.run_algorithm(false_function)
		else:
			self.throw(f"Invalid condition: {condition}")


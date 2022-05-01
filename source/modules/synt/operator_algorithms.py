# Operator Algorithms

# add
def add(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get output
	output_variable = args[0] if len(args) > 0 else None
	output_value_type = "number"
	output_value = 0

	# throw error if output variable is not defined
	if output_variable is None:
		self.throw("Output variable not found")
	
	# get input variables
	input_variables = args[1:] if len(args) > 1 else []

	# throw error if input variables are not defined
	if len(input_variables) == 0:
		self.throw("Input variables not found")
	
	# decimal error fix
	decimal_length = 0
	
	# check if any string or decimal is in input variables
	fixed_input_variables = []
	for input_variable in input_variables:
		append_val = input_variable
		if self.value_type(input_variable) == "binary":
			append_val = "0" if input_variable == "off" else "1"
		if self.value_type(input_variable) == "text" and append_val not in "01":
			output_value_type = "text"
			break
		if self.value_type(input_variable) == "nothing":
			output_value_type = "text"
			break
		if self.value_type(input_variable) == "decimal":
			output_value_type = "decimal"
			if len(str(input_variable).split('.')[1]) > decimal_length:
				decimal_length = len(input_variable.split('.')[1])
		fixed_input_variables.append(append_val)
	
	# fix input variables
	if output_value_type != "text":
		input_variables = fixed_input_variables
	
	# set initial output value
	if output_value_type == "number":
		output_value = 0
	elif output_value_type == "decimal":
		output_value = 0.0
	else:
		output_value = ""
	
	# add input variables to output variable
	for value in input_variables:
		if output_value_type == "number":
			output_value += int(value)
		elif output_value_type == "decimal":
			output_value += float(value)
		else:
			output_value += str(value)
	
	# fix decimal errors
	if output_value_type == "decimal":
		if len(str(output_value).split('.')[1]) > decimal_length:
			# split decimal into integer and decimal
			integral_part = str(output_value).split('.')[0]
			fractional_part = str(output_value).split('.')[1]

			# extra
			buffer = 0
			negative = False if integral_part[0] != '-' else True

			# edit fractional part
			partial_fractional_part = str(int(fractional_part[:decimal_length + 1]))
			if int(fractional_part[decimal_length+1]) > 5:
				buffer = "0." + ("0" * decimal_length) + "1"
				buffer = float(buffer)
				partial_fractional_part = float("0." + partial_fractional_part) + buffer
				buffer = int(str(partial_fractional_part).split('.')[0])
				fractional_part = int(str(partial_fractional_part).split('.')[1])
			else:
				buffer = "0." + ("0" * decimal_length) + "0"
				buffer = float(buffer)
				partial_fractional_part = float("0." + partial_fractional_part) + buffer
				buffer = int(str(partial_fractional_part).split('.')[0])
				fractional_part = int(str(partial_fractional_part).split('.')[1])
			
			# edit integral part
			integral_part = str("-" * negative) + str(int(integral_part) + int(buffer))

			# combine parts
			output_value = str(integral_part) + "." + str(fractional_part)

	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"value": str(output_value)
	}

	# update output variable
	self.update_variable(output_variable_data)

# subtract
def subtract(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get output
	output_variable = args[0] if len(args) > 0 else None
	output_value_type = "number"
	output_value = 0

	# throw error if output variable is not defined
	if output_variable is None:
		self.throw("Output variable not found")
	
	# get input variables
	input_variables = args[1:] if len(args) > 1 else []

	# throw error if input variables are not defined
	if len(input_variables) == 0:
		self.throw("Input variables not found")
	
	# append input variables with respective value types
	text_input_variables = []
	number_input_variables = []

	# put input variables into respective arrays
	for input_variable in input_variables:
		append_val = input_variable
		if self.value_type(input_variable) == "binary":
			value = 0 if input_variable == "off" else 1
			number_input_variables.append(value)
		elif self.value_type(input_variable) == "number":
			number_input_variables.append(int(input_variable))
		elif self.value_type(input_variable) == "decimal":
			number_input_variables.append(float(input_variable))
		elif self.value_type(input_variable) == "nothing":
			number_input_variables.append(0)
		else:
			text_input_variables.append(input_variable)
	
	# check if any string is in input variables
	if len(text_input_variables) > 0:
		output_value = text_input_variables[0]
		for index, input_variable in enumerate(input_variables):
			if index == 0:
				continue
			else:
				output_value = output_value.replace(str(input_variable), "")
	else:
		# numeric difference
		output_value = 0
		for index, input_variable in enumerate(number_input_variables):
			if index == 0:
				output_value += input_variable
			else:
				output_value -= input_variable
	
	# fix decimal errors
	if output_value_type == "decimal":
		if len(str(output_value).split('.')[1]) > decimal_length:
			# split decimal into integer and decimal
			integral_part = str(output_value).split('.')[0]
			fractional_part = str(output_value).split('.')[1]

			# extra
			buffer = 0
			negative = False if integral_part[0] != '-' else True

			# edit fractional part
			partial_fractional_part = str(int(fractional_part[:decimal_length + 1]))
			if int(fractional_part[decimal_length+1]) > 5:
				buffer = "0." + ("0" * decimal_length) + "1"
				buffer = float(buffer)
				partial_fractional_part = float("0." + partial_fractional_part) + buffer
				buffer = int(str(partial_fractional_part).split('.')[0])
				fractional_part = int(str(partial_fractional_part).split('.')[1])
			else:
				buffer = "0." + ("0" * decimal_length) + "0"
				buffer = float(buffer)
				partial_fractional_part = float("0." + partial_fractional_part) + buffer
				buffer = int(str(partial_fractional_part).split('.')[0])
				fractional_part = int(str(partial_fractional_part).split('.')[1])
			
			# edit integral part
			integral_part = str("-" * negative) + str(int(integral_part) + int(buffer))

			# combine parts
			output_value = str(integral_part) + "." + str(fractional_part)

	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"value": str(output_value)
	}

	# update output variable
	self.update_variable(output_variable_data)

# multiply
def multiply(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get output
	output_variable = args[0] if len(args) > 0 else None
	output_value_type = "number"
	output_value = 0

	# throw error if output variable is not defined
	if output_variable is None:
		self.throw("Output variable not found")
	
	# get input variables
	input_variables = args[1:] if len(args) > 1 else []

	# throw error if input variables are not defined
	if len(input_variables) == 0:
		self.throw("Input variables not found")

	# append input variables with respective value types
	text_input_variables = []
	number_input_variables = []
	denominator_input_variables = []

	# put input variables into respective arrays
	for input_variable in input_variables:
		append_val = input_variable
		if self.value_type(input_variable) == "binary":
			value = 0 if input_variable == "off" else 1
			number_input_variables.append(value)
		elif self.value_type(input_variable) == "number":
			number_input_variables.append(input_variable)
		elif self.value_type(input_variable) == "decimal":
			power_of_ten = len(str(input_variable).split('.')[1])
			value = float(input_variable) * (10 ** power_of_ten)
			number_input_variables.append(value)
			denominator_input_variables.append(10 ** power_of_ten)
		else:
			text_input_variables.append(input_variable)
	
	# multiplication for text
	text_output_value = ""
	for text_input_variable in text_input_variables:
		text_output_value += str(text_input_variable)
	
	# multiplication for number
	number_output_value = 1
	for number_input_variable in number_input_variables:
		number_output_value *= int(number_input_variable)
	
	# multiplication for denominator
	denominator_output_value = 1
	for denominator_input_variable in denominator_input_variables:
		denominator_output_value *= denominator_input_variable
	
	# final decimal value for numbers
	output_decimal_value = number_output_value / denominator_output_value

	# output variable
	if text_output_value == "":
		output_value = output_decimal_value
		
		# set output value type
		if int(output_value) == output_value:
			output_value_type = "number"
		else:
			output_value_type = "decimal"
	else:
		repeat_count = int(float(output_decimal_value))
		extra_count = int(len(text_output_value) * (float(str("0." + str(float(output_decimal_value)).split('.')[1]))))
		output_value = str(text_output_value * repeat_count) + str(text_output_value[:extra_count])
		output_value_type = "text"
	
	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"value": str(output_value)
	}

	# update output variable
	self.update_variable(output_variable_data)

# divide
def divide(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get output
	output_variable = args[0] if len(args) > 0 else None
	output_value_type = "number"
	output_value = 0

	# throw error if output variable is not defined
	if output_variable is None:
		self.throw("Output variable not found")
	
	# get input variables
	numerator_variable = args[1] if len(args) > 1 else None
	denominator_variable = args[2] if len(args) > 2 else None

	# throw error if input variables are not defined
	if numerator_variable is None:
		self.throw("Input variables not found: numerator")
	if denominator_variable is None:
		self.throw("Input variables not found: denominator")

	# check numerator variable type
	if self.value_type(numerator_variable) == "binary":
		numerator_variable = {"type": "num", "value": 0} if numerator_variable == "off" else {"type": "num", "value": 1}
	elif self.value_type(numerator_variable) == "number":
		numerator_variable = {"type": "num", "value": int(numerator_variable)}
	elif self.value_type(numerator_variable) == "decimal":
		integral_part = int(str(numerator_variable).split('.')[0])
		fractional_part = int(str(numerator_variable).split('.')[1])
		power_of_ten = len(str(fractional_part))
		integral_value = float(str(integral_part)+str(fractional_part)) * (10 ** power_of_ten)
		numerator_variable = {"type": "decimal", "value": [integral_value, 10 ** power_of_ten]}
	elif self.value_type(numerator_variable) == "nothing":
		numerator_variable = {"type": "num", "value": 0}
	else:
		numerator_variable = {"type": "num", "value": int(len(str(numerator_variable)))}
	
	# check denominator variable type
	if self.value_type(denominator_variable) == "binary":
		denominator_variable = {"type": "num", "value": 0} if denominator_variable == "off" else {"type": "num", "value": 1}
	elif self.value_type(denominator_variable) == "number":
		denominator_variable = {"type": "num", "value": int(denominator_variable)}
	elif self.value_type(denominator_variable) == "decimal":
		integral_part = int(str(denominator_variable).split('.')[0])
		fractional_part = int(str(denominator_variable).split('.')[1])
		power_of_ten = len(str(fractional_part))
		integral_value = float(str(integral_part)+str(fractional_part)) * (10 ** power_of_ten)
		denominator_variable = {"type": "decimal", "value": [integral_value, 10 ** power_of_ten]}
	elif self.value_type(denominator_variable) == "nothing":
		denominator_variable = {"type": "num", "value": 0}
	else:
		denominator_variable = {"type": "num", "value": int(len(str(denominator_variable)))}

	# validate numerator variable
	if numerator_variable["type"] == "text":
		self.throw("Invalid numerator type: text")

	# validate denominator variable
	if denominator_variable["type"] == "text":
		self.throw("Invalid denominator type: text")
	if denominator_variable["type"] == "num" and denominator_variable["value"] == 0:
		self.throw("Invalid denominator value: 0")
	if denominator_variable["type"] == "decimal" and denominator_variable["value"][0] == 0:
		self.throw("Invalid denominator value: 0")
	
	# get output
	if numerator_variable["type"] == "num":
		if denominator_variable["type"] == "num":
			output_value = numerator_variable["value"] / denominator_variable["value"]
		elif denominator_variable["type"] == "decimal":
			output_value = numerator_variable["value"] / denominator_variable["value"][0]
			output_value = output_value / denominator_variable["value"][1]
	elif numerator_variable["type"] == "decimal":
		if denominator_variable["type"] == "num":
			output_value = numerator_variable["value"][0] / denominator_variable["value"]
			output_value = output_value * numerator_variable["value"][1]
		elif denominator_variable["type"] == "decimal":
			output_value = numerator_variable["value"][0] / denominator_variable["value"][0]
			output_value = output_value * numerator_variable["value"][1]
			output_value = output_value / denominator_variable["value"][1]
	
	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"value": str(output_value)
	}

	# update output variable
	self.update_variable(output_variable_data)

# power
def power(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get output
	output_variable = args[0] if len(args) > 0 else None
	output_value_type = "number"
	output_value = 0

	# throw error if output variable is not defined
	if output_variable is None:
		self.throw("Output variable not found")
	
	# get input variables
	base_variable = args[1] if len(args) > 1 else None
	exponent_variable = args[2] if len(args) > 2 else None

	# throw error if input variables are not defined
	if base_variable is None:
		self.throw("Input variables not found: base")
	if exponent_variable is None:
		self.throw("Input variables not found: exponent")

	# check base variable type
	if self.value_type(base_variable) == "binary":
		base_variable = {"type": "num", "value": 0} if base_variable == "off" else {"type": "num", "value": 1}
	elif self.value_type(base_variable) == "number":
		base_variable = {"type": "num", "value": int(base_variable)}
	elif self.value_type(base_variable) == "decimal":
		base_variable = {"type": "decimal", "value": float(base_variable)}
	elif self.value_type(base_variable) == "nothing":
		base_variable = {"type": "num", "value": 0}
	else:
		base_variable = {"type": "text", "value": str(base_variable)}

	# check exponent variable type
	if self.value_type(exponent_variable) == "binary":
		exponent_variable = {"type": "num", "value": 0} if exponent_variable == "off" else {"type": "num", "value": 1}
	elif self.value_type(exponent_variable) == "number":
		exponent_variable = {"type": "num", "value": int(exponent_variable)}
	elif self.value_type(exponent_variable) == "decimal":
		exponent_variable = {"type": "decimal", "value": float(exponent_variable)}
	elif self.value_type(exponent_variable) == "nothing":
		exponent_variable = {"type": "num", "value": 0}
	else:
		exponent_variable = {"type": "num", "value": int(len(str(exponent_variable)))}
	
	# validate base variable
	if base_variable["type"] == "text":
		if exponent_variable["type"] == "decimal":
			base_variable["type"] = "num"
			base_variable["value"] = int(len(str(base_variable["value"])))
	
	# calculate output for text
	if base_variable["type"] == "text":
		output_value = str(base_variable["value"]) * exponent_variable["value"]
		output_value = str(output_value)
		output_value_type = "text"
	else:
		if base_variable["type"] == "num":
			output_value = float(base_variable["value"]) ** float(exponent_variable["value"])
		else:
			if exponent_variable["type"] == "num":
				base_variable["value"] = [int(str(float(base_variable["value"])).replace(".", "")), 10 ** len(str(float(base_variable["value"])).split(".")[1])]
				output_value = base_variable["value"][0] ** exponent_variable["value"]
				output_value = output_value / (base_variable["value"][1] ** exponent_variable["value"])
			else:
				output_value = float(base_variable["value"]) ** float(exponent_variable["value"])
		output_value_type = "number" if int(output_value) == output_value else "decimal"
		if output_value_type == "decimal":
			output_value = str(output_value)
		else:
			output_value = str(int(output_value))
	
	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"value": output_value,
		"type": output_value_type
	}

	# update output variable
	self.update_variable(output_variable_data)

# type
def object_type(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get output variable
	output_variable = args[0] if len(args) > 0 else None

	# throw error if output variable is not defined
	if output_variable is None:
		self.throw("Output variable not found")
	
	# get input variables
	input_variable = args[1] if len(args) > 1 else ''
	
	# get input variable value type
	input_variable_type = self.value_type(input_variable)

	# check if input variable is defined
	if input_variable_type == "collection":
		input_variable_type = "collection"
	elif input_variable in self.variables:
		input_variable_type = self.variables[input_variable]["type"]
	
	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"value": input_variable_type
	}

	# update output variable
	self.update_variable(output_variable_data)


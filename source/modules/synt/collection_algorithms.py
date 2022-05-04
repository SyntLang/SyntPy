# Collection Algorithms

# count
def count(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get data
	output_variable = args[0] if len(args) > 0 else None
	input_variable = args[1] if len(args) > 1 else None
	output_value = 0

	# throw error if output variable is not defined
	if output_variable is None:
		self.throw("Output variable not found")
		return
	
	# throw error if input variable is not defined
	if input_variable is None:
		self.throw("Input variable not found")
		return
	
	# check input variable type
	if input_variable not in self.variables:
		output_value = len(input_variable)
	else:
		# if collection
		if self.variables[input_variable]["type"] == "collection":
			output_value = len(self.variables[input_variable]["value"])
		else:
			output_value = len(str(self.variables[input_variable]["value"]))
	
	# set output variable data
	output_variable_data = {
		"name": output_variable,
		"type": "number",
		"value": output_value
	}

	# set output variable
	self.variables.update({output_variable : output_variable_data})

# push
def insert(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get data
	variable = args[0] if len(args) > 0 else None
	value = args[1] if len(args) > 1 else None
	index = args[2] if len(args) > 2 else None

	# throw error if variable is not defined
	if variable is None:
		self.throw("Variable not found")
		return
	elif variable not in self.variables:
		self.throw(f"Variable not found: {variable}")
		return
	
	# if value is not defined
	if value is None:
		value = ""
	
	# insert value
	if self.variables[variable]["type"] == "collection":
		if index is None:
			self.variables[variable]["value"].append([value])
		else:
			# convert index to int
			if self.value_type(index) == "number":
				index = int(index)
			elif self.value_type(index) == "decimal":
				index = int(index)
			else:
				index = len(index)
			self.variables[variable]["value"].insert(index, [value])
	elif self.variables[variable]["type"] == "text":
		if index is None:
			self.variables[variable]["value"] += value
		else:
			# convert index to int
			if self.value_type(index) == "number":
				index = int(index)
			elif self.value_type(index) == "decimal":
				index = int(index)
			elif self.value_type(index) == "binary":
				index = len(index) - 1
			else:
				index = len(index)
			self.variables[variable]["value"] = self.variables[variable]["value"][:index] + value + self.variables[variable]["value"][index:]
	else:
		self.throw(f"Can not insert value to a {self.variables[variable]['type']}")
		return

# remove
def remove(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get data
	variable = args[0] if len(args) > 0 else None
	value = args[1] if len(args) > 1 else None
	repeat = args[2] if len(args) > 2 else None

	# throw error if variable is not defined
	if variable is None:
		self.throw("Variable not found")
		return
	elif variable not in self.variables:
		self.throw(f"Variable not found: {variable}")
		return
	
	# if value is not defined
	if value is None:
		self.throw("Value not found")
		return
	
	# remove value
	if self.variables[variable]["type"] == "collection":
		values = self.variables[variable]["value"]
		if repeat is None:
			self.variables[variable]["value"] = [x for x in values if x != [value]]
		else:
			self.variables[variable]["value"] = []
			c = 0
			for x in values:
				if x != [value]:
					self.variables[variable]["value"].append(x)
				else:
					c += 1
					if c > int(repeat):
						self.variables[variable]["value"].append(x)
	else:
		if repeat is None:
			self.variables[variable]["value"] = self.variables[variable]["value"].replace(value, "")
		else:
			if self.value_type(repeat) == "number":
				repeat = int(repeat)
			elif self.value_type(repeat) == "decimal":
				repeat = int(repeat)
			elif self.value_type(repeat) == "binary":
				repeat = len(repeat) - 1
			else:
				repeat = len(repeat)
			self.variables[variable]["value"] = self.variables[variable]["value"].replace(value, "", repeat)

# delete
def delete(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get data
	variable = args[0] if len(args) > 0 else None
	index = args[1] if len(args) > 1 else None

	# throw error if variable is not defined
	if variable is None:
		self.throw("Variable not found")
		return
	elif variable not in self.variables:
		self.throw(f"Variable not found: {variable}")
		return
	
	# if index is not defined
	if index is None:
		self.throw("Index not found")
		return
	
	# convert index to int
	if self.value_type(index) == "number":
		index = int(index)
	elif self.value_type(index) == "decimal":
		index = int(index)
	elif self.value_type(index) == "binary":
		index = len(index) - 1
	else:
		index = len(index)

	# exceeding index
	if index > len(self.variables[variable]["value"]) - 1:
		index = len(self.variables[variable]["value"]) - 1
	
	# delete value
	if self.variables[variable]["type"] == "collection":
		del self.variables[variable]["value"][index]
	else:
		self.variables[variable]["value"] = self.variables[variable]["value"][:index] + self.variables[variable]["value"][index + 1:]


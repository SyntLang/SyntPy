# Variable Algorithms

# meta
def meta(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get input data
	meta_name = args[0] if len(args) > 0 else None
	meta_value = args[1] if len(args) > 1 else None

	# validate input data
	if meta_name is None:
		self.throw("Meta name not found")
	if meta_value is None:
		self.throw(f"Meta value not found: {meta_name}")
	
	# set meta data
	self.meta.update({meta_name : meta_value})

# var
def var(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# variable data
	variable_data = {
		"type" : args[0] if len(args) > 0 else None,
		"name" : args[1] if len(args) > 1 else None,
		"value" : args[2] if len(args) > 2 else ""
	}

	# insert variable to self storage
	self.create_variable(variable_data)

# alg
def alg(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return
	
	# get algorithm data
	algorithm_data = {
		"name": args[0] if len(args) > 0 else None,
		"args_name": args[1] if len(args) > 1 else None,
		"data": args[2] if len(args) > 2 else []
	}

	# throw error if algorithm data is not defined
	if algorithm_data["name"] is None:
		self.throw("Algorithm data not found: name")
	
	# append algorithm data to self
	self.script_algorithms.update({
		algorithm_data["name"] : {
			"args_name": algorithm_data["args_name"],
			"data": algorithm_data["data"]
		}
	})

# result
def result(self, *args):
	# check if run_status is run
	if self.run_status == "run":
		pass
	else:
		return

	# get result value and variable name
	result_value = args[0] if len(args) > 0 else ""
	result_variable_name = self.algorithm_output_variable_name_list[-1] if len(self.algorithm_output_variable_name_list) > 0 else None

	# validate result data
	if result_variable_name is None:
		self.throw("Result variable name not found")
		return
	if result_variable_name not in self.variables:
		self.throw(f"Variable does not exist: {result_variable_name}")
		return
	
	# get result data
	result_variable_data = self.variables[result_variable_name]

	# set result data
	self.update_variable({
		"name": result_variable_name,
		"type": result_variable_data["type"],
		"value": result_value
	})
	del self.algorithm_output_variable_name_list[-1]


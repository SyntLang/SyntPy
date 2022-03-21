# Variable Algorithms

# meta
def meta(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return
	
	# get input data
	meta_name = args[0] if len(args) > 0 else None
	meta_value = args[1] if len(args) > 1 else None

	# validate input data
	if meta_name is None:
		engine.throw("Meta name not found")
	if meta_value is None:
		engine.throw(f"Meta value not found: {meta_name}")
	
	# set meta data
	engine.meta.update({meta_name : meta_value})

# var
def var(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return
	
	# variable data
	variable_data = {
		"type" : args[0] if len(args) > 0 else None,
		"name" : args[1] if len(args) > 1 else None,
		"value" : args[2] if len(args) > 2 else ""
	}

	# insert variable to engine storage
	engine.create_variable(variable_data)

# alg
def alg(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
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
		engine.throw("Algorithm data not found: name")
	
	# append algorithm data to engine
	engine.script_algorithms.update({
		algorithm_data["name"] : {
			"args_name": algorithm_data["args_name"],
			"data": algorithm_data["data"]
		}
	})

# result
def result(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return

	# get result value and variable name
	result_value = args[0] if len(args) > 0 else ""
	result_variable_name = engine.algorithm_output_variable_name_list[-1] if len(engine.algorithm_output_variable_name_list) > 0 else None

	# validate result data
	if result_variable_name is None:
		engine.throw("Result variable name not found")
		return
	if result_variable_name not in engine.variables:
		engine.throw(f"Variable does not exist: {result_variable_name}")
		return
	
	# get result data
	result_variable_data = engine.variables[result_variable_name]

	# set result data
	engine.update_variable({
		"name": result_variable_name,
		"type": result_variable_data["type"],
		"value": result_value
	})
	del engine.algorithm_output_variable_name_list[-1]


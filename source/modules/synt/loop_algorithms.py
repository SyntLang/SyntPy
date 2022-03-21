# Loop Algorithms

# repeat
def repeat(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return

	# input
	repeat_count = args[0] if len(args) > 0 else 1
	repeat_function = args[1] if len(args) > 1 else None

	# check if repeat_function is a valid
	if repeat_function is None:
		engine.throw("Repeat Function not found")
	
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return
	
	# validate repeat_count
	if engine.value_type(repeat_count) != "number":
		if engine.value_type(repeat_count) == "decimal":
			repeat_count = float(repeat_count)
		elif engine.value_type(repeat_count) == "text":
			repeat_count = len(repeat_count)
		elif engine.value_type(repeat_count) == "binary":
			repeat_count = 1 if repeat_count == "on" else 0
		else:
			repeat_count = 0
	
	# convert repeat count to int
	repeat_count = int(repeat_count)

	# repeat
	for _ in range(repeat_count):
		engine.run_algorithm(repeat_function)

# loop
def loop(engine, *args):
	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return

	# input
	loop_argument = args[0] if len(args) > 0 else None
	loop_function = args[1] if len(args) > 1 else None

	# check if loop_function is a valid
	if loop_function is None:
		engine.throw("Loop Function not found")

	# check if run_status is run
	if engine.run_status == "run":
		pass
	else:
		return

	# validate loop_argument
	if engine.value_type(loop_argument) != "number":
		if engine.value_type(loop_argument) == "decimal":
			loop_argument = float(loop_argument)
		elif engine.value_type(loop_argument) == "text":
			loop_argument = len(loop_argument)
		elif engine.value_type(loop_argument) == "binary":
			loop_argument = 1 if loop_argument == "on" else 0
		else:
			loop_argument = 0

	# convert loop argument to int
	loop_argument = int(loop_argument)

	# loop
	if loop_argument:
		engine.run_algorithm(loop_function)
		engine.run_token_id -= 1
	else:
		pass


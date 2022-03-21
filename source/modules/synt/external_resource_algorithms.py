# External Resource Algorithms

# modules
import os

# module
def module(engine, *args):
	# get module name
	module_name = str(args[0]) + '.synt' if len(args) > 0 else None

	# validate file path
	if module_name is None:
		engine.throw(f"Module not found")
	else:
		# get module meta path
		module_path = engine.meta["MODULES_PATH"] if "MODULES_PATH" in engine.meta else None
		
		# validate module path
		if module_path is None:
			engine.run_algorithm("warn", ['"Modules Path(META:#QUOTEMODULES_PATH#QUOTE) not found, setting to #QUOTE.#QUOTE(Engine Directory)"'])
			module_path = "."
			engine.meta["MODULES_PATH"] = module_path
		
		# get module file path
		module_file_path = os.path.join(module_path, module_name)
		
		# validate module file path
		if not os.path.exists(module_file_path):
			engine.throw(f'Module not found: "{".".join(module_name.split(".")[:-1])}" ({module_file_path})')
		else:
			# run module
			with open(module_file_path, 'r') as module_file:
				# get module code
				module_code = module_file.read()
				engine.module_run_token_id = 0

				# tokenize code
				tokens = engine.tokenize(module_code)

				# iteration
				while engine.module_run_token_id < len(tokens):
					# token data
					token = tokens[engine.module_run_token_id]
					
					# run algorithm
					try:
						engine.run(token)
					except Exception as UnknownError:
						engine.throw(str(UnknownError))
					
					# update token id
					engine.module_run_token_id += 1


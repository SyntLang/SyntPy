# External Resource Algorithms

# modules
import os

# module
def module(self, *args):
	# get module name
	module_name = str(args[0]) + '.synt' if len(args) > 0 else None

	# validate file path
	if module_name is None:
		self.throw(f"Module not found")
	else:
		# get module meta path
		module_path = self.meta["MODULES_PATH"] if "MODULES_PATH" in self.meta else None
		
		# validate module path
		if module_path is None:
			self.run_algorithm("warn", ['"Modules Path(META:#QUOTEMODULES_PATH#QUOTE) not found, setting to #QUOTE.#QUOTE(self Directory)"'])
			module_path = "."
			self.meta["MODULES_PATH"] = module_path
		
		# get module file path
		module_file_path = os.path.join(module_path, module_name)
		
		# validate module file path
		if not os.path.exists(module_file_path):
			self.throw(f'Module not found: "{".".join(module_name.split(".")[:-1])}" ({module_file_path})')
		else:
			# run module
			with open(module_file_path, 'r') as module_file:
				# get module code
				module_code = module_file.read()
				self.module_run_token_id = 0

				# tokenize code
				tokens = self.tokenize(module_code)

				# iteration
				while self.module_run_token_id < len(tokens):
					# token data
					token = tokens[self.module_run_token_id]
					
					# run algorithm
					try:
						self.run(token)
					except Exception as UnknownError:
						self.throw(str(UnknownError))
					
					# update token id
					self.module_run_token_id += 1


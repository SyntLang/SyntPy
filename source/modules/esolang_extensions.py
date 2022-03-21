# Esolang Extensions

# modules
import os

# Esolang Class
class Esolang:
	# default information
	name = "Esolang"
	file_ext = ".esl"
	ver = "0.0.0"

	# default tokens
	splitter_tokens = {
		"\n": "",
		"[": ".",
		"]": ",",
		"{": ".",
		"}": ",",
	}
	sub_splitter_tokens = [
		" "
	]
	strip_tokens = [
		"\t"
	]

	# default variables and functions
	algorithms = {}
	variables = {}
	meta = {}
	script_algorithms = {}

	# variables and algorithms details
	variable_types = [
		"int",
		"float",
		"str",
		"bool",
		"none",
		"list",
	]
	variable_type_definitions = {
		"int": "int",
		"float": "float",
		"str": "str",
		"bool": "bool",
		"none": "none",
		"list": "list"
	}
	boolean_names = {
		"0" : "false",
		"1" : "true",
	}

	# special characters
	special_characters = {
		'N': '\n',
		'T': '\t'
	}

	# triggers
	special_characters_trigger = '\\'
	variable_trigger = '$'
	meta_trigger = '@'
	item_trigger = '#'

	# run case
	log = False
	run_status = "break"
	algorithm_output_variable_name_list = []

	# initialize Esolang class
	def __init__(self, *args, **kwargs):
		# reset engine
		self.reset(*args, **kwargs)

	# reset engine
	def reset(self, *args, **kwargs):
		# esolang information
		self.name = kwargs["name"] if "name" in kwargs else self.name
		self.file_ext = kwargs["file_ext"] if "file_ext" in kwargs else self.file_ext
		self.ver = kwargs["ver"] if "file_ext" in kwargs else self.ver

		# esolang tokens (for syntax)
		self.splitter_tokens = kwargs["splitter_tokens"] if "splitter_tokens" in kwargs else self.splitter_tokens
		self.sub_splitter_tokens = kwargs["sub_splitter_tokens"] if "sub_splitter_tokens" in kwargs else self.sub_splitter_tokens
		self.strip_tokens = kwargs["strip_tokens"] if "strip_tokens" in kwargs else self.strip_tokens
		self.blocker_tokens = []
		self.unblocker_tokens = []

		# add tokens to blocker and unblocker from splitters automatically
		for token in self.splitter_tokens:
			if self.splitter_tokens[token] == ".":
				# blocker token
				self.blocker_tokens.append(token)
			elif self.splitter_tokens[token] == ",":
				# unblocker token
				self.unblocker_tokens.append(token)
		
		# esolang variables and functions
		self.algorithms = kwargs["algorithms"] if "algorithms" in kwargs else self.algorithms
		self.variables = kwargs["variables"] if "variables" in kwargs else self.variables

		# logs
		self.log = kwargs["log"] if "log" in kwargs else False
		self.clear_logs()

		# run case
		self.algorithm_output_variable_name_list = []

	# strip unrequested tokens
	def stripper(self, code:str):
		# final output
		output = code

		# strip tokens
		for token in self.strip_tokens:
			output = output.replace(token, "")
		
		# return output
		return output

	# split code
	def splitter(self, code:str):
		# final tokens list
		tokens = []

		# tokenize code
		itr_token = ""
		for char in code:
			# add char to iterating token
			itr_token += char
			
			# check if char is splitter
			if char in self.splitter_tokens:
				# check if char is token end
				if self.splitter_tokens[char] == ",":
					tokens.append(itr_token)
					itr_token = ""
				else:
					# add iterating token to output tokens
					tokens.append(itr_token[:-1])
					itr_token = ""

					# check if starting token
					if self.splitter_tokens[char] == ".":
						itr_token += char
		
		# add last iterating token
		tokens.append(itr_token)

		# return tokens
		return tokens
	
	# sub-split code tokens
	def sub_splitter(self, code_tokens:list):
		# final output
		tokens = []

		# sub-split tokens
		itr_token_list = []
		for token in code_tokens:
			# iterate through token
			itr_token = ""

			# check if token is splitter
			if token in self.splitter_tokens:
				itr_token_list = token
			else:
				# create sub-tokens
				for char in token:
					# add char to iterating token
					itr_token += char

					# check if char is sub-splitter
					if char in self.sub_splitter_tokens:
						# add sub-splitter to current token list
						itr_token_list.append(itr_token[:-1])
						itr_token = ""
			
				# add last iterating token
				itr_token_list.append(itr_token)

			# add iterating token list to output tokens
			tokens.append(itr_token_list)
			itr_token_list = []

		# return output
		return tokens
	
	# organize tokens
	def organize_splits(self, code_tokens:list):
		# final organized tokens
		organized_tokens = []

		# remove empty tokens
		partial_code_tokens = []
		for token in code_tokens:
			if any(token):
				partial_code_tokens.append(token)

		# partial tokens
		block = False
		partial_token = []
		for token in partial_code_tokens:
			# check if token is a blocker
			if token in self.blocker_tokens:
				block = True
			
			# if blocked add into partial tokens
			if block:
				partial_token.append(token)
			else:
				# add block to directly organized tokens
				organized_tokens.append(token)
			
			# check if token is unblocker
			if token in self.unblocker_tokens:
				# reset
				block = False
				organized_tokens.append(partial_token)
				partial_token = []
		
		# collect algorithms and collections
		partial_collections = []
		itr_index = 0
		while itr_index < len(organized_tokens):
			if itr_index == len(organized_tokens) - 1:
				# check if token is collection or algorithm
				if organized_tokens[itr_index][0] in self.splitter_tokens:
					# throw error that collection is unknown
					self.throw("Unknown collection: " + str(organized_tokens[itr_index][0]))
				else:
					# simply add to partial collections
					partial_collections.append(organized_tokens[itr_index])
					itr_index += 1
			else:
				# check if next token is a collection or algorithm
				if organized_tokens[itr_index + 1][0] in self.splitter_tokens:
					# add collection with current token to partial collections
					this_collection = organized_tokens[itr_index] + [organized_tokens[itr_index + 1][1:-1]]
					partial_collections.append(this_collection)
					itr_index += 2
				else:
					# add only current token to partial collections
					partial_collections.append(organized_tokens[itr_index])
					itr_index += 1
		
		# set organized tokens to partial collections
		organized_tokens = partial_collections

		# return organized tokens
		return organized_tokens
	
	# tokenize code
	def tokenize(self, code:str):
		# strip code
		partial_code = self.stripper(code)

		# split code
		code_tokens = self.splitter(partial_code)

		# sub-split code tokens
		code_tokens = self.sub_splitter(code_tokens)

		# organize code tokens
		code_tokens = self.organize_splits(code_tokens)

		# return code tokens
		return code_tokens
	
	# Error Handler
	def throw(self, msg, **options):
		# print msg
		print(f"LOG[{options['type'] if 'type' in options else 'ERROR'}]: {msg}")

		# stop execution
		self.run_status = "break"

		# stop logs if disabled
		if self.log == False:
			return

		# store in logs
		if os.path.isfile("logs/" + self.name + ".log"):
			with open("logs/" + self.name + ".log", "a") as f:
				f.write("LOG[ERROR]: " + msg + "\n")
		else:
			if os.path.isdir("logs"):
				with open("logs/" + self.name + ".log", "w") as f:
					f.write("LOG[ERROR]: " + msg + "\n")
			else:
				os.mkdir("logs")
				with open("logs/" + self.name + ".log", "w") as f:
					f.write("LOG[ERROR]: " + msg + "\n")
	
	# clear logs
	def clear_logs(self):
		if os.path.isfile("logs/" + self.name + ".log"):
			with open("logs/" + self.name + ".log", "w") as f:
				f.write("")
	
	# run
	def run(self, tokens):
		# create algorithm and arguments from token
		alg = tokens[0]
		args = tokens[1:]
		
		# check if alg is valid
		if alg in self.algorithms:
			self.algorithms[alg](self, *self.convert_variables(args))
		elif alg in self.script_algorithms:
			# inputs for alg
			predefined = {}
			args_name = self.script_algorithms[alg]['args_name']

			# return variable and arguments
			return_variable = args[0] if len(args) > 0 else None
			args = args[1:] if len(args) > 1 else []
			args = self.convert_variables(args)

			if args_name in self.variables:
				predefined = self.variables[args_name]
			self.variables[args_name] = {
				"name": args_name,
				"type": 'collection',
				"value": [[item] for item in args]
			}
			
			self.run_algorithm(alg, args, return_variable)
			
			del self.variables[args_name]
			if len(predefined):
				self.variables[args_name] = predefined
		else:
			self.throw("Algorithm not found: " + alg)
	
	# variable convert
	def convert_variables(self, data:list):
		# final arguments
		args = []

		# covert argument to string
		argument_string = " ".join([data if type(data[-1]) != type([]) else data[:-1]][0] if len(data) > 0 else [])
		
		# split for strings
		args = argument_string.split("\"")
		if len(args) % 2 == 0:
			self.throw("Invalid string placement")
		
		# convert to separate args
		partial_args = []
		for index, arg in enumerate(args):
			if index % 2 != 0:
				partial_args.append(arg)
			else:
				for token in arg.split(" "):
					partial_args.append(token)
		
		# apply partial args
		args = partial_args

		# check for variables
		partial_args = []
		for token in args:
			if token:
				if len(self.variables) != 0 or len(self.meta) != 0 or len(self.special_characters) != 0:
					# refresh variables
					self.refresh_variables()

					# create partial tokens
					partial_token = token

					# replace variables and special characters
					for meta in self.meta:
						partial_token = partial_token.replace(f'{self.meta_trigger}{meta}{self.meta_trigger}', self.meta[meta])
					for variable in self.variables:
						if self.variables[variable]["type"] == "collection":
							for _ in range(partial_token.count(f"{self.variable_trigger}{variable}{self.variable_trigger}")):
								partial_partial_token = partial_token.split(f"{self.variable_trigger}{variable}{self.variable_trigger}")
								if len(partial_partial_token) > 1:
									if partial_partial_token[1]:
										if partial_partial_token[1][0] == self.item_trigger:
											partial_partial_token = partial_partial_token[1].split(self.item_trigger)
											if len(partial_partial_token) > 2:
												item_num = partial_partial_token[1]
												original_item_num = partial_partial_token[1]
												if self.value_type(str(item_num)) == self.variable_type_definitions["int"]:
													item_num = int(item_num)
												elif self.value_type(str(item_num)) == self.variable_type_definitions["float"]:
													item_num = int(float(item_num))
												elif self.value_type(str(item_num)) == self.variable_type_definitions["bool"]:
													item_num = 0 if self.boolean_names["0"] == item_num else 1
												else:
													item_num = len(item_num)
												coll_item = self.variables[variable]["value"][int(item_num) if int(item_num) < len(self.variables[variable]["value"]) else -1][0] if len(self.variables[variable]["value"]) > 0 else ""
												partial_token = partial_token.replace(f"{self.variable_trigger}{variable}{self.variable_trigger}{self.item_trigger}{original_item_num}{self.item_trigger}", coll_item)
											else:
												partial_token = partial_token.replace(f"{self.variable_trigger}{variable}{self.variable_trigger}", str(self.variables[variable]["value"])[1:-1].replace('"', '').replace("'", ''))
										else:
											partial_token = partial_token.replace(f"{self.variable_trigger}{variable}{self.variable_trigger}", str(self.variables[variable]["value"])[1:-1].replace('"', '').replace("'", ''))
									else:
										partial_token = partial_token.replace(f"{self.variable_trigger}{variable}{self.variable_trigger}", str(self.variables[variable]["value"])[1:-1].replace('"', '').replace("'", ''))
								else:
									partial_token = partial_token.replace(f"{self.variable_trigger}{variable}{self.variable_trigger}", str(self.variables[variable]["value"])[1:-1].replace('"', '').replace("'", ''))
						else:
							partial_token = partial_token.replace(f"{self.variable_trigger}{variable}{self.variable_trigger}", self.variables[variable]["value"])
					for special_character in self.special_characters:
						partial_token = partial_token.replace(f'{self.special_characters_trigger}{special_character}', self.special_characters[special_character])
					
					# add to partial args
					partial_args.append(partial_token)
				else:
					partial_args.append(token)
		
		# apply partial arguments
		args = (partial_args if type(data[-1]) != type([]) else partial_args + [data[-1]]) if len(data) > 0 else partial_args

		# return arguments
		return args
	
	# create variables
	def create_variable(self, variable_data:dict):
		# final variable data
		final_variable_data = {}

		# validate variable data
		if "name" not in variable_data:
			self.throw("Variable name not found")
		if "type" not in variable_data:
			self.throw("Variable type not found")
		if not(variable_data["name"]):
			self.throw("Variable name is empty")
		if not(variable_data["type"]):
			self.throw("Variable type is empty")
		if variable_data["type"] not in self.variable_types:
			self.throw(f"Variable type does not exist: {variable_data['type']}")
		
		# insert primary data to final variable data
		final_variable_data["name"] = variable_data["name"]
		final_variable_data["type"] = variable_data["type"]
		
		# variable value
		if "value" not in variable_data:
			final_variable_data["value"] = ""
		else:
			final_variable_data["value"] = variable_data["value"]
		
		# adaptations for collections
		if final_variable_data["type"] == "collection":
			final_variable_data["value"] = [[" ".join(item)] for item in final_variable_data["value"]]
		
		# add variable to storage
		self.variables[final_variable_data["name"]] = final_variable_data
	
	# update variable
	def update_variable(self, variable_data:dict):
		# check if variable exists
		if variable_data["name"] not in self.variables:
			self.throw(f"Variable does not exist: {variable_data['name']}")
		else:
			# update variable
			self.variables[variable_data["name"]]["value"] = variable_data["value"]

		# refresh variables
		self.refresh_variables()

	# get value data type
	def value_type(self, value:str):
		# final value type
		value_type = "none"

		# check for each character
		numeric_chars = "+-0123456789"
		for character in str(value):
			if character in numeric_chars:
				if value_type == "none" or value_type == "int":
					value_type = "int"
				elif value_type == "float":
					value_type = "float"
				else:
					value_type = "str"
			elif character == ".":
				if value_type == "int":
					value_type = "float"
				else:
					value_type = "str"
			else:
				if value == self.boolean_names["0"] or value == self.boolean_names["1"]:
					value_type = "bool"
				else:
					value_type = "str"
		
		# fix sign problem
		if value_type == "int":
			true_number = str(value).strip("+").strip("-")
			if len(true_number) == 0:
				value_type = "str"
			else:
				if str(value).count("+") + str(value).count("-") > 1:
					value_type = "str"
		
		# check if value is list
		if (str(value)[0] == "[" and str(value)[-1] == "]") if len(str(value)) > 0 else False:
			value_type = "list"
		
		# convert to variable in storage
		value_type = self.variable_type_definitions[value_type]

		# return value type
		return value_type

	# get variable data type
	def variable_type(self, variable_name:str):
		# check if variable exists
		if variable_name not in self.variables:
			self.throw(f"Variable does not exist: {variable_name}")
		
		# return variable type
		return self.variables[variable_name]["type"]
	
	# refresh variables
	def refresh_variables(self):
		# refresh variables
		for variable in self.variables:
			# check is variable value matches type
			if self.variable_type(variable) == self.value_type(self.variables[variable]["value"]):
				pass
			else:
				if self.variables[variable]["type"] == self.variable_type_definitions["int"]:
					if self.value_type(self.variables[variable]["value"]) == self.variable_type_definitions["float"]:
						self.variables[variable]["value"] = int(float(self.variables[variable]["value"]))
					elif self.value_type(self.variables[variable]["value"]) == self.variable_type_definitions["bool"]:
						state = 0 if self.variables[variable]["value"] == self.boolean_names["0"] else 1
						self.variables[variable]["value"] = int(state)
					else:
						self.variables[variable]["value"] = len(self.variables[variable]["value"])
				elif self.variables[variable]["type"] == self.variable_type_definitions["float"]:
					if self.value_type(self.variables[variable]["value"]) == self.variable_type_definitions["int"]:
						self.variables[variable]["value"] = float(self.variables[variable]["value"])
					elif self.value_type(self.variables[variable]["value"]) == self.variable_type_definitions["bool"]:
						state = 0 if self.variables[variable]["value"] == self.boolean_names["0"] else 1
						self.variables[variable]["value"] = float(int(state))
					else:
						self.variables[variable]["value"] = float(len(self.variables[variable]["value"]))
				elif self.variables[variable]["type"] == self.variable_type_definitions["bool"]:
					self.variables[variable]["value"] = self.boolean_names["0"] if int(float(len(self.variables[variable]["value"]))) == 0 else self.boolean_names["1"]
				elif self.variables[variable]["type"] == self.variable_type_definitions["none"]:
					self.variables[variable]["value"] = ""
				elif self.variables[variable]["type"] == self.variable_type_definitions["list"]:
					if type(self.variables[variable]["value"]) == type([]):
						self.variables[variable]["value"] = self.variables[variable]["value"]
					else:
						self.variables[variable]["value"] = [self.variables[variable]["value"]]
				else:
					self.variables[variable]["value"] = self.variables[variable]["value"]
				self.variables[variable]["value"] = str(self.variables[variable]["value"])
	
	# run algorithm
	def run_algorithm(self, algorithm_name:str, algorithm_args:list=[], return_variable_name:str=""):
		# get algorithm
		if algorithm_name not in self.algorithms and algorithm_name not in self.script_algorithms:
			self.throw(f"Algorithm not found: {algorithm_name}")
		else:
			if algorithm_name in self.algorithms:
				self.run([algorithm_name] + algorithm_args)
			else:
				algorithm_tokens = self.script_algorithms[algorithm_name]["data"]
				if return_variable_name != "":
					self.algorithm_output_variable_name_list.append(return_variable_name)

				# programming language
				for index, token in enumerate(algorithm_tokens):
					# run algorithm
					self.run(token)


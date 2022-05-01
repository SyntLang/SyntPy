# Synt self

# modules
import modules
import os
import sys

# general modules
import modules.esolang_extensions
import modules.synt

# synt modules
import modules.synt.algorithms_data

# Synt self
class Synt(modules.esolang_extensions.Esolang):
	# Synt self Information
	name = "Synt"
	file_ext = ".synt"
	ver = "0.4[DEV]"

	# Synt self Tokens
	splitter_tokens = {
		"\n": "",
		";": "",
		"[": ".",
		"]": ",",
		"{": ".",
		"}": ",",
	}
	sub_splitter_tokens = [
		" "
	]
	strip_tokens = [
		"\t",
	]

	# Synt self Algorithms
	variables = {}
	algorithms = modules.synt.algorithms_data.algorithms
	meta = {}
	script_algorithms = {}

	# variables and algorithms details
	variable_types = [
		'binary',
		'number',
		'decimal',
		'text',
		'nothing',
		'collection',
	]
	variable_type_definitions = {
		'bool': 'binary',
		'int': 'number',
		'float': 'decimal',
		'str': 'text',
		'none': 'nothing',
		'list': 'collection'
	}
	boolean_names = {
		'0': "off",
		'1': "on"
	}

	# keywords
	special_characters = {
		'NEWLINE': '\n',
		'INDENT': '\t',
		'BACKSPACE': '\b',
		'START': '\r',
		'SPACE': ' ',
		'LEFTSQUARE': '[',
		'RIGHTSQUARE': ']',
		'LEFTCURLY': '{',
		'RIGHTCURLY': '}',
		'COMMA': ',',
		'DOT': '.',
		'SEMICOLON': ';',
		'COLON': ':',
		'EQUAL': '=',
		'HASH': '#',
		'QUESTION': '?',
		'EXCLAMATION': '!',
		'QUOTE': '"',
		'APOSTROPHE': "'",
	}
	logic_operators = {
		"="  : ["equals to", "equals", "="],
		"!=" : ["not equals to", "not", "!="],
		">" : ["greater than", "greater", ">"],
		"<" : ["less than", "less", "<"],
		">=" : ["greater than equal to", "notless", ">="],
		"<=" : ["less than equal to", "notgreater", "<="],
		"<-" : ["contains", "contains", "<-"],
		"!<-" : ["does not contain", "notcontains", "!<-"],
		"_%" : ["starts with", "starts", "_%"],
		"!_%" : ["does not start with", "notstarts", "!_%"],
		"%_" : ["ends with", "ends", "%_"],
		"!%_" : ["does not end with", "notends", "!%_"],
	}

	# triggers
	special_characters_trigger = '#'
	variable_trigger = '#'
	meta_trigger = '?'
	item_trigger = "%"

	# run status
	log = False
	run_status = 'break'
	run_token_id = 0
	compiled = False
	compiled_code = ""

	# run language
	def run_code(self, code:str):
		# reset self
		self.reset()
		self.run_status = 'run'
		self.run_token_id = 0

		# tokenize code
		tokens = self.tokenize(code)

		# iteration
		while self.run_token_id < len(tokens):
			# token data
			token = tokens[self.run_token_id]
			
			# run algorithm
			try:
				self.run(token)
			except Exception as UnknownError:
				self.throw(f'{UnknownError}', type="CORE ERROR")
			
			# update token id
			self.run_token_id += 1
		
		# set run status
		self.run_status = 'break'

		# end function
		return
	
	def start(self):
		# check compiled
		if self.compiled:
			# run compiled code
			os.system("cls")
			self.run_code(self.compiled_code)

			# block rest of self
			return

		# ready
		os.system("cls")
		print(f"Running Synt self v{self.ver}")

		# modes selections
		mode_valid = False
		mode = ""

		# get self arguments
		self_options = sys.argv

		# remove python source file name
		if self_options[0].endswith('.py'):
			self_options.pop(0)

		# check if arguments passed
		if len(self_options) > 0:
			self_options = self_options[0]
		else:
			self_options = ""
		
		# check argument mode
		code_file = ""
		if self_options:
			if self_options.startswith("*"):
				mode = self_options[1:]
			else:
				mode = "f"
				code_file = self_options
		

		# select mode if not specified in arguments
		if mode not in ["f", "file", "i", "interactive", "q", "quit", "compile", "c"]:
			while not mode_valid:
				# mode input
				mode = input("Mode: ")
				modes = [
					"file", "f",
					"interactive", "i",
					"quit", "q",
					"compile", "c",
				]

				# check mode
				if mode in modes:
					mode_valid = True
				else:
					# more instructions
					print("Mode not valid.")
					print("Valid modes: file[f], interactive[i], quit[q], compile[c]")
		
		# clear console before continuing
		os.system("cls")

		# quit if mode is quit
		if mode in ["quit", "q"]:
			print("Terminated.")
			return
		
		# file mode
		if mode in ["file", "f"]:
			self.file(code_file)

		# interactive mode
		if mode in ["interactive", "i"]:
			self.interactive()

		# compile mode
		if mode in ["compile", "c"]:
			print("Compiling can only be done using command line arguments.")

	# file mode
	def file(self, code_file:str):
		# request code file
		problem_args = False
		while True:
			# get file
			requested_file = code_file if code_file and not problem_args else input("File Path(empty to quit): ")
			problem_args = True

			# check if wants to quit
			if requested_file == "":
				os.system("cls")
				print("Terminated.")
				return

			# check if file exists
			if os.path.isfile(requested_file):
				# get code from requested file
				with open(requested_file, "r") as code_file:
					code = code_file.read()
					
					# clear console
					os.system("cls")

					# run code as synt script
					self.run_code(code)

					# stop loop from requesting file again
					break
			else:
				# more instructions
				print("File Not Found!")
				print("If your file exists consider putting is beside self or use complete path to file.")
	
	# interactive mode
	def interactive(self):
		# start self
		self.reset()
		self.run_status = "run"

		# run forever till ended
		main_code = ""
		multi_line_token = ""
		interactive_running = True
		while interactive_running:
			# get code
			code = input("Synt>>> " if main_code == "" else "        ")
			main_code += code + "\n"

			# check if any multi-line code
			multi_line_token = multi_line_token if multi_line_token else ""
			if multi_line_token:
				for token in self.unblocker_tokens:
					if token in code:
						multi_line_token = ""
						break
			else:
				for token in self.blocker_tokens:
					if token in code:
						multi_line_token = token
						break

			# run code
			if multi_line_token == "":
				if main_code[:-1]:
					tokens = self.tokenize(main_code[:-1])
					for token in tokens:
						self.run_token_id = 0
						while self.run_token_id < 1:
							self.run_token_id += 1
							try:
								self.run(token)
							except Exception as UnknownError:
								self.throw(str(UnknownError))
				main_code = ""
			
			# check if wants to quit
			if self.run_status == "break":
				return


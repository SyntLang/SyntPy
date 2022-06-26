# Synt self

# modules
import modules
import os
import sys
import time

# general modules
import modules.esolang_extensions
import modules.synt
import modules.synt.interactive_mode
import modules.synt.file_mode

# synt modules
import modules.synt.algorithms_data

# Synt self
class Synt(modules.esolang_extensions.Esolang):
	# Synt self Information
	name = "Synt"
	file_ext = ".synt"
	ver = "0.7[DEV]"

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
	initial_item_trigger = '<'
	end_item_trigger = ">"

	# run status
	log = False
	run_status = 'break'
	run_token_id = 0
	compiled = False
	compiled_code = ""
	mode = ""
	mode_override = ""

	# engine components
	tick = 0
	last_tick = time.time()
	tick_paused = False

	# console
	cmd = os.popen("ver").read()
	cmd = cmd.strip("").strip("\n")
	cmd = cmd.startswith("Microsoft")
	console = "cmd"
	console_clear_cmd = "cls" if cmd else "clear"

	interactive = modules.synt.interactive_mode.interactive
	file = modules.synt.file_mode.file

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
				self.throw(f'{UnknownError}', type=f"CORE ERROR::{self.run_token_id}::{token}")
			
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
			os.system(f"{self.console_clear_cmd}")
			self.run_code(self.compiled_code)

			# block rest of self
			return

		# ready
		os.system(f"{self.console_clear_cmd}")
		print(f"Running Synt self v{self.ver}")

		# modes selections
		mode_valid = False
		mode = self.mode_override if self.mode_override else ""
		self.mode = mode

		# get self arguments
		self_options = sys.argv

		# remove source file name
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
		
		# force mode
		if self.mode_override:
			mode = self.mode_override

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
			self.mode = mode
		
		# clear console before continuing
		os.system(f"{self.console_clear_cmd}")

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


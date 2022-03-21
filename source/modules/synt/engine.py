# Synt Engine

# modules
import modules
import os
import argparse

# general modules
import modules.esolang_extensions
import modules.synt

# synt modules
import modules.synt.algorithms_data

# Synt Engine
class Synt(modules.esolang_extensions.Esolang):
	# Synt Engine Information
	name = "Synt"
	file_ext = ".synt"
	ver = "0.4[DEV]"

	# Synt Engine Tokens
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

	# Synt Engine Algorithms
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

	# special characters
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

	# triggers
	special_characters_trigger = '#'
	variable_trigger = '#'
	meta_trigger = '?'
	item_trigger = "%"

	# run status
	log = False
	run_status = 'break'
	run_token_id = 0

	# run language
	def run_code(self, code:str):
		# reset engine
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
				self.throw(str(UnknownError))
			
			# update token id
			self.run_token_id += 1
		
		# set run status
		self.run_status = 'break'

		# end function
		return
	
	def engine(self):
		# ready
		os.system("cls")
		print(f"Running Synt Engine v{self.ver}")

		# parse arguments
		parser = argparse.ArgumentParser(description="Synt Programming Language")
		parser.add_argument("-m", "--mode", help="select mode")
		parser.add_argument("-f", "--file", help="file to run")
		args = parser.parse_args()

		# modes selections
		mode_valid = False
		mode = "q"

		# select mode if not specified in arguments
		if args.mode in ["f", "file", "i", "interactive", "q", "quit"]:
			mode = args.mode
		else:
			while not mode_valid:
				# mode input
				mode = input("Mode: ")
				modes = [
					"file", "f",
					"interactive", "i",
					"quit", "q",
				]

				# check mode
				if mode in modes:
					mode_valid = True
				else:
					# more instructions
					print("Mode not valid.")
					print("Valid modes: file[f], interactive[i], quit[q]")
		
		# clear console before continuing
		os.system("cls")

		# quit if mode is quit
		if mode in ["quit", "q"]:
			print("Terminated.")
			return
		
		# file mode
		if mode in ["file", "f"]:
			self.file(args)

		# interactive mode
		if mode in ["interactive", "i"]:
			self.interactive()

	# file mode
	def file(self, args):
		# request code file
		problem_args = False
		while True:
			# get file
			requested_file = args.file if args.file and not problem_args else input("File Path(empty to quit): ")
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
				print("If your file exists consider putting is beside engine or use complete path to file.")
	
	# interactive mode
	def interactive(self):
		# start engine
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
						self.run(token)
				main_code = ""
			
			# check if wants to quit
			if self.run_status == "break":
				return


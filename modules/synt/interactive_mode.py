# interactive mode

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
			self.run_status = "run"


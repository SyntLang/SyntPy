# file mode

# modules
import os

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
			os.system(f"{self.console_clear_cmd}")
			print("Terminated.")
			return

		# check if file exists
		if os.path.isfile(requested_file):
			# get code from requested file
			with open(requested_file, "r") as code_file:
				code = code_file.read()
				
				# clear console
				os.system(f"{self.console_clear_cmd}")

				# run code as synt script
				self.run_code(code)

				# stop loop from requesting file again
				break
		else:
			# more instructions
			print("File Not Found!")
			print("If your file exists consider putting is beside self or use complete path to file.")


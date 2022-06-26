# Synt Export Compiler

# modules
import os
import sys

# compiler
class Compiler:
	# export data
	cname = "export"
	expo_dir = "export"
	src_dir = "source"
	src_lib = []
	py_dir = "engine\\Python310"
	super_code = ""
	file_system = {}
	src_code = ""

	# initialize
	def __init__(self, **options):
		# get export data
		cname = options["cname"] if "cname" in options else self.cname
		expo_dir = options["expo_dir"] if "expo_dir" in options else self.expo_dir
		src_dir = options["src_dir"] if "src_dir" in options else self.src_dir
		src_code = options["src_code"] if "src_code" in options else self.src_code
		py_dir = options["py_dir"] if "py_dir" in options else self.py_dir
		src_lib = options["src_lib"] if "src_lib" in options else self.src_lib
		
		# set export data
		self.cname = cname
		self.expo_dir = f"{os.getcwd()}\\{expo_dir}"
		self.src_dir = f"{os.getcwd()}\\{src_dir}"
		self.src_code = src_code
		self.py_dir = f"{os.getcwd()}\\{py_dir}"
		self.src_lib = src_lib

		# export spyc
		self.create_canvas()
		self.load_source()
		self.spyc()
	
	# create spyc(Synt - Python Compiled) file
	def create_canvas(self):
		# check for existing directories
		if os.path.isdir(self.expo_dir):
			expo_dir = self.expo_dir.split("\\")[-1]
			exports = ["." for _ in os.listdir() if _.startswith(expo_dir)]
			exports_count = len(exports) + 1
			self.expo_dir = f"{self.expo_dir}_{exports_count}"
		
		# create export directory
		if not(os.path.isdir(self.expo_dir)):
			os.mkdir(self.expo_dir)
		
		# create spyc file
		spyc = open(f"{self.expo_dir}/{self.cname}.spyc", "w")
		spyc.write("")
		spyc.close()
	
	# load source
	def load_source(self):
		# main file
		main_file = f"{self.src_dir}/main.py"
		with open(main_file, "r") as main:
			self.file_system["main.py"] = main.read()
		
		# modules
		modules_dir = f"{self.src_dir}/modules"
		for module in os.listdir(modules_dir):
			if module.endswith(".py"):
				with open(f"{modules_dir}/{module}", "r") as module_file:
					self.file_system[f"modules/{module}"] = module_file.read()
			if module == "synt":
				for synt_file in os.listdir(f"{modules_dir}/{module}"):
					if synt_file.endswith(".py"):
						file_path = f"{modules_dir}/{module}/{synt_file}"
						with open(file_path, "r") as synt_module_file:
							data = synt_module_file.read()
							self.file_system[f"modules/synt/{synt_file}"] = data
	
	# compile spyc
	def spyc(self):
		# arrange file system according to import structures
		files = list(self.file_system.keys())
		order = []
		itr = 0

		# push modules to top
		for filename in files:
			if filename.startswith("modules"):
				if not(filename.startswith("modules/synt")):
					if not(filename.endswith("__init__.py")):
						if not(filename.endswith("compiler.py")):
							order.append(filename)
		
		# push synt modules
		for filename in files:
			if filename.startswith("modules"):
				if filename.startswith("modules/synt"):
					if not(filename.endswith("__init__.py")):
						if not(filename.endswith("compiler.py")):
							if not(filename.endswith("algorithms_data.py")):
								if not(filename.endswith("root.py")):
									order.append(filename)
		
		# append main in last
		order.append("modules/synt/algorithms_data.py")
		order.append("modules/synt/root.py")
		order.append("main.py")

		# edit imports and system
		code_chunks = []
		for filename in order:
			code_chunks.append(self.file_system[filename])

		# merge code
		self.super_code = "\n".join(code_chunks)
		
		# write spyc
		with open(f"{self.expo_dir}/{self.cname}.spyc", "w") as spyc:
			# remove comments, imports and empty lines
			code = ""
			libs = []
			for line in self.super_code.split("\n"):
				if not(line.strip("\t").startswith("#")):
					if not(line.strip("\t").startswith("import")):
						if line.strip("\t"):
							if line.strip("\t").startswith("__compiler__"):
								code += "\tsynt_engine.compiled = True\n"
								code += "\tsynt_engine.compiled_code = \"\"\"\n"
								code += self.src_code
								code += "\n\"\"\"\n"
							else:
								code += line + "\n"
					else:
						libs.append(line.strip("\t"))
			
			# update libs
			synt_libs = [lib for lib in libs if lib.startswith("import modules")]
			libs = [lib for lib in libs if not(lib.startswith("import modules"))]
			libs = list(set(libs))

			# update code
			libs = "\n".join(libs)
			code = f"{libs}\n{code}"
			code = code.replace("modules.synt.", "modules.")
			code = code.replace("modules.", "")

			# synt libs
			for lib in synt_libs:
				lib_name = lib.split(" ")[1]
				if len(lib_name.split(".")) > 1:
					lib_name = lib_name.split(".")[-1]
					lib_name = lib_name.replace("synt.", "")
					code = code.replace(f"{lib_name}.", "")
			
			# final code
			self.super_code = code

			# write spyc
			spyc.write(self.super_code)

# use compiler module
def compiler_main():
	# check arguments
	args = sys.argv

	# Exe Compile
	if "*compile" in args or "*c" in args:
		# warn
		print("Compile Mode is still in heavy development.")
		use = input("Do you want to continue? (Y[Default]/N):")
		if use.lower() in ["n", "no"]:
			sys.exit()

		# get argument index
		arg_index = args.index("*compile" if "*compile" in args else "*c")

		# get further arguments
		filename = "main.synt"
		if arg_index < len(args) - 1:
			filename = args[arg_index + 1]
		
		# source code file
		while not(os.path.isfile(filename)):
			filename = input("File Path(empty to quit): ")
			if not(filename):
				print("Terminated.")
				sys.exit()
		
		# get source code
		with open(filename, "r") as source_code_file:
			os.system("cls")
			source_code = source_code_file.read()

			# compile spyc
			print("Compiling to SPyC")
			compiler = Compiler(src_code=source_code)

			# check spyc
			if os.path.isfile(f"{compiler.expo_dir}/{compiler.cname}.spyc"):
				print("Successfully compiled to SPyC.")
			else:
				print("Compiling to SPyC Failed.")
				sys.exit()

			# compile exe
			print("Compiling to EXE")
			#command = f"{compiler.py_dir}\\python.exe "
			command = f"py "
			command += "-m PyInstaller "
			command += f"\"{compiler.expo_dir}\\{compiler.cname}.spyc\" "
			command += "--onefile --clean --name \"Project\" "
			command += f"--distpath \"{compiler.expo_dir}\" "
			command += "&& cls"
			os.system(command)

			# successful compile
			if os.path.isfile(f"{compiler.expo_dir}/Project.exe"):
				print("Compiled successfully.")

				# remove buffer files
				os.remove(f"{compiler.expo_dir}/{compiler.cname}.spyc")
				print(f"PATH: {compiler.expo_dir}\\Project.exe")
				sys.exit()
			else:
				print("Compiling to EXE failed.")

				# rename spyc to py
				print("Converting SPyC to Python Executable")
				orginal_name = f"{compiler.expo_dir}/{compiler.cname}.spyc"
				new_name = f"{compiler.expo_dir}/{compiler.cname}.py"
				os.rename(orginal_name, new_name)

				# check py
				if os.path.isfile(f"{compiler.expo_dir}/{compiler.cname}.py"):
					print("Successfully converted SPyC to Python Executable.")
					print(f"PATH: {compiler.expo_dir}\\{compiler.cname}.py")
					sys.exit()
				else:
					print("Converting SPyC to Python Executable failed.")
					sys.exit()

	# SPyC Compile
	if "*spyc" in args or "*s" in args:
		# get argument index
		arg_index = args.index("*spyc" if "*spyc" in args else "*s")

		# get further arguments
		filename = "main.synt"
		if arg_index < len(args) - 1:
			filename = args[arg_index + 1]
		
		# source code file
		while not(os.path.isfile(filename)):
			filename = input("File Path(empty to quit): ")
			if not(filename):
				print("Terminated.")
				sys.exit()
		
		# get source code
		with open(filename, "r") as source_code_file:
			os.system("cls")
			source_code = source_code_file.read()

			# compile spyc
			print("Compiling to SPyC")
			compiler = Compiler(src_code=source_code)

			# check spyc
			if os.path.isfile(f"{compiler.expo_dir}/{compiler.cname}.spyc"):
				print("Successfully compiled to SPyC.")
			else:
				print("Compiling to SPyC Failed.")
				sys.exit()

			print("Converting SPyC to Python Executable")
			orginal_name = f"{compiler.expo_dir}/{compiler.cname}.spyc"
			new_name = f"{compiler.expo_dir}/{compiler.cname}.py"
			os.rename(orginal_name, new_name)

			# check py
			if os.path.isfile(f"{compiler.expo_dir}/{compiler.cname}.py"):
				print("Successfully converted SPyC to Python Executable.")
				print(f"PATH: {compiler.expo_dir}\\{compiler.cname}.py")
				sys.exit()
			else:
				print("Converting SPyC to Python Executable failed.")
				sys.exit()
	
	# SPyC Run
	if "**spyc" in args or "**s" in args:
		# get argument index
		arg_index = args.index("**spyc" if "**spyc" in args else "**s")

		# get further arguments
		filename = "main.synt"
		if arg_index < len(args) - 1:
			filename = args[arg_index + 1]
		
		# source code file
		while not(os.path.isfile(filename)):
			filename = input("File Path(empty to quit): ")
			if not(filename):
				print("Terminated.")
				sys.exit()
		
		# get source code
		with open(filename, "r") as source_code_file:
			os.system("cls")
			source_code = source_code_file.read()

			# compile spyc
			print("Compiling to SPyC")
			compiler = Compiler(src_code=source_code)

			# check spyc
			if os.path.isfile(f"{compiler.expo_dir}/{compiler.cname}.spyc"):
				print("Successfully compiled to SPyC.")
			else:
				print("Compiling to SPyC Failed.")
				sys.exit()

			print("Converting SPyC to Python Executable")
			orginal_name = f"{compiler.expo_dir}/{compiler.cname}.spyc"
			new_name = f"{compiler.expo_dir}/{compiler.cname}.py"
			os.rename(orginal_name, new_name)

			# check py
			if os.path.isfile(f"{compiler.expo_dir}/{compiler.cname}.py"):
				print("Successfully converted SPyC to Python Executable.")
				print(f"PATH: {compiler.expo_dir}\\{compiler.cname}.py")
			else:
				print("Converting SPyC to Python Executable failed.")
				sys.exit()
			
			# run py
			print("Running Python Executable")
			os.system(f"{compiler.expo_dir}\\{compiler.cname}.py")

			# delete py
			os.remove(f"{compiler.expo_dir}\\{compiler.cname}.py")

			# delete expo_dir
			os.rmdir(compiler.expo_dir)

# use compiler
compiler_main()


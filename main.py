# Synt Programming Language

# modules
import modules
import modules.synt
import modules.synt.root
import modules.compiler

# main loop
def main():
	# Synt Engine
	synt_engine = modules.synt.root.Synt()
	__compiler__ = None
	synt_engine.start()

# run main loop if not imported
if __name__ == "__main__":
	main()


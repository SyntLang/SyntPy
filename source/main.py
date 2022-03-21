# Synt Programming Language

# modules
import modules
import modules.synt
import modules.synt.engine

# main loop
def main():
	# Synt Engine
	synt_engine = modules.synt.engine.Synt()
	synt_engine.engine()

# run main loop if not imported
if __name__ == "__main__":
	main()


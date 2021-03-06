# Algorithms

# modules
import modules
import modules.synt

# synt modules
import modules.synt.basic_algorithms
import modules.synt.debug_algorithms
import modules.synt.variable_algorithms
import modules.synt.operator_algorithms
import modules.synt.logic_algorithms
import modules.synt.loop_algorithms
import modules.synt.external_resource_algorithms
import modules.synt.iterable_algorithms
import modules.synt.time_algorithms
import modules.synt.console_algorithms
import modules.synt.file_algorithms

# algorithms
algorithms = {
	# comment algorithms
	"$": modules.synt.basic_algorithms.comment,
	"?": modules.synt.basic_algorithms.comment,
	">": modules.synt.basic_algorithms.comment,
	"comment": modules.synt.basic_algorithms.comment,

	# basic algorithms
	"version": modules.synt.basic_algorithms.version,
	"output": modules.synt.basic_algorithms.output,
	"input": modules.synt.basic_algorithms.input_function,
	"end": modules.synt.basic_algorithms.end,

	# debug algorithms
	"restore": modules.synt.debug_algorithms.restore,
	"error": modules.synt.debug_algorithms.error,
	"warn": modules.synt.debug_algorithms.warn,
	
	# variable algorithms
	"meta": modules.synt.variable_algorithms.meta,
	"var": modules.synt.variable_algorithms.var,
	"alg": modules.synt.variable_algorithms.alg,
	"result": modules.synt.variable_algorithms.result,
	
	# operator algorithms
	"add": modules.synt.operator_algorithms.add,
	"subtract": modules.synt.operator_algorithms.subtract,
	"multiply": modules.synt.operator_algorithms.multiply,
	"divide": modules.synt.operator_algorithms.divide,
	"power": modules.synt.operator_algorithms.power,
	"info": modules.synt.operator_algorithms.object_type,

	# logic algorithms
	"check": modules.synt.logic_algorithms.condition,
	"condition": modules.synt.logic_algorithms.check,

	# loop algorithms
	"repeat": modules.synt.loop_algorithms.repeat,
	"loop": modules.synt.loop_algorithms.loop,

	# external resource algorithms
	"module": modules.synt.external_resource_algorithms.module,

	# iterable algorithms
	"count": modules.synt.iterable_algorithms.count,
	"insert": modules.synt.iterable_algorithms.insert,
	"remove": modules.synt.iterable_algorithms.remove,
	"delete": modules.synt.iterable_algorithms.delete,

	# time algorithms
	"reset_tick": modules.synt.time_algorithms.reset_tick,
	"pause_tick": modules.synt.time_algorithms.pause_tick,
	"resume_tick": modules.synt.time_algorithms.resume_tick,
	"get_tick": modules.synt.time_algorithms.get_tick,

	# console algorithms
	"clear": modules.synt.console_algorithms.clear,
	"console": modules.synt.console_algorithms.console,
	
	# file algorithms
	"read": modules.synt.file_algorithms.read,
	"write": modules.synt.file_algorithms.write,
}
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
import modules.synt.collection_algorithms

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
	"check": modules.synt.logic_algorithms.check,
	"condition": modules.synt.logic_algorithms.condition,

	# loop algorithms
	"repeat": modules.synt.loop_algorithms.repeat,
	"loop": modules.synt.loop_algorithms.loop,

	# external resource algorithms
	"module": modules.synt.external_resource_algorithms.module,

	# collection algorithms
	"count": modules.synt.collection_algorithms.count,
	"insert": modules.synt.collection_algorithms.insert,
	"remove": modules.synt.collection_algorithms.remove,
	"delete": modules.synt.collection_algorithms.delete,
}
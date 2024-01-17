from dataclasses import dataclass, field, fields

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

@dataclass
class _StateObject:
	def toDict(self):
		d = {}
		for f in fields(self):
			val = getattr(self, f.name, None)
			if _shouldInclude(val) and val != f.default:
				if isinstance(val, list) and isinstance(val[0], _StateObject):
					val = [v.toDict() for v in val]
				elif isinstance(val, _StateObject):
					val = val.toDict()
				d[f.name] = val
		return d

def _shouldInclude(val):
	if val is None or val == '':
		return False
	if isinstance(val, (list, dict)) and not val:
		return False
	return True

@dataclass
class RopState(_StateObject):
	name: str
	path: str
	ropType: str

	functionCode: str | None = None
	materialCode: str | None = None
	initCode: str | None = None
	opGlobals: str | None = None

	macros: list['Macro'] | None = None
	constants: list['Constant'] | None = None
	textures: list['Texture'] | None = None
	buffers: list['Buffer'] | None = None
	references: list['Reference'] | None = None
	variables: list['Variable'] | None = None
	attributes: list['SurfaceAttribute'] | None = None

	materialId: str | None = None

	inputNames: list[str] | None = None
	inputStates: list['InputState'] | None = None

	libraryNames: list[str] | None = None

	paramSource: str | None = None
	constantSource: str | None = None

	validationErrors: list['ValidationError'] | None = field(default_factory=list)

@dataclass
class InputState(_StateObject):
	functionName: str
	sourceName: str | None = None
	varNames: list[str] | None = None
	varInputNames: list[str] | None = None

@dataclass
class ValidationError(_StateObject):
	path: str
	level: str
	message: str

@dataclass
class Macro(_StateObject):
	name: str
	value: str | int | bool | float | None = None
	enable: bool = True

@dataclass
class Constant(_StateObject):
	name: str
	localName: str
	type: str
	menuOptions: list[str] | None = None

@dataclass
class Texture(_StateObject):
	name: str
	path: str
	type: str

@dataclass
class Reference(_StateObject):
	name: str
	localName: str
	sourceName: str | None
	dataType: str
	owner: str | None
	sourcePath: str | None = None
	category: str | None = None

@dataclass
class Variable(_StateObject):
	name: str
	localName: str
	label: str
	dataType: str
	owner: str
	macros: str | None = None

@dataclass
class SurfaceAttribute(_StateObject):
	name: str
	label: str
	dataType: str
	macros: str | None = None

@dataclass
class Buffer(_StateObject):
	name: str
	type: str
	chop: str
	uniformType: str
	length: int | None
	expr1: str | None = None
	expr2: str | None = None
	expr3: str | None = None
	expr4: str | None = None

@dataclass
class ParamTuplet(_StateObject):
	name: str
	localName: str
	source: str
	size: int
	part1: str | None = None
	part2: str | None = None
	part3: str | None = None
	part4: str | None = None
	status: str | None = None
	conversion: str | None = None
	handling: str = 'runtime'
	localNames: list[str] | None = None

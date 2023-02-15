from dataclasses import dataclass, field, fields
from typing import List, Optional, Union

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
	ropType: str

	functionCode: Optional[str] = None
	materialCode: Optional[str] = None
	initCode: Optional[str] = None
	opGlobals: Optional[str] = None

	macros: Optional[List['Macro']] = None
	constants: Optional[List['Constant']] = None
	textures: Optional[List['Texture']] = None
	buffers: Optional[List['Buffer']] = None
	references: Optional[List['Reference']] = None
	variables: Optional[List['Variable']] = None
	dispatchBlocks: Optional[List['Dispatch']] = None

	materialId: Optional[str] = None

	inputNames: Optional[List[str]] = None
	inputStates: Optional[List['InputState']] = None

	libraryNames: Optional[List[str]] = None

	paramSource: Optional[str] = None
	constantSource: Optional[str] = None

	validationErrors: Optional[List['ValidationError']] = field(default_factory=list)

@dataclass
class InputState(_StateObject):
	functionName: str
	sourceName: Optional[str] = None
	varNames: Optional[List[str]] = None
	varInputNames: Optional[List[str]] = None

@dataclass
class ValidationError(_StateObject):
	path: str
	level: str
	message: str

@dataclass
class Macro(_StateObject):
	name: str
	value: Union[None, str, int, bool, float] = None
	enable: bool = True

@dataclass
class Constant(_StateObject):
	name: str
	localName: str
	type: str
	menuOptions: Optional[List[str]] = None

@dataclass
class Texture(_StateObject):
	name: str
	path: str
	type: str

@dataclass
class Reference(_StateObject):
	name: str
	localName: str
	sourcePath: str
	sourceName: str
	dataType: str
	owner: str

@dataclass
class Variable(_StateObject):
	name: str
	localName: str
	label: str
	dataType: str
	owner: str
	macros: Optional[str] = None

@dataclass
class Dispatch(_StateObject):
	name: str
	category: str
	code: str

@dataclass
class Buffer(_StateObject):
	name: str
	type: str
	chop: str
	uniformType: str
	length: Optional[int]
	expr1: Optional[str] = None
	expr2: Optional[str] = None
	expr3: Optional[str] = None
	expr4: Optional[str] = None

@dataclass
class ParamTuplet(_StateObject):
	name: str
	localName: str
	source: str
	size: int
	part1: Optional[str] = None
	part2: Optional[str] = None
	part3: Optional[str] = None
	part4: Optional[str] = None
	status: Optional[str] = None
	conversion: Optional[str] = None
	handling: str = 'runtime'
	localNames: Optional[List[str]] = None

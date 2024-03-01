from dataclasses import dataclass, field, fields
import json

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
	name: str = ''
	path: str = ''
	ropType: str = ''
	ropFullType: str = ''

	params: list['ParamSpec'] | None = None
	paramTuplets: list['ParamTupletSpec'] | None = None

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

	inputStates: list['InputState'] | None = None

	libraryNames: list[str] | None = None

	paramSource: str | None = None
	constantSource: str | None = None

	validationErrors: list['ValidationError'] | None = field(default_factory=list)

	tags: list[str] | None = None

	opElements: list['OpElementState'] | None = None

	@classmethod
	def fromDict(cls, obj: dict):
		return cls(
			name=obj.get('name'),
			path=obj.get('path'),
			ropType=obj.get('ropType'),
			ropFullType=obj.get('ropFullType'),
			params=[ParamSpec(**p) for p in obj.get('params', [])],
			paramTuplets=[ParamTupletSpec(**p) for p in obj.get('paramTuplets', [])],
			functionCode=obj.get('functionCode'),
			materialCode=obj.get('materialCode'),
			initCode=obj.get('initCode'),
			opGlobals=obj.get('opGlobals'),
			materialId=obj.get('materialId'),
			libraryNames=obj.get('libraryNames'),
			paramSource=obj.get('paramSource'),
			macros=[Macro(**m) for m in obj.get('macros', [])],
			constants=[Constant(**c) for c in obj.get('constants', [])],
			inputStates=[InputState(**i) for i in obj.get('inputStates', [])],
			textures=[Texture(**t) for t in obj.get('textures', [])],
			buffers=[Buffer(**b) for b in obj.get('buffers', [])],
			references=[Reference(**r) for r in obj.get('references', [])],
			attributes=[SurfaceAttribute(**a) for a in obj.get('attributes', [])],
			variables=[Variable(**v) for v in obj.get('variables', [])],
			validationErrors=[ValidationError(**e) for e in obj.get('validationErrors', [])],
			opElements=[OpElementState(**e) for e in obj.get('opElements', [])],
		)

	@classmethod
	def fromJson(cls, text: str):
		if not text:
			return
		return cls.fromDict(json.loads(text))

@dataclass
class InputState(_StateObject):
	functionName: str
	sourceName: str | None = None
	varNames: list[str] | None = None
	varInputNames: list[str] | None = None
	tags: list[str] | None = None
	placeholder: str | None = None
	coordType: list[str] | None = None
	contextType: list[str] | None = None
	returnType: list[str] | None = None

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
	name: str = ''
	localName: str = ''
	sourceName: str | None = None
	dataType: str = ''
	owner: str | None = None
	sourcePath: str | None = None
	category: str | None = None

@dataclass
class Variable(_StateObject):
	name: str = ''
	localName: str = ''
	label: str = ''
	dataType: str = ''
	owner: str = ''
	macros: str | None = None

@dataclass
class SurfaceAttribute(_StateObject):
	name: str = ''
	label: str = ''
	dataType: str = ''
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
class ParamSpec(_StateObject):
	name: str
	localName: str
	source: str
	style: str
	tupletName: str | None
	tupletLocalName: str | None
	vecIndex: int
	status: str | None = None
	handling: str | None = None
	conversion: str | None = None

@dataclass
class ParamTupletSpec(_StateObject):
	name: str
	localName: str
	source: str
	size: int
	style: str | None = None
	part1: str | None = None
	part2: str | None = None
	part3: str | None = None
	part4: str | None = None
	status: str | None = None
	conversion: str | None = None
	handling: str = 'runtime'
	localNames: list[str] | None = None
	sourceVectorPath: str | None = None
	sourceVectorIndex: int | None = None

@dataclass
class OpElementState(_StateObject):
	elementRoot: str
	isNested: bool
	paramGroupTable: str | None = None
	macroTable: str | None = None
	codeReplacements: dict[str, str] | None = None

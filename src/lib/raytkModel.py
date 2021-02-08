from dataclasses import dataclass, field
import dataclasses
import json
import re
from typing import Dict, Iterable, List, Optional, Union
import yaml

from raytkUtil import CoordTypes, ContextTypes, ReturnTypes, cleanDict, ROPInfo, InputInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	import _stubs.TDJSON as TDJSON
else:
	# noinspection PyUnresolvedReferences,PyUnboundLocalVariable
	TDJSON = op.TDModules.mod.TDJSON

@dataclasses.dataclass
class _DataObject_OLD:
	def toObj(self):
		raise NotImplementedError()

	@classmethod
	def fromObj(cls, obj):
		raise NotImplementedError()

	@classmethod
	def fromObjs(cls, objs: List[Dict]):
		return [cls.fromObj(obj) for obj in objs] if objs else []

	@classmethod
	def fromOptionalObj(cls, obj, default=None):
		return cls.fromObj(obj) if obj else default

	@classmethod
	def toObjs(cls, nodes: 'Optional[Iterable[_DataObject_OLD]]'):
		return [n.toObj() for n in nodes] if nodes else []

	@classmethod
	def toOptionalObj(cls, obj: '_DataObject_OLD'):
		return obj.toObj() if obj is not None else None

	@classmethod
	def parseJsonStr(cls, jsonStr: str):
		return cls.fromObj(_parseJson(jsonStr))

	def toJsonStr(self, minify=True):
		return _toJson(self.toObj(), minify=minify)

def _toJson(obj, minify=True):
	return '{}' if not obj else json.dumps(
		obj,
		indent=None if minify else '  ',
		separators=(',', ':') if minify else (',', ': '),
		sort_keys=True,
	)

def _parseJson(jsonStr: str):
	if jsonStr:
		jsonStr = jsonStr.strip()
	return json.loads(jsonStr) if jsonStr else {}

@dataclass
class TypeSpec(_DataObject_OLD):
	"""
	One or several possible data types.
	`*` is equivalent to all available types.
	`foo` is equivalent to one specific type.
	`foo|bar|baz` is equivalent to one of a list of possible types.
	"""
	isAll: bool = False
	types: List[str] = dataclasses.field(default_factory=list)

	def isSingle(self):
		return not self.isAll and len(self.types) == 1

	def __str__(self):
		if self.isAll:
			return '*'
		return '|'.join(self.types)

	@classmethod
	def parse(cls, s: str):
		if not s:
			return cls()
		if s == '*':
			return cls.all()
		return cls(types=s.split('|'))

	@classmethod
	def all(cls):
		return cls(isAll=True)

	def expand(self, allTypes: List[str]):
		if self.isAll:
			return list(allTypes)
		return list(filter(lambda t: t in allTypes, self.types))

	def expandedStr(self, allTypes: List[str]):
		return '|'.join(self.expand(allTypes))

	def supports(self, typeName: str):
		return self.isAll or typeName in self.types

	def toObj(self):
		return str(self)

	@classmethod
	def fromObj(cls, obj):
		return cls.parse(obj)

_typeSpecPatternPart = r'([\*\w|]+)'
_signaturePattern = re.compile(
	fr'\(\s*{_typeSpecPatternPart}\s*,\s*{_typeSpecPatternPart}\s*\)\s*->\s*{_typeSpecPatternPart}')

@dataclass
class FunctionSignature(_DataObject_OLD):
	"""
	Parameter and return types for a function.
	Can either be a single specific signature, or a collection of possible signatures.
	For example: "Takes in 2D coords and any type of context and returns either float or vec4",
	would be represented as:
	`(vec2, *) -> float|vec4`
	"""
	coordType: TypeSpec
	contextType: TypeSpec
	returnType: TypeSpec

	def __str__(self):
		return f'({self.coordType}, {self.contextType})->{self.returnType}'

	@classmethod
	def parse(cls, s: str):
		match = _signaturePattern.fullmatch(s.strip())
		if not match:
			raise ValueError('Invalid signature: ' + repr(s))
		return cls(
			coordType=TypeSpec.parse(match.group(1)),
			contextType=TypeSpec.parse(match.group(2)),
			returnType=TypeSpec.parse(match.group(3)),
		)

	@classmethod
	def parseOptional(cls, s: Optional[str]):
		return cls.parse(s) if s else None

	@classmethod
	def create(cls, coordType: str, contextType: str, returnType: str):
		return cls(
			coordType=TypeSpec.parse(coordType),
			contextType=TypeSpec.parse(contextType),
			returnType=TypeSpec.parse(returnType),
		)

	@classmethod
	def all(cls):
		return cls(
			coordType=TypeSpec.all(),
			contextType=TypeSpec.all(),
			returnType=TypeSpec.all())

	@classmethod
	def extractFromHandler(cls, inputHandler: 'COMP'):
		table = inputHandler.op('supported_type_table')
		if not table:
			return cls.all()
		return cls(
			coordType=TypeSpec.parse(str(table['coordType', 1] or '*')),
			contextType=TypeSpec.parse(str(table['contextType', 1] or '*')),
			returnType=TypeSpec.parse(str(table['returnType', 1] or '*')),
		)

	def isSingle(self):
		return self.coordType.isSingle() and self.contextType.isSingle() and self.returnType.isSingle()

	def expandAll(self) -> List['FunctionSignature']:
		coordTypes = self.coordType.expand(CoordTypes.values)
		contextTypes = self.contextType.expand(ContextTypes.values)
		returnTypes = self.returnType.expand(ReturnTypes.values)
		if self.isSingle():
			return [self]
		return [
			FunctionSignature.create(coord, ctx, ret)
			for ret in returnTypes
			for ctx in contextTypes
			for coord in coordTypes
		]

	def toObj(self):
		return str(self)

	@classmethod
	def fromObj(cls, obj):
		return cls.parse(obj)

@dataclass
class OpDefMeta_OLD(_DataObject_OLD):
	opType: Optional[str] = None
	opVersion: Optional[int] = None
	opStatus: Optional[str] = None

	def toObj(self):
		return cleanDict({
			'opType': self.opType,
			'opVersion': self.opVersion,
			'opStatus': self.opStatus,
		})

	@classmethod
	def fromObj(cls, obj: dict):
		return cls(**obj)

@dataclass
class OpSpec_OLD(_DataObject_OLD):
	meta: Optional[OpDefMeta_OLD] = None

	def toObj(self):
		return cleanDict({
			'meta': OpDefMeta_OLD.toOptionalObj(self.meta),
		})

	@classmethod
	def fromObj(cls, obj: dict):
		return cls(
			meta=OpDefMeta_OLD.fromOptionalObj(obj.get('meta')),
		)

@dataclass
class ModelObject(yaml.YAMLObject):
	@classmethod
	def to_yaml(cls, dumper: 'yaml.Dumper', data):
		return dumper.represent_mapping(cls.yaml_tag, data.toYamlDict())

	def toYamlDict(self):
		d = {}
		for f in dataclasses.fields(self):
			val = getattr(self, f.name)
			if _shouldInclude(val) and val != f.default:
				d[f.name] = val
		return d

def _shouldInclude(val):
	if val is None or val == '':
		return False
	if isinstance(val, (list, dict)) and not val:
		return False
	return True

@dataclass
class Expr(ModelObject):
	"""A Python parameter expression."""

	yaml_tag = u'!expr'

	expr: str

def _exprRepresenter(dumper: 'yaml.Dumper', data: 'Expr'):
	return dumper.represent_scalar(Expr.yaml_tag, data.expr, style='')

yaml.add_representer(Expr, _exprRepresenter)
yaml.add_implicit_resolver(Expr.yaml_tag, regexp=re.compile(r'^\$.*$'))

ValueOrExprT = Union[Expr, str, int, float, bool, None]
ValueOrListOrExprT = Union[ValueOrExprT, List[str]]

@dataclass
class File(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Spec for a DAT corresponding to an external file.

		Attributes:
			file: Path to the file, relative to the OP tox.
			name: Name of the associated DAT.
			evaluate: Whether the contents of the file should be evaluated
				as expressions.
	"""

	yaml_tag = u'!file'

	file: str
	name: Optional[str] = None
	evaluate: Optional[bool] = None

CellValueT = Union[str, int, float, bool]

@dataclass
class TableData(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Spec for an table DAT with inline content in the spec.

		Attributes:
			name: Name of the associated DAT.
			rows: List of rows, where each row is a list of cells.
			evaluate: Whether the contents of the table should be evaluated
				as expressions.
	"""

	yaml_tag = u'!table'

	name: Optional[str] = None
	rows: List[List[CellValueT]] = field(default_factory=list)
	evaluate: Optional[bool] = None

@dataclass
class TextData(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Spec for a text DAT with inline content in the spec.

			Attributes:
				name: Name of the associated DAT.
				text: Text for the DAT.
	"""

	yaml_tag = u'!text'

	name: Optional[str] = None
	text: Optional[str] = None


TableSetting = Union[File, TableData, None]
TextSetting = Union[File, TextData, None]

@dataclass
class OpMeta(ModelObject):
	yaml_tag = u'!meta'

	opType: str
	opVersion: int
	opStatus: Optional[str] = None

@dataclass
class InputSpec(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Specification for a ROP definition input.

		Attributes:
			name: Locally unique name for the input.
			label: User-friendly label for the input.
			required: Whether the input must be connected for the containing ROP to
				function properly.
			coordTypes: Coordinate types supported by the input.
				This is a string with space-separated names of types, or the literal
				'*' (meaning all types). Or it can be an Expr that evaluates to such a
				string.
			returnTypes: Return types supported by the input.
			contextTypes: Context types supported by the input.
	"""

	yaml_tag = u'!input'

	name: str
	label: Optional[str] = None

	required: bool = False

	coordTypes: ValueOrExprT = '*'
	returnTypes: ValueOrExprT = '*'
	contextTypes: ValueOrExprT = '*'

@dataclass
class MultiInputSpec(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Specification for a ROP multi-input.

		Attributes:
			inputs: Specs for potential inputs.
			minimumInputs: Minimum number of inputs required for the ROP to function
				properly.
	"""
	yaml_tag = u'!multiInput'

	inputs: List[InputSpec] = field(default_factory=list)
	minimumInputs: Optional[int] = None

@dataclass
class OpDef(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Definition for a ROP.

		Attributes:
			coordType: Name of the coordinate type or expression that produces it.
			returnType: Name of the return type or expression that produces it.
			contextType: Name of the context type or expression that produces it.

			disableInspect: Whether the ROP should disable the "Inspect" feature.

			opGlobals: Code block for global declarations used by the ROP.
				This can either be a Text object with inline content, a File
				object referring to an external file.
			initCode: Code block for initialization code that the ROP needs to run.
			function: Code block for the ROP's primary function.
			material: Code block for the ROP's material block.

			useParams: Spec for the names of ROP Pars that should be fed into the
				shader and made available to the ROP.
			specialParams: Spec for the names of values that come from a CHOP input
				and are made available to the ROP.
			angleParams: Spec for names of ROP Pars that should be converted to
				radians before being passed to the shader.
			macroParams: Spec for names of ROP Pars that should be made available to
				the ROP as preprocessor definitions.
			libraryNames: Spec for names of shared libraries that the ROP depends on.

			bufferTable: Spec for a table of CHOP-based buffers passed to the shader.
			textureTable: Spec for a table of TOP-based textures passed to the shader.
			macroTable: Spec for a table of macros generated for the ROP.

			help: Spec for help text for the ROP.

			callbacks: Code block of Python callback functions used by the ROP.
		"""

	yaml_tag = u'!def'

	coordType: ValueOrExprT = 'useinput'
	returnType: ValueOrExprT = 'useinput'
	contextType: ValueOrExprT = 'useinput'

	disableInspect: bool = False

	opGlobals: TextSetting = None
	initCode: TextSetting = None
	function: TextSetting = None
	material: TextSetting = None

	useParams: ValueOrListOrExprT = None
	specialParams: ValueOrListOrExprT = None
	angleParams: ValueOrListOrExprT = None
	macroParams: ValueOrListOrExprT = None
	libraryNames: ValueOrListOrExprT = None

	bufferTable: TableSetting = None
	textureTable: TableSetting = None
	macroTable: TableSetting = None

	help: TextSetting = None
	callbacks: TextSetting = None

@dataclass
class ParamPage(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Specification for a page of OP parameters.

		Attributes:
			name: Name of the page
			pars: Dict of parameter specs in the format supported by TDJSON.
	"""

	yaml_tag = '!page'

	name: str
	pars: Dict[str, dict] = field(default_factory=list)

	def __post_init__(self):
		for parObj in self.pars.values():
			_cleanParamSpecObj(parObj)

def _cleanParamSpecObj(obj: dict):
	if not obj:
		return
	if 'page' in obj:
		del obj['page']
	defaultVals = {
		'enable': True,
		'startSection': False,
		'readOnly': False,
		'enableExpr': None,
	}
	for key, defVal in defaultVals.items():
		if key in obj and obj[key] == defVal:
			del obj[key]

@dataclass
class OpSpec(ModelObject):
	yaml_tag = u'!opSpec'

	meta: Optional[OpMeta] = None
	opDef: OpDef = field(default_factory=OpDef)

	paramPages: List[ParamPage] = field(default_factory=dict)

	multiInput: Optional[MultiInputSpec] = None
	inputs: Optional[List[InputSpec]] = field(default_factory=list)

def extractOpSpec(rop: 'COMP') -> OpSpec:
	info = ROPInfo(rop)
	spec = OpSpec(
		meta=OpMeta(
			opType=info.opType,
			opVersion=info.opVersion,
			opStatus=info.statusLabel,
		),
		opDef=OpDef(
			coordType=_valueOrExprFromPar(info.opDefPar.Coordtype),
			returnType=_valueOrExprFromPar(info.opDefPar.Returntype),
			contextType=_valueOrExprFromPar(info.opDefPar.Contexttype),
			disableInspect=info.opDefPar.Disableinspect.eval(),
			useParams=_valueOrExprFromPar(info.opDefPar.Params),
			specialParams=_valueOrExprFromPar(info.opDefPar.Specialparams),
			angleParams=_valueOrExprFromPar(info.opDefPar.Angleparams),
			macroParams=_valueOrExprFromPar(info.opDefPar.Macroparams),
			libraryNames=_valueOrExprFromPar(info.opDefPar.Librarynames),
			opGlobals=_extractDatSetting(info.opDefPar.Opglobals),
			initCode=_extractDatSetting(info.opDefPar.Initcode),
			function=_extractDatSetting(info.opDefPar.Functemplate),
			help=_extractDatSetting(info.opDefPar.Help),
			callbacks=_extractDatSetting(info.opDefPar.Callbacks),
			bufferTable=_extractDatSetting(info.opDefPar.Buffertable),
			macroTable=_extractDatSetting(info.opDefPar.Macrotable),
			textureTable=_extractDatSetting(info.opDefPar.Texturetable),
		),
	)
	spec.paramPages = [
		_extractParamPage(page)
		for page in rop.customPages
	]
	multiHandler = info.multiInputHandler
	if multiHandler:
		spec.multiInput = MultiInputSpec(
			minimumInputs=multiHandler.par.Minimuminputs.eval() if multiHandler.par.Minimuminputs > 0 else None,
		)
	for inputHandler in info.inputHandlers:
		inputInfo = InputInfo(inputHandler)
		if inputInfo.multiHandler:
			spec.multiInput.inputs.append(_extractInputSpec(inputHandler))
		else:
			spec.inputs.append(_extractInputSpec(inputHandler))
	return spec

_ignorePars = 'Help', 'Inspect', 'Updateop'

def _extractParamPage(page: 'Page') -> ParamPage:
	return ParamPage(
		name=page.name,
		pars={
			parTuplet[0].tupletName: dict(TDJSON.parameterToJSONPar(parTuplet[0]))
			for parTuplet in page.parTuplets
			if parTuplet[0].tupletName not in _ignorePars
		},
	)

def _extractInputSpec(handler: 'COMP') -> InputSpec:
	info = InputInfo(handler)
	return InputSpec(
		name=info.name,
		label=info.label,
		required=info.required,
		coordTypes=_extractInputSupportSetting(info.handlerPar.Supportcoordtypes, info.supportedCoordTypes),
		returnTypes=_extractInputSupportSetting(info.handlerPar.Supportreturntypes, info.supportedReturnTypes),
		contextTypes=_extractInputSupportSetting(info.handlerPar.Supportcontexttypes, info.supportedContextTypes),
	)

def _extractInputSupportSetting(par: 'Par', expandedList: List[str]) -> ValueOrExprT:
	if par.mode == ParMode.EXPRESSION:
		return Expr(par.expr)
	elif par.mode == ParMode.CONSTANT:
		if par.val == '*':
			return '*'
		return ' '.join(expandedList)
	else:
		raise Exception(f'Unsupported input supported type parameter mode {par.mode} for {par!r}')

def _valueOrExprFromPar(par: Optional['Par']) -> ValueOrExprT:
	if par is None:
		return None
	if par.mode == ParMode.CONSTANT:
		if par.val == '':
			return None
		return par.val
	if par.mode == ParMode.EXPRESSION:
		return Expr(par.expr)
	raise Exception(f'Parameter mode {par.mode} not supported for {par!r}')

def _extractDatSetting(par: Optional['Par']) -> Union[TextSetting, TableSetting]:
	if par is None:
		return None
	if par.mode != ParMode.CONSTANT:
		raise Exception(f'Parameter mode {par.mode} not supported for {par!r}')
	if not par:
		return None
	from raytkTools import EditorItemGraph
	graph = EditorItemGraph.fromPar(par)
	if not graph.supported:
		raise Exception(f'DAT setup not supported for {par!r}')
	if graph.file:
		return File(
			graph.file.eval(),
			name=graph.sourceDat.name,
			evaluate=graph.hasEval or None,
		)
	if graph.endDat.isTable:
		return _extractTableData(
			graph.sourceDat,
			hasEval=graph.hasEval,
		)
	else:
		return _extractTextData(graph.sourceDat)

def _extractTableData(dat: 'DAT', hasEval: bool = False):
	return TableData(
		name=dat.name,
		rows=[
			[cell.val for cell in row]
			for row in dat.rows()
		],
		evaluate=hasEval or None,
	)

def _extractTextData(dat: 'DAT'):
	return TextData(
		name=dat.name,
		text=dat.text,
	)

from dataclasses import dataclass, field
import dataclasses
import json
import re
from typing import Dict, Iterable, List, Optional, Union
import yaml

from raytkUtil import CoordTypes, ContextTypes, ReturnTypes, cleanDict, ROPInfo, InputInfo, RaytkTags

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

CellValueT = Union[str, int, float, bool]

@dataclass
class TableData(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Spec for an table DAT with either inline content or an external file.

		Attributes:
			name: Name of the associated DAT.
			file: Path to the file, relative to the project root.
			rows: List of rows, where each row is a list of cells.
			evaluate: Whether the contents of the table should be evaluated
				as expressions.
	"""

	yaml_tag = u'!table'

	file: Optional[str] = None
	name: Optional[str] = None
	rows: List[List[CellValueT]] = field(default_factory=list)
	evaluate: Optional[bool] = None

@dataclass
class TextData(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Spec for a text DAT with either inline content or an external file.

		Attributes:
			name: Name of the associated DAT.
			file: Path to the file, relative to the project root.
			text: Text for the DAT.
	"""

	yaml_tag = u'!text'

	file: Optional[str] = None
	name: Optional[str] = None
	text: Optional[str] = None

@dataclass
class ROPMeta(ModelObject):
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
class ROPDef(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Definition for a ROP.

		Attributes:
			coordType: Name of the coordinate type or expression that produces it.
			returnType: Name of the return type or expression that produces it.
			contextType: Name of the context type or expression that produces it.

			disableInspect: Whether the ROP should disable the "Inspect" feature.

			opGlobals: Code block for global declarations used by the ROP.
				This is a TextData object with either inline content or a reference to
				an external file.
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

	opGlobals: Optional[TextData] = None
	initCode: Optional[TextData] = None
	function: Optional[TextData] = None
	material: Optional[TextData] = None

	useParams: ValueOrListOrExprT = None
	specialParams: ValueOrListOrExprT = None
	angleParams: ValueOrListOrExprT = None
	macroParams: ValueOrListOrExprT = None
	libraryNames: ValueOrListOrExprT = None

	bufferTable: Optional[TableData] = None
	textureTable: Optional[TableData] = None
	macroTable: Optional[TableData] = None

	help: Optional[TextData] = None
	callbacks: Optional[TextData] = None

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
class ROPSpec(ModelObject):
	yaml_tag = u'!rop'

	meta: Optional[ROPMeta] = None
	opDef: ROPDef = field(default_factory=ROPDef)

	paramPages: List[ParamPage] = field(default_factory=dict)

	multiInput: Optional[MultiInputSpec] = None
	inputs: Optional[List[InputSpec]] = field(default_factory=list)

def extractOpSpec(rop: 'COMP', skipParams=False) -> ROPSpec:
	info = ROPInfo(rop)
	spec = ROPSpec(
		meta=ROPMeta(
			opType=info.opType,
			opVersion=info.opVersion,
			opStatus=info.statusLabel,
		),
		opDef=ROPDef(
			coordType=_valueOrExprFromPar(info.opDefPar.Coordtype),
			returnType=_valueOrExprFromPar(info.opDefPar.Returntype),
			contextType=_valueOrExprFromPar(info.opDefPar.Contexttype),
			disableInspect=info.opDefPar.Disableinspect.eval(),
			useParams=_valueOrExprFromPar(info.opDefPar.Params),
			specialParams=_valueOrExprFromPar(info.opDefPar.Specialparams),
			angleParams=_valueOrExprFromPar(info.opDefPar.Angleparams),
			macroParams=_valueOrExprFromPar(info.opDefPar.Macroparams),
			libraryNames=_valueOrExprFromPar(info.opDefPar.Librarynames),
			opGlobals=_extractDatSetting(info.opDefPar.Opglobals, isText=True),
			initCode=_extractDatSetting(info.opDefPar.Initcode, isText=True),
			function=_extractDatSetting(info.opDefPar.Functemplate, isText=True),
			help=_extractDatSetting(info.opDefPar.Help, isText=True),
			callbacks=_extractDatSetting(info.opDefPar.Callbacks, isText=True),
			bufferTable=_extractDatSetting(info.opDefPar.Buffertable, isText=False),
			macroTable=_extractDatSetting(info.opDefPar.Macrotable, isText=False),
			textureTable=_extractDatSetting(info.opDefPar.Texturetable, isText=False),
		),
	)
	if not skipParams:
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

def _extractDatSetting(par: Optional['Par'], isText: bool) -> Union[TextData, TableData, None]:
	if par is None:
		return None
	if par.mode != ParMode.CONSTANT:
		raise Exception(f'Parameter mode {par.mode} not supported for {par!r}')
	if not par:
		return None
	graph = EditorItemGraph.fromPar(par)
	if not graph.supported:
		raise Exception(f'DAT setup not supported for {par!r}')
	if graph.file:
		if isText:
			return TextData(
				file=graph.file.eval(),
				name=graph.sourceDat.name,
			)
		else:
			return TableData(
				file=graph.file.eval(),
				name=graph.sourceDat.name,
				evaluate=graph.hasEval or None,
			)
	if graph.endDat.isTable:
		return TableData(
			name=graph.sourceDat.name,
			rows=[
				[cell.val for cell in row]
				for row in graph.sourceDat.rows()
			],
			evaluate=graph.hasEval or None,
		)
	else:
		return TextData(
			name=graph.sourceDat.name,
			text=graph.sourceDat.text,
		)

@dataclass
class EditorItemGraph:
	par: 'Par'
	endDat: 'Optional[DAT]' = None
	sourceDat: 'Optional[DAT]' = None
	hasEval: bool = False
	hasMerge: bool = False
	supported: bool = False
	file: 'Optional[Par]' = None

	@classmethod
	def fromPar(cls, par: 'Par'):
		endDat = par.eval()  # type: Optional[DAT]
		if not endDat:
			return cls(par, supported=True)
		if isinstance(endDat, (tableDAT, textDAT)):
			return cls(
				par,
				endDat=endDat,
				sourceDat=endDat,
				hasEval=False,
				hasMerge=False,
				supported=True,
				file=endDat.par['file'],
			)
		dat = endDat
		if isinstance(dat, nullDAT):
			if not dat.inputs:
				return cls(par, supported=False)
			dat = dat.inputs[0]
		hasEval = False
		hasMerge = False
		if isinstance(dat, evaluateDAT):
			if not dat.inputs:
				return cls(par, endDat=endDat, supported=False)
			hasEval = True
			dat = dat.inputs[0]
		if isinstance(dat, (tableDAT, textDAT)):
			return cls(
				par,
				endDat=endDat,
				sourceDat=dat,
				hasMerge=hasMerge,
				hasEval=hasEval,
				supported=True,
				file=dat.par['file'],
			)
		return cls(par, supported=False)

class ROPSpecLoader:
	def __init__(self, rop: 'COMP', spec: ROPSpec):
		self.rop = rop
		self.info = ROPInfo(rop)
		self.spec = spec

	def loadSpec(self):
		self._removeGeneratedOps()
		self._loadMeta()
		self._loadParamPages()
		self._loadOpDefSettings()
		self._loadOpDefTextBlocks()
		self._loadOpDefTables()
		self._loadInputs()

	def _removeGeneratedOps(self):
		for o in self.rop.children:
			if o.valid and RaytkTags.generated.name in o.tags:
				try:
					o.destroy()
				except:
					pass

	def _loadMeta(self):
		meta = self.spec.meta
		if not meta:
			return
		self.info.opVersion = meta.opVersion
		self.info.opType = meta.opType

	def _loadParamPages(self):
		newNames = [pageSpec.name for pageSpec in self.spec.paramPages]
		for page in list(self.rop.customPages):
			if page.name not in newNames:
				page.destroy()
		for pageSpec in self.spec.paramPages:
			TDJSON.addParametersFromJSONList(self.rop, pageSpec.pars.values())

	def _loadInputs(self):
		raise NotImplementedError()

	def _loadOpDefSettings(self):
		p = self.info.opDefPar
		d = self.spec.opDef
		_updatePar(p.Coordtype, d.coordType)
		_updatePar(p.Returntype, d.returnType)
		_updatePar(p.Contexttype, d.contextType)
		_updatePar(p.Disableinspect, d.disableInspect)

		_updatePar(p.Params, d.useParams)
		_updatePar(p.Specialparams, d.specialParams)
		_updatePar(p.Angleparams, d.angleParams)
		_updatePar(p.Macroparams, d.macroParams)
		_updatePar(p.Librarynames, d.libraryNames)

	def _loadOpDefTextBlocks(self):
		p = self.info.opDefPar
		d = self.spec.opDef
		x = -100
		y = -500
		self._loadTextSetting(p.Functemplate, d.function, defaultName='function', x=x, y=200)
		self._loadTextSetting(p.Opglobals, d.opGlobals, defaultName='globals', x=x, y=y)
		y -= 150
		self._loadTextSetting(p.Initcode, d.initCode, defaultName='init', x=x, y=y)
		y -= 150
		self._loadTextSetting(p.Materialcode, d.material, defaultName='material', x=x, y=y)
		self._loadTextSetting(p.Callbacks, d.callbacks, defaultName='callbacks', x=200, y=200)
		self._loadTextSetting(p.Help, d.help, defaultName='help', x=0, y=400)

	def _loadOpDefTables(self):
		p = self.info.opDefPar
		d = self.spec.opDef
		x = -400
		y = -100
		self._loadTableSetting(p.Macrotable, d.macroTable, defaultName='macros', x=x, y=y)
		y -= 150
		self._loadTableSetting(p.Buffertable, d.bufferTable, defaultName='buffers', x=x, y=y)
		y -= 150
		self._loadTableSetting(p.Texturetable, d.textureTable, defaultName='textures', x=x, y=y)

	def _loadTextSetting(
			self,
			par: 'Par',
			val: Optional[TextData],
			defaultName: str,
			x: int, y: int):
		if val is None:
			_setParVal(par, '')
			return
		srcDat = self.rop.create(textDAT, val.name or defaultName)
		srcDat.nodeX = x
		srcDat.nodeY = y
		RaytkTags.generated.apply(srcDat, True)
		if val.file:
			srcDat.par.file = val.file
			srcDat.par.loadonstartpulse.pulse()
			RaytkTags.fileSync.apply(srcDat, True)
		else:
			srcDat.text = val.text or ''
		_setParVal(par, srcDat)

	def _loadTableSetting(
			self,
			par: 'Par',
			val: Optional[TableData],
			defaultName: str,
			x: int, y: int):
		if val is None:
			_setParVal(par, '')
			return
		srcDat = self.rop.create(tableDAT, val.name or defaultName)
		srcDat.nodeX = x
		srcDat.nodeY = y
		RaytkTags.generated.apply(srcDat, True)
		if val.file:
			srcDat.par.file = val.file
			srcDat.par.loadonstartpulse.pulse()
			RaytkTags.fileSync.apply(srcDat, True)
		else:
			srcDat.clear()
			for row in val.rows:
				srcDat.appendRow(row)
		if not val.evaluate:
			_setParVal(par, srcDat)
		else:
			evalDat = self.rop.create(evaluateDAT, 'eval_' + srcDat.name)
			RaytkTags.generated.apply(evalDat, True)
			evalDat.nodeX = srcDat.nodeX + 150
			evalDat.nodeY = srcDat.nodeY
			evalDat.inputConnectors[0].connect(srcDat)
			_setParVal(par, evalDat)

def _updatePar(par: 'Par', val: ValueOrListOrExprT):
	if val is None:
		_setParVal(par, par.default)
	elif isinstance(val, Expr):
		if not val.expr:
			_setParVal(par, '')
		else:
			_setParExpr(par, val.expr)
	elif isinstance(val, list):
		_setParVal(par, ' '.join(val))
	else:
		_setParVal(par, val)

def _setParVal(par: 'Par', val):
	par.val = val if val is not None else ''
	par.expr = ''
	par.mode = ParMode.CONSTANT

def _setParExpr(par: 'Par', expr: str):
	par.val = ''
	par.expr = expr
	par.mode = ParMode.EXPRESSION

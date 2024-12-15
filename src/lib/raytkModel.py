"""
Toolkit model which works with operator type specifications and metadata.

This should only be used within development tools.
"""

from dataclasses import dataclass, field
import dataclasses
from io import StringIO
from pathlib import Path
import re
import yaml

from raytkUtil import ROPInfo, InputInfo, RaytkTags, OpDefParsT

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from _typeAliases import *
	import _stubs.TDJSON as TDJSON
else:
	# noinspection PyUnresolvedReferences,PyUnboundLocalVariable
	TDJSON = op.TDModules.mod.TDJSON

@dataclass
class ModelObject(yaml.YAMLObject):
	yaml_loader = yaml.FullLoader

	@classmethod
	def to_yaml(cls, dumper: yaml.Dumper, data):
		return dumper.represent_mapping(cls.yaml_tag, data.toYamlDict())

	@classmethod
	def parseFromText(cls, text: str):
		return yaml.load(StringIO(text), Loader=cls.yaml_loader)

	def toYamlDict(self):
		d = {}
		for f in dataclasses.fields(self):
			val = getattr(self, f.name, None)
			if _shouldInclude(val) and val != f.default:
				d[f.name] = val
		return d

	def writeToFile(self, file: Path | str):
		file = Path(file)
		text = self.toYamlText()
		file.write_text(text)

	def toYamlText(self):
		return yaml.dump(self, default_style='', sort_keys=False)

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

def _exprRepresenter(dumper: yaml.Dumper, data: Expr):
	return dumper.represent_scalar(Expr.yaml_tag, data.expr, style='')

# yaml.add_representer(Expr, _exprRepresenter)
yaml.add_implicit_resolver(Expr.yaml_tag, regexp=re.compile(r'^\$.*$'), Loader=ModelObject.yaml_loader)

ValueOrExprT = Expr | str | int | float | bool | None
ValueOrListOrExprT = ValueOrExprT | list[str]

CellValueT = str | int | float | bool

@dataclass
class EvalDatOptions(ModelObject):
	yaml_tag = u'!evalOpts'

	excludeFirstRow: bool = False
	excludeFirstCol: bool = False
	rows: str | None = '*'
	cols: str | None = '*'

	@classmethod
	def fromDat(cls, dat: evaluateDAT | None):
		if not dat:
			return None
		return cls(
			excludeFirstRow=dat.par.xfirstrow.eval(),
			excludeFirstCol=dat.par.xfirstcol.eval(),
			rows=_extractDatEvalPart(dat.par.extractrows, dat.par.rownames),
			cols=_extractDatEvalPart(dat.par.extractcols, dat.par.colnames),
		)

	def isAllDefaults(self):
		if self.excludeFirstRow or self.excludeFirstCol:
			return False
		return self.rows != '*' or self.cols != '*'

def _extractDatEvalPart(modePar: Par, namesPar: Par):
	if modePar.mode != ParMode.CONSTANT:
		raise Exception(f'Unsupported mode for {modePar!r}')
	if namesPar.mode != ParMode.CONSTANT:
		raise Exception(f'Unsupported mode for {namesPar!r}')
	if modePar == 'all':
		return '*'
	elif modePar == 'bynames':
		return namesPar.val
	raise Exception(f'Unsupported eval dat scope mode: {modePar!r}')

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

	file: str | None = None
	name: str | None = None
	rows: list[list[CellValueT]] = field(default_factory=list)
	evaluate: bool | None = None
	evalOpts: EvalDatOptions | None = None

	def toYamlDict(self):
		obj = super().toYamlDict()
		if not obj.get('evaluate') and 'evalOpts' in obj:
			del obj['evalOpts']
		elif self.evalOpts and self.evalOpts.isAllDefaults():
			del obj['evalOpts']
		return obj

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

	file: str | None = None
	name: str | None = None
	text: str | None = None

@dataclass
class ROPMeta(ModelObject):
	yaml_tag = u'!meta'

	opType: str = ''
	opVersion: int = 0
	opStatus: str | None = None
	
	@classmethod
	def fromRopInfo(cls, ropInfo: ROPInfo):
		obj = cls()
		obj.updateFromRopInfo(ropInfo)
		return obj

	def updateFromRopInfo(self, ropInfo: ROPInfo):
		self.opType = ropInfo.opType
		self.opVersion = ropInfo.opVersion
		self.opStatus = ropInfo.statusLabel

	def applyToRopInfo(self, ropInfo: ROPInfo):
		ropInfo.opType = self.opType
		ropInfo.opVersion = self.opVersion
		ropInfo.setOpStatus(self.opStatus)

@dataclass
class CoordTypes(ModelObject):
	yaml_tag = u'!coordT'

	Allcoordtype: ValueOrExprT = None
	Coordtypefloat: ValueOrExprT = None
	Coordtypevec2: ValueOrExprT = None
	Coordtypevec3: ValueOrExprT = None
	Coordtypevec4: ValueOrExprT = None

	@classmethod
	def fromComp(cls, specComp: COMP):
		return cls(**_valOrExprDictFromPars(specComp.pars('Allcoordtype', 'Coordtype*')))

	def toYamlDict(self):
		if self.Allcoordtype is True:
			return {'Allcoordtype': True}
		return _excludeFalseVals(super().toYamlDict())

@dataclass
class ContextTypes(ModelObject):
	yaml_tag = u'!contextT'

	Allcontexttype: ValueOrExprT = None
	Contexttypecontext: ValueOrExprT = None
	Contexttypematerialcontext: ValueOrExprT = None
	Contexttypecameracontext: ValueOrExprT = None
	Contexttypelightcontext: ValueOrExprT = None
	Contexttyperaycontext: ValueOrExprT = None
	Contexttypevertexcontext: ValueOrExprT = None
	Contexttypepixelcontext: ValueOrExprT = None

	@classmethod
	def fromComp(cls, specComp: COMP):
		return cls(**_valOrExprDictFromPars(specComp.pars('Allcontexttype', 'Contexttype*')))

	def toYamlDict(self):
		if self.Allcontexttype is True:
			return {'Allcontexttype': True}
		return _excludeFalseVals(super().toYamlDict())

@dataclass
class ReturnTypes(ModelObject):
	yaml_tag = u'!returnT'

	Allreturntype: ValueOrExprT = None
	Returntypesdf: ValueOrExprT = None
	Returntypefloat: ValueOrExprT = None
	Returntypevec4: ValueOrExprT = None
	Returntyperay: ValueOrExprT = None
	Returntypelight: ValueOrExprT = None
	Returntypevolume: ValueOrExprT = None

	@classmethod
	def fromComp(cls, specComp: COMP):
		return ReturnTypes(**_valOrExprDictFromPars(specComp.pars('Allreturntype', 'Returntype*')))

	def toYamlDict(self):
		if self.Allreturntype is True:
			return {'Allreturntype': True}
		return _excludeFalseVals(super().toYamlDict())

def _excludeFalseVals(obj: dict):
	if not obj:
		return obj
	return {
		key: val
		for key, val in obj.items()
		if val is not False
	}
	pass

@dataclass
class InputSpec(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Specification for a ROP definition input.

		Attributes:
			Name: Locally unique name for the input.
			Label: User-friendly label for the input.
			Required: Whether the input must be connected for the containing ROP to
				function properly.
			coordType: Coordinate types supported by the input.
				This is a string with space-separated names of types, or the literal
				'*' (meaning all types). Or it can be an Expr that evaluates to such a
				string.
			returnType: Return types supported by the input.
			contextType: Context types supported by the input.
	"""
	yaml_tag = u'!input'

	Source: ValueOrExprT = None
	Name: ValueOrExprT = None
	Label: ValueOrExprT = None
	Localalias: ValueOrExprT = None
	Help: ValueOrExprT = None
	Variables: ValueOrExprT = None
	Variableinputs: ValueOrExprT = None

	Required: ValueOrExprT = False
	Prohibited: ValueOrExprT = False

	coordType: CoordTypes | None = None
	contextType: ContextTypes | None = None
	returnType: ReturnTypes | None = None

	@classmethod
	def fromComp(cls, handler: COMP):
		return cls(
			coordType=CoordTypes.fromComp(handler),
			contextType=ContextTypes.fromComp(handler),
			returnType=ReturnTypes.fromComp(handler),
			**_valOrExprDictFromPars(handler.pars(
				'Source', 'Name', 'Label', 'Localalias', 'Help', 'Required', 'Prohibited', 'Variables', 'Variableinputs')))

	@classmethod
	def fromCompList(cls, handlers: list[COMP], forMulti: bool):
		return [
			cls.fromComp(handler)
			for handler in handlers
			if forMulti == (InputInfo(handler).multiHandler is not None)
		]

@dataclass
class MultiInputSpec(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Specification for a ROP multi-input.

		Attributes:
			Minimuminputs: Minimum number of inputs required for the ROP to function
				properly.
	"""
	yaml_tag = u'!multiInput'

	Minimuminputs: ValueOrExprT = None

	Coordtypereductionmode: ValueOrExprT = None
	Coordtypereductionscope: ValueOrListOrExprT = None
	Coordtypepreference: ValueOrListOrExprT = None

	Contexttypereductionmode: ValueOrExprT = None
	Contexttypereductionscope: ValueOrListOrExprT = None
	Contexttypepreference: ValueOrListOrExprT = None

	Returntypereductionmode: ValueOrExprT = None
	Returntypereductionscope: ValueOrListOrExprT = None
	Returntypepreference: ValueOrListOrExprT = None

	inputs: list[InputSpec] = field(default_factory=list)

	@classmethod
	def fromComps(cls, multiHandler: COMP, inputHandlers: list[COMP]):
		if not multiHandler:
			return None
		return cls(
			inputs=InputSpec.fromCompList(inputHandlers, True),
			**_valOrExprDictFromPars(multiHandler.pars(
				'Minimuminputs', 'Coordtype*', 'Contexttype*', 'Returntype*'))
		)
def _setParValsFromDict(o: OP, parVals: dict):
	for name, val in parVals.items():
		o.par[name] = val

@dataclass
class ROPTypeSpec(ModelObject):
	yaml_tag = u'!ropTypes'

	Useinputcoordtype: ValueOrExprT = True
	Useinputcontexttype: ValueOrExprT = True
	Useinputreturntype: ValueOrExprT = True

	coordType: CoordTypes | None = None
	contextType: ContextTypes | None = None
	returnType: ReturnTypes | None = None

	@classmethod
	def fromComp(cls, specComp: COMP):
		if not specComp:
			return None
		return cls(
			coordType=CoordTypes.fromComp(specComp),
			contextType=ContextTypes.fromComp(specComp),
			returnType=ReturnTypes.fromComp(specComp),
			**_valOrExprDictFromPars(specComp.pars('Useinput*')))

	def applyTo(self, specComp: COMP):
		specComp.par.Useinputcoordtype = self.Useinputcoordtype
		specComp.par.Useinputcontexttype = self.Useinputcontexttype
		specComp.par.Useinputreturntype = self.Useinputreturntype
		if self.coordType == '*':
			specComp.par.Allcoordtype = True
		else:
			specComp.par.Allcoordtype = False
			_setParValsFromDict(specComp, self.coordType.toYamlDict())
		if self.contextType == '*':
			specComp.par.Allcontexttype = True
		else:
			specComp.par.Allcontexttype = False
			_setParValsFromDict(specComp, self.contextType.toYamlDict())
		if self.returnType == '*':
			specComp.par.Allreturntype = True
		else:
			specComp.par.Allreturntype = False
			_setParValsFromDict(specComp, self.returnType.toYamlDict())

	def toYamlDict(self):
		obj = super().toYamlDict()
		for key in ('Useinputcoordtype', 'Useinputcontexttype', 'Useinputreturntype'):
			if obj.get(key) is False:
				del obj[key]
		return obj

_TableSetting = TableData | Expr | None
_TextSetting = TextData | Expr | None

@dataclass
class ExternalSpec(ModelObject):
	yaml_tag = u'!external'

	file: str

	def resolve(self):
		if not self.file:
			return None
		file = Path(self.file)
		text = file.read_text()
		if not text.strip():
			return None
		return yaml.load(text)

@dataclass
class NoneSpec(ModelObject):
	"""
	Indicates that something is explicitly being set as None or an empty list/dict.

	This makes it possible to differentiate between a setting being omitted (and
	therefore kept as it is in the tox) vs it being intentionally set to being empty
	or missing (which would cause it to be cleared out in the tox).
	"""

	yaml_tag = u'!none'

@dataclass
class ROPDef(ModelObject):
	# noinspection PyUnresolvedReferences
	"""Definition for a ROP.

		Attributes:
			disableInspect: Whether the ROP should disable the "Inspect" feature.

			typeSpec: Settings for the ROP's coord/context/return types.
			opGlobals: Code block for global declarations used by the ROP.
				This is a TextData object with either inline content or a reference to
				an external file.
			initCode: Code block for initialization code that the ROP needs to run
				once per shader execution.
			function: Code block for the ROP's primary function.
			material: Code block for the ROP's material block.

			libraryNames: Spec for names of shared libraries that the ROP depends on.

			bufferTable: Spec for a table of CHOP-based buffers passed to the shader.
			textureTable: Spec for a table of TOP-based textures passed to the shader.
			macroTable: Spec for a table of macros generated for the ROP.

			help: Spec for help text for the ROP.

			callbacks: Code block of Python callback functions used by the ROP.
		"""

	yaml_tag = u'!def'

	enable: ValueOrExprT = None
	useRuntimeBypass: ValueOrExprT = False
	paramsOp: ValueOrExprT = None
	disableInspect: bool = False

	typeSpec: ROPTypeSpec | ExternalSpec | None = None

	opGlobals: _TextSetting = None
	init: _TextSetting = None
	function: _TextSetting = None
	material: _TextSetting = None
	callbacks: _TextSetting = None

	lockParams: ValueOrListOrExprT = None

	paramGroupTable: _TableSetting = None

	libraryNames: ValueOrListOrExprT = None

	bufferTable: _TableSetting = None
	textureTable: _TableSetting = None
	macroTable: _TableSetting = None
	variableTable: _TableSetting = None
	referenceTable: _TableSetting = None
	tagTable: _TableSetting = None

	generatedMacroTables: ValueOrExprT = None

	help: _TextSetting = None
	keywords: ValueOrListOrExprT = None
	shortcuts: ValueOrListOrExprT = None
	displayCategory: ValueOrExprT = None
	flags: ValueOrListOrExprT = None

	@classmethod
	def fromComp(cls, opDefComp: COMP):
		obj = cls()
		obj.updateFromComp(opDefComp)
		return obj

	def updateFromComp(self, opDefComp: COMP):
		# noinspection PyTypeChecker
		pars = opDefComp.par  # type: OpDefParsT
		self.enable = _valOrExprFromPar(pars.Enable)
		self.useRuntimeBypass = _valOrExprFromPar(pars.Useruntimebypass)
		self.paramsOp = _valOrExprFromPar(pars.Paramsop)

		self.typeSpec = ROPTypeSpec.fromComp(pars.Typespec.eval())

		self.opGlobals = _extractDatSetting(pars.Opglobals)
		self.init = _extractDatSetting(pars.Initcode)
		self.function = _extractDatSetting(pars.Functemplate)
		self.material = _extractDatSetting(pars.Materialcode)
		self.callbacks = _extractDatSetting(pars.Callbacks)

		self.lockParams = _valOrExprFromPar(pars.Lockpars, useList=True)

		self.paramGroupTable = _valOrExprFromPar(pars.Paramgrouptable)

		self.libraryNames = _valOrExprFromPar(pars.Librarynames, useList=True)

		self.bufferTable = _extractDatSetting(pars.Buffertable)
		self.textureTable = _extractDatSetting(pars.Texturetable)
		self.macroTable = _extractDatSetting(pars.Macrotable)
		self.variableTable = _extractDatSetting(pars.Variabletable)
		self.referenceTable = _extractDatSetting(pars.Referencetable)
		self.tagTable = _extractDatSetting(pars.Tagtable)

		self.generatedMacroTables = _valOrExprFromPar(pars.Generatedmacrotables)

		self.help = _extractDatSetting(pars.Help)
		self.keywords = _valOrExprFromPar(pars.Keywords, useList=True)
		self.shortcuts = _valOrExprFromPar(pars.Shortcuts, useList=True)
		self.displayCategory = _valOrExprFromPar(pars.Displaycategory)
		self.flags = _valOrExprFromPar(pars.Flags, useList=True)

	def applyToComp(self, opDefComp: COMP):
		# noinspection PyTypeChecker
		pars = opDefComp.par  # type: OpDefParsT

		_updatePar(pars.Enable, self.enable)
		_updatePar(pars.Useruntimebypass, self.useRuntimeBypass)
		_updatePar(pars.Paramsop, self.paramsOp)

		if self.typeSpec:
			typeSpecComp = pars.Typespec.eval()
			self.typeSpec.applyTo(typeSpecComp)

		_updatePar(pars.Lockpars, self.lockParams)

		_updatePar(pars.Paramgrouptable, self.paramGroupTable)

		_updatePar(pars.Librarynames, self.libraryNames)

		_updatePar(pars.Generatedmacrotables, self.generatedMacroTables)

		_updatePar(pars.Keywords, self.keywords)
		_updatePar(pars.Shortcuts, self.shortcuts)
		_updatePar(pars.Displaycategory, self.displayCategory)
		_updatePar(pars.Flags, self.flags)

		# TODO: DAT-based params


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
	pars: dict[str, dict] = field(default_factory=dict)

	def __post_init__(self):
		for parObj in self.pars.values():
			_cleanParamSpecObj(parObj)

	@staticmethod
	def _isIncluded(parTuplet: 'ParTupletT'):
		ignorePars = 'Help', 'Inspect', 'Updateop'
		if parTuplet[0].tupletName in ignorePars:
			return False
		if parTuplet[0].name.startswith('Createref') or parTuplet[0].name.startswith('Creatersel'):
			return False
		return True

	@classmethod
	def fromPage(cls, page: Page):
		return cls(
			name=page.name,
			pars={
				parTuplet[0].tupletName: dict(TDJSON.parameterToJSONPar(parTuplet[0]))
				for parTuplet in page.parTuplets
				if cls._isIncluded(parTuplet)
			},
		)

	@classmethod
	def fromCustomPages(cls, comp: OP):
		paramPages = []
		for page in comp.customPages:
			paramPage = cls.fromPage(page)
			if paramPage.pars:
				paramPages.append(paramPage)
		return paramPages

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
		'clampMin': False,
		'clampMax': False,
		'min': 0,
		'max': 1,
	}
	for key, defVal in defaultVals.items():
		if key in obj and obj[key] == defVal:
			del obj[key]
	if obj.get('menuSource'):
		if 'menuNames' in obj:
			del obj['menuNames']
		if 'menuLabels' in obj:
			del obj['menuLabels']

_ValueOrExprOrDatT = ValueOrExprT | TableData | TextData | None

@dataclass
class OpElementSpec(ModelObject):
	yaml_tag = u'!opElement'

	name: str
	elementType: str
	params: dict[str, _ValueOrExprOrDatT] = field(default_factory=dict)

	@classmethod
	def extract(cls, comp: COMP):
		opElement = comp.op('opElement')
		spec = cls(comp.name, opElement.par.Elementtype.eval())
		spec.updateFromComp(comp)
		return spec

	def updateFromComp(self, comp: COMP):
		for par in comp.customPars:
			if par.isPulse or par.isMomentary:
				continue
			if par.name == 'Hostop':
				continue
			if par.style == DAT:
				val = _extractDatSetting(par)
			else:
				val = _valOrExprFromPar(par)
			self.params[par.name] = val

	@classmethod
	def findAndExtract(cls, rop: COMP):
		return [
			cls.extract(opElement.parent())
			for opElement in rop.ops('*/opElement')
		]

@dataclass
class ROPSpecBase(ModelObject):
	meta: ROPMeta | None = None
	paramPages: list[ParamPage] | None = field(default_factory=list)

	@classmethod
	def extract(cls, rop: COMP, skipParams=False):
		spec = cls()
		spec.updateFromRop(rop, skipParams)
		return spec

	def updateFromRop(self, rop: COMP, skipParams=False):
		ropInfo = ROPInfo(rop)
		if self.meta:
			self.meta.updateFromRopInfo(ropInfo)
		else:
			self.meta = ROPMeta.fromRopInfo(ropInfo)
		if not skipParams:
			self.paramPages = ParamPage.fromCustomPages(rop)

@dataclass
class ROPSpec(ROPSpecBase):
	yaml_tag = u'!rop'

	opDef: ROPDef = field(default_factory=ROPDef)

	multiInput: MultiInputSpec | None = None
	inputs: list[InputSpec] = field(default_factory=list)

	elements: list[OpElementSpec] = field(default_factory=list)

	def updateFromRop(self, rop: COMP, skipParams=False):
		ropInfo = ROPInfo(rop)
		super().updateFromRop(rop, skipParams)
		self.opDef.updateFromComp(ropInfo.opDef)
		self.multiInput = MultiInputSpec.fromComps(ropInfo.multiInputHandler, ropInfo.inputHandlers)
		self.inputs = InputSpec.fromCompList(ropInfo.inputHandlers, forMulti=False)
		self.elements = OpElementSpec.findAndExtract(rop)

@dataclass
class RCompSpec(ROPSpecBase):
	yaml_tag = u'!rcomp'

def _extractDatSetting(par: Par | None) -> TextData | TableData | Expr | None:
	if par is None:
		return None
	if par.mode == ParMode.EXPRESSION:
		return Expr(par.expr)
	if par.mode != ParMode.CONSTANT:
		raise Exception(f'Parameter mode {par.mode} not supported for {par!r}')
	if not par:
		return None
	graph = EditorItemGraph.fromPar(par)
	if not graph.supported:
		print(f'DAT setup not supported for {par!r}')
		return _valOrExprFromPar(par)
	evalOpts = None
	if graph.evalDat:
		evalOpts = EvalDatOptions.fromDat(graph.evalDat)
	if graph.file:
		if graph.sourceDat.isText:
			return TextData(
				file=graph.file.eval(),
				name=graph.sourceDat.name,
			)
		else:
			return TableData(
				file=graph.file.eval(),
				name=graph.sourceDat.name,
				evaluate=graph.hasEval or None,
				evalOpts=evalOpts,
			)
	if graph.endDat.isTable:
		return TableData(
			name=graph.sourceDat.name,
			rows=[
				[cell.val for cell in row]
				for row in graph.sourceDat.rows()
			],
			evaluate=graph.hasEval or None,
			evalOpts=evalOpts,
		)
	else:
		return TextData(
			name=graph.sourceDat.name,
			text=graph.sourceDat.text,
		)

@dataclass
class EditorItemGraph:
	par: Par
	endDat: DAT | None = None
	sourceDat: DAT | None = None
	evalDat: evaluateDAT | None = None
	hasEval: bool = False
	supported: bool = False
	file: Par | None = None

	@classmethod
	def fromPar(cls, par: Par):
		endDat = par.eval()  # type: DAT | None
		if not endDat:
			return cls(par, supported=True)
		if isinstance(endDat, (tableDAT, textDAT)):
			return cls(
				par,
				endDat=endDat,
				sourceDat=endDat,
				evalDat=None,
				hasEval=False,
				supported=True,
				file=endDat.par['file'],
			)
		hasEval = False
		evalDat = None
		dats = _opChain(endDat)
		if not isinstance(dats[0], (tableDAT, textDAT)):
			return cls(par, endDat=endDat, supported=False)
		for dat in dats[1:]:
			if isinstance(dat, evaluateDAT):
				evalDat = dat
				hasEval = True
			elif not isinstance(dat, (nullDAT, substituteDAT)):
				return cls(
					par,
					sourceDat=dats[0],
					endDat=endDat,
					evalDat=evalDat,
					hasEval=hasEval,
					file=dats[0].par.file,
					supported=False,
				)
		return cls(
			par,
			sourceDat=dats[0],
			endDat=endDat,
			evalDat=evalDat,
			hasEval=hasEval,
			file=dats[0].par.file,
			supported=True,
		)

def _opChain(endOp: DAT):
	chain = [endOp]
	o = endOp
	while True:
		if not o.inputs:
			return chain
		o = o.inputs[0]
		chain.insert(0, o)

class ROPSpecLoader:
	def __init__(self, rop: COMP, spec: ROPSpec):
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
		# TODO: typeSpec support
		_updatePar(p.Useruntimebypass, d.useRuntimeBypass)
		_updatePar(p.Disableinspect, d.disableInspect)

		_updatePar(p.Librarynames, d.libraryNames)

	def _loadOpDefTextBlocks(self):
		p = self.info.opDefPar
		d = self.spec.opDef
		x = -100
		y = -500
		self._loadTextSetting(p.Functemplate, d.function, defaultName='function', x=x, y=200)
		self._loadTextSetting(p.Opglobals, d.opGlobals, defaultName='globals', x=x, y=y)
		y -= 150
		self._loadTextSetting(p.Initcode, d.init, defaultName='init', x=x, y=y)
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
			par: Par,
			val: TextData | None,
			defaultName: str,
			x: int, y: int):
		raise Exception('TODO: support for eval opts')
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
			par: Par,
			val: TableData | None,
			defaultName: str,
			x: int, y: int):
		raise Exception('TODO: support for eval opts')
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

def _updatePar(par: Par, val: ValueOrListOrExprT):
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

def _setParVal(par: Par, val):
	par.val = val if val is not None else ''
	par.expr = ''
	par.mode = ParMode.CONSTANT

def _setParExpr(par: Par, expr: str):
	par.val = ''
	par.expr = expr
	par.mode = ParMode.EXPRESSION

def _valOrExprFromPar(par: Par | None, useList=False):
	if par is None:
		return None
	if par.mode == ParMode.CONSTANT:
		if useList and par.isString and ' ' in par.val:
			return par.val.split(' ')
		return par.val
	if par.mode == ParMode.EXPRESSION:
		return Expr(par.expr)
	raise Exception(f'Parameter mode {par.mode} not supported for {par!r}')

def _valOrExprDictFromPars(pars: list[Par]):
	return {
		p.name: _valOrExprFromPar(p)
		for p in pars
	}

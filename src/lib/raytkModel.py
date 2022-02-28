"""
Toolkit model which works with operator type specifications and metadata.

This should only be used within development tools.
"""

from dataclasses import dataclass, field
import dataclasses
import json
from pathlib import Path
import re
from typing import Dict, Iterable, List, Optional, Union
import yaml

from raytkUtil import cleanDict, ROPInfo, InputInfo, RaytkTags

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

	def writeToFile(self, file: 'Union[Path, str]'):
		file = Path(file)
		text = yaml.dump(self, default_style='', sort_keys=False)
		file.write_text(text)

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
class EvalDatOptions(ModelObject):
	yaml_tag = u'!evalOpts'

	excludeFirstRow: bool = False
	excludeFirstCol: bool = False
	rows: Optional[str] = '*'
	cols: Optional[str] = '*'

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
	evalOpts: Optional[EvalDatOptions] = None

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
class CoordTypes(ModelObject):
	yaml_tag = u'!coordT'

	Allcoordtype: ValueOrExprT = None
	Coordtypefloat: ValueOrExprT = None
	Coordtypevec2: ValueOrExprT = None
	Coordtypevec3: ValueOrExprT = None

@dataclass
class ContextTypes(ModelObject):
	yaml_tag = u'!contextT'

	Allcontexttype: ValueOrExprT = None
	Contexttypecontext: ValueOrExprT = None
	Contexttypematerialcontext: ValueOrExprT = None
	Contexttypecameracontext: ValueOrExprT = None
	Contexttypelightcontext: ValueOrExprT = None
	Contexttyperaycontext: ValueOrExprT = None
	Contexttypeparticlecontext: ValueOrExprT = None

@dataclass
class ReturnTypes(ModelObject):
	yaml_tag = u'!returnT'

	Allreturntype: ValueOrExprT = None
	Returntypesdf: ValueOrExprT = None
	Returntypefloat: ValueOrExprT = None
	Returntypevec4: ValueOrExprT = None
	Returntyperay: ValueOrExprT = None
	Returntypelight: ValueOrExprT = None
	Returntypeparticle: ValueOrExprT = None

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

	Required: ValueOrExprT = False

	coordType: Optional[CoordTypes] = None
	contextType: Optional[ContextTypes] = None
	returnType: Optional[ReturnTypes] = None

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

	inputs: List[InputSpec] = field(default_factory=list)

def _getParValsDict(pars: 'Iterable[Par]'):
	return {
		p.name: p.eval()
		for p in pars
		if not p.isPulse and not p.isMomentary
	}
def _setParValsFromDict(o: 'OP', parVals: dict):
	for name, val in parVals.items():
		o.par[name] = val

@dataclass
class ROPTypeSpec(ModelObject):
	yaml_tag = u'!ropTypes'

	Useinputcoordtype: ValueOrExprT = True
	Useinputcontexttype: ValueOrExprT = True
	Useinputreturntype: ValueOrExprT = True

	coordType: Optional[CoordTypes] = None
	contextType: Optional[ContextTypes] = None
	returnType: Optional[ReturnTypes] = None

	@classmethod
	def extract(cls, specComp: 'COMP'):
		spec = cls(
			**_getParValsDict(specComp.pars('Useinput*')))
		if specComp.par.Allcoordtype:
			spec.coordType = '*'
		else:
			spec.coordType = CoordTypes(**_getParValsDict(specComp.pars('Coordtype*')))
		if specComp.par.Allcontexttype:
			spec.contextType = '*'
		else:
			spec.contextType = ContextTypes(**_getParValsDict(specComp.pars('Contexttype*')))
		if specComp.par.Allreturntype:
			spec.returnType = '*'
		else:
			spec.returnType = ReturnTypes(**_getParValsDict(specComp.pars('Returntype*')))
		return spec

	def applyTo(self, specComp: 'COMP'):
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

_TableSetting = Union[TableData, Expr, None]
_TextSetting = Union[TextData, Expr, None]

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
			stageInitCode: Code block for initialization code that the ROP needs to
				run before each render stage.
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

	enable: ValueOrExprT = None
	useRuntimeBypass: ValueOrExprT = False
	paramsOp: ValueOrExprT = None
	disableInspect: bool = False

	typeSpec: Union[ROPTypeSpec, ExternalSpec, None] = None

	opGlobals: _TextSetting = None
	init: _TextSetting = None
	stageInit: _TextSetting = None
	function: _TextSetting = None
	material: _TextSetting = None
	callbacks: _TextSetting = None

	useParams: ValueOrListOrExprT = None
	specialParams: ValueOrListOrExprT = None
	angleParams: ValueOrListOrExprT = None
	macroParams: ValueOrListOrExprT = None
	lockParams: ValueOrListOrExprT = None

	paramListTable: _TableSetting = None

	libraryNames: ValueOrListOrExprT = None

	bufferTable: _TableSetting = None
	textureTable: _TableSetting = None
	macroTable: _TableSetting = None
	variableTable: _TableSetting = None
	referenceTable: _TableSetting = None

	generatedMacroTables: ValueOrExprT = None

	help: _TextSetting = None
	keywords: ValueOrListOrExprT = None
	shortcuts: ValueOrListOrExprT = None

	def resolveExternalSpecs(self):
		if isinstance(self.typeSpec, ExternalSpec):
			self.typeSpec = self.typeSpec.resolve()

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
	pars: Dict[str, dict] = field(default_factory=dict)

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

@dataclass
class ROPSpec(ModelObject):
	yaml_tag = u'!rop'

	meta: Union[ROPMeta, ExternalSpec, None] = None
	opDef: Union[ROPDef, ExternalSpec] = field(default_factory=ROPDef)

	paramPages: Union[List[ParamPage], ExternalSpec, None] = field(default_factory=list)

	multiInput: Union[MultiInputSpec, ExternalSpec, None] = None
	inputs: Union[List[InputSpec], ExternalSpec] = field(default_factory=list)

	def resolveExternalSpecs(self):
		if isinstance(self.meta, ExternalSpec):
			self.meta = self.meta.resolve()
		if isinstance(self.opDef, ExternalSpec):
			self.opDef = self.opDef.resolve()
		if isinstance(self.paramPages, ExternalSpec):
			self.paramPages = self.paramPages.resolve()
		if isinstance(self.multiInput, ExternalSpec):
			self.multiInput = self.multiInput.resolve()
		if isinstance(self.inputs, ExternalSpec):
			self.inputs = self.inputs.resolve()

	@classmethod
	def extract_OLD(cls, rop: 'COMP', skipParams=False) -> 'ROPSpec':
		info = ROPInfo(rop)
		spec = ROPSpec(
			meta=ROPMeta(
				opType=info.opType,
				opVersion=int(info.opVersion),
				opStatus=info.statusLabel,
			),
			opDef=ROPDef(
				typeSpec=ROPTypeSpec.extract(info.opDefPar.Typespec.eval()),
				useRuntimeBypass=info.opDefPar.Useruntimebypass.eval(),
				disableInspect=info.opDefPar.Disableinspect.eval(),
				useParams=_valueOrExprFromPar(info.opDefPar.Params),
				specialParams=_valueOrExprFromPar(info.opDefPar.Specialparams),
				angleParams=_valueOrExprFromPar(info.opDefPar.Angleparams),
				macroParams=_valueOrExprFromPar(info.opDefPar.Macroparams),
				libraryNames=_valueOrExprFromPar(info.opDefPar.Librarynames),
				opGlobals=_extractDatSetting(info.opDefPar.Opglobals, isText=True),
				init=_extractDatSetting(info.opDefPar.Initcode, isText=True),
				stageInit=_extractDatSetting(info.opDefPar.Stageinitcode, isText=True),
				function=_extractDatSetting(info.opDefPar.Functemplate, isText=True),
				material=_extractDatSetting(info.opDefPar.Materialcode, isText=True),
				help=_extractDatSetting(info.opDefPar.Help, isText=True),
				callbacks=_extractDatSetting(info.opDefPar.Callbacks, isText=True),
				bufferTable=_extractDatSetting(info.opDefPar.Buffertable, isText=False),
				macroTable=_extractDatSetting(info.opDefPar.Macrotable, isText=False),
				textureTable=_extractDatSetting(info.opDefPar.Texturetable, isText=False),
				variableTable=_extractDatSetting(info.opDefPar.Variabletable, isText=False),
				referenceTable=_extractDatSetting(info.opDefPar.Referencetable, isText=False),
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
				Minimuminputs=multiHandler.par.Minimuminputs.eval() if multiHandler.par.Minimuminputs > 0 else None,
			)
		for inputHandler in info.inputHandlers:
			inputInfo = InputInfo(inputHandler)
			if inputInfo.multiHandler:
				spec.multiInput.inputs.append(_extractInputSpec(inputHandler))
			else:
				spec.inputs.append(_extractInputSpec(inputHandler))
		return spec

	@classmethod
	def extract(cls, rop: 'COMP', skipParams=False):
		extractor = _SpecExtractor(rop)
		return extractor.extract(skipParams)

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
		Name=info.name,
		Label=info.label,
		Required=info.required,
		coordType=_extractInputSupportSetting(info.handlerPar.Supportcoordtypes, info.supportedCoordTypes),
		returnType=_extractInputSupportSetting(info.handlerPar.Supportreturntypes, info.supportedReturnTypes),
		contextType=_extractInputSupportSetting(info.handlerPar.Supportcontexttypes, info.supportedContextTypes),
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

def _loadFieldsFromPars(obj: 'ModelObject', pars: 'Iterable[Par]'):
	for p in pars:
		v = _valueOrExprFromPar(p)
		setattr(obj, p.name, v)

def _extractDatEvalPart(modePar: 'Par', namesPar: 'Par'):
	if modePar.mode != ParMode.CONSTANT:
		raise Exception(f'Unsupported mode for {modePar!r}')
	if namesPar.mode != ParMode.CONSTANT:
		raise Exception(f'Unsupported mode for {namesPar!r}')
	if modePar == 'all':
		return '*'
	elif modePar == 'bynames':
		return namesPar.val
	raise Exception(f'Unsupported eval dat scope mode: {modePar!r}')

def _extractEvalOpts(dat: 'Optional[evaluateDAT]'):
	if not dat:
		return None
	return EvalDatOptions(
		excludeFirstRow=dat.par.xfirstrow.eval(),
		excludeFirstCol=dat.par.xfirstcol.eval(),
		rows=_extractDatEvalPart(dat.par.extractrows, dat.par.rownames),
		cols=_extractDatEvalPart(dat.par.extractcols, dat.par.colnames),
	)

def _extractDatSetting(par: Optional['Par'], isText: bool) -> Union[TextData, TableData, Expr, None]:
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
		raise Exception(f'DAT setup not supported for {par!r}')
	evalOpts = None
	if graph.evalDat:
		evalOpts = _extractEvalOpts(graph.evalDat)
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
	par: 'Par'
	endDat: 'Optional[DAT]' = None
	sourceDat: 'Optional[DAT]' = None
	evalDat: 'Optional[evaluateDAT]' = None
	hasEval: bool = False
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

def _opChain(endOp: 'DAT'):
	chain = [endOp]
	o = endOp
	while True:
		if not o.inputs:
			return chain
		o = o.inputs[0]
		chain.insert(0, o)

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
		# TODO: typeSpec support
		_updatePar(p.Useruntimebypass, d.useRuntimeBypass)
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
		self._loadTextSetting(p.Initcode, d.init, defaultName='init', x=x, y=y)
		y -= 150
		self._loadTextSetting(p.Stageinitcode, d.stageInit, defaultName='stageInit', x=x, y=y)
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
			par: 'Par',
			val: Optional[TableData],
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

class _SpecExtractor:
	def __init__(self, rop: 'COMP'):
		self.rop = rop
		self.ropInfo = ROPInfo(rop)

	def extract(self, skipParams=False) -> 'ROPSpec':
		return ROPSpec(
			meta=self._extractMeta(),
			opDef=self._extractOpDef(),
			paramPages=None if skipParams else self._extractParamPages(),
			multiInput=self._extractMultiInput(),
			inputs=self._extractInputs(forMulti=False),
		)

	def _extractMeta(self):
		return ROPMeta(
			opType=self.ropInfo.opType,
			opVersion=self.ropInfo.opVersion,
			opStatus=self.ropInfo.statusLabel,
		)

	def _extractOpDef(self) -> 'ROPDef':
		pars = self.ropInfo.opDefPar
		return ROPDef(
			enable=self._valOrExprFromPar(pars.Enable),
			useRuntimeBypass=self._valOrExprFromPar(pars.Useruntimebypass),
			paramsOp=self._valOrExprFromPar(pars.Paramsop),

			typeSpec=self._extractTypeSpec(),

			opGlobals=self._datSettingFromPar(pars.Opglobals, isText=True),
			init=self._datSettingFromPar(pars.Initcode, isText=True),
			stageInit=self._datSettingFromPar(pars.Stageinitcode, isText=True),
			function=self._datSettingFromPar(pars.Functemplate, isText=True),
			material=self._datSettingFromPar(pars.Materialcode, isText=True),
			callbacks=self._datSettingFromPar(pars.Callbacks, isText=True),

			useParams=self._valOrExprFromPar(pars.Params, useList=True),
			specialParams=self._valOrExprFromPar(pars.Specialparams, useList=True),
			angleParams=self._valOrExprFromPar(pars.Angleparams, useList=True),
			macroParams=self._valOrExprFromPar(pars.Macroparams, useList=True),
			lockParams=self._valOrExprFromPar(pars.Lockpars, useList=True),

			paramListTable=self._valOrExprFromPar(pars.Paramlisttable),

			libraryNames=self._valOrExprFromPar(pars.Librarynames, useList=True),

			bufferTable=self._valOrExprFromPar(pars.Buffertable, useList=True),
			textureTable=self._valOrExprFromPar(pars.Texturetable, useList=True),
			macroTable=self._valOrExprFromPar(pars.Macrotable, useList=True),
			variableTable=self._valOrExprFromPar(pars.Variabletable, useList=True),
			referenceTable=self._valOrExprFromPar(pars.Referencetable, useList=True),

			generatedMacroTables=self._valOrExprFromPar(pars.Generatedmacrotables),

			help=self._valOrExprFromPar(pars.Help),
			keywords=self._valOrExprFromPar(pars.Keywords, useList=True),
			shortcuts=self._valOrExprFromPar(pars.Shortcuts, useList=True),
		)

	def _extractTypeSpec(self) -> 'ROPTypeSpec':
		specComp = self.ropInfo.typeSpec
		return ROPTypeSpec(
			coordType=self._extractCoordTypes(specComp),
			contextType=self._extractContextTypes(specComp),
			returnType=self._extractReturnTypes(specComp),
			**self._valOrExprDictFromPars(specComp.pars('Useinput*')))

	def _extractCoordTypes(self, specComp: 'COMP'):
		return CoordTypes(**self._valOrExprDictFromPars(specComp.pars('Allcoordtype', 'Coordtype*')))

	def _extractContextTypes(self, specComp: 'COMP'):
		return ContextTypes(**self._valOrExprDictFromPars(specComp.pars('Allcontexttype', 'Contexttype*')))

	def _extractReturnTypes(self, specComp: 'COMP'):
		return ReturnTypes(**self._valOrExprDictFromPars(specComp.pars('Allreturntype', 'Returntype*')))

	def _extractParamPages(self) -> 'List[ParamPage]':
		paramPages = []
		for page in self.rop.customPages:
			paramPage = self._extractParamPage(page)
			if paramPage:
				paramPages.append(paramPage)
		return paramPages

	@staticmethod
	def _extractParamPage(page: 'Page') -> 'Optional[ParamPage]':
		ignorePars = 'Help', 'Inspect', 'Updateop'
		return ParamPage(
			name=page.name,
			pars={
				parTuplet[0].tupletName: dict(TDJSON.parameterToJSONPar(parTuplet[0]))
				for parTuplet in page.parTuplets
				if parTuplet[0].tupletName not in ignorePars
			},
		)

	def _extractMultiInput(self) -> 'Optional[MultiInputSpec]':
		multiHandler = self.ropInfo.multiInputHandler
		if not multiHandler:
			return None
		return MultiInputSpec(
			inputs=self._extractInputs(forMulti=True),
			**self._valOrExprDictFromPars(multiHandler.pars(
				'Minimuminputs', 'Coordtype*', 'Contexttype*', 'Returntype*'))
		)

	def _extractInputs(self, forMulti: bool) -> 'List[InputSpec]':
		return [
			self._extractInput(handler)
			for handler in self.ropInfo.inputHandlers
			if forMulti == (InputInfo(handler).multiHandler is not None)
		]

	def _extractInput(self, handler: 'COMP') -> 'InputSpec':
		return InputSpec(
			coordType=self._extractCoordTypes(handler),
			contextType=self._extractContextTypes(handler),
			returnType=self._extractReturnTypes(handler),
			**self._valOrExprDictFromPars(handler.pars(
				'Source', 'Name', 'Label', 'Localalias', 'Help', 'Required'))
		)

	@staticmethod
	def _datSettingFromPar(
			par: 'Optional[Par]', isText: bool) -> 'Union[TextData, TableData, Expr, None]':
		return _extractDatSetting(par, isText)

	@staticmethod
	def _valOrExprFromPar(par: 'Optional[Par]', useList=False):
		if par is None:
			return None
		if par.mode == ParMode.CONSTANT:
			if useList and par.isString and ' ' in par.val:
				return par.val.split(' ')
			return par.val
		if par.mode == ParMode.EXPRESSION:
			return Expr(par.expr)
		raise Exception(f'Parameter mode {par.mode} not supported for {par!r}')

	def _valOrExprDictFromPars(self, pars: 'Iterable[Par]'):
		return {
			p.name: self._valOrExprFromPar(p)
			for p in pars
		}

from raytkUtil import CoordTypes, ContextTypes, ReturnTypes, ROPInfo
from dataclasses import dataclass, field
import re
from typing import Dict, List, Optional, Union

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	import _stubs.TDJSON as TDJSON
	from _typeAliases import *
else:
	# noinspection PyUnresolvedReferences,PyUnboundLocalVariable
	TDJSON = op.TDModules.mod.TDJSON

@dataclass
class TypeSpec:
	"""
	One or several possible data types.
	`*` is equivalent to all available types.
	`foo` is equivalent to one specific type.
	`foo|bar|baz` is equivalent to one of a list of possible types.
	"""
	isAll: bool = False
	types: List[str] = field(default_factory=list)

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
			return cls(isAll=True)
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

typeSpecPatternPart = r'([\*\w|]+)'
signaturePattern = re.compile(
	fr'\(\s*{typeSpecPatternPart}\s*,\s*{typeSpecPatternPart}\s*\)\s*->\s*{typeSpecPatternPart}')

@dataclass
class FunctionSignature:
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
		match = signaturePattern.fullmatch(s.strip())
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

TableDataT = List[List[str]]

@dataclass
class ROPInputSpec:
	name: Optional[str] = None
	label: Optional[str] = None
	signature: Optional[FunctionSignature] = None

	def toObj(self):
		return cleanDict({
			'name': self.name,
			'label': self.label,
			'signature': str(self.signature) if self.signature else None,
		})

	@classmethod
	def fromObj(cls, obj: dict):
		sig = obj.get('signature')
		return cls(
			name=obj.get('name'),
			label=obj.get('label'),
			signature=FunctionSignature.parse(sig) if sig else None,
		)

	@classmethod
	def fromObjs(cls, objs: Optional[List[dict]]):
		return [cls.fromObj(o) for o in objs] if objs else []

	@classmethod
	def extractFromHandler(cls, inputHandler: 'COMP'):
		inDat = inputHandler.inputs[0]  # type DAT
		labelPar = inDat.par.label  # type: Par
		supportedTypeTable = inputHandler.op('supported_type_table')
		return cls(
			name=inDat.name,
			label=labelPar.eval() if (labelPar.mode == ParMode.EXPRESSION and labelPar.expr == 'me.name') else None,
			signature=FunctionSignature.create(
				str(supportedTypeTable['coordType', 1] or ''),
				str(supportedTypeTable['contextType', 1] or ''),
				str(supportedTypeTable['returnType', 1] or ''),
			) if supportedTypeTable else None
		)

@dataclass
class ValueOrExpr:
	value: Union[str, int, float, List[Union[str, int, float]]] = None
	expr: Optional[str] = None
	bind: Optional[str] = None

	def toObj(self):
		if self.bind:
			return {'@': self.bind}
		if self.expr:
			return {'$': self.expr}
		return self.value

	@classmethod
	def fromObj(cls, obj):
		if not obj:
			return None
		if isinstance(obj, dict):
			if '@' in obj:
				return cls(bind=obj['@'])
			if '$' in obj:
				return cls(expr=obj['$'])
		return cls(value=obj)

	@classmethod
	def fromPar(cls, par: 'Par'):
		if par.mode == ParMode.BIND:
			return cls(bind=par.bindExpr)
		if par.mode == ParMode.EXPRESSION:
			return cls(expr=par.expr)
		if par.mode == ParMode.CONSTANT:
			return cls(value=par.eval())
		raise ValueError(f'Unsupported par {par!r}')

@dataclass
class TableSpec:
	file: Optional[ValueOrExpr] = None
	data: Union[str, TableDataT] = None
	isExpr: bool = False
	isText: bool = False

	def toObj(self):
		return cleanDict({
			'file': toObjIfPossible(self.file),
			'data': self.data,
			'isExpr': self.isExpr or None,
			'isText': self.isText or None,
		})

	@classmethod
	def fromObj(cls, obj: dict):
		if not obj:
			return None
		return cls(
			file=ValueOrExpr.fromObj(obj.get('file')),
			**excludeKeys(obj, ['file']))

	@classmethod
	def extractFromDAT(cls, dat: 'DAT'):
		if not dat:
			return None
		if not dat.inputs:
			mainDat = dat
			isExpr = False
		else:
			mainDat = dat.inputs[0]
			if mainDat.inputs:
				raise ValueError(f'Unsupported dat {dat} with input {mainDat}')
			isExpr = isinstance(dat, evaluateDAT)
		if mainDat.par['file']:
			return cls(
				file=ValueOrExpr.fromPar(mainDat.par.file),
				isExpr=isExpr)
		if mainDat.isText:
			return cls(
				data=mainDat.text,
				isText=True,
			)
		return cls(
			data=[
				[cell.val for cell in row]
				for row in mainDat.rows()
			],
			isExpr=isExpr)

def parseSpecOrValueOrExpr(obj: Union[dict, str, List[str]]) -> 'Optional[ValueOrExprOrTable]':
	if not obj:
		return None
	if isinstance(obj, list) or isinstance(obj, str):
		return ValueOrExpr(obj)
	if not isinstance(obj, dict):
		raise ValueError(f'Unsupported type {obj!r}')
	if '@' in obj or '$' in obj:
		return ValueOrExpr.fromObj(obj)
	if 'file' in obj or 'data' in obj or 'isExpr' in obj:
		return TableSpec.fromObj(obj)
	return ValueOrExpr.fromObj(obj)

def getParValuesFromCellsExpr(datName: str):
	return f"' '.join([str(c) for c in op('{datName}').cells()])"

valuesFromCellsExprPattern = re.compile(r"' '\.join\(\[str\(c\) for c in op\('(\w+)'\).cells\(\)\]\)")

def specOrValueOrExprFromPar(par: 'Par'):
	if par.mode == ParMode.EXPRESSION and par.isString:
		match = valuesFromCellsExprPattern.fullmatch(par.expr)
		if match and match.group(1):
			dat = par.owner.op(match.group(1))
			if dat and dat.isDAT:
				return TableSpec.extractFromDAT(dat)
	return ValueOrExpr.fromPar(par)

def toObjIfPossible(obj):
	if obj and hasattr(obj, 'toObj'):
		return obj.toObj()
	return obj

ValueOrExprOrTable = Union[ValueOrExpr, TableSpec]

def cleanParamSpecObj(obj: dict):
	if not obj:
		return None
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
	return obj

def clearParamPageSpecObj(obj: dict):
	if not obj:
		return None
	return {
		param: cleanParamSpecObj(paramObj)
		for param, paramObj in obj.items()
	}

def clearParamPageSpecsObj(obj: dict):
	if not obj:
		return None
	return {
		page: clearParamPageSpecObj(paramsObj)
		for page, paramsObj in obj.items()
	}

@dataclass
class ROPDefinition:
	paramPages: Dict[str, Dict[str, dict]] = field(default_factory=list)
	function: Optional[TableSpec] = None
	useParams: ValueOrExprOrTable = None
	specialParams: ValueOrExprOrTable = None
	macros: Optional[TableSpec] = None
	help: ValueOrExprOrTable = None
	inputs: List[ROPInputSpec] = field(default_factory=list)

	def toObj(self):
		return cleanDict({
			'paramPages': clearParamPageSpecsObj(self.paramPages),
			'function': toObjIfPossible(self.function),
			'useParams': toObjIfPossible(self.useParams),
			'specialParams': toObjIfPossible(self.specialParams),
			'macros': toObjIfPossible(self.macros),
			'help': toObjIfPossible(self.help),
			'inputs': [i.toObj() for i in self.inputs] if self.inputs else None,
		})

	@classmethod
	def fromObj(cls, obj: dict):
		return cls(
			inputs=ROPInputSpec.fromObjs(obj.get('inputs')),
			useParams=parseSpecOrValueOrExpr(obj.get('useParams')),
			specialParams=parseSpecOrValueOrExpr(obj.get('specialParams')),
			macros=TableSpec.fromObj(obj.get('macros')),
			function=parseSpecOrValueOrExpr(obj.get('function')),
			help=parseSpecOrValueOrExpr(obj.get('help')),
			**excludeKeys(obj, [
				'inputs', 'useParams', 'specialParams', 'macros', 'function'
			]))

	@classmethod
	def extractFromROP(cls, rop: 'COMP'):
		info = ROPInfo(rop)
		inputHandlers = rop.ops('inputDefinitionHandler_*')
		# top to bottom
		inputHandlers.sort(key=lambda o: -o.nodeY)
		return cls(
			paramPages=TDJSON.opToJSONOp(rop, includeCustomPages=True, includeBuiltInPages=False),
			help=TableSpec.extractFromDAT(info.opDefPar.Help.eval()),
			function=TableSpec.extractFromDAT(info.opDefPar.Functemplate.eval()),
			macros=TableSpec.extractFromDAT(info.opDefPar.Macrotable.eval()),
			useParams=specOrValueOrExprFromPar(info.opDefPar.Params),
			specialParams=specOrValueOrExprFromPar(info.opDefPar.Specialparams),
			inputs=[
				ROPInputSpec.extractFromHandler(inputHandler)
				for inputHandler in inputHandlers
			],
		)

@dataclass
class ROPParamHelp:
	name: Optional[str] = None
	label: Optional[str] = None
	summary: Optional[str] = None
	detail: Optional[str] = None

	def formatMarkdownListItem(self):
		text = f'* {self.label} (`{self.name}`)'
		if self.summary:
			text += f': {self.summary}'
		if self.detail:
			text += f'\n  {self.detail}'
		return text

	@classmethod
	def parseMarkdownListItem(cls, text: str):
		obj = ROPParamHelp()
		if not text.startswith('* '):
			raise ValueError(f'Invalid param markdown list item: {text!r}')
		text = text[2:]
		pass

@dataclass
class ROPHelp:
	name: Optional[str] = None
	summary: Optional[str] = None
	detail: Optional[str] = None
	parameters: List[ROPParamHelp] = field(default_factory=list)

def cleanDict(d):
	if not d:
		return None
	return {
		key: val
		for key, val in d.items()
		if not (val is None or (isinstance(val, (str, list, dict, tuple)) and len(val) == 0))
	}

def mergeDicts(*parts):
	x = {}
	for part in parts:
		if part:
			x.update(part)
	return x

def excludeKeys(d, keys):
	if not d:
		return {}
	return {
		key: val
		for key, val in d.items()
		if key not in keys
	}

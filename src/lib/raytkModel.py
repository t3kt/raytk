from raytkUtil import CoordTypes, ContextTypes, ReturnTypes, ROPInfo
from dataclasses import dataclass, field, asdict
import re
from typing import Dict, List, Optional

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	import _stubs.TDJSON as TDJSON
else:
	# noinspection PyUnresolvedReferences
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

@dataclass
class ROPInputSpec:
	name: Optional[str] = None
	label: Optional[str] = None
	signature: Optional[FunctionSignature] = None

	def toDict(self):
		return cleanDict({
			'name': self.name,
			'label': self.label,
			'signature': str(self.signature) if self.signature else None,
		})

	@classmethod
	def fromDict(cls, obj: dict):
		sig = obj.get('signature')
		return cls(
			name=obj.get('name'),
			label=obj.get('label'),
			signature=FunctionSignature.parse(sig) if sig else None,
		)

	@classmethod
	def fromDicts(cls, objs: Optional[List[dict]]):
		return [cls.fromDict(o) for o in objs] if objs else []

	@classmethod
	def extractFromHandler(cls, inputHandler: 'COMP'):
		inDat = inputHandler.inputs[0]  # type DAT
		labelPar = inDat.par.label  # type: Par
		spec = cls(
			name=inDat.name,
			label=labelPar.eval() if (labelPar.mode == ParMode.EXPRESSION and labelPar.expr == 'me.name') else None,
		)
		pass

@dataclass
class ROPDefinition:
	paramPages: Dict[str, Dict[str, dict]] = field(default_factory=list)
	functionFile: Optional[str] = None
	useParams: List[str] = field(default_factory=list)
	helpFile: Optional[str] = None
	inputs: List[ROPInputSpec] = field(default_factory=list)

	def toDict(self):
		return cleanDict({
			'paramPages': self.paramPages,
			'functionFile': self.functionFile,
			'useParams': self.useParams,
			'helpFile': self.helpFile,
			'inputs': [i.toDict() for i in self.inputs] if self.inputs else None,
		})

	@classmethod
	def fromDict(cls, obj: dict):
		return cls(
			inputs=ROPInputSpec.fromDicts(obj.get('inputs')),
			**excludeKeys(obj, ['inputs']))

	@classmethod
	def extractFromROP(cls, rop: 'COMP'):
		info = ROPInfo(rop)
		return cls(
			paramPages=TDJSON.opToJSONOp(rop, includeCustomPages=True, includeBuiltInPages=False),
			helpFile=_fileFromDat(info.helpDAT),
			functionFile=_fileFromDat(info.functionDAT),
		)

def _fileFromDat(dat: 'DAT'):
	if not dat or not dat.par['file']:
		return None
	return str(dat.par.file)

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

# _paramHelpPattern = re.compile(r'\*\s+([\w\s\d]+)\s+\(([A-Z][a-z0-9]*)\):\s+()?')

@dataclass
class ROPHelp:
	name: Optional[str] = None
	summary: Optional[str] = None
	detail: Optional[str] = None
	parameters: List[ROPParamHelp] = field(default_factory=list)

def _getSingleString(vals: List[str]):
	if not vals:
		return None
	if len(vals) > 1:
		return ' '.join(vals)
	return vals[0]

def _parseTextObject(text: str) -> Dict[str, List[str]]:
	obj = {}
	for line in text.splitlines():
		line = line.strip()
		if not line.startswith('@'):
			continue
		parts = re.split(r'\W+', line[1:])
		key = parts[0]
		vals = parts[1:]
		if not vals:
			continue
		if key not in obj:
			obj[key] = []
		obj[key] += vals
	return obj

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

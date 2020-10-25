from raytkUtil import CoordTypes, ContextTypes, ReturnTypes
from dataclasses import dataclass, field
import re
from typing import Dict, List, Optional

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
	def create(cls, coordType: str, contextType: str, returnType: str):
		return cls(
			coordType=TypeSpec.parse(coordType),
			contextType=TypeSpec.parse(contextType),
			returnType=TypeSpec.parse(returnType),
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

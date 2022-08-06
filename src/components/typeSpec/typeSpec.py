from typing import Optional, List, Tuple

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def _typeTable() -> 'DAT':
	return op('typeTable')

def _getAllTypesInCategory(typeTable: 'DAT', category: str):
	filterColumn = 'is' + category[0].upper() + category[1:]
	return [
		typeTable[row, 'name'].val
		for row in range(1, typeTable.numRows)
		if typeTable[row, filterColumn] == '1'
	]

class _Category:
	name: str
	togglePrefix: str
	allToggle: str
	useInputToggle: str

	def __init__(self, name: str):
		self.name = name
		self.togglePrefix = name.capitalize()
		self.allToggle = 'All' + name.lower()
		self.useInputToggle = 'Useinput' + name.lower()
		self.allTypes = _getAllTypesInCategory(_typeTable(), name)

	def getSpec(self, parHost: 'OP'):
		isAll = bool(parHost and parHost.par[self.allToggle])
		return TypeSpec(
			useInput=bool(parHost and parHost.par[self.useInputToggle]),
			supportsAll=isAll,
			supported=[] if isAll else [
				t
				for t in self.allTypes
				if parHost and parHost.par[self.togglePrefix + t.lower()]
			],
		)

_categories = [
	_Category('coordType'),
	_Category('contextType'),
	_Category('returnType'),
]

def buildSupportedTypeTable(dat: 'scriptDAT', parHost: 'OP'):
	dat.clear()
	dat.appendRow(['category', 'spec', 'types'])
	for cat in _categories:
		typeSpec = cat.getSpec(parHost)
		dat.appendRow([
			cat.name,
			typeSpec.formatSpec(cat.allTypes),
			typeSpec.formatTypes(cat.allTypes),
		])

class TypeSpec:
	"""
	A specification for a category of types (such as coordinate types) that an operator/input/etc supports using.
	Each ROP has 3 of these:
	* Coordinate type spec
	* Context type spec
	* Return type spec

	A type spec is either:
	* A single type (e.g. 'vec2')
	* A set of several types (e.g. 'vec2|vec3')
	* All available types ('*')
	"""
	useInput: bool = False
	supportsAll: bool = False
	supported: 'Optional[List[str]]' = None

	def __init__(self, useInput=False, supportsAll=False, supported: Optional[List[str]] = None):
		self.useInput = useInput
		self.supportsAll = supportsAll
		self.supported = supported

	def expandedTypes(self, allTypes: List[str]) -> List[str]:
		if self.supportsAll:
			return list(allTypes)
		return [
			t
			for t in allTypes
			if self.supported and t in self.supported
		]

	def formatSpec(self, allTypes: List[str]) -> str:
		types = self.expandedTypes(allTypes)
		if self.supportsAll:
			spec = '*'
		else:
			spec = ' '.join(types)
		if self.useInput:
			return f'useinput|{spec}'
		return spec

	def formatTypes(self, allTypes: List[str]) -> str:
		types = self.expandedTypes(allTypes)
		return ' '.join(types)

	@classmethod
	def parseSpec(cls, spec: str):
		if not spec:
			return cls()
		useInput, spec = _parseUseInput(spec)
		return cls(
			useInput=useInput,
			supportsAll=spec == '*',
			supported=None if spec == '*' else spec.split(' '),
		)
# duplicated in opDefinition - for size savings
def _parseUseInput(spec: str) -> Tuple[bool, str]:
	useInput = spec.startswith('useinput|')
	if useInput:
		spec = spec[9:]  # len('useinput|')
	return useInput, spec

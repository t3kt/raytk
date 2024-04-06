# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def _getAllTypesInCategory(typeTable: DAT, category: str):
	filterColumn = 'is' + category[0].upper() + category[1:]
	return [typeTable[row, 'name'].val for row in range(1, typeTable.numRows) if typeTable[row, filterColumn] == '1']

class _Category:
	def __init__(self, name: str):
		self.name = name
		self.togglePrefix = name.capitalize()
		self.allToggle = 'All' + name.lower()
		self.useInputToggle = 'Useinput' + name.lower()
		self.allTypes = _getAllTypesInCategory(op('typeTable'), name)

	def getSpec(self, parHost: OP):
		isAll = bool(parHost and parHost.par[self.allToggle])
		return TypeSpec(
			useInput=bool(parHost and parHost.par[self.useInputToggle]),
			supportsAll=isAll,
			supported=[] if isAll else [t for t in self.allTypes if parHost and parHost.par[self.togglePrefix + t.lower()]],
		)

_categories = [_Category('coordType'), _Category('contextType'), _Category('returnType')]

def buildSupportedTypeTable(dat: scriptDAT, parHost: OP):
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
	useInput: bool = False
	supportsAll: bool = False
	supported: list[str] | None = None

	def __init__(self, useInput=False, supportsAll=False, supported: list[str] | None = None):
		self.useInput = useInput
		self.supportsAll = supportsAll
		self.supported = supported

	def expandedTypes(self, allTypes: list[str]) -> list[str]:
		if self.supportsAll:
			return list(allTypes)
		return [t for t in allTypes if self.supported and t in self.supported]

	def formatSpec(self, allTypes: list[str]) -> str:
		spec = '*' if self.supportsAll else ' '.join(self.expandedTypes(allTypes))
		if self.useInput:
			return f'useinput|{spec}'
		return spec

	def formatTypes(self, allTypes: list[str]) -> str:
		return ' '.join(self.expandedTypes(allTypes))

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
def _parseUseInput(spec: str) -> tuple[bool, str]:
	useInput = spec.startswith('useinput|')
	if useInput:
		spec = spec[9:]
	return useInput, spec

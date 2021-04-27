from raytkTypes import TypeSpec

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def _typeTable() -> 'DAT':
	return op('typeTable')

class _Category:
	name: str
	togglePrefix: str
	allToggle: str
	useInputToggle: str
	fallbackPar: str

	def __init__(self, name: str):
		self.name = name
		self.togglePrefix = name.capitalize()
		self.allToggle = 'All' + name.lower()
		self.useInputToggle = 'Useinput' + name.lower()
		self.fallbackPar = 'Fallback' + name.lower()
		filterColumn = 'is' + name[0].upper() + name[1:]
		table = _typeTable()
		self.allTypes = [
			table[row, 'name'].val
			for row in range(1, table.numRows)
			if table[row, filterColumn] == '1'
		]

	def getSpec(self):
		isAll = bool(parent().par[self.allToggle])
		return TypeSpec(
			useInput=bool(parent().par[self.useInputToggle]),
			supportsAll=isAll,
			supported=[] if isAll else [
				t
				for t in self.allTypes
				if parent().par[self.togglePrefix + t.lower()]
			],
			fallback=str(parent().par[self.fallbackPar]),
		)

_categories = [
	_Category('coordType'),
	_Category('contextType'),
	_Category('returnType'),
]

def buildSupportedTypeTable(dat: 'scriptDAT'):
	dat.clear()
	dat.appendRow(['category', 'spec', 'types'])
	for cat in _categories:
		typeSpec = cat.getSpec()
		dat.appendRow([
			cat.name,
			typeSpec.formatSpec(cat.allTypes),
			typeSpec.formatTypes(cat.allTypes),
		])

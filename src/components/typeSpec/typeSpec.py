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
	filterColumn: str

	def __init__(self, name: str):
		self.name = name
		self.togglePrefix = name.capitalize()
		self.allToggle = 'All' + name.lower()
		self.useInputToggle = 'Useinput' + name.lower()
		self.fallbackPar = 'Fallback' + name.lower()
		self.filterColumn = 'is' + name[0].upper() + name[1:]

	def allTypes(self):
		table = _typeTable()
		return [
			table[row, 'name'].val
			for row in range(1, table.numRows)
			if table[row, self.filterColumn] == '1'
		]

	def expandedTypes(self):
		allTypes = self.allTypes()
		if self.supportsAllTypes():
			return allTypes
		return [
			t
			for t in allTypes
			if parent().par[self.togglePrefix + t.lower()]
		]

	def supportsAllTypes(self):
		return parent().par[self.allToggle]

	def useInputType(self):
		return parent().par[self.useInputToggle]

	def fallbackType(self):
		return parent().par[self.fallbackPar].eval()

_categories = [
	_Category('coordType'),
	_Category('contextType'),
	_Category('returnType'),
]

def buildSupportedTypeTable(dat: 'scriptDAT'):
	dat.clear()
	dat.appendRow(['category', 'spec', 'types'])
	for cat in _categories:
		types = cat.expandedTypes()
		if cat.supportsAllTypes():
			spec = '*'
		else:
			spec = ' '.join(types)
		if cat.useInputType():
			spec = f'useinput|{cat.fallbackType()}:{spec}'
		dat.appendRow([
			cat.name,
			spec,
			' '.join(types),
		])

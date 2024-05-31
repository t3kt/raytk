# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

typeTable = op('typeTable')

for handler in ops('inputHandler*'):
	i = handler.digits
	prefix = f"op('inputTable')[{i}, "
	handler.par.Prohibited.expr = f"op('inputTable')[{i}, 'exists'] != '1'"
	handler.par.Localalias.expr = prefix + "'name']"
	handler.par.Allcoordtype.expr = prefix + "'coordType'] in ('auto', '')"

	def processCategory(category: str):
		col = 'is' + category[0].upper() + category[1:]
		handler.par['All' + category.lower()].expr = prefix + f"'{category}'].val in ('auto', '')"
		for r in range(1, typeTable.numRows):
			if typeTable[r, col] == '1':
				typeName = typeTable[r, 'name'].val
				handler.par[category.capitalize() + typeName.lower()].expr = prefix + f"'{category}'] == '{typeName}'"

	processCategory('coordType')
	processCategory('contextType')
	processCategory('returnType')

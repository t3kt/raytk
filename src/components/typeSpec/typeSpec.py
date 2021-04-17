# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def _typeTable() -> 'DAT':
	return op('typeTable')

def _expandedTypes(
		listParName: 'str',
		toggleParPrefix: 'str',
		filterColumn: 'str',
):
	val = parent().par[listParName].eval()
	table = _typeTable()
	allTypes = [
		table[row, 'name'].val
		for row in range(1, table.numRows)
		if table[row, filterColumn] == '1'
	]
	if val == '*':
		return allTypes
	supported = tdu.split(val)
	return [
		t
		for t in allTypes
		if t in supported or parent().par[toggleParPrefix + t.lower()]
	]

def buildSupportedTypeTable(dat: 'scriptDAT'):
	dat.clear()
	dat.appendRows([
		['coordType', ' '.join(_expandedTypes('Supportcoordtypes', 'Supportcoordtype', 'isCoordType'))],
		['contextType', ' '.join(_expandedTypes('Supportcontexttypes', 'Supportcontexttype', 'isContextType'))],
		['returnType', ' '.join(_expandedTypes('Supportreturntypes', 'Supportreturntype', 'isReturnType'))],
	])

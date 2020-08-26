# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildExportTable(dat: 'DAT', uniformTable: 'DAT'):
	dat.clear()
	dat.appendRow(['path', 'parameter', 'value'])
	path = str(parent().par.Materialpath)
	offset = int(parent().par.Firstindex)
	for row in range(1, uniformTable.numRows):
		_addArray(
			dat,
			path,
			row + offset - 1,
			uniformTable[row, 'name'].val,
			uniformTable[row, 'chop'].val,
			uniformTable[row, 'type'].val,
			uniformTable[row, 'uniformType'].val,
		)

def _addArray(dat: 'DAT', path, i, name, chop, unitType, mode):
	dat.appendRow([path, f'chopuniname{i}', repr(name)])
	dat.appendRow([path, f'chopunitype{i}', unitType])
	dat.appendRow([path, f'chop{i}', repr(chop)])
	dat.appendRow([path, f'choparraytype{i}', mode])

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildExportTable(dat: 'DAT', uniformTable: 'DAT'):
	dat.clear()
	dat.appendRow(['path', 'parameter', 'value'])
	path = str(parent().par.Exportpath)
	arrayIndex = int(parent().par.Firstarrayindex)
	vectorIndex = int(parent().par.Firstvectorindex)
	for row in range(1, uniformTable.numRows):
		uniType = str(uniformTable[row, 'uniformType'])
		if uniType == 'vector':
			_addVector(
				dat,
				path=path,
				i=vectorIndex,
				name=str(uniformTable[row, 'name']),
				expr1=uniformTable[row, 'expr1'] or '0',
				expr2=uniformTable[row, 'expr2'] or '0',
				expr3=uniformTable[row, 'expr3'] or '0',
				expr4=uniformTable[row, 'expr4'] or '0',
			)
			arrayIndex += 1
		else:
			_addArray(
				dat,
				path=path,
				i=arrayIndex,
				name=uniformTable[row, 'name'].val,
				chop=uniformTable[row, 'chop'].val,
				unitType=uniformTable[row, 'type'].val,
				mode=uniType,
			)
			arrayIndex += 1

def _addArray(dat: 'DAT', path: str, i: int, name: str, chop: str, unitType: str, mode: str):
	dat.appendRow([path, f'chopuniname{i}', repr(name)])
	dat.appendRow([path, f'chopunitype{i}', unitType])
	dat.appendRow([path, f'chop{i}', repr(chop)])
	dat.appendRow([path, f'choparraytype{i}', mode])

def _addVector(dat: 'DAT', path, i, name, expr1, expr2, expr3, expr4):
	dat.appendRow([path, f'uniname{i}', repr(name)])
	dat.appendRow([path, f'value{i}x', expr1])
	dat.appendRow([path, f'value{i}y', expr2])
	dat.appendRow([path, f'value{i}z', expr3])
	dat.appendRow([path, f'value{i}w', expr4])

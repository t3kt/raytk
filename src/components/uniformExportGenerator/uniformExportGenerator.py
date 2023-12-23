# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def buildExportTable(dat: DAT, uniformTable: DAT):
	dat.clear()
	dat.appendRow(['path', 'parameter', 'value'])
	path = str(parent().par.Exportpath)
	arrayIndex = int(parent().par.Firstarrayindex)
	vectorIndex = int(parent().par.Firstvectorindex)
	constIndex = 0
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
			vectorIndex += 1
		elif uniType == 'uniformarray':
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
		elif uniType == 'constant':
			_addConstant(
				dat,
				path=path,
				i=constIndex,
				name=uniformTable[row, 'name'].val,
				expr=uniformTable[row, 'expr1'].val or '0',
			)
			constIndex += 1
		else:
			raise Exception(f'Invalid uniform type: {uniType}')

def _addArray(dat: DAT, path: str, i: int, name: str, chop: str, unitType: str, mode: str):
	dat.appendRow([path, f'array{i}name', repr(name)])
	dat.appendRow([path, f'array{i}type', unitType])
	dat.appendRow([path, f'array{i}chop', repr(chop)])
	dat.appendRow([path, f'array{i}arraytype', mode])

def _addVector(dat: DAT, path: str, i: int, name: str, expr1: str, expr2: str, expr3: str, expr4: str):
	dat.appendRow([path, f'vec{i}name', repr(name)])
	dat.appendRow([path, f'vec{i}valuex', expr1])
	dat.appendRow([path, f'vec{i}valuey', expr2])
	dat.appendRow([path, f'vec{i}valuez', expr3])
	dat.appendRow([path, f'vec{i}valuew', expr4])

def _addConstant(dat: DAT, path: str, i: int, name: str, expr: str):
	dat.appendRow([path, f'const{i}name', repr(name)])
	dat.appendRow([path, f'const{i}value', expr])

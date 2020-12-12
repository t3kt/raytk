# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: 'DAT'):
	dat.clear()
	dat.appendCol([
		'typeName',
		'category',
		'version',
		'toolkitVersion',
		'coordType',
		'contextType',
		'returnType',
	])
	dat.appendCol([])
	opDef = parent().par.Definitionop.eval()
	if not opDef:
		return
	opType = opDef.par.Raytkoptype.eval()
	if opType:
		parts = opType.rsplit('.', maxsplit=2)
		dat['category', 1], dat['typeName', 1] = parts[1:]
	dat['version', 1] = opDef.par.Raytkopversion
	dat['toolkitVersion', 1] = opDef.par.Raytkversion
	defTable = opDef.op('definition_out')  # type: DAT
	if defTable and defTable.numRows > 1:
		dat['coordType', 1] = defTable[1, 'coordType']
		dat['contextType', 1] = defTable[1, 'contextType']
		dat['returnType', 1] = defTable[1, 'returnType']


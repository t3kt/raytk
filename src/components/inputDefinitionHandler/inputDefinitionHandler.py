from raytkUtil import TypeTableHelper

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def checkInputDefinition(dat: 'DAT'):
	dat.clear()
	dat.copy(dat.inputs[0])
	clearInputTypeErrors()
	if dat.numRows < 2:
		return
	checkType(str(dat[1, 'coordType'] or ''), 'coordType')
	checkType(str(dat[1, 'contextType'] or ''), 'contextType')
	checkType(str(dat[1, 'returnType'] or ''), 'returnType')

def checkType(typeName: str, typeCategory: str, silent=False):
	if not typeName:
		if not silent:
			reportError(f'Invalid input {typeCategory}: {typeName!r}')
		return False
	supported = tdu.split(parent().par['Support' + typeCategory.lower() + 's'] or '')
	if '*' in supported or typeName in supported:
		return True
	if parent().par['Support' + typeCategory.lower() + typeName.lower()]:
		return True
	if not silent:
		reportError(f'Input does not support {typeCategory} {typeName}')
	return False

def reportError(message: str):
	parent().addScriptError(message)

def clearInputTypeErrors():
	parent().clearScriptErrors(error='Input does not support *')

def updateTypeParMenus():
	helper = TypeTableHelper(op('typeTable'))
	helper.updateCoordTypePar(parent().par.Supportcoordtypes)
	helper.updateReturnTypePar(parent().par.Supportreturntypes)
	helper.updateContextTypePar(parent().par.Supportcontexttypes)

def buildSupportedTypeTable(dat: 'DAT'):
	dat.clear()
	typeTable = op('typeTable')
	helper = TypeTableHelper(typeTable)
	allNames = [c.val for c in typeTable.col('name')[1:]]
	for category, filterColumn in [
		('coordType', 'isCoordType'),
		('contextType', 'isContextType'),
		('returnType', 'isReturnType'),
	]:
		dat.appendRow(
			[
				category,
				' '.join(
					[
						name
						for name in allNames
						if helper.isTypeAvailableForCategory(name, filterColumn) and checkType(name, category, silent=True)
					]),
			])



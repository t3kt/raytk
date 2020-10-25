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
	checkType(dat, 'coordType')
	checkType(dat, 'contextType')
	checkType(dat, 'returnType')

def checkType(dat: 'DAT', typeCategory: str):
	typeName = str(dat[1, typeCategory] or '')
	if not typeName:
		reportError(f'Invalid input {typeCategory}: {typeName!r}')
		return
	supported = tdu.split(parent().par['Support' + typeCategory.lower() + 's'] or '')
	if '*' in supported or typeName in supported:
		return
	if parent().par['Support' + typeCategory.lower() + typeName]:
		return
	reportError(f'Input does not support {typeCategory} {typeName}')

def reportError(message: str):
	parent().addScriptError(message)

def clearInputTypeErrors():
	parent().clearScriptErrors(error='Input does not support *')

def updateTypeParMenus():
	helper = TypeTableHelper(op('typeTable'))
	helper.updateCoordTypePar(parent().par.Supportcoordtypes)
	helper.updateReturnTypePar(parent().par.Supportreturntypes)
	helper.updateContextTypePar(parent().par.Supportcontexttypes)

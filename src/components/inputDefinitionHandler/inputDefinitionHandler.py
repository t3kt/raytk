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
	coordType = dat[1, 'coordType'].val
	returnType = dat[1, 'returnType'].val
	contextType = dat[1, 'contextType'].val
	supportedCoordTypes = tdu.split(parent().par['Supportcoordtypes'] or '')
	supportedReturnTypes = tdu.split(parent().par['Supportreturntypes'] or '')
	supportedContextTypes = tdu.split(parent().par['Supportcontexttypes'] or '')
	if not parent().par['Supportcoordtype' + coordType.lower()] and coordType not in supportedCoordTypes:
		reportError('Input does not support coordType ' + coordType)
	if not parent().par['Supportreturntype' + returnType.lower()] and coordType not in supportedReturnTypes:
		reportError('Input does not support returnType ' + returnType)
	if not parent().par['Supportcontexttype' + contextType.lower()] and coordType not in supportedContextTypes:
		reportError('Input does not support contextType ' + contextType)

def reportError(message: str):
	parent().addScriptError(message)

def clearInputTypeErrors():
	parent().clearScriptErrors(error='Input does not support *')

def updateTypeParMenus():
	helper = TypeTableHelper(op('typeTable'))
	helper.updateCoordTypePar(parent().par.Supportcoordtypes)
	helper.updateReturnTypePar(parent().par.Supportreturntypes)
	helper.updateContextTypePar(parent().par.Supportcontexttypes)

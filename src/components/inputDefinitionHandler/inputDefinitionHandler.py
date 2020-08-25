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
	if not parent().par['Supportcoordtype' + coordType.lower()]:
		reportError('Input does not support coordType ' + coordType)
	if not parent().par['Supportreturntype' + returnType.lower()]:
		reportError('Input does not support returnType ' + returnType)
	if not parent().par['Supportcontexttype' + contextType.lower()]:
		reportError('Input does not support contextType ' + contextType)

def reportError(message: str):
	parent().addScriptError(message)

def clearInputTypeErrors():
	parent().clearScriptErrors(error='Input does not support *')

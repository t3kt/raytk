# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def checkInputDefinition(dat: 'DAT'):
	dat.clearScriptErrors()
	if dat.numRows < 2:
		return
	coordType = dat[1, 'coordType'].val
	returnType = dat[1, 'returnType'].val
	contextType = dat[1, 'contextType'].val
	if not parent().par['Supportcoordtype' + coordType]:
		_reportError(dat, 'Input does not support coordType ' + coordType)
	if not parent().par['Supportreturntype' + returnType]:
		_reportError(dat, 'Input does not support returnType ' + returnType)
	if not parent().par['Supportcontexttype' + contextType]:
		_reportError(dat, 'Input does not support contextType ' + contextType)

def _reportError(dat: 'DAT', message: str):
	dat.addScriptErrors(message)

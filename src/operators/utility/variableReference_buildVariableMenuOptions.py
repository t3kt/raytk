import json
from raytkUtil import ROPInfo

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	sourceVars = _getVars()
	if not sourceVars:
		dat.appendRow(['', ''])
		return
	for variableObj in sourceVars:
		dat.appendRow([variableObj.localName, f'{variableObj.label} ({variableObj.dataType})'])

def _getVars():
	source = parent().par.Source.eval()
	info = ROPInfo(source)
	if not info.isROP:
		return []
	opDefExt = info.opDefExt
	if not opDefExt:
		return []
	state = opDefExt.getRopState()
	return state.variables or []

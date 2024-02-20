# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: scriptDAT):
	dat.copy(dat.inputs[0])
	if dat.numRows < 2:
		return
	_applyReduction(dat[1, 'coordType'], parent().par.Coordtypepreference)
	_applyReduction(dat[1, 'contextType'], parent().par.Contexttypepreference)
	_applyReduction(dat[1, 'returnType'], parent().par.Returntypepreference)

def _applyReduction(cell: Cell, prefs: Par):
	if not prefs or not cell:
		return
	if ' ' not in cell.val:
		return
	supportedTypes = tdu.split(cell)
	preferredTypes = tdu.split(prefs)
	for t in preferredTypes:
		if t in supportedTypes:
			cell.val = t
			return

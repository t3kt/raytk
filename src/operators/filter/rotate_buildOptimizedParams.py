from rotate import getParams

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: DAT):
	dat.clear()
	dat.appendRow(['names', 'source', 'handling', 'readOnlyHandling', 'conversion', 'enable'])
	for par in getParams():
		if par.mode != ParMode.CONSTANT:
			dat.appendRow([par.name, 'param', 'runtime', 'macro', '', '1'])

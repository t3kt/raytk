# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

from raytkTypes import getAllTypes

def onCook(dat: scriptDAT):
	dat.clear()
	dat.appendRow(['outputType', 'returnAs'])
	for dataType in getAllTypes():
		if dataType.vectorLength is None:
			continue
		dat.appendRow([dataType.name, dataType.returnAsType])

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat: scriptDAT):
	dat.clear()
	opThumbFiles = dat.inputs[0]  # type: DAT
	pathPrefix = 'libraryThumbs/thumbImages/thumb__'
	dat.appendRow(['opPath', 'thumb'])
	for i in range(1, opThumbFiles.numRows):
		dat.appendRow([
			opThumbFiles[i, 'opPath'],
			pathPrefix + str(i),
		])

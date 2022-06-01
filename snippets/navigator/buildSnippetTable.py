# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

	from navigator import Navigator
	ext.navigator = Navigator(COMP())

def onCook(dat):
	ext.navigator.buildSnippetTable(
		dat,
		folderDat=dat.inputs[0],
		opTable=dat.inputs[1],
	)

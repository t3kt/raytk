# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from ..tester import TestManager
	ext.tester = TestManager(COMP())

def onLoadTrigger():
	table = op('versionTable')
	name = op('version_dropmenu').par.Value0.eval()
	toxPath = str(table[name, 'tox'] or '')
	ext.tester.loadToolkitTox(toxPath)


	pass

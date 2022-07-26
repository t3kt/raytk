# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from navigator import Navigator
	ext.navigator = Navigator(COMP())

def onSelectRow(info: dict):
	ext.navigator.onSnippetListSelect(info['rowData']['rowObject']['name'])





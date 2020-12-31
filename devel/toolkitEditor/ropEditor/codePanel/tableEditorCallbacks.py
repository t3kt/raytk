# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .codePanel import CodePanel
	# noinspection PyTypeChecker
	ext.codePanel = CodePanel(COMP())

def onCreateItem(info: dict):
	item = info.get('item')
	if item:
		ext.codePanel.onCreateItem(item)

def onDeleteItem(info: dict):
	item = info.get('item')
	if item:
		ext.codePanel.onDeleteItem(item)

def onExternalizeItem(info: dict):
	item = info.get('item')
	if item:
		ext.codePanel.onExternalizeItem(item)

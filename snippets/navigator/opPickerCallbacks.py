# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from navigator import Navigator

	ext.navigator = Navigator(COMP())

def onKeyboardShortcut(info: dict):
	pass

def onPickItem(info: dict):
	ext.navigator.onOpPickerPickItem(info.get('item'))

def onRolloverItem(info: dict):
	pass

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .ropEditor import ROPEditor

	ext.ropEditor = ROPEditor(COMP())

def onKeyboardShortcut(info: dict):
	ext.ropEditor.onKeyboardShortcut(info.get('shortcutName'))

def onPickItem(info: dict):
	ext.ropEditor.onEditItem(info.get('item'))

def onEditItem(info: dict):
	ext.ropEditor.onEditItem(info.get('item'))

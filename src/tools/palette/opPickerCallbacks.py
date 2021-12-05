# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .palette import Palette

	ext.palette = Palette(COMP())

def onKeyboardShortcut(info: dict):
	ext.palette.onKeyboardShortcut(info.get('shortcutName'))

def onPickItem(info: dict):
	ext.palette.onPickItem(info.get('item'))

def onRolloverItem(info: dict):
	ext.palette.onRolloverItem(info.get('item'))

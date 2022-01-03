# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .editorTools import EditorTools
	ext.editorTools = EditorTools(COMP())

def onKey(dat, key, character, alt, lAlt, rAlt, ctrl, lCtrl, rCtrl, shift, lShift, rShift, state, time, cmd, lCmd, rCmd):
	return

def onShortcut(dat, shortcutName, time):
	ext.editorTools.Open()

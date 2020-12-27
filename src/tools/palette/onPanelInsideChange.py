# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .palette import Palette
	ext.palette = Palette(COMP())

def onValueChange(panelValue, prev):
	ext.palette.onPanelInsideChange(panelValue)

# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .palette import Palette
	ext.palette = Palette(COMP())

def onDone(timerOp, segment, interrupt):
	ext.palette.onCloseTimerComplete()

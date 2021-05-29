# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .palette import Palette
	ext.palette = Palette(COMP())

def onStart():
	run('ext.palette.Initialize()', delayFrames=5, delayRef=root, fromOP=me)

def onCreate():
	onStart()

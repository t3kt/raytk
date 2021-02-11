# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onPulse(par):
	ui.undo.startBlock('Create light')
	light = parent(2).create(lightCOMP)
	o = parent()
	o.par.Light = light
	light.dock = o
	o.showDocked = True
	light.nodeX = o.nodeX
	light.nodeY = o.nodeY - o.nodeHeight - 120
	ui.undo.endBlock()

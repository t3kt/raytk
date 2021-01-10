# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from ..outputBuffersPanel import OutputBuffersPanel
	ext.outputBuffersPanel = OutputBuffersPanel(COMP())

def onOffToOn(panelValue):
	ext.outputBuffersPanel.onSelectItem(parent())

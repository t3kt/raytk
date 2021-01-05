# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .opPicker import OpPicker
	ext.opPicker = OpPicker(COMP())

def onValueChange(panelValue: 'PanelValue', prev):
	ext.opPicker.setFilterText(panelValue.val)

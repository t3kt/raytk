# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from .opPicker import OpPicker
	ext.opPicker = OpPicker(COMP())

def onValueChange(par, prev):
	ext.opPicker.onFilterSettingChange()

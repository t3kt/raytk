# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *
	from . import opDefinition as _opDef
	mod.opDefinition = _opDef

def onTableChange(dat):
	mod.opDefinition.onValidationChange(dat)
